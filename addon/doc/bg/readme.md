# Емотикони #

* Authors: Chris Leo, Noelia Ruiz Martínez, Mesar Hameed, Francisco Javier
  Estrada Martínez
* Изтегляне [стабилна версия][1]
* Изтегляне [работна версия][2]

Using this add-on, spoken text containing emoticon characters will be
replaced by its more human friendly description.

For example: the sequence ":)" will be spoken as "smiling smiley", or for
example NVDA will recognize the meaning of each emoji.

Можете да се възползвате от следните възможности:

## Insert Emoticon ##

When you are unsure of the characters for a particular smiley, this addon
enables you to select and insert it into your text such as in a chat.

Press NVDA+I, or from menu Preferences -> Manage emoticons -> Insert emoticon, to open a dialog with the provided emoticons or emoji.

This dialog allows you to choose an emoticon and to view the emoticons that
interest you:

*	An editable field allows you to filter the search for the desired emoticon
  among the emoticons available.
*	Through a set of radio buttons, you can choose to view    only emoji category (alt+E) or view only standard emoticon category (alt+s) or view all emoticons available (alt+A).
*	In the list of emoticons (alt+L) are displayed  on three columns respectively: the name of emoticon, the type of emoticon (standard emoticon or emoji), the  corresponding character.

When you press OK, the characters for the chosen emoticon will be copied to
your clipboard, ready for pasting.

## Персонализиране на емотиконите ##

From NVDA MENU, Preferences -> Manage emoticons -> Customize emoticons, you can open a dialog setting to add or to edit available emoticons.

This dialog allows you to save an emoticons speech dictionary with your
customizations.

При натискане на бутона "Запиши и експортирай речника", речников файл с име
emoticons.dic ще бъде записан в папката с вашите потребителски настройки, в
подпапката speechDicts.

## Настройки за задействането ##

From menu Preferences -> Manage Emoticons -> Activation settings, you can choose whether to Activate speaking of emoticons when starting NVDA. By default it is disabled.
It is also possible to save your choice for this setting.

## Клавишни комбинации: ##

These are the key command available by default, you can edit those or add
new key to open Activation settings dialog or Emoticon Dictionary dialog:

* NVDA+E: Превключва изговарянето на емотиконите като такива или като
  текстови знаци.
* NVDA+I: show a dialog to select an emoticon you want to copy.


## Changes for 5.0 ##

* Added support for emojis.
* Improvements for Insert Emoticon dialog with a filter field and radio
  buttons to choose displayed emoticons.
* Using guiHelper for Activation settings dialog and Insert Emoticon dialog:
  requires NVDA 2016.4 or higher versions

## Промени във версия 4.0 ##

* Ако прозорецът за вмъкване на емотикон бъде отворен при наличието на друг
  отворен прозорец с настройки, NVDA ще изведе съответното съобщение за
  грешка.


## Промени във версия 3.0 ##

* В прозореца за Персонализиране на емотиконите, вече е възможно да се укаже
  че даден шаблон трябва да съвпада само с цели думи, в съгласие с речниците
  за реч в NVDA 2014.4.


## Промени във версия 2.0 ##

* Помощта за добавката е достъпна от мениджъра на добавките.


## Промени във версия 1.1 ##

* Премахнат е дублиращ се емотикон.
* Добавени са няколко усмивки.

## Промени във версия 1.0 ##

* Първоначално издание.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=emo

[2]: http://addons.nvda-project.org/files/get.php?file=emo-dev
