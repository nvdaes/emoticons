# Emoticons #

* Authors: Chris Leo, Noelia Ruiz Martínez, Mesar Hameed, Francisco Javier
  Estrada Martínez
* [Stabile Version herunterladen][1]
* [Testversion herunterladen][2]

Using this add-on, spoken text containing emoticon characters will be
replaced by its more human friendly description.

For example: the sequence ":)" will be spoken as "smiling smiley", or for
example NVDA will recognize the meaning of each emoji.

Folgende Features:

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

## Benutzerdefinierte Emoticons ##

From NVDA MENU, Preferences -> Manage emoticons -> Customize emoticons, you can open a dialog setting to add or to edit available emoticons.

This dialog allows you to save an emoticons speech dictionary with your
customizations.

Der Schalter "Wörterbuch speichern und exportieren" legt eine Datei namens
"Emoticons.dic" in Ihrem "User Config"-Verzeichnis unterhalb von
"speechDicts" ab.

## Aktivierungseinstellungen ##

From menu Preferences -> Manage Emoticons -> Activation settings, you can choose whether to Activate speaking of emoticons when starting NVDA. By default it is disabled.
It is also possible to save your choice for this setting.

## Tastenkombinationen: ##

These are the key command available by default, you can edit those or add
new key to open Activation settings dialog or Emoticon Dictionary dialog:

* NVDA+E: Legt fest, ob Text so gelesen wird, wie er geschrieben wurde oder
  ob Emoticons durch die menschliche Beschreibung ersetzt werden sollen.
* NVDA+I: show a dialog to select an emoticon you want to copy.


## Changes for 5.0 ##

* Added support for emojis.
* Improvements for Insert Emoticon dialog with a filter field and radio
  buttons to choose displayed emoticons.
* Using guiHelper for Activation settings dialog and Insert Emoticon dialog:
  requires NVDA 2016.4 or higher versions

## Änderungen in 4.0 ##

* Wenn der Dialog Smiley einfügen geöffnet wird, während ein
  Einstellungsdialog von NVDA aktiv ist, wird die zugehörige Fehlermeldung
  ausgegeben.


## Änderungen in 3.0 ##

* Im Dialog Smileys verwalten kann nun festgelegt werden, dass ein Muster
  nur gültig ist, wenn es ein ganzes Wort ist. Vergleichbar mit
  deAussprache-Wörterbüchern von NVDA 2014.4.


## Änderungen in 2.0 ##

* Eine Hilfe für diese Erweiterung ist in der Erweiterungsverwaltung
  verfügbar.


## Änderungen in 1.1 ##

* Doppeltes Emoticon entfernt.
* Smileys hinzugefügt.

## Änderungen in 1.0 ##

* Ehrstveröffentlichung

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=emo

[2]: http://addons.nvda-project.org/files/get.php?file=emo-dev
