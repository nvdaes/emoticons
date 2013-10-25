# -*- coding: UTF-8 -*-

import addonHandler
import speechDictHandler
import os
import shutil
import gui
import wx

addonHandler.initTranslation()

def onInstall():
	for addon in addonHandler.getAvailableAddons():
		if addon.manifest['name'] == "Emoticons":
			if gui.messageBox(
				# Translators: the label of a message box dialog.
				_("You have installed the Emoticons add-on, probably an old and incompatible version with this one. Do you want to uninstall the old version?"),
				# Translators: the title of a message box dialog.
				_("Uninstall incompatible add-on"),
				wx.YES|wx.NO|wx.ICON_WARNING)==wx.YES:
					addon.requestRemove()
			break
	if os.path.isfile(os.path.join(speechDictHandler.speechDictsPath, "emoticons.dic")):
		if gui.messageBox(
		# Translators: the label of a message box dialog.
		_("You seem to have a dictionary for this add-on. Do you want to import it?"),
		# Translators: the title of a message box dialog.
		_("Import emoticons dictionary"),
		wx.YES|wx.NO|wx.ICON_WARNING)==wx.YES:
			try:
				shutil.copy(os.path.join(speechDictHandler.speechDictsPath, "emoticons.dic"), os.path.join(os.path.dirname(__file__), "globalPlugins"))
			except:
				pass
