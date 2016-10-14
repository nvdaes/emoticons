# -*- coding: UTF-8 -*-
#Copyright (C) 2013-2016 Chris Leo, Mesar Hameed
# Released under GPL 2

import addonHandler
from collections import namedtuple

addonHandler.initTranslation()

Smiley = namedtuple('Smiley', 'pattern name chars isEmoji')
emoticons = [
	# Translators: :) Smile
	Smiley(r'(\s|^)(:([\-]|)([)]{1})(\B|\s|$))', _("smiling smiley"), r':)', False),
	# Translators: :( Sad
	Smiley(r'(\s|^)(:([\-]|)([(]{1})\B)', _("sad smiley"), r':(', False),
	# Translators: :D Laugh
	Smiley(r'(\s|^)(:([\-]|)([D]{1,})\b)', _("Laughing smiley"), r':D', False),
	# Translators: :O Surprised
	Smiley(r'(\s|^)(:([\-]|)([O]{1})(\W|\s|$))', _("surprised smiley"), r':O', False),
	# Translators: ;) Wink;
	Smiley(r'(\s|^)(;([\-]|)([)D]{1})(\B|\s|$))', _("winking smiley"), r';)', False),
	# Translators: ;( Crying
	Smiley(r'(\s|^)(;([\-]|)([(]{1})(\B|\s|$))', _("crying smiley"), r';(', False),
	# Translators: (:| Sweating
	Smiley(r'(\s|^)\((:[\|])(\B|\s|$)', _("sweating smiley"), r'(:|', False),
	# translators:  :|] Robot (a robot head)
	Smiley(r'(\s|^)(:[\|][\]])(\W|\s|$)', _("Robot Smiley"), r':|]', False),
	# Translators: :| Speechless
	Smiley(r'(\s|^)(:[\|])(\B|\s|$)', _("speechless smiley"), r':|', False),
	# Translators: :* Kiss
	Smiley(r'(\s|^)(:([\-]|)([\*]{1})(\B|\s|$))', _("kiss smiley"), r':*', False),
	# Translators: :P Cheeky
	Smiley(r'(\s|^)(:([\-]|)([pP])(\W|\s|$))', _("cheeky smiley"), r':P', False),
	# Translators: :$ Blushing
	Smiley(r'(\s|^)(:[\$])(\B|\s|$)', _("blushing smiley"), r':$', False),
	# Translators: :^) Wondering
	Smiley(r'(\s|^)(:[\^][\)])(\B|\s|$)', _("wondering smiley"), r':^)', False),
	# Translators: |-) Sleepy
	Smiley(r'(\s|^)([\|][\-][\)])(\B|\s|$)', _("sleepy smiley"), r'|-)', False),
	# Translators: |-( Dull
	Smiley(r'(\s|^)([\|][\-][\(])(\B|\s|$)', _("dull smiley"), r'|-(', False),
	# Translators: :x My lips are sealed
	Smiley(r'(\s|^)(:([\-]|)([xX])\b)', _("my lips are sealed smiley"), r':x', False),
	# Translators: \o/ Dancing
	Smiley(r'(\s|^)([\\]o[/])(\B|\s|$)', _("dancing smiley"), r'\o/', False),
	# Translators: :'( crying a lot smiley
	Smiley(r"(\s|^)([:]['][\(])(\B|\s|$)", _("crying a lot smiley"), r":'(", False),
	# Translators: >:( Angry
	Smiley(r'(\s|^)(>:[\(])(\B|\s|$)', _("angry smiley"), r'>:(', False),
	# Translators: :/ Worried
	Smiley(r'(\s|^)(:[/])(\B|\s|$)', _("worried smiley"), r':/', False),
	# Translators: <3 Heart
	Smiley(r'(\s|^)<3(\W|\s|$)', _("heart smiley"), r'<3', False),
	# Translators:  O:)  O:-) Angel
	Smiley(r'(\s|^)(O:([\-]|)([)])(\W|\s|$))', _("Angel Smiley"), r'O:)', False),
	# Translators:  O.o  o.O  Confused
	Smiley(r'(\s|^)[Oo][\.][oO](\B|\s|$)', _("Confused Smiley"), r'O.o', False),
	# Translators:   3:-) Devil
	Smiley(r'(\s|^)(3:([\-]|)([\)]))(\B|\s|$)', _("Devil Smiley"), r'3:-)', False),
	# Translators:  ^_^ Keke (This smiley is inspired by the Asian style, which is a happy face.)
	Smiley(r'(\s|^)[\^]_[\^](\B|\s|$)', _("Keke Smiley"), r'^_^', False),
	# Translators: -_- Bored (This smiley face has its eyes closed and is sporting a very small grin.)
	Smiley(r'(\s|^)[\-]_[\-](\B|\s|$)', _("Bored smiley"), r'-_-', False),
	# Translators:  >:O  Upset, angry or shouting...
	Smiley(r'(\s|^)(>:O)(\W|\s|$)', _("Angry Smiley"), r'>:O', False),
	# Translators:  :3  Cat (Cat faced smiley with curly lips)
	Smiley(r'(\s|^)(:3)(\W|\s|$)', _("Cat Smiley"), r':3', False),
	# Translators: (-.-)ZZZ Iӭ Sleepy
	Smiley(r'(\s|^)\([-][\.][-]\)ZZZ(\B|\s|$)', _("I am Sleepy smiley"), r'(-.-)ZZZ', False),
	# Translators: 8-) Glasses
	Smiley(r'(\s|^)8[-][)](\B|\s|$)', _("glasses smiley"), r'8-)', False),
	# Translators: (^^^) shark
	Smiley(r'(\s|^)\([\^]{3}\)(\B|\s|$)', _("shark smiley"), r'(^^^)', False),
	# Translators: (worry) Worried
	Smiley(r'(\s|^)\(worry\)(\B|\s|$)', _("worried smiley"), r'(worry)', False),
	# Translators:  (cash) Cash
	Smiley(r'(\s|^)\(cash\)(\B|\s|$)', _("cash smiley"), r'(cash)', False),
	# Translators: (flex) Muscle
	Smiley(r'(\s|^)\(flex\)(\B|\s|$)', _("muscle smiley"), r'(flex)', False),
	# Translators: (beer) Beer
	Smiley(r'(\s|^)\(beer\)(\B|\s|$)', _("beer smiley"), r'(beer)', False),
	# Translators: (d) Drink
	Smiley(r'(\s|^)\(d\)(\B|\s|$)', _("drink smiley"), r'(d)', False),
	# Translators: (ninja) Ninja
	Smiley(r'(\s|^)\(ninja\)(\B|\s|$)', _("ninja smiley"), r'(ninja)', False),
	# Translators: (cool) Cool
	Smiley(r'(\s|^)\(cool\)(\B|\s|$)', _("cool smiley"), r'(cool)', False),
	# Translators: (inlove) In Love
	Smiley(r'(\s|^)\(inlove\)(\B|\s|$)', _("in love smiley"), r'(inlove)', False),
	# Translators: (yn) Fingers crossed
	Smiley(r'(\s|^)([\(]yn[\)])(\B|\s|$)', _("fingers crossed smiley"), r'(yn)', False),
	# Translators: (yawn) Yawn
	Smiley(r'(\s|^)\(yawn\)(\B|\s|$)', _("yawning smiley"), r'(yawn)', False),
	# Translators: (puke) Puking
	Smiley(r'(\s|^)\(puke\)(\B|\s|$)', _("puking smiley"), r'(puke)', False),
	# Translators: (doh) Doh!
	Smiley(r'(\s|^)\(doh\)(\B|\s|$)', _("doh! smiley"), r'(doh)', False),
	# Translators: (angry) Angry
	Smiley(r'(\s|^)\(angry\)(\B|\s|$)', _("angry smiley"), r'(angry)', False),
	# Translators: (wasntme) It wasn't me!
	Smiley(r'(\s|^)\(wasntme\)(\B|\s|$)', _("it wasn't me! smiley"), r'(wasntme)', False),
	# Translators: (party) Party
	Smiley(r'(\s|^)\(party\)(\B|\s|$)', _("party smiley"), r'(party)', False),
	# Translators: (mm) Mmmm...
	Smiley(r'(\s|^)\(mm\)(\B|\s|$)', _("mmmmmm... smiley"), r'(mm)', False),
	# Translators: (nerd) Nerdy
	Smiley(r'(\s|^)\(nerd\)(\B|\s|$)', _("nerdy smiley"), r'(nerd)', False),
	# Translators: (wave) Hi
	Smiley(r'(\s|^)\(wave\)(\B|\s|$)', _("hi smiley"), r'(wave)', False),
	# Translators: (facepalm) Facepalm
	Smiley(r'(\s|^)\(facepalm\)(\B|\s|$)', _("facepalm smiley"), r'(facepalm)', False),
	# Translators: (devil) Devil
	Smiley(r'(\s|^)\(devil\)(\B|\s|$)', _("devil smiley"), r'(devil)', False),
	# Translators: (angel) Angel
	Smiley(r'(\s|^)\(angel\)(\B|\s|$)', _("angel smiley"), r'(angel)', False),
	# Translators: (envy) Envy
	Smiley(r'(\s|^)\(envy\)(\B|\s|$)', _("envy smiley"), r'(envy)', False),
	# Translators: (wait) Wait
	Smiley(r'(\s|^)\(wait\)(\B|\s|$)', _("wait smiley"), r'(wait)', False),
	# Translators: (hug) Hug
	Smiley(r'(\s|^)\(hug\)(\B|\s|$)', _("hug smiley"), r'(hug)', False),
	# Translators: (makeup) Make-up
	Smiley(r'(\s|^)\(makeup\)(\B|\s|$)', _("make-up smiley"), r'(makeup)', False),
	# Translators: (chuckle) Giggle
	Smiley(r'(\s|^)\(chuckle\)(\B|\s|$)', _("giggle smiley"), r'(chuckle)', False),
	# Translators: (clap) Clapping
	Smiley(r'(\s|^)\(clap\)(\B|\s|$)', _("clapping smiley"), r'(clap)', False),
	# Translators: (think) Thinking
	Smiley(r'(\s|^)\(think\)(\B|\s|$)', _("thinking smiley"), r'(think)', False),
	# Translators: (bow) Bowing
	Smiley(r'(\s|^)\(bow\)(\B|\s|$)', _("bowing smiley"), r'(bow)', False),
	# Translators: (rofl) Rolling on the floor laughing
	Smiley(r'(\s|^)\(rofl\)(\B|\s|$)', _("rolling on the floor laughing! smiley"), r'(rofl)', False),
	# Translators: (whew) Relieved
	Smiley(r'(\s|^)\(whew\)(\B|\s|$)', _("relieved smiley"), r'(whew)', False),
	# Translators: (happy) Happy
	Smiley(r'(\s|^)\(happy\)(\B|\s|$)', _("happy smiley"), r'(happy)', False),
	# Translators: (smirk) Smirking
	Smiley(r'(\s|^)\(smirk\)(\B|\s|$)', _("smirking smiley"), r'(smirk)', False),
	# Translators: (nod) Nodding
	Smiley(r'(\s|^)\(nod\)(\B|\s|$)', _("nodding smiley"), r'(nod)', False),
	# Translators: (shake) Shake
	Smiley(r'(\s|^)\(shake\)(\B|\s|$)', _("shakeing smiley"), r'(shake)', False),
	# Translators: (waiting) Waiting
	Smiley(r'(\s|^)\(waiting\)(\B|\s|$)', _("waiting smiley"), r'(waiting)', False),
	# Translators: (emo) Emo;
	Smiley(r'(\s|^)\(emo\)(\B|\s|$)', _("Emo smiley"), r'(emo)', False),
	# Translators: (y) Yes
	Smiley(r'(\s|^)\(y\)(\B|\s|$)', _("yes smiley"), r'(y)', False),
	# Translators: (n) no;
	Smiley(r'(\s|^)\(n\)(\B|\s|$)', _("no smiley"), r'(n)', False),
	# Translators: (handshake) Handshake
	Smiley(r'(\s|^)\(handshake\)(\B|\s|$)', _("handshake smiley"), r'(handshake)', False),
	# Translators: (highfive) High five
	Smiley(r'(\s|^)\(highfive\)(\B|\s|$)', _("high five smiley"), r'(highfive)', False),
	# Translators: (heart) Heart
	Smiley(r'(\s|^)\(heart\)(\B|\s|$)', _("heart smiley"), r'(heart)', False),
	# Translators: (lalala) Lalala;
	Smiley(r'(\s|^)\(lalala\)(\B|\s|$)', _("lalala smiley"), r'(lalala)', False),
	# Translators: (heidy) Heidy;
	Smiley(r'(\s|^)\(heidy\)(\B|\s|$)', _("heidy smiley"), r'(heidy)', False),
	# Translators: (F) Flower
	Smiley(r'(\s|^)\(F\)(\B|\s|$)', _("flower smiley"), r'(F)', False),
	# Translators: (rain) Raining
	Smiley(r'(\s|^)\(rain\)(\B|\s|$)', _("raining smiley"), r'(rain)', False),
	# Translators: (sun) Sun
	Smiley(r'(\s|^)\(sun\)(\B|\s|$)', _("sunny smiley"), r'(sun)', False),
	# Translators: (tumbleweed) Tumbleweed
	Smiley(r'(\s|^)\(tumbleweed\)(\B|\s|$)', _("tumbleweed smiley"), r'(tumbleweed)', False),
	# Translators: (music) Music
	Smiley(r'(\s|^)\(music\)(\B|\s|$)', _("music smiley"), r'(music)', False),
	# Translators: (bandit) Bandit
	Smiley(r'(\s|^)\(bandit\)(\B|\s|$)', _("bandit smiley"), r'(bandit)', False),
	# Translators: (tmi) Too much information
	Smiley(r'(\s|^)\(tmi\)(\B|\s|$)', _("too much information smiley"), r'(tmi)', False),
	# Translators: (coffee) Coffee
	Smiley(r'(\s|^)\(coffee\)(\B|\s|$)', _("coffee smiley"), r'(coffee)', False),
	# Translators: (pi) Pizza
	Smiley(r'(\s|^)\(pi\)(\B|\s|$)', _("pizza smiley"), r'(pi)', False),
	# Translators: (^) Cake
	Smiley(r'(\s|^)([\(][\^][\)])(\B|\s|$)', _("cake smiley"), r'(^)', False),
	# Translators: (*) Star
	Smiley(r'(\s|^)([\(][\*][\)])(\B|\s|$)', _("star smiley"), r'(*)', False),
	# Translators: (emoji) Latin cross
	Smiley(u'✝', _("Latin cross"), '✝', True),
]
