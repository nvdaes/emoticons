# Emotikoni #

* Autori: Chris Leo, Noelia Ruiz Martínez, Mesar Hameed, Francisco Javier
  Estrada Martínez

Uz ovaj dodatak, svi emotikoni u izgovorenom tekstu biće zamenjeni
odgovarajućim opisom.

Na primer: ":)" će biti izgovoreno kao "Smajli koji se osmehuje", ili NVDA
će reći značenje svakog emoji znaka

Evo nekoliko osnovnih mogućnosti dodatka:

## Ubacivanje emotikona ##

Nekada je slika vredna 1000 reči: Koristite novi emoji da oživite vaše
poruke i kažete vašim prijateljima kako se osećate.

Kada niste sigurni o znakovima za neki smajli, ovaj dodatak vam dozvoljava
da ga izaberete i unesete u tekst kao što je ćaskanje.

Pritisnite NVDA+I, ili iz menija alati -> emotikoni > ubaci emotikon, da otvorite dijalog sa ponuđenim emotikonima ili emojima.

Ovaj dijalog vam dozvoljava da izaberete emotikon i prikažete emotikone koji
vas interesuju:

*	Polje za uređivanje vam dozvoljava da pretražujete emotikone i prikažete
  samo one koji vas interesuju.
*	Kroz različite radio dugmiće, možete da izaberete prikaz samo emoji
  kategorije(alt+E) ili samo kategorije standardnih emotikona(alt+t) ili sve
  dostupne emotikone(alt+s).
*	U listi emotikona(alt+L) emotikoni su prikazani u tri kolone: Ime
  emotikona, vrsta emotikona(standardan emotikon ili emoji), odgovarajući
  znakovi.

Kada pritisnete OK, znakovi za izabran emotikon će biti kopirani u
privremenu memoriju, spremni da se nalepe.

## Ubaci simbol ##

This dialog allows you to choose one of the symbols available in the
Punctuation/symbol pronunciation dialog of NVDA. You can use the Filter edit
box or the arrow keys to select an item from the symbols list.

If you want to copy various symbols, use the Add button to append them to
the Symbols to copy edit box.

Then, press OK and the selected emoji or symbol, or the symbols contained in
the mentioned edit box, will be copied to your clipboard, ready for pasting.

## Associate gestures to symbols ##

From NVDA's menu, Preferences submenu, Input gestures dialog, category
Insert symbols, you can configure NVDA to type symbols through associated
gestures.

You can use the Edit field edit box to reduce the number of symbols
presented, so that this category can be expanded faster.

## Rečnik emotikona ##

Dodatak za emotikone vam dozvoljava da imate različite rečnike za različite
profile podešavanja.

Ovo znači da možete da uredite ili napravite rečnik za svaki vaš prilagođeni
profil.

Iz NVDA menija, opcije-> govorni rečnici-> rečnik emotikona, možete otvoriti dijalog za dodavanje ili uređivanje emotikona.

Čuvajući vaša prilagođavanja, nova podešavanja za čitanje emotikona će se
primeniti samo na onaj profil koji trenutno uređujete.

Na primer, možda želite da NVDA izgovara prilagođene emotikone samo u XxChat
programu, ali ne u drugim programima za ćaskanje: Možete ovo da uradite
pravljenjem profila za XxChat aplikaciju i zatim da mu pridružite govorni
rečnik iz menija govornih rečnika, opcija rečnik emotikona. Ispod pogledajte
dodatne detalje za podešavanje emotikona u zavisnosti od profila
podešavanja.

Takođe možete da izvezete vaš rečnik emotikona aktiviranjem dugmeta "Sačuvaj
i izvezi rečnik ": Na ovaj način vaši govorni rečnici će biti sačuvani u
folderu sa korisničkimm podešavanjima, speechDicts/emoticons podfolderu.

Tačno ime i lokacija rečnika zavise od profila koji se uređuje, a oni će
biti prikazani u naslovu dijaloga za rečnik emotikona.

## Podešavanja emotikona ##

Iz menija opcije-> podešavanja-> emotikoni možete otvoriti panel da podesite aktivaciju govornih rečnika za svaki profil.

U panelu podešavanja emotikona možete izabrati da li će se rečnik automatski aktivirati kada NVDA promeni profil na onaj koji trenutno uređujete. Podrazumevano je ovo onemogućeno u standardnim NVDA podešavanjima i svim drugim profilima.

Takođe, moguće je odrediti da li će dodatak izgovarati Emoji znakove. Ovo
može biti korisno kako bi se sačuvao izgovor simbola ako je neki Emoji znak
uključen u NVDA.

Ako želite da održavate vaš folder sa podešavanjima, u ovom dijalogu takođe
je moguće izabrati da li će rečnici koji se ne koriste (koji su pridruženi
nepostojećim profilima ) biti uklonjeni iz dodatka kada se zatvori.

