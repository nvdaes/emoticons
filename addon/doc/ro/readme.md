# Emoticoane #

* Authors: Chris Leo, Noelia Ruiz Martínez, Mesar Hameed, Francisco Javier
  Estrada Martínez
* Descarcă [versiunea stabilă][1]
* Descarcă [versiunea în dezvoltare][2]

Using this add-on, spoken text containing emoticon characters will be
replaced by its more human friendly description.

For example: the sequence ":)" will be spoken as "smiling smiley", or for
example NVDA will recognize the meaning of each emoji.

Există următoarele caracteristici:

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

## Personalizează emoticoanele ##

From NVDA MENU, Preferences -> Manage emoticons -> Customize emoticons, you can open a dialog setting to add or to edit available emoticons.

This dialog allows you to save an emoticons speech dictionary with your
customizations.

Apăsând butonul "Salvare și exportare dicționar", un fișier numit
emoticons.dic va fi salvat în folderul de configurare al utilizatorului, în
sub-folderul speechDicts.

## Setări de activare ##

From menu Preferences -> Manage Emoticons -> Activation settings, you can choose whether to Activate speaking of emoticons when starting NVDA. By default it is disabled.
It is also possible to save your choice for this setting.

## Comenzi de tastatură ##

These are the key command available by default, you can edit those or add
new key to open Activation settings dialog or Emoticon Dictionary dialog:

* NVDA+E: Comută între vorbirea textului așa cum este scris, sau cu
  descrierea emoticoanelor.
* NVDA+I: show a dialog to select an emoticon you want to copy.


## Changes for 5.0 ##

* Added support for emojis.
* Improvements for Insert Emoticon dialog with a filter field and radio
  buttons to choose displayed emoticons.
* Using guiHelper for Activation settings dialog and Insert Emoticon dialog:
  requires NVDA 2016.4 or higher versions

## Modificări aduse în 4.0 ##

* Dacă dialogul de Înserare emoticon este deschis când alt dialog de setări
  este activ, NVDA va arăta un mesaj de eroare.


## Modifcări aduse în verisunea 3.0. ##

* În dialogul de persoanlziare emoticon, este acum posibil să specifici dacă
  un model trebuie să fie asemănător dacă este un cuvânt întreg, în
  acordanță cu dicționarele de vorbire versiunii NVDA 2014.4.


## Modificări aduse în versiunea 2.0. ##

* Ajutorul add-on-ului este disponibil din manager-ul de add-on-uri.


## Modifcări aduse în versiunea 1.1. ##

* Au fost șterse emoticoanele duplicate.
* Au mai fost adăugate ceva emoticoane.

## Modificări aduse în versiuna 1.0. ##

* Versiunea Inițială.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=emo

[2]: http://addons.nvda-project.org/files/get.php?file=emo-dev
