# Emotikoni #
* Autori: Chris Leo, Noelia Ruiz Martínez, Mesar Hameed, Francisco Javier
  Estrada Martínez
* NVDA kompatibilnost: 2019.3 i novije
* Preuzmi [stabilnu verziju][1]
* Preuzmi [razvojnu verziju][2]

Kad se koristi ovaj dodatak, emotikoni će se izgovoriti riječima ljudskog
jezika.

Na primjer, znakovni niz „:)” će se izgovoriti kao „smješkajući smješko” ili
npr. NVDA će prepoznati značenje svakog emojija.

Moguće je koristiti sljedeće funkcije:

## Umetni emotikon ##

Ponekad je slika vrijedna tisuću riječi: koristite novi emoji da biste
oživili vaše poruke i kažete prijateljima kako se osjećate.

Kada niste sigurni za neki smješko, ovaj dodatak dozvoljava, odabrati i
umetnuti ga u tekst kao što je chat.

Pritisnite NVDA+I ili iz izbornika Alati>Emotikoni>Umetni emotikon, da biste otvorili dijaloški okvir dostupnih emotikona ili emojia.

Ovaj dijaloški okvir dozvoljava biranje emotikona i pregledavanje emotikona
koji vas zanimaju:

*	Uredivo polje, koje omogućuje pretraživanje emotikona koji vas zanimaju.
*	Pomoću različitih izbornih gumba, možete izabrati prikaz emoji kategorije
  (Alt+E), prikaz kategorije standarnih emotikona (alt+S) ili sve dostupne
  emotikone (Alt+A).
*	U popisu emotikona (Alt+L) prikazana su u tri stupca: ime emotikona, vrsta
  emotikona (standardni emotikon ili emoji) te odgovarajući znak.

Kad pritisnete U redu, znakovi za odabrani emotikon će se kopirati u
međuspremnik, spremni da ih zalijepite.

## Umetni znak ##

Ovaj dijaloški okvir omogućuje odabir jednog od znakova dostupnih u
dijaloškom okviru izgovora interpunkcija/znakova. Pomoću okvira za
uređivanje filtra ili tipki sa strelicama možete odabrati stavku s popisa
znakova. Zatim pritisnite U redu i odabrani emojiji ili znak kopirat će se u
međuspremnik i spreman je za umetanje.

## Rječnik emotikona ##

Dodatak Emotikoni dozvoljava različite govorne rječnike korištenjem
konfiguracijskih profila.

To znači da možete stvoriti ili urediti poseban govorni rječnik za svaki
svoj prilagođeni profil.

U NVDA izborniku, Postavke>Govorni rječnici>Rječnik emotikona, možete otvoriti dijaloški okvir za dodavanje ili uređivanje dostupnih emotikona.

Spremanjem vaših prilagodbi, nove postavke za čitanje emotikona će se
primjenjivati samo za profil koji trenutačno uređujete.

Primjerice, želite da NVDA izgovara prilagođene emotikone samo u XxChat
programu, ali ne u drugim programima za čavrljanje: možete kreirati profil
za XxChat aplikaciju i dodijeliti je govornom rječniku otvaranjem izbornika
Govorni rječnik, opcija za Rječnik emotikona. Vidi niže dolje o postavkama
za Emotikone u odnosu na konfiguracijski profil.

Također možete izvesti svaki prilagođeni govorni rječnik pritiskom tipke
„Spremi i izvezi rječnik”: na taj način će se vaši govorni rječnici spremiti
u mapu vaše korisničke konfiguracije, u podmapu „speechDicts/emoticons”.

Točno ime i lokacija datoteke rječnika bit će bazirana na konfiguracijskom
profilu koji se trenutačno uređuje, koji će biti prikazan u naslovu
dijaloškog okvira Rječnik emotikona.

## Postavke Emotikona ##

Iz izbornika Postavke>Postavke>Emotikoni otvara ploču za konfiguriranje aktiviranja vaših govornih rječnika za svaki profil.

U dijaloškom okviru aktivacijskih postavki možete izabrati želite li da se govorni rječnik automatski aktivira kad se NVDA prebaci u profil koji trenutačno uređujete. Prema zadanim postavkima, ova opcija je isključena u uobičajenoj NVDA konfiguraciji i svim novim profilima.

Pored toga, moguće je odrediti treba li se govoriti o dodatak emojis. Ovo bi
moglo biti korisno za očuvanje izgovaranja simbola ako su emojii uključeni u
NVDA konfiguraciju.

Ako želite izbrisati mape s konfiguracijom, možete odabrati da se rječnici
neće koristiti (nepostojeći profili će biti uklonjeni iz dodatka).

## Tipkovnički prečaci: ##

Ovo su zadani tipkovnički prečaci. Možete ih urediti ili dodati novi prečac
za otvaranje dijaloškog okvira za Postavke emotikona ili dijaloškog okvira
za Rječnik emotikona:

* NVDA+E: uključuje i isključuje izgovaranje emotikona. Prebacuje između
  izgovaranja teksta kako je napisan i opisa emotikona.
* NVDA+I: Prikazuje dijaloški okvir za biranje emotikona koji želite
  kopirati.
