# Emotikony / Emoticons #

* Authors: Chris Leo, Noelia Ruiz Martínez, Mesar Hameed, Francisco Javier
  Estrada Martínez
* Pobierz [wersja stabilna][1]
* Pobierz [wersja rozwojowa][2]

Using this add-on, spoken text containing emoticon characters will be
replaced by its more human friendly description.

For example: the sequence ":)" will be spoken as "smiling smiley", or for
example NVDA will recognize the meaning of each emoji.

Możesz wykorzystać następujące funkcje:

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

## Dostosuj emotikony ##

From NVDA MENU, Preferences -> Manage emoticons -> Customize emoticons, you can open a dialog setting to add or to edit available emoticons.

This dialog allows you to save an emoticons speech dictionary with your
customizations.

Naciśnij przycisk "Zapisz i eksportuj słownik", plik słownika o nazwie
emoticons.dic zostanie zapisany w twoim folderze konfiguracji użytkownika,
podfolderze speechDicts.

## Ustawienia aktywacji ##

From menu Preferences -> Manage Emoticons -> Activation settings, you can choose whether to Activate speaking of emoticons when starting NVDA. By default it is disabled.

It is also possible to save your choice for this setting.

## Skróty klawiszowe: ##

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

## Changes for 4.0 ##

* If the Insert smiley dialog is opened when another settings dialog is
  active, NVDA will show the corresponding error message.


## Zmiany dla wersji 3.0 ##

* W oknie konfiguracji dodatku, , można teraz określić, że wzorzec powinien
  pasować tylko, jeśli jest całym słowem, zgodnie ze słownikami mowy NVDA
  2014.4.


## Zmiany dla wersji 2.0 ##

* Pomoc dodatku dostępna w managerze dodatków.


## Zmiany dla wersji 1.1 ##

* Usunięty powielony emotikon.
* Dodano kilka buź.

## Zmiany dla wersji 1.0 ##

* Pierwsza wersja.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=emo

[2]: https://addons.nvda-project.org/files/get.php?file=emo-dev
