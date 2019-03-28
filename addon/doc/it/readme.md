# Emoticons #

* Autori: Chris Leo, Noelia Ruiz Martínez, Mesar Hameed, Francisco Javier
  Estrada Martínez
* Compatibilità con NVDA: dalla 2018.3 alla 2019.1
* Scarica la [versione stabile][1]
* Scarica la[versione in sviluppo][2]

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

Con la combinazione di tasti NVDA+I, o dal menu Strumenti->  Inserisci emoticon, è possibile aprire una finestra di dialogo con le emoticon o emoji.

Questa finestra di dialogo consente di scegliere un emoticon e visualizzare
le emoticon che ti interessano:

*	Un campo modificabile permette di filtrare la ricerca per l'emoticon
  desiderato tra le emoticon disponibili. 
*	Tramite dei pulsanti radio è possibile scegliere di visualizzare solo la
  categoria emoji (alt+E) o visualizzare solo gli emoticon standard (alt+s)
  oppure visualizzare tutti gli emoticon disponibili (alt+A).
*	Nella lista di emoticon (alt+L), vi sono presenti tre colonne,
  rispettivamente: il nome dell'emoticon, il tipo di emoticon (standard
  emoticon o emoji), il carattere corrispondente. 

Quando si preme OK, il carattere dell'emoticon scelto verrà copiato negli
appunti, pronto per essere incollato.

## Dizionario Emoticons ##

Il componente aggiuntivo Emoticons permette di avere più dizionari
servendosi dei profili di configurazione.

Ciò significa che   è possibile creare o modificare un dizionario di voce
per ogni profilo personale.

Dal menu di NVDA, Preferenze -> Dizionario Emoticons, è possibile aprire una finestra di dialogo per aggiungere o modificare gli emoticon disponibili.

Quando si salva la configurazione, le nuove impostazioni di lettura si
applicano solo al profilo personale in uso.

Per esempio, se si preferisce che NVDA legga le classiche emoticons solo in
uno specifico programma di chat, ma non in altre applicazioni di chat, si
può creare un profilo personale per lo specifico programma ed assegnargli
un dizionario di voce dal menu Dizionari, Dizionario Emoticons. Vedi di
seguito per le impostazioni in relazione alla configurazione  di un profilo
personale.

Con il pulsante "Salva ed esporta dizionario" è possibile salvare il
dizionario chiamato emoticons.dic nella cartella di configurazione personale
speechDicts.

Il nome ed il percorso del dizionario deriva dal nome dell'attuale profilo
in fase di modifica, questo verrà indicato nel titolo della finestra del
dizionario.

## Impostazioni Emoticons ##

Dal menu preferenze > Impostazioni, è possibile visualizzare le impostazioni Emoticons e scegliere se Attivare la lettura di emoticon per ogni profilo. Di default è disattivato.

Nel pannello impostazioni Emoticons è possibile scegliere se attivare o meno il dizionario per il profilo in fase di modifica. Di default è disattivato sia per la configurazione normale che per tutti i nuovi profili.

Moreover, it's possible to determine if the add-on emojis should be
spoken. This could be useful to preserve symbols speaking if emojis are
included in NVDA's configuration.

Se si preferisce tenere  pulita la cartella di configurazione, è possibile
rimuovere i dizionari non utilizzati (quelli associati ad un profilo
eliminato) e che non vengono caricati.

## Comandi rapidi: ##

Di seguito i comandi rapidi disponibili di default: E' possibile modificarli
o aggiungerne di nuovi per aprire le impostazioni o la finestra Dizionario
Emoticons:

* NVDA+E: Attiva o disattiva la lettura degli emoticon.
* NVDA+I: visualizza una finestra di dialogo per selezionare un emoticon che
  si desidera copiare negli appunti.
* Not assigned: open a browseable message showing the symbol where the
  review cursor is positioned, so that the whole description can be reviewed
  in browse mode.
* Not assigned: open a browseable message showing the symbol where the caret
  is positioned, so that the whole description can be reviewed in browse
  mode.

Nota: In Windows 10 è possibile utilizzare la finestra per inserire emoji. 


## Changes for 10.0 ##

* Added commands to show the symbol where the review cursor or caret are
  positioned. Gestures for these commands can be assigned from the Input
  gestures dialog, Text review category.

## Changes for 9.0 ##

* Added the possibility of choosing if add-on emojis should be spoken.
* Used appropiate encoding for dictionary names, fixing errors when they
  contain certain characters.
* The translated summary of the add-on is properly used for the title
  presented in add-on help, accessible from the add-on manager.
* Added a note mentioning the emoji panel available on Windows 10.

## Changes for 8.0 ##

* Compatibile con NVDA 2018.3 o superiori.

## Changes for 7.0 ##

* La finestra per impostare l'ttivazione è stato spostato nel pannello delle
  impostazioni di NVDA, in modo che il profilo corrente verrà visualizzato
  nel titolo della finestra di dialogo.
* IL menu emoticons è stato rimosso, la voce Inserisci Emoticons è stata
  spostata nel menu Strumenti e la finestra per creare un dizionario nel
  menu Personalizza,Dizionari,Dizionario Emoticons.
* Richiesto NVDA 2018.2 o superiore.
* Se è necessario è possibile scaricare la [versione compatibile con NVDA
  2017.3][3].

## Novità nella versione 6.0 ##

* Aggiunto il supporto per i profili di configurazione.
* In NVDA 2017.4 o superiori, le impostazioni ed i dizionari personali
  cambiano automaticamente rispetto al profilo in uso. Nella versione 2017.3
  o precedenti per aplicare la configurazione è necessario ricaricare i
  componenti aggiuntivi (premere nvda+control+F3).
* Se si sceglie di importare le impostazioni del componente aggiuntivo
  durante l'installazione , i file obsoleti (emoticon.ini ed emoticon.dic)
  saranno rimossi e adattati alla nuova versione. 

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

[1]: https://addons.nvda-project.org/files/get.php?file=emo

[2]: https://addons.nvda-project.org/files/get.php?file=emo-dev

[3]: https://addons.nvda-project.org/files/get.php?file=emo-o
