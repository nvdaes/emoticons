# Emoticons #
* Autori: Chris Leo, Noelia Ruiz Martínez, Mesar Hameed, Francisco Javier
  Estrada Martínez
* NVDA compatibility: 2019.3 or later
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

Press NVDA+I, or from menu Tools -> Emoticons > Insert emoticon, to open a dialog with the provided emoticons or emoji.

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

## Insert symbol ##

This dialog allows you to choose one of the symbols available in the
Punctuation/symbol pronunciation dialog of NVDA. You can use the Filter edit
box or the arrow keys to select an item from the symbols list. Then, press
OK and the selected emoji or symbol will be copied to your clipboard, ready
for pasting.

## Dicționar de emoticoane ##

Suplimentul Emoticons vă permite să aveți diferite dicționare de vorbire
folosind profiluri de configurare.

Aceasta înseamnă că puteți crea sau edita un dicționar de vorbire specific
pentru fiecare profil personalizat.

Din meniul NVDA, Preferințe -> Dicționare de vorbire -> Dicționar de emoticoane, puteți să deschideți un dialog cu setările unde puteți adăuga sau edita emoticoanle disponibile.

Salvându-vă particularizările, noile setări de citire ale emoticoanelor se
vor aplica numai profilului pe care îl editați în prezent.

De exemplu, ați putea dori ca NVDA să pronunțe emoticoane personalizate
numai în programul XxChat, dar nu în alte programe de chat: puteți face
acest lucru creând un profil pentru aplicația XxChat și atribuiți un
dicționar de vorbire din meniul din meniul dicționare de vorbire, opțiunea
„Dicționar de emoticoane. Vedeți mai jos setările de activare în raport cu
profilurile de configurare.

De asemenea, puteți să exportați fiecare dicționar de vorbire apăsând
butonul "Salvează și exportă dicționar": în felul acesta, dicționarele
dumneavoastră de vorbire vor fi salvate în folderul de configurare al
utilizatorului, subfolder-ul speechDicts/emoticons.

Numele exact și locația fișierului de dicționar vor fi bazate pe editarea
profilului de configurare, care va fi afișat în titlul dialogului dicționar
Emoticons.

## Setări Emoticons ##

Din meniul Preferințe -> Setări Emoticoane deschide un dialog pentru a configura activarea dicționarelor de vorbire pentru fiecare profil.

Din panoul de setări al Emoticons, puteți dacă ar trebui sau nu ca dicționarul de vorbire să se activeze automat atunci când NVDA se comută la profilul pe care actualmente îl editați. În mod implicit, este dezactivată în configurația normală a NVDA și în toate profilurile dumneavoastră.

În plus, e posibil să se determine dacă emoji-urile suplimentului trebuie să
fie pronunțate. Această funcție poate fi utilă în menținerea pronunțării
simbolurilor dacă emoji-urile sunt incluse în configurația NVDA.

Dacă doriți să păstrați curate folderele de configurare, în această
fereastră de dialog este posibil de asemenea să alegeți dacă dicționarele
care nu sunt utilizate (asociate profilurilor inexistente) vor fi eliminate
din supliment atunci când nu sunt încărcate.

## Comenzi de tastatură: ##

Acestea sunt scurtăturile disponibile în mod implicit, puteți să le editați
sau puteți adăuga o nouă tastă pentru a deschide panoul de setări al
Emoticons sau dialogul dicționarului de emoticoane:

* NVDA + E: activarea/dezactivarea pronunțării emoticoanelor, comută între
  pronunțarea textului așa cum este scris, sau cu emoticoanele înlocuite cu
  descrierea umană.
* NVDA+I: Arată un dialog pentru a selecta emoticonul pe care vreți să îl
  copiați.
* Not assigned: show a dialog to select an NVDA's symbol you want to copy.
* Neatribuită: deschide un mesaj de navigare care arată simbolul la care
  este poziționat cursorul de scriere, astfel încât descrierea să fie
  parcursă în modul de navigare.
* Neatribuită: deschide un mesaj de navigare care arată simbolul la care
  este poziționat cursorul de scriere, astfel încât descrierea să fie
  parcursă în modul de navigare.

Notă: În Windows 10, este posibil să folosiți și panoul de emoji.

## Changes for 13.0 ##

