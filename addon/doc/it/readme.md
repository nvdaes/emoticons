# Emoticons #
* Autori: Chris Leo, Noelia Ruiz Martínez, Mesar Hameed, Francisco Javier
  Estrada Martínez
* Versioni di NVDA compatibili: 2019.3 o superiori
* Scarica la [versione stabile][1]
* Scarica la[versione in sviluppo][2]

Utilizzando questo componente aggiuntivo, la lettura dei caratteri che
compongono una emoticon verrà sostituita con una sua descrizione.

Per esempio: la sequenza ":)" sarà pronunciata "Smiley Sorriso", ed inoltre
NVDA potrà riconoscere il nome degli emoji quando presenti nel testo.

È possibile usufruire delle seguenti funzionalità:

## Inserire emoticon ##

A volte un'immagine vale più di mille parole: usa i nuovi emoji per
vivacizzare i tuoi messaggi, e per far sapere ai tuoi amici come ti senti.

Se non sai quale carattere usare per un emoticon, questo componente
aggiuntivo ti permette di riconoscere e sceglierne uno e copiarlo negli
appunti per poi inserirlo in campi di editazione, come per esempio in una
chat.

Premi NVDA+I, o scegli Strumenti->  Inserisci emoticon dal menu di NVDA, per aprire una finestra di dialogo contenente  le emoticon o emoji disponibili.

Questa finestra di dialogo consente di scegliere un emoticon e visualizzare
le emoticon che ti interessano:

*	Un campo editabile permette di filtrare la ricerca per l'emoticon
  desiderato tra le emoticon disponibili.
*	Tramite dei pulsanti radio è possibile scegliere di visualizzare solo la
  categoria emoji (alt+E) o visualizzare solo gli emoticon standard (alt+s)
  oppure visualizzare tutti gli emoticon disponibili (alt+A).
*	Nella lista delle emoticon (alt+L),, su tre colonne, sono mostrati
  rispettivamente: il nome dell'emoticon, il tipo di emoticon (standard
  emoticon o emoji) e il carattere corrispondente.

Quando si preme OK, i caratteri dell'emoticon scelto verranno copiati negli
appunti, pronto per essere incollato.

## Dizionario Emoticons ##

Il componente aggiuntivo Emoticons permette di avere più dizionari
servendosi dei profili di configurazione.

Ciò significa che   è possibile creare o modificare un dizionario di voce
per ogni profilo personale.

Scegliendo Preferenze -> Dizionario Emoticons dal menu di NVDA, , è possibile aprire una finestra di dialogo per aggiungere o modificare gli emoticon disponibili.

Quando si salva la configurazione, le nuove impostazioni di lettura saranno
applicate solo al profilo personale in uso.

Per esempio, se si preferisce che NVDA legga le emoticons solo in uno
specifico programma di chat, ma non in altre applicazioni di chat, si può
creare un profilo personale per lo specifico programma ed assegnargli  un
dizionario di voce dal menu Dizionari -> Dizionario Emoticons. Vedi di
seguito per le impostazioni di Emoticons in relazione alla configurazione
di un profilo personale.

Con il pulsante "Salva ed esporta dizionario" è possibile salvare il
dizionario chiamato emoticons.dic nella cartella di configurazione personale
speechDicts.

Il nome ed il percorso del dizionario derivano dal profilo di configurazione
corrente, che verrà indicato nel titolo della finestra del dizionario di
Emoticons.

## Impostazioni Emoticons ##

Scegliendo Preferenze -> Impostazioni -> Emoticons dal menu di NVDA, è possibile aprire una finestra per scegliere se Attivare la lettura delle emoticon per ogni profilo. Di default è disattivato.

Nel pannello impostazioni di Emoticons è possibile scegliere se attivare o meno il dizionario per il profilo che si sta modificando. Per default, questa impostazione è disattivata nella configurazione normale di NVDA e in tutti i nuovi profili.

È inoltre possibile decidere se far leggere gli emoji dal componente
aggiuntivo, oppure mantenere la lettura degli emoji dalla configurazione di
NVDA.

Se si preferisce tenere  pulite le cartelle di configurazione, in questa
finestra è anche possibile scegliere se i dizionari non utilizzati (quelli
associati ad un profilo non più esistnete) verranno rimossi quando il
componente agguintivo viene terminato.

## Comandi rapidi: ##

Di seguito i comandi rapidi disponibili di default: E' possibile modificarli
o aggiungerne di nuovi per aprire le impostazioni o la finestra Dizionario
Emoticons:

* NVDA+E: Attiva o disattiva la lettura delle emoticon. Passa dalla lettura
  del testo delle emoticons così com'è scritto alla lettura della loro
  descrizione completa.
* NVDA+I: visualizza una finestra di dialogo per selezionare un emoticon che
  si desidera copiare negli appunti.
* Non assegnato: apre un messaggio leggibile in modalità navigazione, che
  mostra il simbolo presente alla posizione del cursore di controllo e la
  sua descrizione per esteso.
* Non assegnato: apre un messaggio leggibile in modalità navigazione, che
  mostra il simbolo presente alla posizione del cursore di sistema e la sua
  descrizione per esteso.

Nota: In Windows 10 è possibile utilizzare la finestra emoji nativa.

## Novità nella versione 12.0 ##

* Richiede NVDA 2019.3 o superiore.

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

* Aggiunta la possibilità di scegliere se gli emoji devono esser letti dal
  componente aggiuntivo.
* Introdotta una più appropriata codifica per i nomi dei dizionari, che
  evita errori quando questi contengono di specifici caratteri.
* Il riepilogo tradotto dell'addon viene usato correttamente per il titolo
  mostrato nella guida per il componente, raggiungibile dal Gestore
  componenti aggiuntivi.
* Nella guida viene menzionato il pannello emoji presente in Windows 10.

## Novità nella versione 8.0 ##

* Compatibile con NVDA 2018.3 o superiori.

## Novità nella versione 7.0 ##

* La finestra delle impostazioni di attivazione è stata spostata in un
  pannello delle impostazioni di NVDA, in modo che il profilo corrente verrà
  visualizzato nel titolo della finestra di dialogo Impostazioni di NVDA.
* IL menu Gestisci Emoticons è stato rimosso, la voce Inserisci Emoticons è
  stata spostata nel menu Strumenti e la finestra per creare un dizionario
  nel menu Personalizza -> Dizionari -> Dizionario Emoticons.
* Richiede NVDA 2018.2 o superiore.
* Se è necessario, è possibile scaricare la [versione compatibile con NVDA
  2017.3][3].

## Novità nella versione 6.0 ##

* Aggiunto il supporto per i profili di configurazione.
* In NVDA 2017.4 o versioni successive, le impostazioni ed i dizionari
  personali cambiano automaticamente a seconda del profilo in uso. Nella
  versione 2017.3 o precedenti, è possibile aplicare le modifiche
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

* Versione iniziale


[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=emo

[2]: https://addons.nvda-project.org/files/get.php?file=emo-dev

[3]: https://addons.nvda-project.org/files/get.php?file=emo-o
