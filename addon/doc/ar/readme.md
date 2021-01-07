# Emoticons #

* Authors: Chris Leo, Noelia Ruiz Martínez, Mesar Hameed, Francisco Javier
  Estrada Martínez
* تحميل [الإصدار النهائي][1]
* تحميل [الإصدار التجريبي][2]

Using this add-on, spoken text containing emoticon characters will be
replaced by its more human friendly description.

For example: the sequence ":)" will be spoken as "smiling smiley", or for
example NVDA will recognize the meaning of each emoji.

يمكنك الاستفادة من هذه الميزات:

## Insert Emoticon ##

Sometimes an image is worth a 1000 words: use the new emoji to liven up your
instant message and to let your friends know how you’re feeling.

When you are unsure of the characters for a particular smiley, this addon
enables you to select and insert it into your text such as in a chat.

Press NVDA+I, or from menu Preferences -> Manage emoticons -> Insert emoticon, to open a dialog with the provided emoticons or emoji.

This dialog allows you to choose an emoticon and to view the emoticons that
interest you:

*	An editable field allows you to filter the search for the desired emoticon
  among the emoticons available.
*	Through a set of radio buttons, you can choose to view only emoji category
  (alt+E) or view only standard emoticon category (alt+s) or view all
  emoticons available (alt+A).
*	In the list of emoticons (alt+L) are displayed on three columns
  respectively: the name of emoticon, the type of emoticon (standard
  emoticon or emoji), the corresponding character.

When you press OK, the characters for the chosen emoticon will be copied to
your clipboard, ready for pasting.

## تخصيص رموز المشاعر ##

From NVDA MENU, Preferences -> Manage emoticons -> Customize emoticons, you can open a dialog setting to add or to edit available emoticons.

This dialog allows you to save an emoticons speech dictionary with your
customizations.

بالضغط على زر "حفظ وتصدير المعجم" سيتم حفظ ملف باسم emoticons.dic داخل مجلد
إعدادات المستخدم ثم مجلد معاجم النطق المتفرع عنه.

## إعدادات التفعيل ##

From menu Preferences -> Manage Emoticons -> Activation settings, you can choose whether to Activate speaking of emoticons when starting NVDA. By default it is disabled.

It is also possible to save your choice for this setting.

## مفاتيح الاختصار: ##

These are the key command available by default, you can edit those or add
new key to open Activation settings dialog or Emoticon Dictionary dialog:

* NVDA+E: speaching emoticons on/off, toggles between speaking text as it is
  written, or with the emoticons replaced by the human description.
* NVDA+I: show a dialog to select an emoticon you want to copy.


## Changes for 5.0 ##

* Added support for emojis.
* Improvements for Insert Emoticon dialog with a filter field and radio
  buttons to choose displayed emoticons.
* Using guiHelper for Activation settings dialog and Insert Emoticon dialog:
  requires NVDA 2016.4 or higher versions

## مستجدات الإصدار 4.0 ##

* إذا كانت محاورة إدراج رموز المشاعر مفتوحة بالتزامن مع تنشيط محاورة أخرى,
  ستظهر رسالة الخطأ التي تفيد بذلك.


## مستجدات الإصدار 3.0 ##

* أصبح من الممكن تخصيص نطق الكلمة الأصلية عندما تتطابق مع الكلمة البديلة,
  طبقا لمعاجم النطق ب NVDA2014.4. بمحاورة تخصيص رموز المشاعر.


## مستجدات الإصدار 2.0 ##

* توافر ملف المساعدة بمدير الإضافات البرمجية.


## مستجدات الإصدار 1.1 ##

* حذف رموز المشاعر المكررة.
* تمت إضافة المزيد من رموز المشاعر.

## مستجدات الإصدار 1.0 ##

* إصدار بدائي

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=emo

[2]: https://addons.nvda-project.org/files/get.php?file=emo-dev
