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
*	Through a set of radio buttons, you can choose to view only emoji category
  (alt+E) or view only standard emoticon category (alt+s) or view all
  emoticons available (alt+A).
*	In the list of emoticons (alt+L) are displayed on three columns
  respectively: the name of emoticon, the type of emoticon (standard
  emoticon or emoji), the corresponding character.

Quando si preme OK, il carattere dell'emoticon scelto verrà copiato negli
appunti, pronto per essere incollato.

## Personalizza emoticon ##

Dal menu di NVDA, Preferenze -> Emoticons -> Personalizza Emoticons, è possibile aprire una finestra di dialogo per aggiungere o modificare gli emoticon disponibili.

Questa finestra di dialogo consente di salvare e personalizzare un
dizionario di voce con i vostri emoticons.

Con il pulsante "Salva ed esporta dizionario" è possibile salvare il
dizionario chiamato emoticons.dic nella cartella di configurazione personale
speechDicts.

## Impostazioni di attivazione ##

Dal menu preferenze > Emoticons > Impostazioni di Attivazione, è possibile scegliere se Attivare la lettura di emoticon all'avvio di NVDA. Di default è disabilitato.

È inoltre possibile salvare la configurazione per questa impostazione.

## Comandi rapidi: ##

Di seguito i comandi rapidi disponibili di default: questi comandi possono
esser modificati, ed è anche possibile aggiungere comandi rapidi per aprire
la finestra Personalizza Emoticons e Impostazioni di Attivazione:

* NVDA+E: Attiva o disattiva la lettura degli emoticons, legge il nome
  dell'emoticon al posto dei caratteri usati.
* NVDA+I: visualizza una finestra di dialogo per selezionare un emoticon che
  si desidera copiare negli appunti.


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
