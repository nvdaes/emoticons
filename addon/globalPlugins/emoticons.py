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
	(r'(\s|^)(:([\-]|)([)]{1})(\B|\s|$))', _("smiling smiley")),
	# Translators:  :( Sad
	(r'(\s|^)(:([\-]|)([(]{1})\B)', _("sad smiley")),
	# Translators:   :D Laugh
	(r'(\s|^)(:([\-]|)([D]{1,})\b)', _("Laughing smiley")),
	# Translators:  (cool) Cool
	(r'(\s|^)\(cool\)(\B|\s|$)', _("cool smiley")),
	# Translators:  :O Surprised
	(r'(\s|^)(:([\-]|)([O]{1})(\W|\s|$))', _("surprised smiley")),
	# Translators:  ;) Wink;
	(r'(\s|^)(;([\-]|)([)D]{1})(\B|\s|$))', _("winking smiley")),
	# Translators:  ;( Crying
	(r'(\s|^)(;([\-]|)([(]{1})(\B|\s|$))', _("crying smiley")),
	# Translators:  (:| Sweating
	(r'(\s|^)\((:[\|])(\B|\s|$)', _("sweating smiley")),
	# Translators:  :| Speechless
	(r'(\s|^)(:[\|])(\B|\s|$)', _("speechless smiley")),
	# Translators:  :* Kiss
	(r'(\s|^)(:([\-]|)([\*]{1})(\B|\s|$))', _("kiss smiley")),
	# Translators:  :P Cheeky
	(r'(\s|^)(:([\-]|)([pP])(\W|\s|$))', _("cheeky smiley")),
	# Translators:  :$ Blushing
	(r'(\s|^)(:[\$])(\B|\s|$)', _("blushing smiley")),
	# Translators:  :^) Wondering
	(r'(\s|^)(:[\^][\)])(\B|\s|$)', _("wondering smiley")),
	# Translators:  |-) Sleepy
	(r'(\s|^)([\|][\-][\)])(\B|\s|$)', _("sleepy smiley")),
	# Translators:  |-( Dull
	(r'(\s|^)([\|][\-][\(])(\B|\s|$)', _("dull smiley")),
	# Translators:  (inlove) In Love
	(r'(\s|^)\(inlove\)(\B|\s|$)', _("in love smiley")),
	# Translators:  ]:) Evil grin
	(r'(\s|^)()\]:\)(\B|\s|$)', _("evil grin smiley")),
	# Translators:  (yn) Fingers crossed
	(r'(\s|^)([\(]yn[\)])(\B|\s|$)', _("fingers crossed smiley")),
	# Translators:  (yawn) Yawn
	(r'(\s|^)\(yawn\)(\B|\s|$)', _("yawning smiley")),
	# Translators:  (puke) Puking
	(r'(\s|^)\(puke\)(\B|\s|$)', _("puking smiley")),
	# Translators:  (doh) Doh!
	(r'(\s|^)\(doh\)(\B|\s|$)', _("doh! smiley")),
	# Translators:  (angry) Angry
	(r'(\s|^)\(angry\)(\B|\s|$)', _("angry smiley")),
	# Translators:  (wasntme) It wasn't me!
	(r'(\s|^)\(wasntme\)(\B|\s|$)', _("it wasn't me! smiley")),
	# Translators:  (party) Party
	(r'(\s|^)\(party\)(\B|\s|$)', _("party smiley")),
	# Translators:  (worry) Worried
	(r'(\s|^)\(worry\)(\B|\s|$)', _("worried smiley")),
	# Translators:  (mm) Mmmm...
	(r'(\s|^)\(mm\)(\B|\s|$)', _("mmmmmm... smiley")),
	# Translators:  (nerd) Nerdy
	(r'(\s|^)\(nerd\)(\B|\s|$)', _("nerdy smiley")),
	# Translators:  :x My lips are sealed
	(r'(\s|^)(:([\-]|)([xX])\b)', _("my lips are sealed smiley")),
	# Translators:  (wave) Hi
	(r'(\s|^)\(wave\)(\B|\s|$)', _("hi smiley")),
	# Translators:  (facepalm) Facepalm
	(r'(\s|^)\(facepalm\)(\B|\s|$)', _("facepalm smiley")),
	# Translators:  (devil) Devil
	(r'(\s|^)\(devil\)(\B|\s|$)', _("devil smiley")),
	# Translators:  (angel) Angel
	(r'(\s|^)\(angel\)(\B|\s|$)', _("angel smiley")),
	# Translators:  (envy) Envy
	(r'(\s|^)\(envy\)(\B|\s|$)', _("envy smiley")),
	# Translators:  (wait) Wait
	(r'(\s|^)\(wait\)(\B|\s|$)', _("wait smiley")),
	# Translators:  (hug) Hug
	(r'(\s|^)\(hug\)(\B|\s|$)', _("hug smiley")),
	# Translators:  (makeup) Make-up
	(r'(\s|^)\(makeup\)(\B|\s|$)', _("make-up smiley")),
	# Translators:  (chuckle) Giggle
	(r'(\s|^)\(chuckle\)(\B|\s|$)', _("giggle smiley")),
	# Translators:  (clap) Clapping
	(r'(\s|^)\(clap\)(\B|\s|$)', _("clapping smiley")),
	# Translators:  (think) Thinking
	(r'(\s|^)\(think\)(\B|\s|$)', _("thinking smiley")),
	# Translators:  (bow) Bowing
	(r'(\s|^)\(bow\)(\B|\s|$)', _("bowing smiley")),
	# Translators:  (rofl) Rolling on the floor laughing
	(r'(\s|^)\(rofl\)(\B|\s|$)', _("rolling on the floor laughing! smiley")),
	# Translators:  (whew) Relieved
	(r'(\s|^)\(whew\)(\B|\s|$)', _("relieved smiley")),
	# Translators:  (happy) Happy
	(r'(\s|^)\(happy\)(\B|\s|$)', _("happy smiley")),
	# Translators:  (smirk) Smirking
	(r'(\s|^)\(smirk\)(\B|\s|$)', _("smirking smiley")),
	# Translators:  (nod) Nodding
	(r'(\s|^)\(nod\)(\B|\s|$)', _("nodding smiley")),
	# Translators:  (shake) Shake
	(r'(\s|^)\(shake\)(\B|\s|$)', _("shakeing smiley")),
	# Translators:  (waiting) Waiting
	(r'(\s|^)\(waiting\)(\B|\s|$)', _("waiting smiley")),
	# Translators:  (emo) Emo;
	(r'(\s|^)\(emo\)(\B|\s|$)', _("Emo smiley")),
	# Translators:  (y) Yes
	(r'(\s|^)\(y\)(\B|\s|$)', _("yes smiley")),
	# Translators:  (n) no;
	(r'(\s|^)\(n\)(\B|\s|$)', _("nO smiley")),
	# Translators:  (handshake) Handshake
	(r'(\s|^)\(handshake\)(\B|\s|$)', _("handshake smiley")),
	# Translators:  (highfive) High five
	(r'(\s|^)\(highfive\)(\B|\s|$)', _("high five smiley")),
	# Translators:  (heart) Heart
	(r'(\s|^)\(heart\)(\B|\s|$)', _("heart smiley")),
	# Translators:  (lalala) Lalala;
	(r'(\s|^)\(lalala\)(\B|\s|$)', _("lalala smiley")),
	# Translators:  (heidy) Heidy;
	(r'(\s|^)\(heidy\)(\B|\s|$)', _("heidy smiley")),
	# Translators:  (F) Flower
	(r'(\s|^)\(F\)(\B|\s|$)', _("flower smiley")),
	# Translators:  (rain) Raining
	(r'(\s|^)\(rain\)(\B|\s|$)', _("raining smiley")),
	# Translators:  (sun) Sun
	(r'(\s|^)\(sun\)(\B|\s|$)', _("sunny smiley")),
	# Translators:  (tumbleweed) Tumbleweed
	(r'(\s|^)\(tumbleweed\)(\B|\s|$)', _("tumbleweed smiley")),
	# Translators:  (music) Music
	(r'(\s|^)\(music\)(\B|\s|$)', _("music smiley")),
	# Translators:  (bandit) Bandit
	(r'(\s|^)\(bandit\)(\B|\s|$)', _("bandit smiley")),
	# Translators:  (tmi) Too much information
	(r'(\s|^)\(tmi\)(\B|\s|$)', _("too much information smiley")),
	# Translators:  (coffee) Coffee
	(r'(\s|^)\(coffee\)(\B|\s|$)', _("coffee smiley")),
	# Translators:  (pi) Pizza
	(r'(\s|^)\(pi\)(\B|\s|$)', _("pizza smiley")),
	# Translators:  (cash) Cash
	(r'(\s|^)\(cash\)(\B|\s|$)', _("cash smiley")),
	# Translators:  (flex) Muscle
	(r'(\s|^)\(flex\)(\B|\s|$)', _("muscle smiley")),
	# Translators:  (^) Cake
	(r'(\s|^)([\(][\^][\)])(\B|\s|$)', _("cake smiley")),
	# Translators:  (beer) Beer
	(r'(\s|^)\(beer\)(\B|\s|$)', _("beer smiley")),
	# Translators:  (d) Drink
	(r'(\s|^)\(d\)(\B|\s|$)', _("drink smiley")),
	# Translators:  \o/ Dancing
	(r'(\s|^)([\\]o[/])(\B|\s|$)', _("dancing smiley")),
	# Translators:  (ninja) Ninja
	(r'(\s|^)\(ninja\)(\B|\s|$)', _("ninja smiley")),
	# Translators:  (*) Star
	(r'(\s|^)([\(][\*][\)])(\B|\s|$)', _("star smiley")),
	# Translators:  Facebook  Smiley  :'( Crying
	("(\s|^)([:]['][\(])(\B|\s|$)", _("crying smiley")),
	# Translators:  >:( Angry
	(r'(\s|^)(>:[\(])(\B|\s|$)', _("angry smiley")),
	# Translators:  :/ Worried
	(r'(\s|^)(:[/])(\B|\s|$)', _("worried smiley")),
	# Translators:  <3 Heart
	(r'(\s|^)<3(\W|\s|$)', _("heart smiley")),
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
			# Translators: A prefix to each emoticon name, added to the temporary speech dictionary, visible in temporary speech dictionary dialog when the addon is active, to explain an entry.
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
