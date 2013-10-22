# -*- coding: UTF-8 -*-

from collections import namedtuple

import globalPluginHandler
import speechDictHandler
import ui
import addonHandler

try:
	from globalCommands import SCRCAT_SPEECH
except:
	SCRCAT_SPEECH = None

addonHandler.initTranslation()

Smiley = namedtuple('Smiley', 'pattern name chars')
emoticons = [
	# Translators: :) Smile
	Smiley(r'(\s|^)(:([\-]|)([)]{1})(\B|\s|$))', _("smiling smiley"), r':)'),
	# Translators: :( Sad
	Smiley(r'(\s|^)(:([\-]|)([(]{1})\B)', _("sad smiley"), r':('),
	# Translators: :D Laugh
	Smiley(r'(\s|^)(:([\-]|)([D]{1,})\b)', _("Laughing smiley"), r':D'),
	# Translators: (cool) Cool
	Smiley(r'(\s|^)\(cool\)(\B|\s|$)', _("cool smiley"), r'(cool)'),
	# Translators: :O Surprised
	Smiley(r'(\s|^)(:([\-]|)([O]{1})(\W|\s|$))', _("surprised smiley"), r':O'),
	# Translators: ;) Wink;
	Smiley(r'(\s|^)(;([\-]|)([)D]{1})(\B|\s|$))', _("winking smiley"), r';)'),
	# Translators: ;( Crying
	Smiley(r'(\s|^)(;([\-]|)([(]{1})(\B|\s|$))', _("crying smiley"), r';('),
	# Translators: (:| Sweating
	Smiley(r'(\s|^)\((:[\|])(\B|\s|$)', _("sweating smiley"), r'(:|'),
	# Translators: :| Speechless
	Smiley(r'(\s|^)(:[\|])(\B|\s|$)', _("speechless smiley"), r':|'),
	# Translators: :* Kiss
	Smiley(r'(\s|^)(:([\-]|)([\*]{1})(\B|\s|$))', _("kiss smiley"), r':*'),
	# Translators: :P Cheeky
	Smiley(r'(\s|^)(:([\-]|)([pP])(\W|\s|$))', _("cheeky smiley"), r':P'),
	# Translators: :$ Blushing
	Smiley(r'(\s|^)(:[\$])(\B|\s|$)', _("blushing smiley"), r':$'),
	# Translators: :^) Wondering
	Smiley(r'(\s|^)(:[\^][\)])(\B|\s|$)', _("wondering smiley"), r':^)'),
	# Translators: |-) Sleepy
	Smiley(r'(\s|^)([\|][\-][\)])(\B|\s|$)', _("sleepy smiley"), r'|-)'),
	# Translators: |-( Dull
	Smiley(r'(\s|^)([\|][\-][\(])(\B|\s|$)', _("dull smiley"), r'|-('),
	# Translators: (inlove) In Love
	Smiley(r'(\s|^)\(inlove\)(\B|\s|$)', _("in love smiley"), r'(inlove)'),
	# Translators: ]:) Evil grin
	Smiley(r'(\s|^)()\]:\)(\B|\s|$)', _("evil grin smiley"), r']:)'),
	# Translators: (yn) Fingers crossed
	Smiley(r'(\s|^)([\(]yn[\)])(\B|\s|$)', _("fingers crossed smiley"), r'(yn)'),
	# Translators: (yawn) Yawn
	Smiley(r'(\s|^)\(yawn\)(\B|\s|$)', _("yawning smiley"), r'(yawn)'),
	# Translators: (puke) Puking
	Smiley(r'(\s|^)\(puke\)(\B|\s|$)', _("puking smiley"), r'(puke)'),
	# Translators: (doh) Doh!
	Smiley(r'(\s|^)\(doh\)(\B|\s|$)', _("doh! smiley"), r'(doh)'),
	# Translators: (angry) Angry
	Smiley(r'(\s|^)\(angry\)(\B|\s|$)', _("angry smiley"), r'(angry)'),
	# Translators: (wasntme) It wasn't me!
	Smiley(r'(\s|^)\(wasntme\)(\B|\s|$)', _("it wasn't me! smiley"), r'(wasntme)'),
	# Translators: (party) Party
	Smiley(r'(\s|^)\(party\)(\B|\s|$)', _("party smiley"), r'(party)'),
	# Translators: (worry) Worried
	Smiley(r'(\s|^)\(worry\)(\B|\s|$)', _("worried smiley"), r'(worry)'),
	# Translators: (mm) Mmmm...
	Smiley(r'(\s|^)\(mm\)(\B|\s|$)', _("mmmmmm... smiley"), r'(mm)'),
	# Translators: (nerd) Nerdy
	Smiley(r'(\s|^)\(nerd\)(\B|\s|$)', _("nerdy smiley"), r'(nerd)'),
	# Translators: :x My lips are sealed
	Smiley(r'(\s|^)(:([\-]|)([xX])\b)', _("my lips are sealed smiley"), r':x'),
	# Translators: (wave) Hi
	Smiley(r'(\s|^)\(wave\)(\B|\s|$)', _("hi smiley"), r'(wave)'),
	# Translators: (facepalm) Facepalm
	Smiley(r'(\s|^)\(facepalm\)(\B|\s|$)', _("facepalm smiley"), r'(facepalm)'),
	# Translators: (devil) Devil
	Smiley(r'(\s|^)\(devil\)(\B|\s|$)', _("devil smiley"), r'(devil)'),
	# Translators: (angel) Angel
	Smiley(r'(\s|^)\(angel\)(\B|\s|$)', _("angel smiley"), r'(angel)'),
	# Translators: (envy) Envy
	Smiley(r'(\s|^)\(envy\)(\B|\s|$)', _("envy smiley"), r'(envy)'),
	# Translators: (wait) Wait
	Smiley(r'(\s|^)\(wait\)(\B|\s|$)', _("wait smiley"), r'(wait)'),
	# Translators: (hug) Hug
	Smiley(r'(\s|^)\(hug\)(\B|\s|$)', _("hug smiley"), r'(hug)'),
	# Translators: (makeup) Make-up
	Smiley(r'(\s|^)\(makeup\)(\B|\s|$)', _("make-up smiley"), r'(makeup)'),
	# Translators: (chuckle) Giggle
	Smiley(r'(\s|^)\(chuckle\)(\B|\s|$)', _("giggle smiley"), r'(chuckle)'),
	# Translators: (clap) Clapping
	Smiley(r'(\s|^)\(clap\)(\B|\s|$)', _("clapping smiley"), r'(clap)'),
	# Translators: (think) Thinking
	Smiley(r'(\s|^)\(think\)(\B|\s|$)', _("thinking smiley"), r'(think)'),
	# Translators: (bow) Bowing
	Smiley(r'(\s|^)\(bow\)(\B|\s|$)', _("bowing smiley"), r'(bow)'),
	# Translators: (rofl) Rolling on the floor laughing
	Smiley(r'(\s|^)\(rofl\)(\B|\s|$)', _("rolling on the floor laughing! smiley"), r'(rofl)'),
	# Translators: (whew) Relieved
	Smiley(r'(\s|^)\(whew\)(\B|\s|$)', _("relieved smiley"), r'(whew)'),
	# Translators: (happy) Happy
	Smiley(r'(\s|^)\(happy\)(\B|\s|$)', _("happy smiley"), r'(happy)'),
	# Translators: (smirk) Smirking
	Smiley(r'(\s|^)\(smirk\)(\B|\s|$)', _("smirking smiley"), r'(smirk)'),
	# Translators: (nod) Nodding
	Smiley(r'(\s|^)\(nod\)(\B|\s|$)', _("nodding smiley"), r'(nod)'),
	# Translators: (shake) Shake
	Smiley(r'(\s|^)\(shake\)(\B|\s|$)', _("shakeing smiley"), r'(shake)'),
	# Translators: (waiting) Waiting
	Smiley(r'(\s|^)\(waiting\)(\B|\s|$)', _("waiting smiley"), r'(waiting)'),
	# Translators: (emo) Emo;
	Smiley(r'(\s|^)\(emo\)(\B|\s|$)', _("Emo smiley"), r'(emo)'),
	# Translators: (y) Yes
	Smiley(r'(\s|^)\(y\)(\B|\s|$)', _("yes smiley"), r'(y)'),
	# Translators: (n) no;
	Smiley(r'(\s|^)\(n\)(\B|\s|$)', _("nO smiley"), r'(n)'),
	# Translators: (handshake) Handshake
	Smiley(r'(\s|^)\(handshake\)(\B|\s|$)', _("handshake smiley"), r'(handshake)'),
	# Translators: (highfive) High five
	Smiley(r'(\s|^)\(highfive\)(\B|\s|$)', _("high five smiley"), r'(highfive)'),
	# Translators: (heart) Heart
	Smiley(r'(\s|^)\(heart\)(\B|\s|$)', _("heart smiley"), r'(heart)'),
	# Translators: (lalala) Lalala;
	Smiley(r'(\s|^)\(lalala\)(\B|\s|$)', _("lalala smiley"), r'(lalala)'),
	# Translators: (heidy) Heidy;
	Smiley(r'(\s|^)\(heidy\)(\B|\s|$)', _("heidy smiley"), r'(heidy)'),
	# Translators: (F) Flower
	Smiley(r'(\s|^)\(F\)(\B|\s|$)', _("flower smiley"), r'(F)'),
	# Translators: (rain) Raining
	Smiley(r'(\s|^)\(rain\)(\B|\s|$)', _("raining smiley"), r'(rain)'),
	# Translators: (sun) Sun
	Smiley(r'(\s|^)\(sun\)(\B|\s|$)', _("sunny smiley"), r'(sun)'),
	# Translators: (tumbleweed) Tumbleweed
	Smiley(r'(\s|^)\(tumbleweed\)(\B|\s|$)', _("tumbleweed smiley"), r'(tumbleweed)'),
	# Translators: (music) Music
	Smiley(r'(\s|^)\(music\)(\B|\s|$)', _("music smiley"), r'(music)'),
	# Translators: (bandit) Bandit
	Smiley(r'(\s|^)\(bandit\)(\B|\s|$)', _("bandit smiley"), r'(bandit)'),
	# Translators: (tmi) Too much information
	Smiley(r'(\s|^)\(tmi\)(\B|\s|$)', _("too much information smiley"), r'(tmi)'),
	# Translators: (coffee) Coffee
	Smiley(r'(\s|^)\(coffee\)(\B|\s|$)', _("coffee smiley"), r'(coffee)'),
	# Translators: (pi) Pizza
	Smiley(r'(\s|^)\(pi\)(\B|\s|$)', _("pizza smiley"), r'(pi)'),
	# Translators:  (cash) Cash
	Smiley(r'(\s|^)\(cash\)(\B|\s|$)', _("cash smiley"), r'(cash)'),
	# Translators: (flex) Muscle
	Smiley(r'(\s|^)\(flex\)(\B|\s|$)', _("muscle smiley"), r'(flex)'),
	# Translators: (^) Cake
	Smiley(r'(\s|^)([\(][\^][\)])(\B|\s|$)', _("cake smiley"), r'(^)'),
	# Translators: (beer) Beer
	Smiley(r'(\s|^)\(beer\)(\B|\s|$)', _("beer smiley"), r'(beer)'),
	# Translators: (d) Drink
	Smiley(r'(\s|^)\(d\)(\B|\s|$)', _("drink smiley"), r'(d)'),
	# Translators: \o/ Dancing
	Smiley(r'(\s|^)([\\]o[/])(\B|\s|$)', _("dancing smiley"), r'\o/'),
	# Translators: (ninja) Ninja
	Smiley(r'(\s|^)\(ninja\)(\B|\s|$)', _("ninja smiley"), r'(ninja)'),
	# Translators: (*) Star
	Smiley(r'(\s|^)([\(][\*][\)])(\B|\s|$)', _("star smiley"), r'(*)'),
	# Translators: :'( crying a lot smiley
	Smiley(r"(\s|^)([:]['][\(])(\B|\s|$)", _("crying a lot smiley"), r":'("),
	# Translators: >:( Angry
	Smiley(r'(\s|^)(>:[\(])(\B|\s|$)', _("angry smiley"), r'>:('),
	# Translators: :/ Worried
	Smiley(r'(\s|^)(:[/])(\B|\s|$)', _("worried smiley"), r':/'),
	# Translators: <3 Heart
	Smiley(r'(\s|^)<3(\W|\s|$)', _("heart smiley"), r'<3'),
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
		for em in emoticons:
			# Translators: A prefix to each emoticon name, added to the temporary speech dictionary, visible in temporary speech dictionary dialog when the addon is active, to explain an entry.
			comment = _("Emoticon: %s") % em.name
			otherReplacement = " %s; " % em.name
			# Case and reg are always True
			self.SD.append(speechDictHandler.SpeechDictEntry(em.pattern, otherReplacement, comment, True, True))


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
