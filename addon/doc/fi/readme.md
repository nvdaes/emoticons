# Hymiöt #

* Authors: Chris Leo, Noelia Ruiz Martínez, Mesar Hameed, Francisco Javier
  Estrada Martínez
* Lataa [vakaa versio][1]
* Lataa [kehitysversio][2]

Using this add-on, spoken text containing emoticon characters will be
replaced by its more human friendly description.

For example: the sequence ":)" will be spoken as "smiling smiley", or for
example NVDA will recognize the meaning of each emoji.

Voit hyödyntää seuraavia ominaisuuksia:

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

## Mukauta hymiöitä ##

From NVDA MENU, Preferences -> Manage emoticons -> Customize emoticons, you can open a dialog setting to add or to edit available emoticons.

This dialog allows you to save an emoticons speech dictionary with your
customizations.

Kun painat "Tallenna ja vie sanasto" -painiketta, asetuskansiossasi olevaan
speechDicts-alikansioon luodaan emoticons.dic-niminen sanastotiedosto.

## Käyttöönoton asetukset ##

From menu Preferences -> Manage Emoticons -> Activation settings, you can choose whether to Activate speaking of emoticons when starting NVDA. By default it is disabled.
It is also possible to save your choice for this setting.

## Näppäinkomennot: ##

These are the key command available by default, you can edit those or add
new key to open Activation settings dialog or Emoticon Dictionary dialog:

* NVDA+E: ottaa käyttöön tekstin lukemisen sellaisena kuin se on kirjoitettu
  tai hymiöiden korvaamisen niiden kuvauksilla.
* NVDA+I: show a dialog to select an emoticon you want to copy.


## Changes for 5.0 ##

* Added support for emojis.
* Improvements for Insert Emoticon dialog with a filter field and radio
  buttons to choose displayed emoticons.
* Using guiHelper for Activation settings dialog and Insert Emoticon dialog:
  requires NVDA 2016.4 or higher versions

## Muutokset versiossa 4.0 ##

* NVDA näyttää virheilmoituksen, jos Lisää hymiö -valintaikkuna avataan
  toisen asetusvalintaikkunan ollessa aktiivisena.


## Muutokset versiossa 3.0 ##

* Mukauta hymiöitä -valintaikkunassa on nyt mahdollista määrittää, että
  haettava merkkijono täsmää vain, jos se on kokonainen sana, kuten
  puhesanastoissa NVDA:n 2014.4-versiosta lähtien.


## Muutokset versiossa 2.0 ##

* Ohje on käytettävissä Lisäosien hallinnasta.


## Muutokset versiossa 1.1 ##

* Poistettu hymiö, joka oli listassa kahteen kertaan.
* Muutama hymiö lisätty.

## Muutokset versiossa 1.0 ##

* Ensimmäinen versio.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=emo

[2]: http://addons.nvda-project.org/files/get.php?file=emo-dev