* Nije dodijeljeno: Prikazuje dijaloški okvir za biranje znaka koji želite
  kopirati.
* Nije dodijeljeno: otvorite poruku koja se može čitati i koja pokazuje
  simbol na kojem se nalazi pregledni kursor, tako da se čitav opis može
  pregledati u modusu čitanja.
* Nije dodijeljeno: otvorite poruku koja se može čitati i koja pokazuje
  simbol na kojem se nalazi kursor, tako da se čitav opis može pregledati u
  modusu čitanja.

Napomena: Na Windows 10 je moguće koristiti i ugrađenu ploču emojija.

## Promjene u verziji 13.0 ##

* Ispravljene greške u dijaloškom okviru za umetanje emotikona.
* Dodan je dijaloški okvir za umetanje jednog znaka dostupan u izgovoru
  interpunkcija/znakova.

## Promjene u verziji 12.0 ##

* Zahtijeva NVDA 2019.3 i novije verzije.

## Promjene u verziji 11.0 ##

* Kad se dodatak nadogradi, rječnici spremljeni u prethodnoj verziji dodatka
  automatski će se kopirati u novu verziju, osim ako više ne želite uvesti
  rječnike spremljene u glavnoj NVDA mapi rječnika.
* Kad prikazuju simbol na kojem se nalaze kursor ili pregledni kusor, riječi
  Znak i Zamjena koriste se za razlikovanje samog simbola od njegovog opisa
  u modusu čitanja, što je korisno za korisnike govora.

## Promjene u verziji 10.0 ##

* Dodane su naredbe za prikaz simbola na kojem se nalaze kursor ili
  pregledni kursor. Geste za ove naredbe je moguće dodijeliti u dijaloškom
  okviru Ulazne geste, u kategoriji Pregled teksta.

## Promjene u verziji 9.0 ##

* Dodana je mogućnost za odlučivanje o tome, trebaju li se govoriti emojii
  dodatka.
* Koristi se odgovarajuće kodiranje za nazive rječnika, ispravljajući
  greške, kad sadrže određene znakove.
* Prevedeni sažetak dodatka pravilno se koristi za naslov koji se prikazuje
  u pomoći dodatka, dostupna u upravljaču za dodatke.
* Dodana je napomena u kojoj se spominje ploča s emojijima, koja je dostupna
  u sustavu Windows 10.

## Promjene u verziji 8.0 ##

* Kompatibilno s NVDA 2018.3 i novijim verzijama (obavezno).

## Promjene u verziji 7.0 ##

* Dijaloški okvir postavki za Aktiviranje je premješten na ploču u NVDA
  postavkama, tako da će se trenutačni profil prikazati u naslovu dijaloškog
  okvira NVDA postavki.
* Izbornik „Upravljaj emotikonima” je uklonjen: sada se „Umetni emotikon”
  nalazi u izborniku Alati, a „Prilagodi emotikone” će se prikazati pod
  „Govorni rječnici” kao što je „Rječnik emotikona”.
* Zahtijeva NVDA inačicu 2018.2 ili noviju.
* Ako treba, moguće je preuzeti [zadnju inačicu kompatibilnu s NVDA
  2017.3][3].

## Promjene u verziji 6.0 ##

* Dodana podrška za profile konfiguracije.
* U NVDA verziji 2017.4 ili novijoj, konfiguracijske postavke i prilagođeni
  rječnici će se automatski promijeniti u odnosu na odabrane profile. U NVDA
  verziji 2017.3 ili starijoj, možete primijeniti promjene ponovnim
  učitavanjem dodataka (pritisnite kombinaciju kontrol+NVDA+F3).
* Ako odlučite uvesti postavke tijekom ažuriranja dodatka, zastarjele
  datoteke (emoticons.ini i emoticon.dic) će se ukloniti ili prilagoditi toj
  verziji.

## Promjene u verziji 5.0 ##

* Dodana podrška za emojie.
* Poboljšanja u dijaloškom okviru za umetanje emotikona uključujući i
  odabirne gumbe za izbor kategorije i polje za pretragu emotikona.
* Koristi se guiHelper za dijaloški okvir postavki aktivacije i dijaloški
  okvir za umetanje emotikona: zahtijeva NVDA verziju 2016.4 ili noviju

## Promjene u verziji 4.0 ##

* Ako je dijaloški okvir za umetanje emotikona otvoren u isto vrijeme, kad
  je aktivan i drugi dijaloški okvir postavki, NVDA će prikazati
  odgovarajuću poruku pogreške.


## Promjene u verziji 3.0 ##

* U dijaloškom okviru Prilagodi emotikone, sada je moguće odrediti da se
  uzorak poklapa samo, ako se nađe kao cijela riječ, prema govornim
  riječnicima u NVDA 2014.4.


## Promjene u verziji 2.0 ##

* Pomoć dodatka je dostupna iz upravljača za dodatke.


## Promjene u verziji 1.1 ##

* Izbrisan dupli emotikon.
* Dodano nekoliko smješaka.

## Promjene u verziji 1.0 ##

* Prvo izdanje.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=emo

[2]: https://addons.nvda-project.org/files/get.php?file=emo-dev

[3]: https://addons.nvda-project.org/files/get.php?file=emo-o
