# Emoticons #

* Authors: Chris Leo, Noelia Ruiz Martínez, Mesar Hameed, Francisco Javier
  Estrada Martínez

Utilizzando questo componente aggiuntivo, la lettura dei caratteri che
compongono una emoticon verrà sostituita con una sua descrizione.

Per esempio: la sequenza ":)" sarà pronunciata "Smiley Sorriso", ed inoltre
NVDA potrà riconoscere il nome degli emoji quando presenti nel testo.

È possibile usufruire delle seguenti funzionalità:

## Inserire emoticon ##

Sometimes an image is worth a 1000 words: use the new emoji to liven up your
instant message and to let your friends know how you’re feeling.

Se non sai quale carattere usare per una emoticon, questo componente
aggiuntivo ti permette di selezionarne uno e inserirlo nel testo che stai
scrivendo, come accade nelle chat.

Premi NVDA+I, o scegli Strumenti->Emoticons->Inserisci emoticon dal menu di NVDA, per aprire una finestra di dialogo contenente  le emoticon o emoji disponibili.

Questa finestra di dialogo ti consente di scegliere una emoticon e di
visualizzare la grafia delle emoticon che ti interessano:

*	Un campo editazione permette di filtrare la ricerca dell'emoticon
  desiderata tra le emoticon disponibili.
*	Tramite dei pulsanti radio è possibile scegliere di visualizzare solo le
  emoji (alt+E), solo le emoticon standard (alt+s) o tutte le emoticon
  disponibili (alt+A).
*	Nella lista delle emoticon (alt+L),, su tre colonne, sono mostrati
  rispettivamente: il nome dell'emoticon, il tipo di emoticon (standard
  emoticon o emoji) e i caratteri necessari per ottenerla.

Quando si preme OK, i caratteri dell'emoticon scelta verranno copiati negli
appunti, pronti per essere incollati.

## Inserisci simbolo ##

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

## Dizionario delle emoticons ##

Questo componente aggiuntivo permette di avere più dizionari di pronuncia,
servendosi dei profili di configurazione.

Ciò significa che   è possibile creare o modificare un dizionario di
pronuncia per ogni profilo.

Scegliendo Preferenze->Dizionari->Dizionario Emoticons dal menu di NVDA, , è possibile aprire una finestra di dialogo per aggiungere o modificare gli emoticon disponibili.

Quando si salva la configurazione, le nuove impostazioni di lettura saranno
applicate solo al profilo personale in uso.

Per esempio, se si preferisce che NVDA legga le emoticons solo in uno
specifico programma di chat, ma non in altre applicazioni di chat, si può
creare un profilo personale per lo specifico programma ed assegnargli  un
dizionario di voce dal menu Dizionari -> Dizionario Emoticons. Si veda più
avanti per le impostazioni di Emoticons in relazione ai profili di
configurazione.

E' anche possibile esportare ogni dizionario di pronuncia scegliendo il
pulsante Salva ed Esporta Dizionario. In questo modo i tuoi dizionari di
pronuncia verranno salvati nella cartella configurazione utente di NVDA,
sottocartella speechDicts/emoticons.

Il nome ed il percorso del dizionario si baseranno sul profilo di
configurazione corrente, che verrà indicato nel titolo della finestra del
dizionario di Emoticons.

## Impostazioni di Emoticons ##

Scegliendo Preferenze->Impostazioni->Emoticons dal menu di NVDA, è possibile aprire una finestra per configurare l'Attivazione del dizionario di pronuncia per ogni profilo.

Nella finestra impostazioni di Emoticons è possibile scegliere se il dizionario per il profilo che si sta modificando deve essere attivato automaticamente quando NVDA passa a quel profilo. Per default, questa impostazione è disattivata nella configurazione normale di NVDA e in tutti i nuovi profili.

È inoltre possibile decidere se le emoji dell'add-on devono essere
vocalizzate. Ciò può essere utile per conservare la pronuncia dei simboli
quando le emoji sono incluse nella configurazione di NVDA.

Se si preferisce tenere  pulite le cartelle di configurazione, in questa
finestra è anche possibile scegliere se i dizionari non utilizzati (quelli
associati ad un profilo non più esistente) verranno rimossi quando il
componente aggiuntivo viene scaricato dalla memoria.

## Comandi rapidi: ##

Questi sono i comandi rapidi disponibili di default: E' possibile
modificarli  o aggiungerne di nuovi per aprire le impostazioni o la finestra
Dizionario Emoticons:

* NVDA+E: Attiva o disattiva la lettura delle emoticon. Passa dalla lettura
  del testo delle emoticons così com'è scritto alla lettura della loro
  descrizione completa.
* NVDA+I: visualizza una finestra di dialogo per selezionare un emoticon che
  si desidera copiare negli appunti.
* Non assegnato: visualizza una finestra di dialogo per selezionare un
  simbolo (punteggiatura o altro) che si desidera copiare.
* Non assegnato: apre un messaggio leggibile in modalità navigazione, che
  mostra il simbolo presente alla posizione del cursore di controllo e la
  sua descrizione per esteso.
