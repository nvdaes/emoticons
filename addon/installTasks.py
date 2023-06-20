# -*- coding: UTF-8 -*-
# Copyright (C) 2013-2019 Noelia Ruiz Martínez, other contributors
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
	from NVDAState import WritePaths
	import globalVars
	import os
	import shutil
	import gui
	import wx
	ADDON_DICTS_PATH = os.path.abspath(
		os.path.join(os.path.dirname(__file__), "globalPlugins", "emoticons", "emoticons")
	)
	EXPORT_DICTS_PATH = os.path.join(WritePaths.speechDictsDir, "emoticons")
	if (
		os.path.isfile(os.path.join(WritePaths.speechDictsDir, "emoticons.dic"))
		or os.path.isfile(os.path.join(globalVars.appArgs.configPath, "emoticons.ini"))
		or os.path.isdir(EXPORT_DICTS_PATH)
	):
		if gui.messageBox(
			_(
				# Translators: the label of a message box dialog.
				"You seem to have previous settings saved for this add-on."
				" Do you want to import them, removing deprecated files?"
			),
			# Translators: the title of a message box dialog.
			_("Import Emoticons add-on settings"),
			wx.YES | wx.NO | wx.ICON_WARNING
		) == wx.YES:
			try:
				os.makedirs(EXPORT_DICTS_PATH)
				shutil.copy(os.path.join(WritePaths.speechDictsDir, "emoticons.dic"), EXPORT_DICTS_PATH)
			except Exception:
				pass
			try:
				shutil.copytree(EXPORT_DICTS_PATH, ADDON_DICTS_PATH)
			except Exception:
				pass
			try:
				os.remove(os.path.join(WritePaths.speechDictsDir, "emoticons.dic"))
			except Exception:
				pass
			if os.path.isfile(os.path.join(globalVars.appArgs.configPath, "emoticons.ini")):  # Activate
				config.conf["emoticons"]["announcement"] = 1
				try:
					os.remove(os.path.join(globalVars.appArgs.configPath, "emoticons.ini"))
				except Exception:
					pass
			return
	previousDictsPath = os.path.join(
		globalVars.appArgs.configPath, "addons", "emoticons", "globalPlugins", "emoticons", "emoticons"
	)
	if os.path.isdir(previousDictsPath):
		shutil.copytree(previousDictsPath, ADDON_DICTS_PATH)
