# Emoticons #

* Autori: Chris Leo, Noelia Ruiz Martínez, Mesar Hameed, Francisco Javier
  Estrada Martínez
* Descarcă [versiunea stabilă][1]
* Descarcă [versiunea în dezvoltare][2]

Folosind acest supliment, textul care conține emoticoane va fi înlocuit cu o
descriere mult mai prietenoasă.

De exemplu: secvența ":)" va fi pronunțată ca „zâmbet” sau, de exemplu, NVDA
va recunoaște semnificația fiecărui moji.

Există următoarele caracteristici:

## Inserează Emoticon ##

Uneori, o imagine face cât 1000 de cuvinte: utilizați noul moji pentru a da
viață mesajului dumneavoastră instant și pentru a permite prietenilor să
știe ceea ce simțiți.

Când sunteți nesigur de caracterele pentru un zâmbet particular, add-on-ul
vă permite să-l selectați și inserați în textul dumneavoastră.

Apăsați NVDA+I, sau din meniul preferințe -> Administrare emoticonuri -> Inserare emoticon, pentru a deschide un dialog cu emoticoanele oferite sau mojiuri.

Acest dialog vă permite să alegeți un emoticon și să vizualizați
emoticoanele care vă interesează:

*	Un câmp editabil vă permite să filtrați căutarea pentru emoticonul dorit
  dintre emoticoanele disponibile.
*	Printr-un set de butoane rotative, puteți să alegeți să vizualizați doar
  categoria mojiuri (alt+E) sau să vizualizați doar categoria emoticoanelor
  standard (alt+s) sau să vizualizați toate emoticoanele disponibile
  (alt+A).
  *	În lista emoticoanelor (alt+L) sunt afișate pe trei coloane: numele
  emoticonului, tipul acestuia (emoticon standard sau moji), caracterul
  corespunzător.
*	În lista emoticoanelor (alt+L) sunt afișate pe trei coloane numele
  emoticonului, tipul acestuia (standard sau moji) și caracterul
  corespunzător.

Când apăsați OK, caracterele pentru emoticoanele alese vor fi copiate pe
planșetă, pregătite pentru lipire.

## Personalizați emoticoanele ##

Emoticons add-on allows to have differents speech-dictionaries using
configuration profiles.

This means that you can create or edit a specific speech-dictionary for each
your custom profile.

Din meniul NVDA, Preferințe, Administrare emoticoane, Personalizează emoticoanele, puteți să deschideți un dialog cu setările unde puteți adăuga sau edita emoticoanle disponibile.

Saving your customizations, the new reading settings of emoticons will only
apply to the profile you are currently editing.

For example, you may wish that NVDA spoken custom emoticons only in XxChat
program, but not in other chat programs: you can do this by creating a
profile for the XxChat application and assign to it a speech dictionary from
Customize Emoticons menu. See below for activation setting in relation to
the configuration profiles.

You can also export each custom speech-dictionary pressing "Save and export
dictionary" button: in this way your speech-dictionaries will be saved in
your user config folder, speechDicts/emoticons subfolder.

The exact name and location of the dictionary file will be based on the
editing configuration profile, which will be shown in the title of the
Emoticons dictionary dialog.

## Setări de activare ##

From menu Preferences -> Manage Emoticons -> Activation-settings opens a dialog to configure the activation of your speech-dictionaries for each profile.

In activation-setting dialog you can choose whether or not speech-dictionary should automatically activate when  NVDA switches to the   profile you are currently editing. By default it is disabled in normal configuration of NVDA and in all your new profiles.

If you may wish to keep clean your configuration folders, in this dialog it
is also possible to choose if dictionaries not used (associated with non
existing profiles) will be removed from the add-on when it is unloaded.

## Comenzi de tastatură ##

Acestea sunt scurtăturile disponibile în mod implicit, puteți să le editați
sau puteți adăuga o nouă tastă pentru a deschide dialogul cu activarea
setărilor sau dialogul cu dicționarul emoticoanelor:

* NVDA+E: speaking emoticons on/off, toggles between speaking text as it is
  written, or with the emoticons replaced by the human description.
* NVDA+I: Arată un dialog pentru a selecta emoticonul pe care vreți să îl
  copiați.

## Changes for 6.0 ##

* Added support for configuration profiles.
* In NVDA 2017.4 or later, the configuration settings and custom
  dictionaries will change automatically according with the selected
  profiles. In 2017.3 or earlier, you can apply changes by reloading plugins
  (pressing control+NVDA+f3).
* If you choose to import settings when updating the add-on, deprecated
  files (emoticons.ini and emoticons.dic) will be removed or adapted to this
  version.

## Modificări aduse în 5.0 ##

* A fost adăugat suportul pentru mojiuri.
* Îmbunătățiri pentru dialogul de inserare al emoticoanelor cu un câmp de
  filtrare și butoane rotative pentru a alege emoticoanele afișate.
* Utilizând ghidul de ajutor pentru dialogul de activare al setărilor și
  dialogul de inserare a emoticoanelor: Necesită NVDA 2016.4 sau mai vechi

## Modificări aduse în 4.0 ##

* Dacă dialogul de inserare al emoticonului este deschis când alt dialog de
  setări este activ, NVDA va afișa un mesaj de eroare.


## Modificări aduse în versiunea 3.0. ##

* În dialogul de personalizare emoticon, este acum posibil să specifici dacă
  un model trebuie să fie asemănător dacă este un cuvânt întreg, în
  acordanță cu dicționarele de vorbire versiunii NVDA 2014.4.


## Modificări aduse în versiunea 2.0. ##

* Ajutorul add-on-ului este disponibil din manager-ul de add-on-uri.


## Modificări aduse în versiunea 1.1. ##

* Au fost șterse emoticoanele duplicate.
* Au mai fost adăugate ceva emoticoane.

## Modificări aduse în versiuna 1.0. ##

* Versiunea Inițială.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=emo

[2]: http://addons.nvda-project.org/files/get.php?file=emo-dev
