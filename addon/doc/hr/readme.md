# Emotikoni #

* Authors: Chris Leo, Noelia Ruiz Martínez, Mesar Hameed, Francisco Javier
  Estrada Martínez
* NVDA compatibility: 2018.3 to 2019.1
* Preuzmite [stabilnu inačicu][1]
* Preuzmite [razvojnu inačicu][2]

Using this add-on, spoken text containing emoticon characters will be
replaced by its more human friendly description.

For example: the sequence ":)" will be spoken as "smiling smiley", or for
example NVDA will recognize the meaning of each emoji.

možete imati koristi od slijedećih značajki:

## Insert Emoticon ##

Ponekad je slika vrijedna tisuću riječi: Koristite novi emoji da oživite
vaše poruke i kažete prijateljima kako se osjećate. 

Kada niste sigurni za neki smješko, ovaj dodatak vam dozvoljava da ga
izaberete i umetnete u tekst kao što je čavrljanje. 

Press NVDA+I, or from menu Tools -> Insert emoticon, to open a dialog with the provided emoticons or emoji.

Ovaj dijaloški okvir dozvoljava vam da izaberete emotikon i pregledate
emotikone koji vas zanimaju.

*	Polje za uređivanje dozvoljava vam da pretražujete emotikone i prikažete
  samo one koji vas zanimaju.
*	Kroz različite odabirne gumbe, možete izabrati prikaz samo emoji
  kategorije (Alt+E) ili samo kategoriju standarnih emotikona (alt+S) ili
  sve dostupne emotikone (Alt+A). 
*	U popisu emotikona (Alt+L) prikazane su u tri kolone: ime emotikona, tip
  emotikona (standardni emotikon ili emoji), te odgovarajući znak. 

Kada pritisnete OK, znakovi za odabrani emotikon bit će kopirani u
međuspremnik, spremni da ih zalijepite.

## Emoticons dictionary ##

Dodatak Emotikoni dozvoljava vam da imate različite govorne rječnike za
korištenje konfiguracijskih profila.

This means that you can create or edit a specific speech-dictionary for each
your custom profile.

From NVDA MENU, Preferences -> Speech dictionaries -> Emoticons dictionary, you can open a dialog to add or to edit available emoticons.

Spremanjem vaših prilagodbi, nove postavke za čitanje emotikona će se
primjenjivati samo za profil koji trenutno uređujete.

For example, you may wish that NVDA spoken custom emoticons only in XxChat
program, but not in other chat programs: you can do this by creating a
profile for the XxChat application and assign to it a speech dictionary from
Speech dictionaries menu, Emoticons dictionary option. See below for
Emoticons settings in relation to the configuration profiles.

You can also export each custom speech-dictionary pressing "Save and export
dictionary" button: in this way your speech-dictionaries will be saved in
your user config folder, speechDicts/emoticons subfolder.

Točno ime i lokacija datoteke rječnika bit će bazirana na konfiguracijskom
profilu koji se trenutno uređuje, koji će biti prikazan u naslovu dijaloškog
okvira Rječnik emotikona.

## Emoticons settings ##

From menu Preferences -> Settings -> Emoticons opens a panel to configure the activation of your speech-dictionaries for each profile.

In Emoticons settings panel you can choose whether or not speech-dictionary should automatically activate when  NVDA switches to the   profile you are currently editing. By default it is disabled in normal configuration of NVDA and in all your new profiles.

Ako želite izbrisati mape s konfiguracijom, možete odabrati da se rječnici
neće koristiti (nepostojeći profili će biti uklonjeni iz dodatka).


## Prečaci na tipkovnici: ##

These are the key commands available by default, you can edit those or add
new key to open Emoticons settings panel or Emoticon Dictionary dialog:

* NVDA+E: speaking emoticons on/off, toggles between speaking text as it is
  written, or with the emoticons replaced by the human description.
* NVDA+I: show a dialog to select an emoticon you want to copy.

Note: On Windows 10, it's also possible to use the built-in emoji panel.

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
* U NVDA inačici 2017.4 ili novijoj, konfiguracijske postavke i rječnici će
  se automatski promijeniti u odnosu na odabrane profile. U NVDA inačici
  2017.3 ili starijoj, možete primijeniti promjene ponovnim učitavanjem
  dodataka (pritisnite kombinaciju control+NVDA+F3).
* Ako odlučite uvesti postavke tijekom ažuriranja dodatka, obustavljene
  datoteke (emoticons.ini i emoticon.dic) bit će obrisane ili prilagođene
  toj verziji.

## Changes for 5.0 ##

* Dodana podrška za emotikone.
* Poboljšanja u dijaloškom okviru za umetanje emotikona uključujući i
  odabirne gumbe za izbor kategorije i polje za pretragu emotikona. 
* Koristi se guiHelper za dijaloški okvir postavki aktivacije i dijaloški
  okvir za umetanje emotikona: zahtijeva NVDA inačicu 2016.4 ili noviju

## Changes for 4.0 ##

* Ako je otvoren dijaloški okvir za umetanje emotikona u isto vrijeme kada
  je aktivan i drugi dijaloški okvir postavki, NVDA će prikazati
  odgovarajuću poruku pogreške. 


## Promjene u inačici 3.0 ##

* U dijaloškom okviru prilagodi emotikone, sada je moguće postaviti da se
  uzarak poklapa samo ako se nađe kao cijela riječ, usporedo sa govornim
  riječnicima u NVDA 2014.4.


## izmjene u inačici 2.0 ##

* Pomoć dodatka je dostupna iz upravitelja dodataka.


## Izmjene u inačici 1.1 ##

* Izbrisan dupli emotikon.
* Dodani nekoliko smješaka.

## Promjene u inačici 1.0 ##

* prva inačica.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=emo

[2]: https://addons.nvda-project.org/files/get.php?file=emo-dev

[3]: https://addons.nvda-project.org/files/get.php?file=emo-o