* Non assegnato: apre un messaggio leggibile in modalità navigazione, che
  mostra il simbolo presente alla posizione del cursore di sistema e la sua
  descrizione per esteso.

Nota: dalla versione di Windows 10 è possibile utilizzare la finestra emoji
nativa.

## Changes for 22.0.0 ##

* Requires NVDA 2023.2 or later.

## Changes for 17.0 ##

* Added ability to associate gestures to type symbols.
* Added ability to copy various symbols at the same time.

## Changes for 16.0 ##

* Compatible with NVDA 2023.1.

## Novità nella versione 15.0 ##

* Richiede NVDA 2022.1 o versioni successive.
* Non può essere utilizzato in modalità protetta.

## Novità nella versione 14.0 ##

* Compatibile con NVDA 2021.

## Novità nella versione 13.0 ##

* Corretti alcuni errori nella finestra Inserisci Emoticon.
* Aggiunta una finestra per inserire un simbolo presente nella finestra
  Pronuncia Punteggiatura/Simboli di NVDA.

## Novità nella versione 12.0 ##

* Richiede NVDA 2019.3 o versioni successive.

## Novità nella versione 11.0 ##

* Quando il componente aggiuntivo viene aggiornato, i dizionari salvati
  nella versione precedente verranno automaticamente copiati nella nuova
  versione, a meno che non si preferisca importare i dizionari salvati nella
  cartella principale dei dizionari di NVDA.
* Quando si visualizza il carattere alla posizione dei cursori, si
  utilizzano le diciture carattere e In sostituzione per distinguere meglio
  il carattere e la sua descrizione, cosa utile per chi usa una sintesi
  vocale.

## Novità nella versione 10.0 ##

* Aggiunti comandi per mostrare il carattere alla posizione del cursore di
  sistema o del cursore di controllo e la sua descrizione. È possibile
  assegnare tasti per questi comandi dalla finestra Gesti e tasti di
  immissione sotto la categoria Revisione del Testo.

## Novità nella versione 9.0 ##

* Aggiunta la possibilità di scegliere se gli emoji del componente
  aggiuntivo devono esser letti.
* Introdotta una più appropriata codifica per i nomi dei dizionari, che
  evita errori quando questi contengono specifici caratteri.
* Il riepilogo tradotto dell'addon viene usato correttamente per il titolo
  mostrato nella guida per il componente, raggiungibile dal Gestore
  componenti aggiuntivi.
* Nella guida viene menzionato il pannello emoji presente in Windows 10.

## Novità nella versione 8.0 ##

* Compatibile con NVDA 2018.3 o versioni successive.

## Novità nella versione 7.0 ##

* La finestra delle impostazioni di attivazione è stata spostata in un
  pannello delle impostazioni di NVDA, in modo che il profilo corrente venga
  visualizzato nel titolo della finestra di dialogo Impostazioni di NVDA.
* IL menu Gestisci Emoticons è stato rimosso, la voce Inserisci Emoticons è
  stata spostata nel menu Strumenti e la finestra per creare un dizionario
  nel menu Personalizza -> Dizionari -> Dizionario Emoticons.
* Richiede NVDA 2018.2 o versioni successive.

## Novità nella versione 6.0 ##

* Aggiunto il supporto per i profili di configurazione.
* In NVDA 2017.4 o versioni successive, le impostazioni ed i dizionari
  personali cambieranno automaticamente a seconda del profilo in uso. Nelle
  versioni 2017.3 o precedenti, è possibile aplicare le modifiche
  ricaricando i componenti aggiuntivi (premere nvda+control+F3).
* Se si sceglie di importare le impostazioni quando si aggiorna il
  componente aggiuntivo, i file obsoleti (emoticon.ini ed emoticon.dic)
  saranno rimossi o adattati alla nuova versione.

## Novità nella versione 5.0 ##

* Aggiunto il supporto per le emoji.
* Miglioramenti alla finestra Inserisci Emoticon, con un campo di ricerca e
  pulsanti radio per scegliere quali emoticon visualizzare.
* Viene usato il metodo guiHelper nelle finestre Inserisci Emoticon e
  Impostazioni di Attivazione: richiede NVDA 2016.4 o versioni successive

## Novità nella versione 4.0 ##

* Se la finestra Inserisci Faccina è aperta quando un'altra finestra di
  impostazioni è attiva, NVDA mostrerà il corrispondente messaggio di errore
  .


## Novità nella versione 3.0 ##

* Nella finestra Personalizza Emoticons, è ora possibile effettuare una
  ricerca per sole parole intere, in analogia con i dizionari di NVDA
  2014.4.


## Novità nella versione 2.0 ##

* La guida di questo add-on è disponibile dal menu gestore componenti
  aggiuntivi.


## Novità nella versione 1.1 ##

* Rimosse emoticons duplicate.
* Aggiunte alcune faccine.

## Novità nella versione 1.0 ##

* Versione iniziale.

[[!tag dev stable]]
