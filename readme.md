# Emoticons #

* Authors: Chris Leo, Noelia Ruiz Martínez, Mesar Hameed, Francisco Javier Estrada Martínez
* Download [stable version][1]
* Download [development version][2]

Using this add-on, spoken text containing emoticon characters will be replaced by its more human friendly description.

For example: the sequence ":)" will be spoken as "smiling smiley", or for example NVDA will recognize the meaning of each emoji.

You can take advantage of the following features:

## Insert Emoticon ##

Sometimes an image is worth a 1000 words: use the new emoji to liven up your instant message and to let your friends know how you’re feeling.

When you are unsure of the characters for a particular smiley, this addon enables you to select and insert it into your text such as in a chat.

Press NVDA+I, or from menu Tools -> Insert emoticon, to open a dialog with the provided emoticons or emoji.

This dialog allows you to choose an emoticon and to view the emoticons that interest you:

*	An editable field allows you to filter the search for the desired emoticon among the emoticons available.
*	Through a set of radio buttons, you can choose to view only emoji category (alt+E) or view only standard emoticon category (alt+s) or view all emoticons available (alt+A).
*	In the list of emoticons (alt+L) are displayed on three columns respectively: the name of emoticon, the type of emoticon (standard emoticon or emoji), the corresponding character.

When you press OK, the characters for the chosen emoticon will be copied to your clipboard, ready for pasting.

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

If you may wish to keep clean your configuration folders, in this dialog it is also possible to choose if dictionaries not used (associated with non existing profiles) will be removed from the add-on when it is unloaded.

Also, it's possible to enable Settings only in normal configuration (not recommended). This is intended to disable settings changes in case of speed issues when switching profiles.

## Key Commands: ##

These are the key commands available by default, you can edit those or add new key to open Emoticons settings panel or Emoticon Dictionary dialog:

* NVDA+E: speaking emoticons on/off, toggles between speaking text as it is written, or with the emoticons replaced by the human description.
* NVDA+I: show a dialog to select an emoticon you want to copy.



## Changes for 8.0 ##

* Compatible with NVDA 2018.3 (required).

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

[1]: http://addons.nvda-project.org/files/get.php?file=emo

[2]: http://addons.nvda-project.org/files/get.php?file=emo-dev

[3]: https://github.com/nvdaes/emoticons/releases/download/6.5/emoticons-6.5.nvda-addon