# -*- coding: UTF-8 -*-
#Copyright (C) 2013-2018 Noelia Ruiz Martínez, other contributors
# Released under GPL2

import config
import addonHandler

confspec = {
	"announcement": "integer(default=0)",
	"cleanDicts": "boolean(default=False)",
}
config.conf.spec["emoticons"] = confspec

addonHandler.initTranslation()

def onInstall():
	from gui import SettingsPanel, NVDASettingsDialog
	import speechDictHandler
	import globalVars
	import os
	import shutil
	import gui
	import wx
	ADDON_DICTS_PATH = os.path.join(os.path.dirname(__file__), "globalPlugins", "emoticons", "emoticons")
	EXPORT_DICTS_PATH = os.path.join(speechDictHandler.speechDictsPath, "emoticons")
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
	if os.path.isfile(os.path.join(speechDictHandler.speechDictsPath, "emoticons.dic")) or os.path.isfile(os.path.join(globalVars.appArgs.configPath, "emoticons.ini")) or os.path.isdir(EXPORT_DICTS_PATH):
		if gui.messageBox(
			# Translators: the label of a message box dialog.
			_("You seem to have previous settings saved for this add-on. Do you want to import them, removing deprecated files?"),
			# Translators: the title of a message box dialog.
			_("Import Emoticons add-on settings"),
			wx.YES|wx.NO|wx.ICON_WARNING)==wx.YES:
				try:
					shutil.copy(os.path.join(speechDictHandler.speechDictsPath, "emoticons.dic"), ADDON_DICTS_PATH)
				except:
					pass
				try:
					shutil.copy(os.path.join(speechDictHandler.speechDictsPath, "emoticons.dic"), EXPORT_DICTS_PATH)
				except:
					pass
				try:
					shutil.copytree(EXPORT_DICTS_PATH, ADDON_DICTS_PATH)
				except:
					pass
				try:
					os.remove(os.path.join(speechDictHandler.speechDictsPath, "emoticons.dic"))
				except:
					pass
				if os.path.isfile(os.path.join(globalVars.appArgs.configPath, "emoticons.ini")): # We suppose that emoticons speaking should be activated
					config.conf["emoticons"]["announcement"] = 1
					try:
						os.remove(os.path.join(globalVars.appArgs.configPath, "emoticons.ini"))
					except:
						pass
