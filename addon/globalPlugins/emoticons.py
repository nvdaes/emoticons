# -*- coding: UTF-8 -*-

import globalPluginHandler
import speechDictHandler
import ui
import addonHandler

addonHandler.initTranslation()

emoticons = [
	# Translators:  :) Smile
	('(\s|^)(:([\-]|)([)]{1})(\B|\s|$))', _("\1smiley Smile"), True, True),
	# Translators:  :( Sad
	('(\s|^)(:([\-]|)([(]{1})\B)', _("smiley Sad"), True, True),
	# Translators:   :D Laugh
	('(\s|^)(:([\-]|)([D]{1,})\b)', _("smiley Laugh"), True, True),
	# Translators:  (cool) Cool
	('(\s|^)\(cool\)(\B|\s|$)', _("smiley Cool"), True, True),
	# Translators:  :O Surprised
	('(\s|^)(:([\-]|)([O]{1})(\W|\s|$))', _("smiley Surprised"), True, True),
	# Translators:  ;) Wink;
	('(\s|^)(;([\-]|)([)D]{1})(\B|\s|$))', _("smiley Wink"), True, True),
	# Translators:  ;( Crying
	('(\s|^)(;([\-]|)([(]{1})(\B|\s|$))', _("smiley Crying"), True, True),
	# Translators:  (:| Sweating
	('(\s|^)\((:[\|])(\B|\s|$)', _("smiley Sweating"), True, True),
	# Translators:  :| Speechless
	('(\s|^)(:[\|])(\B|\s|$)', _("smiley Speechless"), True, True),
	# Translators:  :* Kiss
	('(\s|^)(:([\-]|)([\*]{1})(\B|\s|$))', _("smiley Kiss"), True, True),
	# Translators:  :P Cheeky
	('(\s|^)(:([\-]|)([pP])(\W|\s|$))', _("smiley Cheeky"), True, True),
	# Translators:  :$ Blushing
	('(\s|^)(:[\$])(\B|\s|$)', _("smiley Blushing"), True, True),
	# Translators:  :^) Wondering
	('(\s|^)(:[\^][\)])(\B|\s|$)', _("smiley Wondering"), True, True),
	# Translators:  |-) Sleepy
	('(\s|^)([\|][\-][\)])(\B|\s|$)', _("smiley Sleepy"), True, True),
	# Translators:  |-( Dull
	('(\s|^)([\|][\-][\(])(\B|\s|$)', _("smiley Dull"), True, True),
	# Translators:  (inlove) In Love
	('(\s|^)\(inlove\)(\B|\s|$)', _("smiley In Love"), True, True),
	# Translators:  ]:) Evil grin
	('(\s|^)()\]:\)(\B|\s|$)', _("smiley Evil grin"), True, True),
	# Translators:  (yn) Fingers crossed
	('(\s|^)([\(]yn[\)])(\B|\s|$)', _("smiley Fingers crossed"), True, True),
	# Translators:  (yawn) Yawn
	('(\s|^)\(yawn\)(\B|\s|$)', _("smiley Yawn"), True, True),
	# Translators:  (puke) Puking
	('(\s|^)\(puke\)(\B|\s|$)', _("smiley Puking"), True, True),
	# Translators:  (doh) Doh!
	('(\s|^)\(doh\)(\B|\s|$)', _("smiley Doh! "), True, True),
	# Translators:  (angry) Angry
	('(\s|^)\(angry\)(\B|\s|$)', _("smiley Angry"), True, True),
	# Translators:  (wasntme) It wasn't me!
	('(\s|^)\(wasntme\)(\B|\s|$)', _("smiley It wasn't me! "), True, True),
	# Translators:  (party) Party
	('(\s|^)\(party\)(\B|\s|$)', _("smiley Party"), True, True),
	# Translators:  (worry) Worried
	('(\s|^)\(worry\)(\B|\s|$)', _("smiley Worried"), True, True),
	# Translators:  (mm) Mmmm...
	('(\s|^)\(mm\)(\B|\s|$)', _("smiley mmmmmm..."), True, True),
	# Translators:  (nerd) Nerdy
	('(\s|^)\(nerd\)(\B|\s|$)', _("smiley Nerdy;"), True, True),
	# Translators:  :x My lips are sealed
	('(\s|^)(:([\-]|)([xX])\b)', _("smiley My lips are sealed"), True, True),
	# Translators:  (wave) Hi
	('(\s|^)\(wave\)(\B|\s|$)', _("smiley Hi"), True, True),
	# Translators:  (facepalm) Facepalm
	('(\s|^)\(facepalm\)(\B|\s|$)', _("smiley Facepalm"), True, True),
	# Translators:  (devil) Devil
	('(\s|^)\(devil\)(\B|\s|$)', _("smiley Devil"), True, True),
	# Translators:  (angel) Angel
	('(\s|^)\(angel\)(\B|\s|$)', _("smiley Angel"), True, True),
	# Translators:  (envy) Envy
	('(\s|^)\(envy\)(\B|\s|$)', _("smileyEnvy"), True, True),
	# Translators:  (wait) Wait
	('(\s|^)\(wait\)(\B|\s|$)', _("smiley Wait"), True, True),
	# Translators:  (hug) Hug
	('(\s|^)\(hug\)(\B|\s|$)', _("smiley Hug"), True, True),
	# Translators:  (makeup) Make-up
	('(\s|^)\(makeup\)(\B|\s|$)', _("smiley Make-up"), True, True),
	# Translators:  (chuckle) Giggle
	('(\s|^)\(chuckle\)(\B|\s|$)', _("smiley Giggle;"), True, True),
	# Translators:  (clap) Clapping
	('(\s|^)\(clap\)(\B|\s|$)', _("smiley Clapping"), True, True),
	# Translators:  (think) Thinking
	('(\s|^)\(think\)(\B|\s|$)', _("smiley Thinking"), True, True),
	# Translators:  (bow) Bowing
	('(\s|^)\(bow\)(\B|\s|$)', _("smiley Bowing"), True, True),
	# Translators:  (rofl) Rolling on the floor laughing
	('(\s|^)\(rofl\)(\B|\s|$)', _("smiley Rolling on the floor laughing! "), True, True),
	# Translators:  (whew) Relieved
	('(\s|^)\(whew\)(\B|\s|$)', _("smiley Relieved"), True, True),
	# Translators:  (happy) Happy
	('(\s|^)\(happy\)(\B|\s|$)', _("smiley Happy"), True, True),
	# Translators:  (smirk) Smirking
	('(\s|^)\(smirk\)(\B|\s|$)', _("smiley Smirking"), True, True),
	# Translators:  (nod) Nodding
	('(\s|^)\(nod\)(\B|\s|$)', _("smiley Nodding;"), True, True),
	# Translators:  (shake) Shake
	('(\s|^)\(shake\)(\B|\s|$)', _("smiley Shake"), True, True),
	# Translators:  (waiting) Waiting
	('(\s|^)\(waiting\)(\B|\s|$)', _("smiley Waiting"), True, True),
	# Translators:  (emo) Emo;
	('(\s|^)\(emo\)(\B|\s|$)', _("smiley Emo"), True, True),
	# Translators:  (y) Yes
	('(\s|^)\(y\)(\B|\s|$)', _("smiley Yes"), True, True),
	# Translators:  (n) no;
	('(\s|^)\(n\)(\B|\s|$)', _("smiley NO"), True, True),
	# Translators:  (handshake) Handshake
	('(\s|^)\(handshake\)(\B|\s|$)', _("smiley Handshake;"), True, True),
	# Translators:  (highfive) High five
	('(\s|^)\(highfive\)(\B|\s|$)', _("smiley High five"), True, True),
	# Translators:  (heart) Heart
	('(\s|^)\(heart\)(\B|\s|$)', _("smiley Heart"), True, True),
	# Translators:  (lalala) Lalala;
	('(\s|^)\(lalala\)(\B|\s|$)', _("smiley LaLaLa"), True, True),
	# Translators:  (heidy) Heidy;
	('(\s|^)\(heidy\)(\B|\s|$)', _("smiley Heidy;"), True, True),
	# Translators:  (F) Flower
	('(\s|^)\(F\)(\B|\s|$)', _("smiley Flower"), True, True),
	# Translators:  (rain) Raining
	('(\s|^)\(rain\)(\B|\s|$)', _("smiley Raining"), True, True),
	# Translators:  (sun) Sun
	('(\s|^)\(sun\)(\B|\s|$)', _("smiley Sun"), True, True),
	# Translators:  (tumbleweed) Tumbleweed
	('(\s|^)\(tumbleweed\)(\B|\s|$)', _("smiley Tumbleweed"), True, True),
	# Translators:  (music) Music
	('(\s|^)\(music\)(\B|\s|$)', _("smiley Music"), True, True),
	# Translators:  (bandit) Bandit
	('(\s|^)\(bandit\)(\B|\s|$)', _("smiley Bandit"), True, True),
	# Translators:  (tmi) Too much information
	('(\s|^)\(tmi\)(\B|\s|$)', _("smiley Too much information;"), True, True),
	# Translators:  (coffee) Coffee
	('(\s|^)\(coffee\)(\B|\s|$)', _("smiley Coffee"), True, True),
	# Translators:  (pi) Pizza
	('(\s|^)\(pi\)(\B|\s|$)', _("smiley Pizza"), True, True),
	# Translators:  (cash) Cash
	('(\s|^)\(cash\)(\B|\s|$)', _("smiley Cash"), True, True),
	# Translators:  (flex) Muscle
	('(\s|^)\(flex\)(\B|\s|$)', _("smiley Muscle"), True, True),
	# Translators:  (^) Cake
	('(\s|^)([\(][\^][\)])(\B|\s|$)', _("smiley Cake"), True, True),
	# Translators:  (beer) Beer
	('(\s|^)\(beer\)(\B|\s|$)', _("smiley Beer"), True, True),
	# Translators:  (d) Drink
	('(\s|^)\(d\)(\B|\s|$)', _("smiley Drink;"), True, True),
	# Translators:  \o/ Dancing
	('(\s|^)([\\]o[/])(\B|\s|$)', _("smiley Dancing"), True, True),
	# Translators:  (ninja) Ninja
	('(\s|^)\(ninja\)(\B|\s|$)', _("smiley Ninja;"), True, True),
	# Translators:  (*) Star
	('(\s|^)([\(][\*][\)])(\B|\s|$)', _("smiley Star"), True, True),
	# Translators:  Facebook  Smiley  :'( Crying
	("(\s|^)([:]['][\(])(\B|\s|$)", _("smiley Crying"), True, True),
	# Translators:  >:( Angry
	('(\s|^)(>:[\(])(\B|\s|$)', _("smiley Angry"), True, True),
	# Translators:  :/ Worried
	('(\s|^)(:[/])(\B|\s|$)', _("smiley Worried"), True, True),
	# Translators:  <3 Heart
	('(\s|^)<3(\W|\s|$)', _("smiley Heart"), True, True),
	# Translators: regex for Facebook contacts  in Skype v.5 series only.
	('\(xmpp:-([0-9]+)@chat.facebook.com\)', _("(facebook)"), True, True),
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
		for pattern, replacement, case, reg in emoticons:
			comment = "Emoticon: %s" % replacement
			otherReplacement = " %s; " % replacement
			self.SD.append(speechDictHandler.SpeechDictEntry(pattern, otherReplacement, comment, case, reg))

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
