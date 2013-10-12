# -*- coding: UTF-8 -*-

import globalPluginHandler
import os
import speechDictHandler
import languageHandler
import ui
import addonHandler
addonHandler.initTranslation()

_pluginDir = os.path.dirname(__file__) # The root of the addon folder
_dicFileName = "emoticons.dic" # The name of a dictionary for emoticons

def getDicFolder(pluginDir=_pluginDir):
	langs = [languageHandler.getLanguage(), "en"]
	for lang in langs:
		dicFolder = os.path.join(pluginDir, "dic", lang)
		if os.path.isdir(dicFolder):
			return dicFolder
		if "_" in lang:
			tryLang = lang.split("_")[0]
			dicFolder = os.path.join(pluginDir, "dic", tryLang)
			if os.path.isdir(dicFolder):
				return dicFolder
			if tryLang == "en":
				break
		if lang == "en":
			break
	return None

def getDicPath(dicFileName=_dicFileName):
	dicPath = getDicFolder()
	if dicPath is not None:
		dicFile = os.path.join(dicPath, dicFileName)
		if os.path.isfile(dicFile):
			dicPath = dicFile
	return dicPath

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def activateEmoticons(self):
		if self.emoticons == True or self.SD is None:
			return
		self.SD.load(self.dicFile)
		speechDictHandler.dictionaries["temp"].extend(self.SD)
		self.emoticons = True

	def deactivateEmoticons(self):
		if self.emoticons == False or self.SD is None:
			return
		for entry in self.SD:
			speechDictHandler.dictionaries["temp"].remove(entry)
		self.emoticons = False

	def __init__(self):
		super(globalPluginHandler.GlobalPlugin, self).__init__()
		self.emoticons = False
		self.dicFile = getDicPath()
		if self.dicFile is not None:
			self.SD = speechDictHandler.SpeechDict()
		else:
			self.SD = None

	def terminate(self):
		self.deactivateEmoticons()
		self.dicFile = None
		self.SD = None

	def script_toggle(self, gesture):
		if self.SD is None:
			# Translators: message presented when the corresponding dictionary for emoticons is not found.
			ui.message("Emoticons dictionary not found.")
			return
		if self.emoticons == True:
			self.deactivateEmoticons()
			# Translators: message presented when the dictionary for emoticons is unloaded.
			ui.message(_("Emoticons %s") % _("off"))
		else:
			self.activateEmoticons()
			# Translators: message presented when the dictionary for emoticons is loaded.
			ui.message(_("Emoticons %s") % _("on"))
	script_toggle.__doc__ = _("Toggles on and off the speaking of emoticons using speech dictionaries.")

	__gestures = {
		"kb:NVDA+e": "toggle"
	}