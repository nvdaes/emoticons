# -*- coding: UTF-8 -*-

import globalPluginHandler
import speechDictHandler
import ui
import addonHandler

addonHandler.initTranslation()

emoticons = [
	# Translators :( sad smiley
	('(\s|^)(:([\-]|)([(]{1})\B)', _("sad smiley"), "sad", True, True),
]

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def activateEmoticons(self):
		if not self.emoticons:
			speechDictHandler.dictionaries["temp"].extend(self.SD)
			self.emoticons = True

	def deactivateEmoticons(self):
		if self.emoticons:
			for entry in self.SD:
				speechDictHandler.dictionaries["temp"].remove(entry)
			self.emoticons = False

	def __init__(self):
		super(globalPluginHandler.GlobalPlugin, self).__init__()
		self.emoticons = False
		self.SD = speechDictHandler.SpeechDict()
		for pattern, replacement, comment, case, reg in emoticons:
			self.SD.append(speechDictHandler.SpeechDictEntry(pattern, replacement, comment, case, reg))

	def terminate(self):
		self.deactivateEmoticons()
		self.SD = None

	def script_toggle(self, gesture):
		if self.emoticons:
			self.deactivateEmoticons()
			# Translators: message presented when the dictionary for emoticons is unloaded.
			ui.message(_("Emoticons off."))
		else:
			self.activateEmoticons()
			# Translators: message presented when the dictionary for emoticons is loaded.
			ui.message(_("Emoticons on."))
	# Translators: Message presented in input help mode.
	script_toggle.__doc__ = _("Toggles on and off the announcement of emoticons.")

	__gestures = {
		"kb:NVDA+e": "toggle"
	}
