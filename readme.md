# Emoticons #

* Authors: Chris Leo, Noelia Ruiz Martínez, Mesar Hameed, Francisco Javier Estrada Martínez

Using this add-on, spoken text containing emoticon characters will be replaced by its more human friendly description.

For example: the sequence ":)" will be spoken as "smiling smiley", or for example NVDA will recognize the meaning of each emoji.

You can take advantage of the following features:

## Insert Emoticon ##

Sometimes an image is worth a 1000 words: use the new emoji to liven up your instant message and to let your friends know how you’re feeling.

When you are unsure of the characters for a particular smiley, this addon enables you to select and insert it into your text such as in a chat.

Press NVDA+I, or from menu Tools -> Emoticons > Insert emoticon, to open a dialog with the provided emoticons or emoji.

This dialog allows you to choose an emoticon and to view the emoticons that interest you:

*	An editable field allows you to filter the search for the desired emoticon among the emoticons available.
*	Through a set of radio buttons, you can choose to view only emoji category (alt+E) or view only standard emoticon category (alt+s) or view all emoticons available (alt+A).
*	In the list of emoticons (alt+L) are displayed on three columns respectively: the name of emoticon, the type of emoticon (standard emoticon or emoji), the corresponding character.

When you press OK, the characters for the chosen emoticon will be copied to your clipboard, ready for pasting.

## Insert symbol ##

This dialog allows you to choose one of the symbols available in the Punctuation/symbol pronunciation dialog of NVDA. You can use the Filter edit box or the arrow keys to select an item from the symbols list.

If you want to copy various symbols, use the Add button to append them to the Symbols to copy edit box.

Then, press OK and the selected emoji or symbol, or the symbols contained in the mentioned edit box, will be copied to your clipboard, ready for pasting.

## Associate gestures to symbols ##

From NVDA's menu, Preferences submenu, Input gestures dialog, category Insert symbols, you can configure NVDA to type symbols through associated gestures.

You can use the Edit field edit box to reduce the number of symbols presented, so that this category can be expanded faster.

## Emoticons dictionary ##

Emoticons add-on allows to have differents speech-dictionaries using configuration profiles.

This means that you can create or edit a specific speech-dictionary for each your custom profile.

From NVDA MENU, Preferences -> Speech dictionaries -> Emoticons dictionary, you can open a dialog to add or to edit available emoticons.

Saving your customizations, the new reading settings of emoticons  will only apply to the profile you are currently editing.

For example, you may wish that NVDA spoken custom emoticons only in XxChat program, but not in other chat programs: you can do this by creating a profile for the XxChat application and assign to it a speech  dictionary from Speech dictionaries menu, Emoticons dictionary option. See below for Emoticons settings in relation to the configuration profiles.

You can also export each custom speech-dictionary pressing "Save and export dictionary" button: in this way your  speech-dictionaries will be saved in your user config folder, speechDicts/emoticons subfolder. 

The exact name and location of the dictionary file will be based on the editing configuration profile, which will be shown in the title of the Emoticons dictionary dialog.

## Emoticons settings ##

From menu Preferences -> Settings -> Emoticons opens a panel to configure the activation of your speech-dictionaries for each profile.

In Emoticons settings panel you can choose whether or not speech-dictionary should automatically activate when  NVDA switches to the   profile you are currently editing. By default it is disabled in normal configuration of NVDA and in all your new profiles.

Moreover, it's possible to determine if the add-on emojis should be spoken. This could be useful to preserve symbols speaking if emojis are included in NVDA's configuration.

If you may wish to keep clean your configuration folders, in this dialog it is also possible to choose if dictionaries not used (associated with non existing profiles) will be removed from the add-on when it is unloaded.

## Key Commands: ##

These are the key commands available by default, you can edit those or add new key to open Emoticons settings panel or Emoticon Dictionary dialog:

* NVDA+E: speaking emoticons on/off, toggles between speaking text as it is written, or with the emoticons replaced by the human description.
* NVDA+I: show a dialog to select an emoticon you want to copy.
* Not assigned: show a dialog to select an NVDA's symbol you want to copy.
* Not assigned: open a browseable message showing the symbol where the review cursor is positioned, so that the whole description can be reviewed in browse mode.
* Not assigned: open a browseable message showing the symbol where the caret is positioned, so that the whole description can be reviewed in browse mode.

Note: On Windows 10 and higher, it's also possible to use the built-in emoji panel.

## Changes for 22.0.0 ##

* Requires NVDA 2023.2 or later.

## Changes for 17.0 ##

* Added ability to associate gestures to type symbols.
* Added ability to copy various symbols at the same time.

## Changes for 16.0 ##

* Compatible with NVDA 2023.1.

## Changes for 15.0 ##

* Requires NVDA 2022.1 or later.
* Cannot be used in secure mode.

## Changes for 14.0 ##

* Compatible with NVDA 2021.1.

## Changes for 13.0 ##

* Fixed errors in Insert Emoticon dialog.
* Added a dialog to insert a symbol available in the Punctuation/symbol pronunciation of NVDA.

## Changes for 12.0 ##

* Requires NVDA 2019.3 or later.

## Changes for 11.0 ##

* When the add-on is updated, dictionaries saved in the previous version of the add-on will be automatically copied to the new version, unless you prefer to import dictionaries saved in the main dictionaries folder of NVDA.
* When showing the symbol where the caret or the review cursor are positioned, the words Character and Replacement are used to distinguish between the symbol itself and its description in browse mode, useful for speech users.

## Changes for 10.0 ##

* Added commands to show the symbol where the review cursor or caret are positioned. Gestures for these commands can be assigned from the Input gestures dialog, Text review category.

## Changes for 9.0 ##

* Added the possibility of choosing if add-on emojis should be spoken.
* Used appropiate encoding for dictionary names, fixing errors when they contain certain characters.
* The translated summary of the add-on is properly used for the title presented in add-on help, accessible from the add-on manager.
* Added a note mentioning the emoji panel available on Windows 10.

## Changes for 8.0 ##

* Compatible with NVDA 2018.3 or later (required).

## Changes for 7.0 ##

* The Activation settings dialog has been moved to a panel in NVDA settings, so that the current profile will be shown in the title of the NVDA settings dialog.
* The Manage Emoticons menu has been removed: now Insert emoticon will be found under the Tools menu, and Customize Emoticons will be shown under Speech dictionaries like Emoticons dictionary.
* Requires NVDA 2018.2 or later.
* If needed, you can download the [last version compatible with NVDA 2017.3][3].

## Changes for 6.0 ##

* Added support for configuration profiles.
* In NVDA 2017.4 or later, the configuration settings and custom dictionaries will change automatically according with the selected profiles. In 2017.3 or earlier, you can apply changes by reloading plugins (pressing control+NVDA+f3).
* If you choose to import settings when updating the add-on, deprecated files (emoticons.ini and emoticons.dic) will be removed or adapted to this version.

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


[3]: https://www.nvaccess.org/addonStore/legacy?file=emo-o
