# Emoticons #

* Autori: Chris Leo, Noelia Ruiz Martínez, Mesar Hameed, Francisco Javier
  Estrada Martínez
* Download [versione stabile][1]
* Download [versione in sviluppo][1]

L'utilizzo di questo componente aggiuntivo consente di leggere la
descrizione degli emoticons quando si incontrano caratteri che rappresentano
emoticons.

Per esempio: la sequenza ":)" sarà pronunciata "Smiley Sorriso", ed inoltre
NVDA potrà riconoscere il nome degli emoji quando presenti nel testo.

È possibile usufruire delle seguenti funzionalità:

## Inserire emoticon ##

A volte un'immagine vale più di mille parole: usa i nuovi emoji per
vivacizzare i tuoi messaggi, e per far sapere ai tuoi amici come ti senti.

Se non sai quale carattere usare per il tuo emoticon, il componente
aggiuntivo ti da la possibilità di riconoscere e sceglierne uno e copiarlo
negli appunti per poi inserirlo in campi di editazione, come per esempio in
una chat.

Premere NVDA+I, o dal menu Preferenze -> Gestione emoticon -> Inserire emoticon, per aprire una finestra di dialogo con le emoticon o emoji.

Questa finestra di dialogo consente di scegliere un emoticon e visualizzare
le emoticon che ti interessano:

*	Un campo modificabile permette di filtrare la ricerca per l'emoticon
  desiderato tra le emoticon disponibili. 
*	*	Attraverso dei pulsanti radio è possibile scegliere di visualizzare solo
  la categoria emoji (alt+E) o visualizzare solo gli emoticon standard
  (alt+s) oppure visualizzare tutti gli emoticon disponibili (alt+A).
  *	Nell'elenco degli emoticons (alt+E) vengono visualizzati
  rispettivamente: il nome dell'emoticon, il tipo di emoticon (emoticon
  standard o emoji), ed il corrispondente carattere.
*	Nella lista di emoticon (alt+L), vi sono presenti tre colonne,
  rispettivamente: il nome dell'emoticon, il tipo di emoticon (standard
  emoticon o emoji), il carattere corrispondente. 

Quando si preme OK, il carattere dell'emoticon scelto verrà copiato negli
appunti, pronto per essere incollato.

## Personalizza emoticon ##

Emoticons add-on allows to have differents speech-dictionaries using
configuration profiles.

This means that you can create or edit a specific speech-dictionary for each
your custom profile.

Dal menu di NVDA, Preferenze -> Emoticons -> Personalizza Emoticons, è possibile aprire una finestra di dialogo per aggiungere o modificare gli emoticon disponibili.

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

## Impostazioni di attivazione ##

From menu Preferences -> Manage Emoticons -> Activation-settings opens a dialog to configure the activation of your speech-dictionaries for each profile.

In activation-setting dialog you can choose whether or not speech-dictionary should automatically activate when  NVDA switches to the   profile you are currently editing. By default it is disabled in normal configuration of NVDA and in all your new profiles.

If you may wish to keep clean your configuration folders, in this dialog it
is also possible to choose if dictionaries not used (associated with non
existing profiles) will be removed from the add-on when it is unloaded.

## Comandi rapidi: ##

Di seguito i comandi rapidi disponibili di default: questi comandi possono
esser modificati, ed è anche possibile aggiungere comandi rapidi per aprire
la finestra Personalizza Emoticons e Impostazioni di Attivazione:

* NVDA+E: speaking emoticons on/off, toggles between speaking text as it is
  written, or with the emoticons replaced by the human description.
* NVDA+I: visualizza una finestra di dialogo per selezionare un emoticon che
  si desidera copiare negli appunti.

## Novità nella versione 6.0 ##

* Aggiunto il supporto per i profili di configurazione.
* In NVDA 2017.4 or later, the configuration settings and custom
  dictionaries will change automatically according with the selected
  profiles. In 2017.3 or earlier, you can apply changes by reloading plugins
  (pressing control+NVDA+f3).
* If you choose to import settings when updating the add-on, deprecated
  files (emoticons.ini and emoticons.dic) will be removed or adapted to this
  version.

## Novità nella versione 5.0 ##

* Aggiunto il supporto per emoji caratteri UNICODE.
* Aggiunto un campo di ricerca con filtro e i pulsanti radio per scegliere
  quali emoticon visualizzare.
* Viene usato il metodo guiHelper nelle finestre Inserisci Emoticon e
  Impostazioni di Attivazione, il componente aggiuntivo richiede NVDA 2016.4
  o versioni successive.

## Changes for 4.0 ##

* If the Insert smiley dialog is opened when another settings dialog is
  active, NVDA will show the corresponding error message.


## Changes for 3.0 ##

* In the Customize emoticons dialog, it is now possible to specify that a
  pattern should only match if it is a whole word, according to speech
  dictionaries of NVDA 2014.4.


## Cambiamenti per la 2.0 ##

* L'aiuto del componente aggiuntivo è disponibile dal menu gestore
  componenti aggiuntivi.


## Cambiamenti per 1.1 ##

* Rimosse emoticons duplicate
* Aggiunte alcune faccine

## Cambiamenti per 1.0 ##

* Versione iniziale

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=emo

[2]: http://addons.nvda-project.org/files/get.php?file=emo-dev
