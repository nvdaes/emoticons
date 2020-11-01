# -*- coding: UTF-8 -*-
#Copyright (C) 2013-2016 Chris Leo, Mesar Hameed
# Released under GPL 2

import addonHandler
from collections import namedtuple

addonHandler.initTranslation()

Smiley = namedtuple('Smiley', 'pattern name chars isEmoji')
emoticons = [
	# Translators: (emoji) Grinning face, an happy face with normal eyes.
	Smiley(u'😀', _("Grinning face"), '😀', True),
	# Translators: (emoji) Happy face with open mouth and squinting eyes.
	Smiley(u'😄', _("Happy face with open mouth and squinting eyes"), '😄', True),
	# Translators: (emoji) happy face with open mouth.
	Smiley(u'😃', _("Happy face with open mouth"), '😃', True),
	# Translators: (emoji) A smiling face with smiling eyes and rosy cheeks.
	Smiley(u'😊', _("Smiling Face With Smiling Eyes"), '😊', True),
	# Translators: (emoji) smirking face.
	Smiley(u'😏', _("Smirking face"), '😏', True),
	# Translators: (emoji) Slightly Smiling Face: a face that is a little bit happy, with a slight smile and neutral eyes.
	Smiley(u'🙂', _("Slightly smiling face"), '🙂', True),
	# Translators: (emoji) white smiling face.
	Smiley(u'☺', _("white smiling face"), '☺', True),
	# Translators: (emoji) happy face with halo.
	Smiley(u'😇', _("Happy face with halo"), '😇', True),
	# Translators: (emoji) white frowning face.
	Smiley(u'☹', _("White frowning face"), '☹', True),
	# Translators: (emoji) winking face.
	Smiley(u'😉', _("Winking face"), '😉', True),
	# Translators: (emoji) smiling face with heart shaped eyes.
	Smiley(u'😍', _("Smiling face with heart shaped eyes"), '😍', True),
	# Translators: (emoji)  Rose: a single red rose.
	Smiley(u'🌹', _("Rose"), '🌹', True),
	# Translators: (emoji) Expressionless face: a face with straight lined eyes and mouth. A deliberate display of no comment...
	Smiley(u'😑', _("Expressionless face"), '😑', True),
	# Translators: (emoji) neutral face.
	Smiley(u'😐', _("Neutral face"), '😐', True),
	# Translators: (emoji) face without mouth.
	Smiley(u'😶', _("Face without mouth"), '😶', True),
	# Translators: (emoji) face throwing a kiss.
	Smiley(u'😘', _("Face throwing a kiss"), '😘', True),
	# Translators: (emoji) kissing face with closed eyes.
	Smiley(u'😚', _("Kissing face with closed eyes"), '😚', True),
	# Translators: (emoji) Kissing face.
	Smiley(u'😗', _("Kissing face"), '😗', True),
	# Translators: (emoji) kissing face with arched eyes.
	Smiley(u'😙', _("Kissing face with arched eyes"), '😙', True),
	# Translators: (emoji) winking face with stuck out tongue.
	Smiley(u'😜', _("Winking face with stuck out tongue"), '😜', True),
	# Translators: (emoji) face with stuck out tongue and eyes tightly closed.
	Smiley(u'😝', _("Face with stuck out tongue and eyes tightly closed"), '😝', True),
	# Translators: (emoji) A cheeky face with stuck out tongue.
	Smiley(u'😛', _("Face with stuck out tongue"), '😛', True),
	# Translators: (emoji) Hugging Face: a face displayed with an open hands gesture, offering a hug.
	Smiley(u'🤗', _("Hugging face"), '🤗', True),
	# Translators: (emoji) flushed face.
	Smiley(u'😳', _("Flushed face"), '😳', True),
	# Translators: (emoji) Grinning face showing smiling eyes.
	Smiley(u'😁', _("Grinning Face With Smiling Eyes"), '😁', True),
	# Translators: (emoji) A pensive, remorseful and saddened face. Quietly considering where things all went wrong.
	Smiley(u'😔', _("Pensive Face"), '😔', True),
	# Translators: (emoji) devil with evil smile.
	Smiley(u'😈', _("Devil with evil smile"), '😈', True),
	# Translators: (emoji) devil.
	Smiley(u'👿', _("Devil"), '👿', True),
	# Translators: (emoji) relieved face.
	Smiley(u'😌', _("Relieved face"), '😌', True),
	# Translators: (emoji) unamused face.
	Smiley(u'😒', _("Unamused face"), '😒', True),
	# Translators: (emoji) A face with scrunched up and closed eyes, frowning. Used to show helplessness in a situation.
	Smiley(u'😣', _("Persevering Face"), '😣', True),
	# Translators: (emoji) crying face.
	Smiley(u'😢', _("Crying face"), '😢', True),
	# Translators: (emoji) face with tears of joy.
	Smiley(u'😂', _("Face with tears of joy"), '😂', True),
	# Translators: (emoji) loudly crying face.
	Smiley(u'😭', _("Loudly crying face"), '😭', True),
	# Translators: (emoji) sleepy face.
	Smiley(u'😪', _("Sleepy face"), '😪', True),
	# Translators: (emoji) Shrugging: A person shrugging their shoulders to indicate a lack of knowledge about a particular topic, or a lack of care about the result of a situation.
	Smiley(u'🤷', _("Shrugging emoji"), '🤷', True),
	# Translators: (emoji) disappointed face.
	Smiley(u'😞', _("Disappointed face"), '😞', True),
	# Translators: (emoji) disappointed but relieved face.
	Smiley(u'😥', _("Disappointed but relieved face"), '😥', True),
	# Translators: (emoji) Face with a look of concern, with a blue forehead and sweat dripping down the cheek.
	Smiley(u'😰', _("Face With Open Mouth & Cold Sweat"), '😰', True),
	# Translators: (emoji) Happy face with a single drop of sweat on one side of the face.
	Smiley(u'😅', _("Smiling Face With Open Mouth & Cold Sweat"), '😅', True),
	# Translators: (emoji) face with cold sweat.
	Smiley(u'😓', _("Face with cold sweat"), '😓', True),
	# Translators: (emoji) A distraught-looking face with  an open mouth and crescent shaped eyes.
	Smiley(u'😩', _("Weary Face"), '😩', True),
	# Translators: (emoji) An exhausted-looking face with an open mouth and tightly closed eyes.
	Smiley(u'😫', _("Tired Face"), '😫', True),
	# Translators: (emoji) fearful face.
	Smiley(u'😨', _("Fearful face"), '😨', True),
	# Translators: (emoji) face screaming in fear.
	Smiley(u'😱', _("Face screaming in fear"), '😱', True),
	# Translators: (emoji) angry face.
	Smiley(u'😠', _("Angry face"), '😠', True),
	# Translators: (emoji) pouting face.
	Smiley(u'😡', _("Pouting face"), '😡', True),
	# Translators: (emoji) A face with air coming out of its nose, huffing with anger face.
	Smiley(u'😤', _("Face With Steam From Nose"), '😤', True),
	# Translators: (emoji) confounded face.
	Smiley(u'😖', _("Confounded face"), '😖', True),
	# Translators: (emoji) Smiling Face With Open Mouth and Tightly-Closed Eyes.
	Smiley(u'😆', _("Smiling Face With Open Mouth and Tightly-Closed Eyes"), '😆', True),
	# Translators: (emoji) happy face licking lips.
	Smiley(u'😋', _("Happy face licking lips"), '😋', True),
	# Translators: (emoji) happy face with sunglasses.
	Smiley(u'😎', _("Happy face with sunglasses"), '😎', True),
	# Translators: (emoji) sleeping face.
	Smiley(u'😴', _("Sleeping face"), '😴', True),
	# Translators: (emoji) A dizzy face, looking sick or confused from being spun around in circles too many times.
	Smiley(u'😵', _("Dizzy Face"), '😵', True),
	# Translators: (emoji) astonished face.
	Smiley(u'😲', _("Astonished face"), '😲', True),
	# Translators: (emoji) worried face.
	Smiley(u'😟', _("Worried face"), '😟', True),
	# Translators: (emoji) Dismayed face with open eyes and open mouth, appear closer to  a frowning face.
	Smiley(u'😦', _("Frowning Face With Open Mouth"), '😦', True),
	# Translators: (emoji) anguished face.
	Smiley(u'😧', _("Anguished face"), '😧', True),
	# Translators: (emoji) A face with Open Mouth, generally used to represent an element of surprise.
	Smiley(u'😮', _("Face with Open Mouth"), '😮', True),
	# Translators: (emoji) grimacing face.
	Smiley(u'😬', _("Grimacing face"), '😬', True),
	# Translators: (emoji) confused face.
	Smiley(u'😕', _("Confused face"), '😕', True),
	# Translators: (emoji) A face with high eyebrows and an open mouth, it looks more surprised than hushed.
	Smiley(u'😯', _("Hushed Face"), '😯', True),
	# Translators: (emoji) broken heart.
	Smiley(u'💔', _("Broken heart"), '💔', True),
	# Translators: (emoji) pulsating heart.
	Smiley(u'💗', _("Pulsating heart"), '💗', True),
	# Translators: (emoji) beating heart.
	Smiley(u'💓', _("Beating heart"), '💓', True),
	# Translators: (emoji) two hearts.
	Smiley(u'💕', _("Two hearts"), '💕', True),
	# Translators: (emoji) heart with arrow.
	Smiley(u'💘', _("Heart with arrow"), '💘', True),
	# Translators: (emoji) purple heart.
	Smiley(u'💜', _("Purple heart"), '💜', True),
	# Translators: (emoji) red heart.
	Smiley(u'❤', _("Red heart"), '❤', True),
	# Translators: (emoji) yellow heart.
	Smiley(u'💛', _("Yellow heart"), '💛', True),
	# Translators: (emoji) green heart.
	Smiley(u'💚', _("Green heart"), '💚', True),
	# Translators: (emoji) blue heart.
	Smiley(u'💙', _("Blue heart"), '💙', True),
	# Translators: (emoji) This emoji is the version of the phrase ROFL. A person lying on the floor due to an extreme amount of laughter.
	Smiley(u'🤣', _("Rolling on the Floor Laughing"), '🤣', True),
	# Translators: (emoji) A face that is a little bit sad, with a slight frown and neutral eyes.
	Smiley(u'🙁', _("Slightly Frowning Face"), '🙁', True),
	# Translators: (emoji) A face that is upside-down.
	Smiley(u'🙃', _("Upside-down Face"), '🙃', True),
	# Translators: (emoji) A face displaying eyes glancing upward.
	Smiley(u'🙄', _("Face With Rolling Eyes"), '🙄', True),
	# Translators: (emoji) A person with arms forming an X to indicate no or no good.
	Smiley(u'🙅', _("Person Gesturing No"), '🙅', True),
	# Translators: (emoji) A person with arms above his head, making an OK sign with the whole body.
	Smiley(u'🙆', _("Person Gesturing OK"), '🙆', True),
	# Translators: (emoji) A person bowing deeply, express a sincere apology or to request a favour.
	Smiley(u'🙇', _("Person bowing"), '🙇', True),
	# Translators: (emoji) An upset person frowning with dismay.
	Smiley(u'🙍', _("Person Frowning"), '🙍', True),
	# Translators: (emoji) Two hands placed firmly together.
	Smiley(u'🙏', _("Folded Hands"), '🙏', True),
	# Translators: (emoji) A person with a surgical mask on their face.
	Smiley(u'😷', _("Face with medical mask"), '😷', True),
	# Translators: (emoji) A black version of white smiling face.
	Smiley(u'☻', _("Black Smiling Face"), '☻', True),
	# Translators: (emoji) happy cat face with heart shaped eyes.
	Smiley(u'😻', _("Happy cat face with heart shaped eyes"), '😻', True),
	# Translators: (emoji) ok hand sign.
	Smiley(u'👌', _("Ok hand sign"), '👌', True),
	# Translators: (emoji) thumbs up symbol.
	Smiley(u'👍', _("Thumbs up symbol"), '👍', True),
	# Translators: (emoji) thumbs down symbol.
	Smiley(u'👎', _("Thumbs down symbol"), '👎', True),
	# Translators: (emoji) Victory Hand.
	Smiley(u'✌', _("Victory Hand"), '✌', True),
	# Translators: :) Smile
	Smiley(r'(\s|^)(:([\-]|)([)]{1})(\B|\s|$))', _("smiling smiley"), r':-)', False),
	# Translators: :( Sad face.
	Smiley(r'(\s|^)(:([\-]|)([(]{1})\B)', _("Sad face"), r':-(', False),
	# Translators: :D Laugh
	Smiley(r'(\s|^)(:([\-]|)([D]{1,})\b)', _("Laughing smiley"), r':-D', False),
	# Translators: :@ angry face.
	Smiley(r'(\s|^)(:([\-]|)([@]{1})(\B|\s|$))', _("Angry face"), r':@', False),
	# Translators: :O Surprised
	Smiley(r'(\s|^)(:([\-]|)([O]{1})(\W|\s|$))', _("surprised smiley"), r':O', False),
	# Translators: ;) Wink;
	Smiley(r'(\s|^)(;([\-]|)([)D]{1})(\B|\s|$))', _("winking smiley"), r';)', False),
	# Translators: ;( Crying
	Smiley(r'(\s|^)(;([\-]|)([(]{1})(\B|\s|$))', _("crying smiley"), r';(', False),
	# Translators: :s :-S :-Q Confused face:
	Smiley(r'(\s|^)(:([\-]|)([sSQ$])(\b|\s|$))', _("Confused Face"), r':s', False),
	# Translators: (:| Sweating
	Smiley(r'(\s|^)\((:[\|])(\B|\s|$)', _("sweating smiley"), r'(:|', False),
	# Translators: :|] Robot (a robot head)
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
]

def terminate(self):
	global emoticons
	del emoticons
