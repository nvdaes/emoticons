# -*- coding: UTF-8 -*-

import globalPluginHandler
import speechDictHandler
import ui
import addonHandler

addonHandler.initTranslation()

emoticons = [
	# Translators:  :) Smile
	(r'(\s|^)(:([\-]|)([)]{1})(\B|\s|$))', _("\1smiley Smile"), True, True),
	# Translators:  :( Sad
	(r'(\s|^)(:([\-]|)([(]{1})\B)', _("smiley Sad"), True, True),
	# Translators:   :D Laugh
	(r'(\s|^)(:([\-]|)([D]{1,})\b)', _("smiley Laugh"), True, True),
	# Translators:  (cool) Cool
	(r'(\s|^)\(cool\)(\B|\s|$)', _("smiley Cool"), True, True),
	# Translators:  :O Surprised
	(r'(\s|^)(:([\-]|)([O]{1})(\W|\s|$))', _("smiley Surprised"), True, True),
	# Translators:  ;) Wink;
	(r'(\s|^)(;([\-]|)([)D]{1})(\B|\s|$))', _("smiley Wink"), True, True),
	# Translators:  ;( Crying
	(r'(\s|^)(;([\-]|)([(]{1})(\B|\s|$))', _("smiley Crying"), True, True),
	# Translators:  (:| Sweating
	(r'(\s|^)\((:[\|])(\B|\s|$)', _("smiley Sweating"), True, True),
	# Translators:  :| Speechless
	(r'(\s|^)(:[\|])(\B|\s|$)', _("smiley Speechless"), True, True),
	# Translators:  :* Kiss
	(r'(\s|^)(:([\-]|)([\*]{1})(\B|\s|$))', _("smiley Kiss"), True, True),
	# Translators:  :P Cheeky
	(r'(\s|^)(:([\-]|)([pP])(\W|\s|$))', _("smiley Cheeky"), True, True),
	# Translators:  :$ Blushing
	(r'(\s|^)(:[\$])(\B|\s|$)', _("smiley Blushing"), True, True),
	# Translators:  :^) Wondering
	(r'(\s|^)(:[\^][\)])(\B|\s|$)', _("smiley Wondering"), True, True),
	# Translators:  |-) Sleepy
	(r'(\s|^)([\|][\-][\)])(\B|\s|$)', _("smiley Sleepy"), True, True),
	# Translators:  |-( Dull
	(r'(\s|^)([\|][\-][\(])(\B|\s|$)', _("smiley Dull"), True, True),
	# Translators:  (inlove) In Love
	(r'(\s|^)\(inlove\)(\B|\s|$)', _("smiley In Love"), True, True),
	# Translators:  ]:) Evil grin
	(r'(\s|^)()\]:\)(\B|\s|$)', _("smiley Evil grin"), True, True),
	# Translators:  (yn) Fingers crossed
	(r'(\s|^)([\(]yn[\)])(\B|\s|$)', _("smiley Fingers crossed"), True, True),
	# Translators:  (yawn) Yawn
	(r'(\s|^)\(yawn\)(\B|\s|$)', _("smiley Yawn"), True, True),
	# Translators:  (puke) Puking
	(r'(\s|^)\(puke\)(\B|\s|$)', _("smiley Puking"), True, True),
	# Translators:  (doh) Doh!
	(r'(\s|^)\(doh\)(\B|\s|$)', _("smiley Doh! "), True, True),
	# Translators:  (angry) Angry
	(r'(\s|^)\(angry\)(\B|\s|$)', _("smiley Angry"), True, True),
	# Translators:  (wasntme) It wasn't me!
	(r'(\s|^)\(wasntme\)(\B|\s|$)', _("smiley It wasn't me! "), True, True),
	# Translators:  (party) Party
	(r'(\s|^)\(party\)(\B|\s|$)', _("smiley Party"), True, True),
	# Translators:  (worry) Worried
	(r'(\s|^)\(worry\)(\B|\s|$)', _("smiley Worried"), True, True),
	# Translators:  (mm) Mmmm...
	(r'(\s|^)\(mm\)(\B|\s|$)', _("smiley mmmmmm..."), True, True),
	# Translators:  (nerd) Nerdy
	(r'(\s|^)\(nerd\)(\B|\s|$)', _("smiley Nerdy;"), True, True),
	# Translators:  :x My lips are sealed
	(r'(\s|^)(:([\-]|)([xX])\b)', _("smiley My lips are sealed"), True, True),
	# Translators:  (wave) Hi
	(r'(\s|^)\(wave\)(\B|\s|$)', _("smiley Hi"), True, True),
	# Translators:  (facepalm) Facepalm
	(r'(\s|^)\(facepalm\)(\B|\s|$)', _("smiley Facepalm"), True, True),
	# Translators:  (devil) Devil
	(r'(\s|^)\(devil\)(\B|\s|$)', _("smiley Devil"), True, True),
	# Translators:  (angel) Angel
	(r'(\s|^)\(angel\)(\B|\s|$)', _("smiley Angel"), True, True),
	# Translators:  (envy) Envy
	(r'(\s|^)\(envy\)(\B|\s|$)', _("smileyEnvy"), True, True),
	# Translators:  (wait) Wait
	(r'(\s|^)\(wait\)(\B|\s|$)', _("smiley Wait"), True, True),
	# Translators:  (hug) Hug
	(r'(\s|^)\(hug\)(\B|\s|$)', _("smiley Hug"), True, True),
	# Translators:  (makeup) Make-up
	(r'(\s|^)\(makeup\)(\B|\s|$)', _("smiley Make-up"), True, True),
	# Translators:  (chuckle) Giggle
	(r'(\s|^)\(chuckle\)(\B|\s|$)', _("smiley Giggle;"), True, True),
	# Translators:  (clap) Clapping
	(r'(\s|^)\(clap\)(\B|\s|$)', _("smiley Clapping"), True, True),
	# Translators:  (think) Thinking
	(r'(\s|^)\(think\)(\B|\s|$)', _("smiley Thinking"), True, True),
	# Translators:  (bow) Bowing
	(r'(\s|^)\(bow\)(\B|\s|$)', _("smiley Bowing"), True, True),
	# Translators:  (rofl) Rolling on the floor laughing
	(r'(\s|^)\(rofl\)(\B|\s|$)', _("smiley Rolling on the floor laughing! "), True, True),
	# Translators:  (whew) Relieved
	(r'(\s|^)\(whew\)(\B|\s|$)', _("smiley Relieved"), True, True),
	# Translators:  (happy) Happy
	(r'(\s|^)\(happy\)(\B|\s|$)', _("smiley Happy"), True, True),
	# Translators:  (smirk) Smirking
	(r'(\s|^)\(smirk\)(\B|\s|$)', _("smiley Smirking"), True, True),
	# Translators:  (nod) Nodding
	(r'(\s|^)\(nod\)(\B|\s|$)', _("smiley Nodding;"), True, True),
	# Translators:  (shake) Shake
	(r'(\s|^)\(shake\)(\B|\s|$)', _("smiley Shake"), True, True),
	# Translators:  (waiting) Waiting
	(r'(\s|^)\(waiting\)(\B|\s|$)', _("smiley Waiting"), True, True),
	# Translators:  (emo) Emo;
	(r'(\s|^)\(emo\)(\B|\s|$)', _("smiley Emo"), True, True),
	# Translators:  (y) Yes
	(r'(\s|^)\(y\)(\B|\s|$)', _("smiley Yes"), True, True),
	# Translators:  (n) no;
	(r'(\s|^)\(n\)(\B|\s|$)', _("smiley NO"), True, True),
	# Translators:  (handshake) Handshake
	(r'(\s|^)\(handshake\)(\B|\s|$)', _("smiley Handshake;"), True, True),
	# Translators:  (highfive) High five
	(r'(\s|^)\(highfive\)(\B|\s|$)', _("smiley High five"), True, True),
	# Translators:  (heart) Heart
	(r'(\s|^)\(heart\)(\B|\s|$)', _("smiley Heart"), True, True),
	# Translators:  (lalala) Lalala;
	(r'(\s|^)\(lalala\)(\B|\s|$)', _("smiley LaLaLa"), True, True),
	# Translators:  (heidy) Heidy;
	(r'(\s|^)\(heidy\)(\B|\s|$)', _("smiley Heidy;"), True, True),
	# Translators:  (F) Flower
	(r'(\s|^)\(F\)(\B|\s|$)', _("smiley Flower"), True, True),
	# Translators:  (rain) Raining
	(r'(\s|^)\(rain\)(\B|\s|$)', _("smiley Raining"), True, True),
	# Translators:  (sun) Sun
	(r'(\s|^)\(sun\)(\B|\s|$)', _("smiley Sun"), True, True),
	# Translators:  (tumbleweed) Tumbleweed
	(r'(\s|^)\(tumbleweed\)(\B|\s|$)', _("smiley Tumbleweed"), True, True),
	# Translators:  (music) Music
	(r'(\s|^)\(music\)(\B|\s|$)', _("smiley Music"), True, True),
	# Translators:  (bandit) Bandit
	(r'(\s|^)\(bandit\)(\B|\s|$)', _("smiley Bandit"), True, True),
	# Translators:  (tmi) Too much information
	(r'(\s|^)\(tmi\)(\B|\s|$)', _("smiley Too much information;"), True, True),
	# Translators:  (coffee) Coffee
	(r'(\s|^)\(coffee\)(\B|\s|$)', _("smiley Coffee"), True, True),
	# Translators:  (pi) Pizza
	(r'(\s|^)\(pi\)(\B|\s|$)', _("smiley Pizza"), True, True),
	# Translators:  (cash) Cash
	(r'(\s|^)\(cash\)(\B|\s|$)', _("smiley Cash"), True, True),
	# Translators:  (flex) Muscle
	(r'(\s|^)\(flex\)(\B|\s|$)', _("smiley Muscle"), True, True),
	# Translators:  (^) Cake
	(r'(\s|^)([\(][\^][\)])(\B|\s|$)', _("smiley Cake"), True, True),
	# Translators:  (beer) Beer
	(r'(\s|^)\(beer\)(\B|\s|$)', _("smiley Beer"), True, True),
	# Translators:  (d) Drink
	(r'(\s|^)\(d\)(\B|\s|$)', _("smiley Drink;"), True, True),
	# Translators:  \o/ Dancing
	(r'(\s|^)([\\]o[/])(\B|\s|$)', _("smiley Dancing"), True, True),
	# Translators:  (ninja) Ninja
	(r'(\s|^)\(ninja\)(\B|\s|$)', _("smiley Ninja;"), True, True),
	# Translators:  (*) Star
	(r'(\s|^)([\(][\*][\)])(\B|\s|$)', _("smiley Star"), True, True),
	# Translators:  Facebook  Smiley  :'( Crying
	("(\s|^)([:]['][\(])(\B|\s|$)", _("smiley Crying"), True, True),
	# Translators:  >:( Angry
	(r'(\s|^)(>:[\(])(\B|\s|$)', _("smiley Angry"), True, True),
	# Translators:  :/ Worried
	(r'(\s|^)(:[/])(\B|\s|$)', _("smiley Worried"), True, True),
	# Translators:  <3 Heart
	(r'(\s|^)<3(\W|\s|$)', _("smiley Heart"), True, True),
	# Translators: regex for Facebook contacts  in Skype v.5 series only.
	(r'\(xmpp:-([0-9]+)@chat.facebook.com\)', _("(facebook)"), True, True),
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
