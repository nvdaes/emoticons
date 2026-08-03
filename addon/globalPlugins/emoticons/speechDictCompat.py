# -*- coding: UTF-8 -*-
# Copyright (C) 2026 Noelia Ruiz Martínez, Mesar Hameed, Francisco Javier Estrada Martínez
# Released under GPL 2

import globalVars
import speechDictHandler
from logHandler import log

try:
	from speech.extensions import filter_speechSequence as _speechSequenceFilter
except ImportError:
	_speechSequenceFilter = None

try:
	from speechDictHandler.types import EntryType, SpeechDict, SpeechDictEntry
except ImportError:
	# NVDA 2026.1 and earlier expose these types directly from speechDictHandler.
	SpeechDict = speechDictHandler.SpeechDict
	SpeechDictEntry = speechDictHandler.SpeechDictEntry
	REGEXP_ENTRY_TYPE = speechDictHandler.ENTRY_TYPE_REGEXP
else:
	REGEXP_ENTRY_TYPE = EntryType.REGEXP

__all__ = (
	"REGEXP_ENTRY_TYPE",
	"SpeechDict",
	"SpeechDictEntry",
	"SpeechDictionaryBridge",
)


class SpeechDictionaryBridge:
	"""Activate an add-on dictionary through the best API available in NVDA."""

	def __init__(self, speechDictionary):
		self._speechDictionary = speechDictionary
		self._active = False
		self._filterHandler = self._filterSpeechSequence
		self._legacyTempDictionary = None
		self._legacyEntries = ()

	def _filterSpeechSequence(self, speechSequence):
		if not globalVars.speechDictionaryProcessing:
			return speechSequence
		return [
			self._speechDictionary.sub(item) if isinstance(item, str) else item for item in speechSequence
		]

	def activate(self):
		if self._active:
			return
		try:
			if _speechSequenceFilter is not None:
				_speechSequenceFilter.register(self._filterHandler)
			else:
				# Compatibility with NVDA versions predating the public speech filter.
				tempDictionary = speechDictHandler.dictionaries["temp"]
				self._legacyEntries = tuple(self._speechDictionary)
				tempDictionary.extend(self._legacyEntries)
				self._legacyTempDictionary = tempDictionary
		except Exception:
			log.exception("Unable to activate the Emoticons speech dictionary")
			return
		self._active = True

	def deactivate(self):
		if not self._active:
			return
		try:
			if _speechSequenceFilter is not None:
				_speechSequenceFilter.unregister(self._filterHandler)
			elif self._legacyTempDictionary is not None:
				for entry in self._legacyEntries:
					for index, tempEntry in enumerate(self._legacyTempDictionary):
						if tempEntry is entry:
							del self._legacyTempDictionary[index]
							break
		except Exception:
			log.exception("Unable to deactivate the Emoticons speech dictionary")
		finally:
			self._active = False
			self._legacyTempDictionary = None
			self._legacyEntries = ()
