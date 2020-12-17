# Hymiöt #
* Tekijät: Chris Leo, Noelia Ruiz Martínez, Mesar Hameed, Francisco Javier
  Estrada Martínez
* Yhteensopivuus: NVDA 2019.3 tai uudempi
* Lataa [vakaa versio][1]
* Lataa [kehitysversio][2]

Puhutussa tekstissä olevat hymiömerkit korvataan tätä lisäosaa käytettäessä
niiden ihmisystävällisemmillä kuvauksilla.

Esimerkki: Merkit ":)" luetaan "hymyilee", ja NVDA tunnistaa myös emojit.

Voit hyödyntää seuraavia ominaisuuksia:

## Lisää hymiö ##

Joskus kuva kertoo enemmän kuin 1000 sanaa: käytä uusia emojeja
pikaviestiesi elävöittämiseen ja ilmoittaaksesi ystävillesi, miltä sinusta
tuntuu.

Kun olet epävarma jonkin tietyn hymiön merkeistä, tämän lisäosan avulla voit
valita ja lisätä ne tekstiisi, kuten esim. chattiin.

Paina NVDA+I tai valitse Työkalut / Hymiöt / Lisää hymiö avataksesi valintaikkunan, jossa näkyvät käytettävissä olevat hymiöt ja emojit.

Tästä valintaikkunasta voit valita haluamasi hymiön ja tarkastella
sellaisia, jotka sinua kiinnostavat:

*	Muokkauskentän avulla voit suodattaa hakua löytääksesi käytettävissä
  olevien hymiöiden joukosta haluamasi.
*	Valintapainikkeilla voit valita, näytetäänkö vain emojit (Alt+E), vain
  tavalliset hymiöt (Alt+I) vai kaikki käytettävissä olevat hymiöt (Alt+A).
*	Hymiöluettelossa (Alt+H) näytetään kolmessa sarakkeessa hymiön nimi,
  tyyppi (tavallinen tai emoji) sekä vastaava merkki.

Kun painat OK, valitun hymiön merkit kopioidaan leikepöydälle, josta voit
liittää ne haluamaasi paikkaan.

## Lisää symboli ##

Tästä valintaikkunasta voit valita jonkin Välimerkkien ja symboleiden
puhuminen -valintaikkunassa olevista symboleista. Voit käyttää
Suodata-muokkauskenttää tai nuolinäppäimiä symbolin valitsemiseen
luettelosta. Paina sitten OK, jonka jälkeen  valittu emoji tai symboli
kopioidaan leikepöydälle.

## Hymiösanasto ##

Hymiöt-lisäosa mahdollistaa eri puhesanastot asetusprofiileja käyttäen.

Tämä tarkoittaa, että voit luoda kullekin profiilille oman puhesanaston tai
muokata sitä.

Voit avata valintaikkunan uusien hymiöiden lisäämiseksi tai olemassa olevien muokkaamiseksi valitsemalla NVDA-valikosta Asetukset -> Puhesanastot -> Hymiöt.

Uudet hymiöiden lukuasetukset koskevat vain muokattavaa profiilia.

Saatat esim. haluta, että NVDA puhuu muokatut hymiöt XxChatissa, muttei
muissa chattiohjelmissa. Tämä onnistuu luomalla profiili
XxChat-sovellukselle ja liittämällä siihen puhesanasto
Puhesanastot-alavalikosta löytyvää Hymiöt-vaihtoehtoa käyttäen. Katso alta
tietoja asetusprofiileihin liittyvistä Hymiöt-lisäosan asetuksista.

Voit myös viedä luomasi puhesanastot painamalla "Tallenna ja vie sanastot"
-painiketta. Sanastot tallennetaan asetuskansiossasi olevaan
speechDicts\emoticons-alikansioon.

Puhesanastotiedoston tarkka nimi ja sijainti määräytyvät muokattavan
profiilin mukaan, joka näkyy hymiösanastovalintaikkunan nimessä.

## Hymiöt-lisäosan asetukset ##

Asetukset-valikon kohdasta Asetukset -> Hymiöt avautuu paneeli, josta voit määrittää puhesanastojen käyttöönoton asetukset kullekin asetusprofiilille.

Hymiöt-asetuspaneelissa voit valita, otetaanko puhesanasto automaattisesti käyttöön NVDA:n vaihtaessa muokkaamaasi profiiliin. Asetus ei ole  oletusarvoisesti käytössä NVDA:n normaaleissa asetuksissa eikä uusissa profiileissa.

Lisäksi on mahdollista määrittää, puhutaanko lisäosan emojit. Tästä voi olla
hyötyä symbolien puhumisen säilyttämisessä, jos NVDA:n asetuksiin sisältyy
emojeita.

Mikäli haluat pitää asetuskansiosi puhtaana, tästä valintaikkunasta on myös
mahdollista valita, poistetaanko käyttämättömät (ei-olemassa oleviin
profiileihin liitetyt) puhesanastot lisäosasta, kun se poistetaan muistista.

## Näppäinkomennot: ##

Nämä ovat oletusnäppäinkomentoja. Voit muokata niitä tai lisätä uuden
Hymiöt-asetuspaneelin tai hymiösanastovalintaikkunan avaamiseen:

