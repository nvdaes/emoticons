# -*- coding: UTF-8 -*-
# Copyright (C) 2021 Noelia Ruiz Martínez
# Released under GPL 2

import globalPluginHandler
import api
import characterProcessing
import copy
import speech
import ui


class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	# Translators: Script category for commands to insert symbols.
	scriptCategory = _("Insert symbols")

	@classmethod
	def __new__(cls, *args, **kwargs):
		# Iterate through the available symbols, creating scripts for them.
		for symbol in cls.getSymbols():
			cls.addScriptForSymbol(symbol)
		return super(GlobalPlugin, cls).__new__(cls)

	@classmethod
	def getSymbols(cls):
		try:
			processor = characterProcessing._localeSpeechSymbolProcessors.fetchLocaleData(speech.getCurrentLanguage())
		except LookupError:
			processor = characterProcessing._localeSpeechSymbolProcessors.fetchLocaleData("en")
		symbols = [copy.copy(symbol) for symbol in processor.computedSymbols.values()]
		return symbols

	@classmethod
	def _getScriptNameForSymbol(cls, symbol):
		name = symbol.replacement.replace(" ", "_")
		return "symbol_%s" % name

	@classmethod
	def _symbolScript(cls, symbol):
		if api.copyToClip(symbol.identifier):
			# Translators: This is the message when smiley has been copied to the clipboard.
			ui.message(_("Smiley copied to clipboard, ready for you to paste."))
		else:
			# Translators: Message when the emoticon couldn't be copied.
			ui.message(_("Cannot copy smiley."))

	@classmethod
	def addScriptForSymbol(cls, symbol):
		script = lambda self, gesture: cls._symbolScript(symbol)  # Noqa E731
		funcName = script.__name__ = "script_%s" % cls._getScriptNameForSymbol(symbol)
		# Just set the doc string of the script, using the decorator is overkill here.
		# Translators: Message presented in input help mode.
		script.__doc__ = _("Inserts the %s symbol" % symbol.replacement)
		setattr(cls, funcName, script)
