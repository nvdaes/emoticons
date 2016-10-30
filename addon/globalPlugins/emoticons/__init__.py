# -*- coding: UTF-8 -*-
#Copyright (C) 2013-2016 Noelia Ruiz Martínez, Mesar Hameed, Francisco Javier Estrada Martínez
# Released under GPL 2

import globalPluginHandler
import globalVars
import speechDictHandler
import os
import shutil
import api
import ui
import wx
import gui
import addonHandler
from gui.settingsDialogs import SettingsDialog
from gui.settingsDialogs import DictionaryDialog
from smileysList import emoticons

try:
	from globalCommands import SCRCAT_SPEECH, SCRCAT_TOOLS
except:
	SCRCAT_SPEECH = SCRCAT_TOOLS = None

addonHandler.initTranslation()

# Activation at start
from logHandler import log
from cStringIO import StringIO
from configobj import ConfigObj
from validate import Validator

iniFileName = os.path.join(os.path.dirname(__file__), "emoticons.ini")

confspec = ConfigObj(StringIO("""#Configuration file

[Activation settings]
	activateAtStart = integer(default=0)
"""), encoding="UTF-8", list_values=False)
confspec.newlines = "\r\n"
conf = ConfigObj(iniFileName, configspec = confspec, indent_type = "\t", encoding="UTF-8")
val = Validator()
conf.validate(val)

dicFile = os.path.join(os.path.dirname(__file__), "emoticons.dic")
defaultDic = speechDictHandler.SpeechDict()
sD =speechDictHandler.SpeechDict()
emStatus = False
shouldActivateEmoticons = False

def activateEmoticons():
	global emStatus
	speechDictHandler.dictionaries["temp"].extend(sD)
	emStatus = True

def deactivateEmoticons():
	global emStatus
	for entry in sD:
		if entry in speechDictHandler.dictionaries["temp"]:
			speechDictHandler.dictionaries["temp"].remove(entry)
	emStatus = False

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	scriptCategory = SCRCAT_SPEECH

	def __init__(self):
		super(globalPluginHandler.GlobalPlugin, self).__init__()
		global sD, defaultDic
		sD.load(dicFile)
		for em in emoticons:
			if not em.isEmoji:
				# Translators: A prefix to each emoticon name, added to the temporary speech dictionary, visible in temporary speech dictionary dialog when the addon is active, to explain an entry.
				comment = _("Emoticon: %s") % em.name
			else:
				# Translators: A prefix to each emoticon name, added to the temporary speech dictionary, visible in temporary speech dictionary dialog when the addon is active, to explain an entry.
				comment = _("Emoji: %s") % em.name
			otherReplacement = " %s; " % em.name
			# Case and reg are always True
			defaultDic.append(speechDictHandler.SpeechDictEntry(em.pattern, otherReplacement, comment, True, speechDictHandler.ENTRY_TYPE_REGEXP))
		if not os.path.isfile(dicFile):
			sD.extend(defaultDic)
		# Gui
		self.menu = gui.mainFrame.sysTrayIcon.preferencesMenu
		self.emMenu = wx.Menu()
		self.mainItem = self.menu.AppendSubMenu(self.emMenu,
		# Translators: the name of addon submenu.
		_("Manage emoticons"),
		# Translators: the tooltip text for addon submenu.
		_("Emoticons menu"))
		self.insertItem = self.emMenu.Append(wx.ID_ANY,
		# Translators: the name for an item of addon submenu.
		_("&Insert smiley..."),
		# Translators: the tooltip text for an item of addon submenu.
		_("Shows a dialog to insert a smiley"))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onInsertEmoticonDialog, self.insertItem)
		self.dicItem = self.emMenu.Append(wx.ID_ANY,
		# Translators: the name for an item of addon submenu.
		_("&Customize emoticons..."),
		# Translators: the tooltip text for an item of addon submenu.
		_("Shows a dictionary dialog to customize emoticons"))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onEmDicDialog, self.dicItem)
		self.activateItem = self.emMenu.Append(wx.ID_ANY,
		# Translators: the name for an item of addon submenu.
		_("&Activation settings..."),
		# Translators: the tooltip text for an item of addon submenu.
		_("Shows a dialog to choose when emoticons speaking should be activated"))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onActivateDialog, self.activateItem)
		if conf["Activation settings"]["activateAtStart"]:
			activateEmoticons()

	def terminate(self):
		deactivateEmoticons()
		global sD, defaultDic
		sD = defaultDic = None
		try:
			self.menu.RemoveItem(self.mainItem)
		except wx.PyDeadObjectError:
			pass

	def onInsertEmoticonDialog(self, evt):
		gui.mainFrame._popupSettingsDialog(InsertEmoticonDialog)

	def onEmDicDialog(self, evt):
		global shouldActivateEmoticons
		shouldActivateEmoticons = emStatus
		deactivateEmoticons()
		gui.mainFrame._popupSettingsDialog(EmDicDialog,_("Emoticons dictionary"), sD)

	def onActivateDialog(self, evt):
		gui.mainFrame._popupSettingsDialog(ActivateEmoticonsDialog)

	def script_toggleSpeakingEmoticons(self, gesture):
		if not globalVars.speechDictionaryProcessing:
			return
		if emStatus:
			deactivateEmoticons()
			# Translators: message presented when the dictionary for emoticons is unloaded.
			ui.message(_("Emoticons off."))
		else:
			activateEmoticons()
			# Translators: message presented when the dictionary for emoticons is loaded.
			ui.message(_("Emoticons on."))
	# Translators: Message presented in input help mode.
	script_toggleSpeakingEmoticons.__doc__ = _("Toggles on and off the announcement of emoticons.")

	def script_insertEmoticon(self, gesture):
		wx.CallAfter(self.onInsertEmoticonDialog, None)
	script_insertEmoticon.category = SCRCAT_TOOLS
	# Translators: Message presented in input help mode.
	script_insertEmoticon.__doc__ = _("Shows a dialog to select a smiley you want to paste.")

	__gestures = {
		"kb:NVDA+e": "toggleSpeakingEmoticons",
		"kb:NVDA+i": "insertEmoticon",
	}

