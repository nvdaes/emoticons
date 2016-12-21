# Emoticons #

* Authors: Chris Leo, Noelia Ruiz Martínez, Mesar Hameed, Francisco Javier Estrada Martínez
* Download [stable version][1]
* Download [development version][2]

Using this add-on, spoken text containing emoticon characters will be replaced by its more human friendly description.

For example: the sequence  ":)" will be spoken as "smiling smiley", or for example NVDA will recognize  the meaning of each emoji.

You can take advantage of the following features:

## Insert Emoticon Dialog ##

When you are unsure of the characters for a particular smiley, this addon enables you to select and insert it into your text such as in a chat.

Press NVDA+I, or from menu Preferences -> Manage emoticons -> Insert smiley, to open a dialog with the provided emoticons or emoji.

This dialog allows you to choose an emoticon and to view  the emoticons that interest you:

*	A editable field allows you to filter the search for the desired emoticon among the emoticons available.
*	Through a set of radio buttons, you can choose to view    only emoji category (alt+E) or view only standard emoticon category (alt+s) or view all emoticons available (alt+A).
*	In the list of emoticons (alt+L) are displayed  on three columns respectively: the name of emoticon, the type of emoticon (standard emoticon or emoji), the  corresponding character.

When you press OK, the characters for the chosen emoticon will be copied to your clipboard, ready for pasting.

## Customize emoticons ##

From NVDA MENU, Preferences -> Manage emoticons -> Customize emoticons, you can open a dialog setting to add or to edit available emoticons.

This dialog allows you to save an emoticons speech  dictionary  with your customizations.

Pressing "Save and export dictionary" button, a file dictionary named emoticons.dic will be saved in your user config folder, speechDicts subfolder.

## Activation settings ##

From menu Preferences -> Manage Emoticons -> Activation settings, you can choose whether to Activate speaking of emoticons when starting NVDA. By default it is disabled.
It is also possible to save your choice for this setting.

## Key Commands: ##

These are the key command available by default, you can edit those or add new key to open Activation settings dialog or Emoticon Dictionary dialog:

* NVDA+E: toggles between speaking text as it is written, or with the emoticons replaced by the human description.
* NVDA+I: show a dialog to select an emoticon you want to copy.


## Changes for 5.0 ##

* Added support for emojis.
* Improvements for Insert Emoticon dialog with a filter field and radio buttons to choose displayed emoticons.
* Using guiHelper for Activation settings dialog and Insert Emoticon dialog: requires NVDA 2016.4 or higher versions 

## Changes for 4.0 ##

* If the Insert smiley dialog is opened when another settings dialog is active, NVDA will show the corresponding error message.


## Changes for 3.0 ##

* In the Customize emoticons dialog, it is now possible to specify that a pattern should only match if it is a whole word, according to speech dictionaries of NVDA 2014.4.


## Changes for 2.0 ##

* Add-on help is available from the Add-ons Manager.


## Changes for 1.1 ##

* Removed duplicated emoticon.
* Added some smileys.

## Changes for 1.0 ##

* Initial version.

[1]: http://addons.nvda-project.org/files/get.php?file=emo

[2]: http://addons.nvda-project.org/files/get.php?file=emo-dev
