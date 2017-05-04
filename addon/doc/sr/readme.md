# Emotikoni #

* Autori: Chris Leo, Noelia Ruiz Martínez, Mesar Hameed, Francisco Javier
  Estrada Martínez
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

Pritisnite NVDA+I, ili iz menija podešavanja-> upravljanje emotikonima-> ubaci emotikon, da otvorite dijalog sa ponuđenim emotikonima ili emojima.

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

## Prilagođavanje emotikona ##

Iz NVDA menija odaberite Podešavanja > Upravljaj emotikonima > Prilagođavanje emotikona, to će otvoriti prozor u kojem možete dodavati ili menjati postojeće emotikone.

Ovaj dijalog vam dozvoljava da sačuvate govorni rečnik sa vašim prilagođenim
emotikonima.

Pritiskom na dugme "Sačuvaj i prenesi rečnik" biće kreiran fajl
emoticons.dic u kome će biti rečnik emotikona, a biće smešten u folder sa
podešavanjima NVDA, podfolder speechDicts.

## Podešavanja aktivacije ##

Iz menija podešavanja-> upravljanje emotikonima-> podešavanja aktivacije, možete izabrati da li izgovor emotikona treba da se aktivira kada se NVDA pokrene. Onemogućeno je po podrazumevanim podešavanjima.

Takođe je moguće sačuvati vaš izbor za ovo podešavanje.

## Prečice ##

Ovo su komande koje su podrazumevano dostupne, možete ih urediti ili dodati
nove da otvorite dijaloge za podešavanja:

* NVDA+E: uključuje i isključuje opis emotikona
* NVDA+I: otvara prozor za izbor emotikona za kopiranje u privremenu
  memoriju


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

[1]: http://addons.nvda-project.org/files/get.php?file=emo

[2]: http://addons.nvda-project.org/files/get.php?file=emo-dev