class EmoticonFilter(object):
	"""Filter for all emoticons."""
	
	def filter(self, emoticonsList, pattern):
		"""Filters the input list with the specified pattern."""
		if pattern == "": return emoticonsList
		else: return filter(lambda emoticon: pattern.upper() in emoticon.name.upper(), emoticonsList)

class FilterStandard(EmoticonFilter):
	"""Filter just for standard emoticons."""
	
	def filter(self, emoticonsList, pattern):
		filtered = super(FilterStandard, self).filter(emoticonsList, pattern)
		return filter(lambda emoticon: not(emoticon.isEmoji), filtered)

class FilterEmoji(EmoticonFilter):
	"""Filter just for emojis."""
	
	def filter(self, emoticonsList, pattern):
		filtered = super(FilterEmoji, self).filter(emoticonsList, pattern)
		return filter(lambda emoticon: emoticon.isEmoji, filtered)

class InsertEmoticonDialog(wx.Dialog):
	""" A dialog  to insert emoticons from a list. """
	
	filteredEmoticons = emoticons
	filter = EmoticonFilter()
	
	def __init__(self, parent):
		# Translators: Title of the dialog.
		wx.Dialog.__init__(self, parent, title= _("Insert emoticon"), pos = wx.DefaultPosition, size = (500, 600))
		# Filter panel.
		# Translators: A text field to filter emoticons.
		self.lblFilter = wx.StaticText(self, label= _("&Filter:"), pos = (-1, -1))
		self.txtFilter = wx.TextCtrl(self)
		self.Bind(wx.EVT_TEXT, self.onFilterChange, self.txtFilter)
		self.sizerFilter = wx.BoxSizer(wx.HORIZONTAL)
		self.sizerFilter.Add(self.lblFilter, 0, wx.FIXED_MINSIZE)
		self.sizerFilter.Add(self.txtFilter, 1, wx.EXPAND)
		# Radio buttons to choose the emoticon set.
		# Translators: Kind of emoticons to show.
		self.lblShow = wx.StaticText(self, label= _("&Show:"), pos = (-1, -1))
		# Translators: A radio button to choose all types of emoticons.
		self.rdAll = wx.RadioButton(self, label = _("&All"), style = wx.RB_GROUP)
		self.Bind(wx.EVT_RADIOBUTTON, self.onAllEmoticons, self.rdAll)
		# Translators: A radio button to choose only standard emoticons.
		self.rdStandard = wx.RadioButton(self, label = _("&Standard"))
		self.Bind(wx.EVT_RADIOBUTTON, self.onStandardEmoticons, self.rdStandard)
		# Translators: A radio button to choose only emojis.
		self.rdEmojis = wx.RadioButton(self, label = _("Emoj&is"))
		self.Bind(wx.EVT_RADIOBUTTON, self.onEmojis, self.rdEmojis)
		self.sizerRadio = wx.BoxSizer(wx.HORIZONTAL)
		self.sizerRadio.Add(self.lblShow, 0, wx.FIXED_MINSIZE)
		self.sizerRadio.Add(self.rdAll, 0, wx.FIXED_MINSIZE)
		self.sizerRadio.Add(self.rdStandard, 0, wx.FIXED_MINSIZE)
		self.sizerRadio.Add(self.rdEmojis, 0, wx.FIXED_MINSIZE)
		# List of emoticons.
		# Translators: Label for the smileys list.
		self.lblList = wx.StaticText(self, label= _("&List of smilies:"), pos = (-1, -1))
		self.smileysList = wx.ListCtrl(self, size=(490, 400), style=wx.LC_REPORT | wx.BORDER_SUNKEN)
		# Translators: Column which specifies the name  of emoticon.
		self.smileysList.InsertColumn(0, _("Name"))
		# Translators: Column which specifies the type of emoticon (standard or emoji).
		self.smileysList.InsertColumn(1, _("Type"))
		# Translators: The column which contains the emoticon.
		self.smileysList.InsertColumn(2, _("Emoticon"))
		self.smileysList.Bind(wx.EVT_KEY_DOWN, self.onEnterOnList)
		self.sizerList = wx.BoxSizer(wx.VERTICAL)
		self.sizerList.Add(self.lblList, 0, wx.FIXED_MINSIZE)
		self.sizerList.Add(self.smileysList, 1, wx.EXPAND)
		self._loadEmoticons()
		# Buttons.
		self.sizerButtons = self.CreateButtonSizer(wx.OK | wx.CANCEL)
		btnOk = self.FindWindowById(self.GetAffirmativeId())
		self.Bind(wx.EVT_BUTTON, self.onOk, btnOk)
		# Vertical layout
		self.sizerLayout = wx.BoxSizer(wx.VERTICAL)
		self.sizerLayout.Add(self.sizerFilter, 0, wx.FIXED_MINSIZE)
		self.sizerLayout.Add(self.sizerRadio, 0, wx.FIXED_MINSIZE)
		self.sizerLayout.Add(self.sizerList, 1, wx.EXPAND)
		self.sizerLayout.Add(self.sizerButtons, 0, wx.EXPAND)
		
		self.SetSizer(self.sizerLayout)
		self.SetAutoLayout(1)
		self.sizerLayout.Fit(self)
		self.Show(True)
		self.txtFilter.SetFocus()
		
	def _formatIsEmoji(self, isEmoji):
		"""Converts boolean isEmoji property to text."""
		# Translators: Label for emojis in the list.
		if isEmoji: return _("Emoji")
		# Translators: Label for standard emoticons in the list.
		else: return _("Standard")
		
	def _loadEmoticons(self):
		"""Reload the emoticons list."""
		self.smileysList.DeleteAllItems()
		for emoticon in self.filteredEmoticons:
			if not emoticon.isEmoji:
				self.smileysList.Append([emoticon.name, self._formatIsEmoji(emoticon.isEmoji), unicode(emoticon.chars)])
			else:
				self.smileysList.Append([emoticon.name, self._formatIsEmoji(emoticon.isEmoji), emoticon.chars.decode("utf-8")])
			
	def onFilterChange(self, event):
		"""Updates the emoticon list when the filter field changes its content."""
		self.filteredEmoticons = self.filter.filter(emoticons, self.txtFilter.GetValue())
		self._loadEmoticons()
		
	def onEnterOnList(self, evt):
		"""Same effect as click OK button when pressing enter on smileys list."""
		keycode = evt.GetKeyCode()
		if keycode == wx.WXK_RETURN: self.onOk(evt)
		evt.Skip(True)
		
	def onOk(self, evt):
		"""Copy to clipboard the focused emoticon on the list."""
		icon = self.filteredEmoticons[self.smileysList.GetFocusedItem()]
		if not icon.isEmoji:
			iconToInsert = unicode(icon.chars)
		else:
			iconToInsert = icon.chars.decode("utf-8")
		if api.copyToClip(iconToInsert):
			# Translators: This is the message when smiley has been copied to the clipboard.
			wx.CallLater(100, ui.message, _("Smiley copied to clipboard, ready for you to paste."))
		else:
			wx.CallLater(100, ui.message, _("Cannot copy smiley."))
		self.Destroy()
	
	def onAllEmoticons(self, event):
		"""Changes the filter to all emoticons and reload the emoticon list."""
		self.filter = EmoticonFilter()
		self.filteredEmoticons = self.filter.filter(emoticons, self.txtFilter.GetValue())
		self._loadEmoticons()
	
	def onStandardEmoticons(self, event):
		"""Changes the filter to standard emoticons and reloads the emoticon list."""
		self.filter = FilterStandard()
		self.filteredEmoticons = self.filter.filter(emoticons, self.txtFilter.GetValue())
		self._loadEmoticons()

	def onEmojis(self, event):
		"""Changes the filter to emojis and reloads the emoticon list."""
		self.filter = FilterEmoji()
		self.filteredEmoticons = self.filter.filter(emoticons, self.txtFilter.GetValue())
		self._loadEmoticons()

