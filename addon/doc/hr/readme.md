# Emotikoni #

* Authors: Chris Leo, Noelia Ruiz Martínez, Mesar Hameed, Francisco Javier
  Estrada Martínez
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

Pritisnite NVDA+I, ili iz izbornika Postavke > Upravljanje emotikonima > Umetanje emotikona da biste otvorili dijaloški okvir dostupnih emotikona ili emoji

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

## Prilagodi emotikone ##

Dodatak Emotikoni dozvoljava vam da imate različite govorne rječnike za
korištenje konfiguracijskih profila.

This means that you can create or edit a specific speech-dictionary for each
your custom profile.

From NVDA MENU, Preferences -> Manage emoticons -> Customize emoticons, you can open a dialog setting to add or to edit available emoticons.

Spremanjem vaših prilagodbi, nove postavke za čitanje emotikona će se
primjenjivati samo za profil koji trenutno uređujete.

Primjerice, želite da NVDA izgovara prilagođene emotikone samo u XxChat
programu, ali ne u drugim programima za čavrljanje: možete kreirati profil
za XxChat aplikaciju i primijeniti govorni rječnik otvaranjem izbornika
Prilagodi emotikone.

You can also export each custom speech-dictionary pressing "Save and export
dictionary" button: in this way your speech-dictionaries will be saved in
your user config folder, speechDicts/emoticons subfolder.

Točno ime i lokacija datoteke rječnika bit će bazirana na konfiguracijskom
profilu koji se trenutno uređuje, koji će biti prikazan u naslovu dijaloškog
okvira Rječnik emotikona.

## Postavke aktivacije ##

From menu Preferences -> Manage Emoticons -> Activation-settings opens a dialog to configure the activation of your speech-dictionaries for each profile.

U dijaloškom okviru aktivacijskih postavki možete izabrati želite li ili ne želite da se govorni rječnik automatski aktivira kad se NVDA prebacuje u profil koji trenutno uređujete. Prema zadanim postavkima, ova opcija je isključena u uobičajenoj konfiguraciji NVDA i svim novim profilima.

Ako želite izbrisati mape s konfiguracijom, možete odabrati da se rječnici
neće koristiti (nepostojeći profili će biti uklonjeni iz dodatka).

## Prečaci na tipkovnici: ##

Ovo su zadane tipkovničke kratice, iste možete uređivati ili dodati novu
kraticu za otvaranje dijaloškog okvira postavki aktivacije ili dijaloški
okvir rječnika emotikona: 

* NVDA+E: speaking emoticons on/off, toggles between speaking text as it is
  written, or with the emoticons replaced by the human description.
* NVDA+I: show a dialog to select an emoticon you want to copy.

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

[1]: http://addons.nvda-project.org/files/get.php?file=emo

[2]: http://addons.nvda-project.org/files/get.php?file=emo-dev
