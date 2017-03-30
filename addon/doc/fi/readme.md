# Hymiöt #

* Tekijät: Chris Leo, Noelia Ruiz Martínez, Mesar Hameed, Francisco Javier
  Estrada Martínez
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

Paina NVDA+I tai valitse Asetukset-valikko -> Hymiöiden hallinta -> Lisää hymiö avataksesi valintaikkunan, jossa näkyvät käytettävissä olevat hymiöt ja emojit.

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

## Mukauta hymiöitä ##

Voit avata valintaikkunan uusien hymiöiden lisäämiseksi tai olemassa olevien muokkaamiseksi valitsemalla NVDA-valikosta Asetukset -> Hymiöiden hallinta -> Mukauta hymiöitä.

Tässä valintaikkunassa voit tallentaa tekemäsi muokkaukset
hymiöpuhesanastoon.

Kun painat "Tallenna ja vie sanasto" -painiketta, asetuskansiossasi olevaan
speechDicts-alikansioon luodaan emoticons.dic-niminen sanastotiedosto.

## Käyttöönoton asetukset ##

Voit valita, otetaanko hymiöiden puhuminen käyttöön NVDA:ta käynnistettäessä valitsemalla NVDA-valikosta Asetukset -> Hymiöiden hallinta -> Käyttöönoton asetukset. Tämä ei ole oletusarvoisesti käytössä.

Valitsemasi asetus on myös mahdollista tallentaa.

## Näppäinkomennot: ##

Nämä ovat oletusnäppäinkomentoja. Voit muokata niitä tai lisätä uuden
käyttöönottoasetusten valintaikkunan tai hymiösanaston avaamiseen:

* NVDA+E: hymiöiden puhuminen käyttöön/pois käytöstä - ottaa käyttöön
  tekstin lukemisen sellaisena kuin se on kirjoitettu tai hymiöiden
  korvaamisen niiden kuvauksilla.
* NVDA+I: näyttää valintaikkunan, josta voit valita tekstiin lisättävän
  hymiön.


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

[1]: http://addons.nvda-project.org/files/get.php?file=emo

[2]: http://addons.nvda-project.org/files/get.php?file=emo-dev