class EmDicDialog(DictionaryDialog):

	def makeSettings(self, settingsSizer):
		dictListID=wx.NewId()
		entriesSizer=wx.BoxSizer(wx.VERTICAL)
		# Translators: The label for the combo box of dictionary entries in speech dictionary dialog.
		entriesLabel=wx.StaticText(self,-1,label=_("&Dictionary entries"))
		entriesSizer.Add(entriesLabel)
		self.dictList=wx.ListCtrl(self,dictListID,style=wx.LC_REPORT|wx.LC_SINGLE_SEL,size=(550,350))
		# Translators: The label for a column in dictionary entries list used to identify comments for the entry.
		self.dictList.InsertColumn(0,_("Comment"),width=150)
		# Translators: The label for a column in dictionary entries list used to identify pattern (original word or a pattern).
		self.dictList.InsertColumn(1,_("Pattern"),width=150)
		# Translators: The label for a column in dictionary entries list and in a list of symbols from symbol pronunciation dialog used to identify replacement for a pattern or a symbol
		self.dictList.InsertColumn(2,_("Replacement"),width=150)
		# Translators: The label for a column in dictionary entries list used to identify whether the entry is case sensitive or not.
		self.dictList.InsertColumn(3,_("case"),width=50)
		# Translators: The label for a column in dictionary entries list used to identify whether the entry is a regular expression, matches whole words, or matches anywhere.
		self.dictList.InsertColumn(4,_("Type"),width=50)
		self.offOn = (_("off"),_("on"))
		for entry in self.tempSpeechDict:
			self.dictList.Append((entry.comment,entry.pattern,entry.replacement,self.offOn[int(entry.caseSensitive)],DictionaryDialog.TYPE_LABELS[entry.type]))
		self.editingIndex=-1
		entriesSizer.Add(self.dictList,proportion=8)
		settingsSizer.Add(entriesSizer)
		entryButtonsSizer=wx.BoxSizer(wx.HORIZONTAL)
		addButtonID=wx.NewId()
		# Translators: The label for a button in speech dictionaries dialog to add new entries.
		addButton=wx.Button(self,addButtonID,_("&Add"),wx.DefaultPosition)
		entryButtonsSizer.Add(addButton)
		editButtonID=wx.NewId()
		# Translators: The label for a button in speech dictionaries dialog to edit existing entries.
		editButton=wx.Button(self,editButtonID,_("&Edit"),wx.DefaultPosition)
		entryButtonsSizer.Add(editButton)
		removeButtonID=wx.NewId()
		removeButton=wx.Button(self,removeButtonID,_("&Remove"),wx.DefaultPosition)
		entryButtonsSizer.Add(removeButton)
		resetButtonID = wx.NewId()
		resetButton = wx.Button(self,resetButtonID,_("Rese&t"),wx.DefaultPosition)
		self.Bind(wx.EVT_BUTTON,self.OnAddClick,id=addButtonID)
		self.Bind(wx.EVT_BUTTON,self.OnEditClick,id=editButtonID)
		self.Bind(wx.EVT_BUTTON,self.OnRemoveClick,id=removeButtonID)
		self.Bind(wx.EVT_BUTTON,self.OnResetClick,id=resetButtonID)
		settingsSizer.Add(entryButtonsSizer)
		fileButtonsSizer = wx.BoxSizer(wx.HORIZONTAL)
		exportButtonID = wx.NewId()
		# Translators: The label for a button in speech dictionaries dialog to add new entries.
		exportButton = wx.Button(self,exportButtonID,_("Save and e&xport dictionary"),wx.DefaultPosition)
		fileButtonsSizer.Add(exportButton)
		self.Bind(wx.EVT_BUTTON,self.OnExportClick,id=exportButtonID)
		settingsSizer.Add(fileButtonsSizer)

	def OnResetClick(self,evt):
		self.dictList.DeleteAllItems()
		self.tempSpeechDict = []
		self.tempSpeechDict.extend(defaultDic)
		for entry in defaultDic:
			self.dictList.Append((entry.comment,entry.pattern,entry.replacement,True,speechDictHandler.ENTRY_TYPE_REGEXP))
		self.dictList.SetFocus()

	def onOk(self,evt):
		super(EmDicDialog, self).onOk(evt)
		global shouldActivateEmoticons
		if shouldActivateEmoticons:
			activateEmoticons()
		shouldActivateEmoticons = False

	def onCancel(self,evt):
		super(EmDicDialog, self).onCancel(evt)
		global shouldActivateEmoticons
		if shouldActivateEmoticons:
			activateEmoticons()
			shouldActivateEmoticons = False

	def OnExportClick(self,evt):
		self.onOk(None)
		sD.save(os.path.join(speechDictHandler.speechDictsPath, "emoticons.dic"))