* NVDA+E: hymiöiden puhuminen käyttöön/pois käytöstä - ottaa käyttöön
  tekstin lukemisen sellaisena kuin se on kirjoitettu tai hymiöiden
  korvaamisen niiden kuvauksilla.
* NVDA+I: näyttää valintaikkunan, josta voit valita tekstiin lisättävän
  hymiön.
* Ei määritetty: näyttää valintaikkunan, josta voit valita kopioitavan
  NVDA:n symbolin.
* Ei määritetty: Avaa selattavan viestin, jossa näytetään
  tarkastelukohdistimen kohdalla oleva symboli, jotta sen koko kuvausta
  voidaan tarkastella selaustilassa.
* Ei määritetty: Avaa selattavan viestin, jossa näytetään kohdistimen
  kohdalla oleva symboli, jotta sen koko kuvausta voidaan tarkastella
  selaustilassa.

Huom: Windows 10:ssä on mahdollista käyttää myös sisäänrakennettua
emojipaneelia.

## Muutokset versiossa 13.0 ##

* Korjattu Lisää hymiö -valintaikkunan virheitä.
* Lisätty valintaikkuna, josta voidaan lisätä jokin NVDA:n Välimerkkien ja
  symboleiden puhuminen -valintaikkunassa olevista symboleista.

## Muutokset versiossa 12.0 ##

* Edellyttää NVDA 2019.3:a tai uudempaa.

## Muutokset versiossa 11.0 ##

* Kun lisäosa päivitetään, iaemmassa versiossa tallennetut sanastot
  kopioidaan automaattisesti uuteen versioon, paitsi jos haluat tuoda ne
  NVDA:n sanastojen pääkansiosta.
* Kun järjestelmä- tai tarkastelukohdistimen kohdalla oleva symboli
  näytetään, sanoja "merkki" ja "korvaava teksti" käytetään erottamaan
  toisistaan varsinainen symboli ja sen kuvaus, mistä on hyötyä pelkän
  puheen käyttäjille.

## Muutokset versiossa 10.0 ##

* Lisätty komennot, joilla voidaan näyttää tarkastelukohdistimen tai
  järjestelmäkohdistimen kohdalla oleva symboli. Näiden komentojen
  syötekomennot on mahdollista määrittää Syötekomennot-valintaikkunan
  Tekstin tarkastelu -kategoriasta.

## Muutokset versiossa 9.0 ##

* Lisätty mahdollisuus valita, puhutaanko lisäosan emojit.
* Sanastojen nimissä käytetään nyt asianmukaista merkistöä, mikä korjaa
  virheitä, joita ilmeni, kun nimissä oli tiettyjä merkkejä.
* Lisäosan käännettyä yhteenvetoa käytetään asianmukaisesti Lisäosien
  hallinnasta löytyvän lisäosaohjeen nimenä.
* Lisätty maininta Windows 10:n emojipaneelista.

## Muutokset versiossa 8.0 ##

* Yhteensopiva NVDA 2018.3:n tai uudemman kanssa (vaaditaan).

## Muutokset versiossa 7.0 ##

* Käyttöönottoasetusten valintaikkuna on siirretty NVDA:n asetusnäytön
  paneeliin, jotta nykyinen profiili näkyy Asetukset-valintaikkunan nimessä.
* Hymiöiden hallinta -valikko on poistettu. Lisää hymiö -vaihtoehto löytyy
  nyt Työkalut-valikosta, ja "Mukauta hymiöitä" näkyy
  Puhesanastot-alavalikossa nimellä Hymiöt.
* Vaatii NVDA 2018.2:n tai uudemman.
* Tarvittaessa voit ladata [viimeisimmän version, joka on yhteensopiva NVDA
  2017.3:n kanssa.][3]

## Muutokset versiossa 6.0 ##

* Lisätty tuki asetusprofiileille.
* NVDA 2017.4:ssä tai uudemmassa asetukset muuttuvat ja puhesanastot
  vaihtuvat automaattisesti valittuna olevan profiilin
  mukaisesti. 2017.3:ssa tai aiemmassa versiossa voit ottaa muutokset
  käyttöön lataamalla liitännäiset uudelleen (painamalla Ctrl+NVDA+F3).
* Mikäli valitset asetusten tuomisen lisäosaa päivitettäessä, vanhentuneet
  tiedostot (emoticons.ini ja emoticons.dic) poistetaan tai muunnetaan tähän
  versioon sopiviksi.

## Muutokset versiossa 5.0 ##

* Lisätty tuki emojeille.
* Hymiönlisäysvalintaikkunaa paranneltu suodatuskentällä ja
  valintapainikkeilla hymiötyypin valitsemiseksi.
* Käyttöönottoasetusten- ja hymiönlisäysvalintaikkunoiden visuaalista
  esitystä paranneltu noudattamaan NVDA:n ikkunoiden ulkoasua: edellyttää
  NVDA:n 2016.4-versiota tai uudempaa.

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

[1]: https://addons.nvda-project.org/files/get.php?file=emo

[2]: https://addons.nvda-project.org/files/get.php?file=emo-dev

[3]: https://addons.nvda-project.org/files/get.php?file=emo-o