* Fixed errors in Insert Emoticon dialog.
* Added a dialog to insert a symbol available in the Punctuation/symbol
  pronunciation of NVDA.

## Changes for 12.0 ##

* Requires NVDA 2019.3 or later.

## Modificări aduse în versiuna 11.0 ##

* Când suplimentul este actualizat, dicționarele folosite în versiunile
  anterioare vor fi copiate automat pentru a putea fi folosite în noua
  versiune, asta dacă nu preferați să importați dicționarele salvate în
  dosarul principal al dicționarelor NVDA.
* La afișarea simbolului la care este poziționat cursorul de scriere sau cel
  de examinare, cuvintele, caracterele și înlocuirile sunt folosite cu
  scopul de a face o diferență între simbolul în sine și descrierea sa din
  modul de navigare, util pentru cei care folosesc sinteza vocală.

## Modificări aduse în versiuna 10.0 ##

* S-au adăugat comenzi care arată simbolul la care este poziționat cursorul
  de scriere.

## Modificări aduse în 9.0 ##

* Acum, puteți să alegeți dacă emoji-urile suplimentelor vor fi sau nu
  pronunțate.
* S-a utilizat encoding apropiat pentru nnumele de dicționar și s-au reparat
  erori pe care le aveau anumite caractere.
* Cuprinsul tradus al suplimentului este folosit pentru titlul prezentat în
  documentația acestuia, disponibilă în administratorul suplimentelor.
* S-a adăugat o notă care menționează panoul de emoji din Windows 10.

## Modificări aduse în 8.0 ##

* Compatibil cu NVDA 2018.3 (necesar).

## Modificări aduse în 7.0 ##

* Dialogul de activare al setărilor a fost mutat într-un panou din setările
  NVDA, astfel încât profilul curent va fi afișat în titlul dialogului
  setărilor NVDA.
* Meniul Administrare Emoticoane a fost șters: nicio opțiune de genul
  Inserare Emoticon nu va fi găsită în submeniul Instrumente, iar opțiunea
  de personalizare a emoticoanelor va fi afișată sub dicționarele de
  vorbire, la fel ca dicționarul de emoticoane.
* Necesită NVDA 2018.2 sau mai nou.
* Dacă e musai, puteți să descărcați [ultima versiune compatibilă cu NVDA
  2017.3][3].

## Modificări aduse în 6.0 ##

* S-a adăugat suportul pentru configurarea profilurilor.
* În NVDA 2017.4 sau o versiune ulterioară, setările de configurare și
  dicționarele personalizate se vor schimba automat acordându-se cu
  profilurile selectate. În 2017.3 sau mai recent, puteți aplica modificări
  prin reîncărcarea pluginurilor (apăsând control+ NVDA+f3).
* Dacă alegeți să importați setări atunci când actualizați suplimentul,
  fișierele depreciate (emoticons.ini și emoticons.dic) vor fi eliminate sau
  adaptate la această versiune.

## Modificări aduse în 5.0 ##

* A fost adăugat suportul pentru mojiuri.
* Îmbunătățiri pentru dialogul de inserare al emoticoanelor cu un câmp de
  filtrare și butoane rotative pentru a alege emoticoanele afișate.
* Utilizând ghidul de ajutor pentru dialogul de activare al setărilor și
  dialogul de inserare a emoticoanelor: Necesită NVDA 2016.4 sau mai vechi

## Modificări aduse în 4.0 ##

* Dacă dialogul de inserare al emoticonului este deschis când alt dialog de
  setări este activ, NVDA va afișa un mesaj de eroare.


## Modificări aduse în versiunea 3.0 ##

* În dialogul de personalizare emoticon, este acum posibil să specifici dacă
  un model trebuie să fie asemănător dacă este un cuvânt întreg, în
  acordanță cu dicționarele de vorbire versiunii NVDA 2014.4.


## Modificări aduse în versiunea 2.0 ##

* Ajutorul add-on-ului este disponibil din manager-ul de add-on-uri.


## Modificări aduse în versiunea 1.1 ##

* Au fost șterse emoticoanele duplicate.
* Au mai fost adăugate ceva emoticoane.

## Modificări aduse în versiuna 1.0 ##

* Versiunea Inițială.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=emo

[2]: https://addons.nvda-project.org/files/get.php?file=emo-dev

[3]: https://addons.nvda-project.org/files/get.php?file=emo-o
