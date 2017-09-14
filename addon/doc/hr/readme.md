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

From NVDA MENU, Preferences -> Manage emoticons -> Customize emoticons, you can open a dialog setting to add or to edit available emoticons.

Ovaj dijaloški okvir dozvoljava vam da sačuvate govorni rječnik emotikona s
vašim prilagodbama. 

Kada pritisnete gumb spremi i uvezi rječnik, datoteka emoticons.dic će biti
spremljena u vašoj mapi  user config, speechDicts podmapi.

## Postavke aktivacije ##

From menu Preferences -> Manage Emoticons -> Activation settings, you can choose whether to Activate speaking of emoticons when starting NVDA. By default it is disabled.

Također možete spremiti svoj odabir za ovo podešenje.

## Prečaci na tipkovnici: ##

Ovo su zadane tipkovničke kratice, iste možete uređivati ili dodati novu
kraticu za otvaranje dijaloškog okvira postavki aktivacije ili dijaloški
okvir rječnika emotikona: 

* NVDA+E: speaching emoticons on/off, toggles between speaking text as it is
  written, or with the emoticons replaced by the human description.
* NVDA+I: show a dialog to select an emoticon you want to copy.


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