class ActivateEmoticonsDialog(SettingsDialog):

# Translators: this is the label for the Emoticons activate dialog.
	title = _("Activation settings")

	def makeSettings(self, settingsSizer):
		activateSizer=wx.BoxSizer(wx.HORIZONTAL)
		# Translators: The label for a setting in Activate emoticons dialog.
		activateLabel=wx.StaticText(self,-1,label=_("&Activate speaking of emoticons at start:"))
		activateSizer.Add(activateLabel)
		activateListID = wx.NewId()
		self.activateChoices = [
		# Translators: a choice of Activateemoticons dialog.
		_("off"),
		# Translators: a choice of Activateemoticons dialog.
		_("On")]
		# Translators: a combo box in Emoticons dialog.
		self.activateList = wx.Choice(self, activateListID, name=_("Activate at start"), choices=[x for x in self.activateChoices])
		self.activateList.SetSelection(conf["Activation settings"]["activateAtStart"])
		activateSizer.Add(self.activateList)
		settingsSizer.Add(activateSizer,border=10,flag=wx.BOTTOM)
		# Translators: The label for a setting in Activate emoticons dialog to copy activation settings.
		self.copyActivationCheckBox = wx.CheckBox(self, wx.NewId(), label=_("&Copy activation settings"))
		self.copyActivationCheckBox.SetValue(False)
		settingsSizer.Add(self.copyActivationCheckBox,border=10,flag=wx.BOTTOM)

	def postInit(self):
		self.activateList.SetFocus()

	def onOk(self,evt):
		super(ActivateEmoticonsDialog, self).onOk(evt)
		conf["Activation settings"]["activateAtStart"] = self.activateList.GetSelection()
		try:
			conf.validate(val, copy=True)
			conf.write()
			log.info("Emoticons add-on configuration saved.")
		except Exception, e:
			log.warning("Could not save Emoticons add-on configuration.")
			log.debugWarning("", exc_info=True)
			raise e
		if self.copyActivationCheckBox.GetValue():
			try:
				shutil.copy(iniFileName, globalVars.appArgs.configPath)
			except:
				pass
