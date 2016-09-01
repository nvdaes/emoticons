# -*- coding: UTF-8 -*-
#Copyright (C) 2013-2016 Noelia Ruiz Martínez, other contributors
# Released under GPL2

import addonHandler

addonHandler.initTranslation()

def onInstall():
	import speechDictHandler
	import globalVars
	import os
	import shutil
	import gui
	import wx
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
	if os.path.isfile(os.path.join(speechDictHandler.speechDictsPath, "emoticons.dic")) or os.path.isfile(os.path.join(globalVars.appArgs.configPath, "emoticons.ini")):
		if gui.messageBox(
		# Translators: the label of a message box dialog.
		_("You seem to have previous settings saved for this add-on. Do you want to import them?"),
		# Translators: the title of a message box dialog.
		_("Import Emoticons add-on settings"),
		wx.YES|wx.NO|wx.ICON_WARNING)==wx.YES:
			try:
				shutil.copy(os.path.join(speechDictHandler.speechDictsPath, "emoticons.dic"), os.path.join(os.path.dirname(__file__), "globalPlugins", "emoticons"))
			except:
				pass
			try:
				shutil.copy(os.path.join(globalVars.appArgs.configPath, "emoticons.ini"), os.path.join(os.path.dirname(__file__), "globalPlugins", "emoticons"))
			except:
				pass
