# Emoticons #

* Authors: Chris Leo, Noelia Ruiz Martínez, Mesar Hameed
* Download [stable version][1]
* Download [development version][2]

Using this add-on, spoken text containing emoticon characters will be replaced by its more human friendly description.
86 emoticons are defined.

For example: ":)" will be spoken as "smiling smiley", or ":D" will be spoken as "laughing smiley"

You can take advantage of the following features:

## Insert Smiley ##

When you are unsure of the characters for a particular smiley, this feature enables you to select and insert it into your text such as in a chat.
Press **NVDA+I**, or from the **NVDA** menu, choose **Preferences -> Manage Emoticons -> Insert Smiley**, to open a dialog 
with the provided smilies. Choose a smily and pres **OK** to copy the correct characters to your clipboard, ready for pasting.

## Customize Emoticons ##

From the **NVDA** MENU, choose **Preferences -> Manage emoticons -> Customize Emoticons**. You can use this dialog to add or to edit available emoticons.
This dialog allows you to save an emoticons speech dictionary with your customizations.

Press **Save and Export Dictionary** to save a file named emoticons.dic in your user config folder, speechDicts subfolder.

## Activation settings ##

You can choose whether to activate speaking of emoticons when starting NVDA. By default it is disabled.
It is also possible to save your choice for this setting.

## Key Commands ##

* **NVDA+E**: toggles between speaking text as it is written, or with the emoticons replaced by the human description.
* **NVDA+I**: shows a dialog to select a smiley you want to paste.

## Changes for 5.0 ##

* Added support for emojis.
* Improvements for the **Insert Emoticon** dialog with a filter field and radio buttons to choose displayed emoticons.
* Uses **guiHelper** for the **Activation Settings** and the **Insert Emoticon**
Dialog.
* Now requires NVDA 2016.4 or higher versions.

## Changes for 4.0 ##

* If the **Insert Smiley** dialog is opened when another settings dialog is active, NVDA will show the corresponding error message.

## Changes for 3.0 ##

* In the **Customize Emoticons** dialog, it is now possible to specify that a pattern should only match if it is a whole word, according to the NVDA speech dictionaries of NVDA 2014.4.


## Changes for 2.0 ##

* Add-on help is available from the NVDA **Add-ons Manager**.

## Changes for 1.1 ##

* Removed duplicated emoticon.
* Added some smileys.

## Changes for 1.0 ##

* Initial version.

[1]: http://addons.nvda-project.org/files/get.php?file=emo

[2]: http://addons.nvda-project.org/files/get.php?file=emo-dev
