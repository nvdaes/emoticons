# -*- coding: UTF-8 -*-

import globalPluginHandler
import speechDictHandler
import ui
import addonHandler

addonHandler.initTranslation()

firstGroup = "\\1"
emoticonsCase = True
emoticonsReg = True

# Emoticons preceded by \\1 and considered case-sensitive regular expressions
emoticons = [
	# Translators :( sad smiley
	(r'(\b|^)(:([\-]|)([(]{1})\B)', _("sad smiley"), "sad"),
]

complexEmoticons = [
	# (patern, replacement, comment, case, reg),
]

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def activateEmoticons(self):
		if self.emoticons == True or self.SD is None:
			return
		for patern, replacement, comment in emoticons:
			self.SD.append(speechDictHandler.SpeechDictEntry(patern, "{firstExpr}{secondExpr}".format(firstExpr=firstGroup, secondExpr=replacement), comment, emoticonsCase, emoticonsReg))
		for patern, replacement, comment, case, reg in complexEmoticons:
			self.SD.append(speechDictHandler.SpeechDictEntry(patern, replacement, comment, case, reg))
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
		self.SD = speechDictHandler.SpeechDict()

	def terminate(self):
		self.deactivateEmoticons()
		self.SD = None

	def script_toggle(self, gesture):
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