## Prečice ##

Ovo su komande koje su podrazumevano dostupne, možete ih urediti ili dodati
nove da otvorite panel za podešavanja ili dijalog za rečnik emotikona:

* NVDA+E: Uključuje ili isključuje izgovor emotikona, izgovara tekst kao što
  je napisan, ili menja emotikone ljudskim opisima.
* NVDA+I: otvara prozor za izbor emotikona za kopiranje u privremenu
  memoriju
* Nema prečice: Prikazuje dijalog za izbor NVDA simbola za kopiranje.
* Nema prečice: Otvara poruku u režimu pretraživanja koja prikazuje simbol
  na trenutnoj poziciji preglednog kursora, kako biste mogli da pregledate
  ceo opis.
* Nema prečice: Otvara poruku u režimu pretraživanja koja prikazuje simbol
  na poziciji kursora, kako biste mogli da pregledate ceo opis.

Note: On Windows 10 and higher, it's also possible to use the built-in emoji
panel.

## Changes for 17.0 ##

* Added ability to associate gestures to type symbols.
* Added ability to copy various symbols at the same time.

## Changes for 16.0 ##

* Compatible with NVDA 2023.1.

## Changes for 15.0 ##

* Requires NVDA 2022.1 or later.
* Cannot be used in secure mode.

## Promene u 14.0 ##

* Kompatibilan sa NVDA 2021.1.

## Promene u 13.0 ##

* Ispravljene greške u dijalogu za ubacivanje emotikona.
* Dodat dijalog za ubacivanje simbola koji su dostupni u NVDA dijalogu
  izgovora znakova interpunkcije i simbola.

## promene u  12.0 ##

* Zahteva NVDA 2019.3 ili noviji.

## Promene u 11.0 ##

* Kada je dodatak ažuriran, rečnici sačuvani u trenutnoj verziji će
  automatski biti kopirani u novu verziju, osim ako želite da uvezete
  rečnike iz glavnog NVDA foldera.
* Kada se prikazuje simbol na poziciji sistemskog ili preglednog kursora,
  reči znak i zamena se koriste kako bi se razlikovao simbol i njegov opis,
  korisno za korisnike govorne podrške.

## Promene u 10.0 ##

* Dodate komande za prikazivanje simbola na poziciji preglednog ili
  sistemskog kursora. Prečice za ove komande se mogu podesiti u dijalogu
  ulazne komande, iz kategorijje pregled teksta.

## Promene u 9.0 ##

* Dodata mogućnost izbora da li će se Emoji znakovi iz dodatka izgovarati
  ili ne.
* Sada se koristi ispravno kodiranje za rečnike, što ispravlja greške kada
  rečnici sadrže određene znakove.
* Preveden opis dodatka se ispravno koristi kada se aktivira dugme za
  prikazivanje pomoći dodatka, dostupno iz dijaloga upravljanja dodacima.
* Dodata napomena koja spominje dostupnost Emoji panela na Windowsu 10.

## Promene u 8.0 ##

* Kompatibilan uz NVDA 2018.3 ili noviji (minimalna neophodna verzija ).

## Promene u 7.0 ##

* Dijalog aktivacije je premešten u panel sa NVDA podešavanjima, kako bi se
  prikazao naziv trenutnog profila koji se uređuje.
* Uklonjen je  meni upravljanja emotikonima: Sada je opcija za ubacivanje
  emotikona u meniju alati, a prilagođavanje emotikona u govornim rečnicima
  kao opcija rečnika emotikona.
* Zahteva NVDA 2018.2 ili noviji.
* Ako je neophodno, možete preuzeti [poslednju verziju kompatibilnu uz NVDA
  2017.3][3].

## Promene u 6.0 ##

* Dodata podrška za profile podešavanja.
* U NVDA 2017.4 ili novijem, podešavanja i rečnici će se automatski menjati
  u zavisnosti od profila podešavanja. U 2017.3 ili starijem, možete
  primeniti promene tako što ćete ponovo učitati dodatke (pritiskanjem
  kontrol+NVDA+f3).
* Ako izaberete da uvezete podešavanja kada ažurirate dodatak, zastarele
  datoteke (emoticons.ini i emoticons.dic) biće uklonjene ili prilagođene za
  ovu verziju.

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


## Promene u 2.0 ##

* Pomoć za dodatak je dostupna iz menadžera/upravljača dodataka.


## Promene u 1.1 ##

* Uklonjen duplirani emotikon.
* Dodati neki smajliji.

## Promene u 1.0 ##

* Prva verzija

[[!tag dev stable]]

[3]: https://www.nvaccess.org/addonStore/legacy?file=emo-o
