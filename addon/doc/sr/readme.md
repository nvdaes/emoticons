# Emotikoni #

* Authors: Chris Leo, Noelia Ruiz Martínez, Mesar Hameed, Francisco Javier
  Estrada Martínez
* preuzmi [stabilnu verziju][1]
* preuzmi [verziju u razvoju][2]

Using this add-on, spoken text containing emoticon characters will be
replaced by its more human friendly description.

For example: the sequence ":)" will be spoken as "smiling smiley", or for
example NVDA will recognize the meaning of each emoji.

Evo nekoliko osnovnih mogućnosti dodatka:

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

## Prilagođavanje emotikona ##

From NVDA MENU, Preferences -> Manage emoticons -> Customize emoticons, you can open a dialog setting to add or to edit available emoticons.

This dialog allows you to save an emoticons speech dictionary with your
customizations.

Pritiskom na dugme "Sačuvaj i prenesi rečnik" biće kreiran fajl
emoticons.dic u kome će biti rečnik emotikona, a biće smešten u folder sa
podešavanjima NVDA, podfolder speechDicts.

## Podešavanja aktivacije ##

From menu Preferences -> Manage Emoticons -> Activation settings, you can choose whether to Activate speaking of emoticons when starting NVDA. By default it is disabled.
It is also possible to save your choice for this setting.

## Prečice ##

These are the key command available by default, you can edit those or add
new key to open Activation settings dialog or Emoticon Dictionary dialog:

* NVDA+E: uključuje i isključuje opis emotikona
* NVDA+I: show a dialog to select an emoticon you want to copy.


## Changes for 5.0 ##

* Added support for emojis.
* Improvements for Insert Emoticon dialog with a filter field and radio
  buttons to choose displayed emoticons.
* Using guiHelper for Activation settings dialog and Insert Emoticon dialog:
  requires NVDA 2016.4 or higher versions

## Promene u 4.0 ##

* Ako je otvoren dijalog za ubacivanje smajlija kada je neki NVDA dijalog sa
  podešavanjima otvoren, odgovarajuća greška je prikazana.


## Promene u 3.0 ##

* Sada je moguće u dijalogu za prilagođavanje emotikona podesiti da se
  emotikon opisuje samo ako je u pitanju cela reč, što se poklapa sa
  govornim rečnicima od verzije NVDA 2014.4 i u novijim verzijama.


## Promene u 2.9 ##

* Pomoć za dodatak je dostupna iz menadžera/upravljača dodataka.


## Promene u 1.1 ##

* Uklonjen duplirani emotikon.
* Dodati neki smajliji.

## Promene u 1.0 ##

* Prva verzija

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=emo

[2]: http://addons.nvda-project.org/files/get.php?file=emo-dev
