# -*- coding: UTF-8 -*-

import globalPluginHandler
import speechDictHandler
import ui
import addonHandler

try:
	from globalCommands import SCRCAT_SPEECH
except:
	SCRCAT_SPEECH = None

addonHandler.initTranslation()

emoticons = [
	# Translators:  :) Smile
	(r'(\s|^)(:([\-]|)([)]{1})(\B|\s|$))', _("smiley Smile")),
	# Translators:  :( Sad
	(r'(\s|^)(:([\-]|)([(]{1})\B)', _("smiley Sad")),
	# Translators:   :D Laugh
	(r'(\s|^)(:([\-]|)([D]{1,})\b)', _("smiley Laugh")),
	# Translators:  (cool) Cool
	(r'(\s|^)\(cool\)(\B|\s|$)', _("smiley Cool")),
	# Translators:  :O Surprised
	(r'(\s|^)(:([\-]|)([O]{1})(\W|\s|$))', _("smiley Surprised")),
	# Translators:  ;) Wink;
	(r'(\s|^)(;([\-]|)([)D]{1})(\B|\s|$))', _("smiley Wink")),
	# Translators:  ;( Crying
	(r'(\s|^)(;([\-]|)([(]{1})(\B|\s|$))', _("smiley Crying")),
	# Translators:  (:| Sweating
	(r'(\s|^)\((:[\|])(\B|\s|$)', _("smiley Sweating")),
	# Translators:  :| Speechless
	(r'(\s|^)(:[\|])(\B|\s|$)', _("smiley Speechless")),
	# Translators:  :* Kiss
	(r'(\s|^)(:([\-]|)([\*]{1})(\B|\s|$))', _("smiley Kiss")),
	# Translators:  :P Cheeky
	(r'(\s|^)(:([\-]|)([pP])(\W|\s|$))', _("smiley Cheeky")),
	# Translators:  :$ Blushing
	(r'(\s|^)(:[\$])(\B|\s|$)', _("smiley Blushing")),
	# Translators:  :^) Wondering
	(r'(\s|^)(:[\^][\)])(\B|\s|$)', _("smiley Wondering")),
	# Translators:  |-) Sleepy
	(r'(\s|^)([\|][\-][\)])(\B|\s|$)', _("smiley Sleepy")),
	# Translators:  |-( Dull
	(r'(\s|^)([\|][\-][\(])(\B|\s|$)', _("smiley Dull")),
	# Translators:  (inlove) In Love
	(r'(\s|^)\(inlove\)(\B|\s|$)', _("smiley In Love")),
	# Translators:  ]:) Evil grin
	(r'(\s|^)()\]:\)(\B|\s|$)', _("smiley Evil grin")),
	# Translators:  (yn) Fingers crossed
	(r'(\s|^)([\(]yn[\)])(\B|\s|$)', _("smiley Fingers crossed")),
	# Translators:  (yawn) Yawn
	(r'(\s|^)\(yawn\)(\B|\s|$)', _("smiley Yawn")),
	# Translators:  (puke) Puking
	(r'(\s|^)\(puke\)(\B|\s|$)', _("smiley Puking")),
	# Translators:  (doh) Doh!
	(r'(\s|^)\(doh\)(\B|\s|$)', _("smiley Doh! ")),
	# Translators:  (angry) Angry
	(r'(\s|^)\(angry\)(\B|\s|$)', _("smiley Angry")),
	# Translators:  (wasntme) It wasn't me!
	(r'(\s|^)\(wasntme\)(\B|\s|$)', _("smiley It wasn't me! ")),
	# Translators:  (party) Party
	(r'(\s|^)\(party\)(\B|\s|$)', _("smiley Party")),
	# Translators:  (worry) Worried
	(r'(\s|^)\(worry\)(\B|\s|$)', _("smiley Worried")),
	# Translators:  (mm) Mmmm...
	(r'(\s|^)\(mm\)(\B|\s|$)', _("smiley mmmmmm...")),
	# Translators:  (nerd) Nerdy
	(r'(\s|^)\(nerd\)(\B|\s|$)', _("smiley Nerdy")),
	# Translators:  :x My lips are sealed
	(r'(\s|^)(:([\-]|)([xX])\b)', _("smiley My lips are sealed")),
	# Translators:  (wave) Hi
	(r'(\s|^)\(wave\)(\B|\s|$)', _("smiley Hi")),
	# Translators:  (facepalm) Facepalm
	(r'(\s|^)\(facepalm\)(\B|\s|$)', _("smiley Facepalm")),
	# Translators:  (devil) Devil
	(r'(\s|^)\(devil\)(\B|\s|$)', _("smiley Devil")),
	# Translators:  (angel) Angel
	(r'(\s|^)\(angel\)(\B|\s|$)', _("smiley Angel")),
	# Translators:  (envy) Envy
	(r'(\s|^)\(envy\)(\B|\s|$)', _("smileyEnvy")),
	# Translators:  (wait) Wait
	(r'(\s|^)\(wait\)(\B|\s|$)', _("smiley Wait")),
	# Translators:  (hug) Hug
	(r'(\s|^)\(hug\)(\B|\s|$)', _("smiley Hug")),
	# Translators:  (makeup) Make-up
	(r'(\s|^)\(makeup\)(\B|\s|$)', _("smiley Make-up")),
	# Translators:  (chuckle) Giggle
	(r'(\s|^)\(chuckle\)(\B|\s|$)', _("smiley Giggle")),
	# Translators:  (clap) Clapping
	(r'(\s|^)\(clap\)(\B|\s|$)', _("smiley Clapping")),
	# Translators:  (think) Thinking
	(r'(\s|^)\(think\)(\B|\s|$)', _("smiley Thinking")),
	# Translators:  (bow) Bowing
	(r'(\s|^)\(bow\)(\B|\s|$)', _("smiley Bowing")),
	# Translators:  (rofl) Rolling on the floor laughing
	(r'(\s|^)\(rofl\)(\B|\s|$)', _("smiley Rolling on the floor laughing! ")),
	# Translators:  (whew) Relieved
	(r'(\s|^)\(whew\)(\B|\s|$)', _("smiley Relieved")),
	# Translators:  (happy) Happy
	(r'(\s|^)\(happy\)(\B|\s|$)', _("smiley Happy")),
	# Translators:  (smirk) Smirking
	(r'(\s|^)\(smirk\)(\B|\s|$)', _("smiley Smirking")),
	# Translators:  (nod) Nodding
	(r'(\s|^)\(nod\)(\B|\s|$)', _("smiley Nodding")),
	# Translators:  (shake) Shake
	(r'(\s|^)\(shake\)(\B|\s|$)', _("smiley Shake")),
	# Translators:  (waiting) Waiting
	(r'(\s|^)\(waiting\)(\B|\s|$)', _("smiley Waiting")),
	# Translators:  (emo) Emo;
	(r'(\s|^)\(emo\)(\B|\s|$)', _("smiley Emo")),
	# Translators:  (y) Yes
	(r'(\s|^)\(y\)(\B|\s|$)', _("smiley Yes")),
	# Translators:  (n) no;
	(r'(\s|^)\(n\)(\B|\s|$)', _("smiley NO")),
	# Translators:  (handshake) Handshake
	(r'(\s|^)\(handshake\)(\B|\s|$)', _("smiley Handshake")),
	# Translators:  (highfive) High five
	(r'(\s|^)\(highfive\)(\B|\s|$)', _("smiley High five")),
	# Translators:  (heart) Heart
	(r'(\s|^)\(heart\)(\B|\s|$)', _("smiley Heart")),
	# Translators:  (lalala) Lalala;
	(r'(\s|^)\(lalala\)(\B|\s|$)', _("smiley LaLaLa")),
	# Translators:  (heidy) Heidy;
	(r'(\s|^)\(heidy\)(\B|\s|$)', _("smiley Heidy")),
	# Translators:  (F) Flower
	(r'(\s|^)\(F\)(\B|\s|$)', _("smiley Flower")),
	# Translators:  (rain) Raining
	(r'(\s|^)\(rain\)(\B|\s|$)', _("smiley Raining")),
	# Translators:  (sun) Sun
	(r'(\s|^)\(sun\)(\B|\s|$)', _("smiley Sun")),
	# Translators:  (tumbleweed) Tumbleweed
	(r'(\s|^)\(tumbleweed\)(\B|\s|$)', _("smiley Tumbleweed")),
	# Translators:  (music) Music
	(r'(\s|^)\(music\)(\B|\s|$)', _("smiley Music")),
	# Translators:  (bandit) Bandit
	(r'(\s|^)\(bandit\)(\B|\s|$)', _("smiley Bandit")),
	# Translators:  (tmi) Too much information
	(r'(\s|^)\(tmi\)(\B|\s|$)', _("smiley Too much information")),
	# Translators:  (coffee) Coffee
	(r'(\s|^)\(coffee\)(\B|\s|$)', _("smiley Coffee")),
	# Translators:  (pi) Pizza
	(r'(\s|^)\(pi\)(\B|\s|$)', _("smiley Pizza")),
	# Translators:  (cash) Cash
	(r'(\s|^)\(cash\)(\B|\s|$)', _("smiley Cash")),
	# Translators:  (flex) Muscle
	(r'(\s|^)\(flex\)(\B|\s|$)', _("smiley Muscle")),
	# Translators:  (^) Cake
	(r'(\s|^)([\(][\^][\)])(\B|\s|$)', _("smiley Cake")),
	# Translators:  (beer) Beer
	(r'(\s|^)\(beer\)(\B|\s|$)', _("smiley Beer")),
	# Translators:  (d) Drink
	(r'(\s|^)\(d\)(\B|\s|$)', _("smiley Drink")),
	# Translators:  \o/ Dancing
	(r'(\s|^)([\\]o[/])(\B|\s|$)', _("smiley Dancing")),
	# Translators:  (ninja) Ninja
	(r'(\s|^)\(ninja\)(\B|\s|$)', _("smiley Ninja")),
	# Translators:  (*) Star
	(r'(\s|^)([\(][\*][\)])(\B|\s|$)', _("smiley Star")),
	# Translators:  Facebook  Smiley  :'( Crying
	("(\s|^)([:]['][\(])(\B|\s|$)", _("smiley Crying")),
	# Translators:  >:( Angry
	(r'(\s|^)(>:[\(])(\B|\s|$)', _("smiley Angry")),
	# Translators:  :/ Worried
	(r'(\s|^)(:[/])(\B|\s|$)', _("smiley Worried")),
	# Translators:  <3 Heart
	(r'(\s|^)<3(\W|\s|$)', _("smiley Heart")),
	# Translators: regex for Facebook contacts  in Skype v.5 series only.
	(r'\(xmpp:-([0-9]+)@chat.facebook.com\)', _("(facebook)")),
]

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	scriptCategory = SCRCAT_SPEECH

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
		for pattern, replacement in emoticons:
			comment = _("Emoticon: %s") % replacement
			otherReplacement = " %s; " % replacement
			self.SD.append(speechDictHandler.SpeechDictEntry(pattern, otherReplacement, comment, True, True)) # Case and reg are always True

	def terminate(self):
		self.deactivateEmoticons()
		self.SD = None

	def script_toggleSpeakingEmoticons(self, gesture):
		if self.emoticons:
			self.deactivateEmoticons()
			# Translators: message presented when the dictionary for emoticons is unloaded.
			ui.message(_("Emoticons off."))
		else:
			self.activateEmoticons()
			# Translators: message presented when the dictionary for emoticons is loaded.
			ui.message(_("Emoticons on."))
	# Translators: Message presented in input help mode.
	script_toggleSpeakingEmoticons.__doc__ = _("Toggles on and off the announcement of emoticons.")

	__gestures = {
		"kb:NVDA+e": "toggleSpeakingEmoticons",
	}
