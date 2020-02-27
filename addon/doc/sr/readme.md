# Emotikoni #
* Autori: Chris Leo, Noelia Ruiz Martínez, Mesar Hameed, Francisco Javier
  Estrada Martínez
* NVDA compatibility: 2019.3 or later
* preuzmi [stabilnu verziju][1]
* preuzmi [verziju u razvoju][2]

Uz ovaj dodatak, svi emotikoni u izgovorenom tekstu biće zamenjeni
odgovarajućim opisom.

Na primer: ":)" će biti izgovoreno kao "osmeh", ili NVDA će reći značenje
svakog emoji znaka

Evo nekoliko osnovnih mogućnosti dodatka:

## Ubacivanje emotikona ##

Nekada je slika vredna 1000 reči: Koristite novi emoji da oživite vaše
poruke i kažete vašim prijateljima kako se osećate.

Kada niste sigurni o znakovima za neki smajli, ovaj dodatak vam dozvoljava
da ga izaberete i unesete u tekst kao što je ćaskanje.

Press NVDA+I, or from menu Tools -> Insert emoticon, to open a dialog with the provided emoticons or emoji.

Ovaj dijalog vam dozvoljava da izaberete emotikon i prikažete emotikone koji
vas interesuju:

*	Polje za uređivanje vam dozvoljava da pretražujete emotikone i prikažete
  samo one koji vas interesuju.
*	Kroz različite radio dugmiće, možete da izaberete prikaz samo emoji
  kategorije(alt+E) ili samo kategoriju standardnih emotikona(alt+s) ili sve
  dostupne emotikone(alt+A).
*	U listi emotikona(alt+L) su prikazane u tri kolone: Ime emotikona, vrsta
  emotikona(standardan emotikon ili emoji), odgovarajući znakovi.

Kada pritisnete OK, znakovi za izabran emotikon će biti kopirani u
privremenu memoriju, spremni da se nalepe.

## Emoticons dictionary ##

Emoticons add-on allows to have differents speech-dictionaries using
configuration profiles.

This means that you can create or edit a specific speech-dictionary for each
your custom profile.

From NVDA MENU, Preferences -> Speech dictionaries -> Emoticons dictionary, you can open a dialog to add or to edit available emoticons.

Saving your customizations, the new reading settings of emoticons will only
apply to the profile you are currently editing.

For example, you may wish that NVDA spoken custom emoticons only in XxChat
program, but not in other chat programs: you can do this by creating a
profile for the XxChat application and assign to it a speech dictionary from
Speech dictionaries menu, Emoticons dictionary option. See below for
Emoticons settings in relation to the configuration profiles.

You can also export each custom speech-dictionary pressing "Save and export
dictionary" button: in this way your speech-dictionaries will be saved in
your user config folder, speechDicts/emoticons subfolder.

The exact name and location of the dictionary file will be based on the
editing configuration profile, which will be shown in the title of the
Emoticons dictionary dialog.

## Emoticons settings ##

From menu Preferences -> Settings -> Emoticons opens a panel to configure the activation of your speech-dictionaries for each profile.

In Emoticons settings panel you can choose whether or not speech-dictionary should automatically activate when  NVDA switches to the   profile you are currently editing. By default it is disabled in normal configuration of NVDA and in all your new profiles.

Moreover, it's possible to determine if the add-on emojis should be
spoken. This could be useful to preserve symbols speaking if emojis are
included in NVDA's configuration.

If you may wish to keep clean your configuration folders, in this dialog it
is also possible to choose if dictionaries not used (associated with non
existing profiles) will be removed from the add-on when it is unloaded.

## Prečice ##

These are the key commands available by default, you can edit those or add
new key to open Emoticons settings panel or Emoticon Dictionary dialog:

* NVDA+E: speaking emoticons on/off, toggles between speaking text as it is
  written, or with the emoticons replaced by the human description.
* NVDA+I: otvara prozor za izbor emotikona za kopiranje u privremenu
  memoriju
* Not assigned: open a browseable message showing the symbol where the
  review cursor is positioned, so that the whole description can be reviewed
  in browse mode.
* Not assigned: open a browseable message showing the symbol where the caret
  is positioned, so that the whole description can be reviewed in browse
  mode.

Note: On Windows 10, it's also possible to use the built-in emoji panel.

## Changes for 12.0 ##

* Requires NVDA 2019.3 or later.

## Changes for 11.0 ##

* When the add-on is updated, dictionaries saved in the previous version of
  the add-on will be automatically copied to the new version, unless you
  prefer to import dictionaries saved in the main dictionaries folder of
  NVDA.
* When showing the symbol where the caret or the review cursor are
  positioned, the words Character and Replacement are used to distinguish
  between the symbol itself and its description in browse mode, useful for
  speech users.

## Changes for 10.0 ##

* Added commands to show the symbol where the review cursor or caret are
  positioned. Gestures for these commands can be assigned from the Input
  gestures dialog, Text review category.

## Changes for 9.0 ##

* Added the possibility of choosing if add-on emojis should be spoken.
* Used appropiate encoding for dictionary names, fixing errors when they
  contain certain characters.
* The translated summary of the add-on is properly used for the title
  presented in add-on help, accessible from the add-on manager.
* Added a note mentioning the emoji panel available on Windows 10.

## Changes for 8.0 ##

* Compatible with NVDA 2018.3 or later (required).

## Changes for 7.0 ##

* The Activation settings dialog has been moved to a panel in NVDA settings,
  so that the current profile will be shown in the title of the NVDA
  settings dialog.
* The Manage Emoticons menu has been removed: now Insert emoticon will be
  found under the Tools menu, and Customize Emoticons will be shown under
  Speech dictionaries like Emoticons dictionary.
* Requires NVDA 2018.2 or later.
* If needed, you can download the [last version compatible with NVDA
  2017.3][3].

## Changes for 6.0 ##

* Added support for configuration profiles.
* In NVDA 2017.4 or later, the configuration settings and custom
  dictionaries will change automatically according with the selected
  profiles. In 2017.3 or earlier, you can apply changes by reloading plugins
  (pressing control+NVDA+f3).
* If you choose to import settings when updating the add-on, deprecated
  files (emoticons.ini and emoticons.dic) will be removed or adapted to this
  version.

## Promene u 5.0 ##

* Dodata podrška za emoji.
* Poboljšanja u dijalogu za ubacivanje emotikona uključujući radio dugmiće
  za izbor kategorije i polje za pretragu emotikona.
* Koristi se guiHelper za dijalog za podešavanja aktivacije i ubacivanje
  emotikona: Zahteva NVDA 2016.4 ili noviji

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

[1]: https://addons.nvda-project.org/files/get.php?file=emo

[2]: https://addons.nvda-project.org/files/get.php?file=emo-dev

[3]: https://addons.nvda-project.org/files/get.php?file=emo-o
