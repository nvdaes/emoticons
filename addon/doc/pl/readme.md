# Emotikony / Emoticons #


* Autorzy: Chris Leo, Noelia Ruiz Martínez, Mesar Hameed, Francisco Javier
  Estrada Martínez
* Pobierz [wersja stabilna][1]
* Pobierz [wersja rozwojowa][2]

Przy użyciu tego dodatku, wypowiadany tekst zawierający znaki emotikonów
zostanie zastąpiony przez bardziej przyjazne opisy.

Dla przykładu: ":)" zostanie odczytane jako "Buzia uśmiech", albo emoji
będzie przeczytany w odpowiedni sposób, zrozumiały dla użytkownika.

Możesz wykorzystać następujące funkcje:

## Wstaw uśmieszek ##

W niektórych sytuacjach, obraz jest warty 1000 słów: użyj nowego emoji, aby
ożywić twoje wiadomości błyskawiczne i pokazać swoim przyjaciołom, jak się
czujesz.

Jeśli nie jesteś pewien znaku dla określonego uśmiechu, ten dodatek pozwala
oznaczyć i dodać smajliki .

Press NVDA+I, or from menu Tools -> Insert emoticon, to open a dialog with the provided emoticons or emoji.

Ten dialog umożliwia wybór emotikonu i przeglądanie emotikonów, które cię
interesują:

*	Pole edycyjne pozwala filtrować wyszukiwanie rządanego emotikonu wśród
  dostępnych.
*	Poprzez przyciski opcji, można wybrać tylko emoji (alt+E) albo standardowe
  emotikony (alt+s) oraz wszystkie dostępne emotikony (alt+A).
*	Na liście emotikonów (alt+L) wyświetlane są trzy kolumny: nazwa emotikonu,
  typ emotikonu (emotikon standardowy lub emoji), i odpowiedni znaczek.

Po naciśnięciu "ok", znaczki dla wybranego emotikonu będą skopiowane do
schowka, już gotowe do wklejenia.

## Emoticons dictionary ##

Ten dodatek pozwala korzystać z różnych słowników wymowy używających profili
konfiguracji.

Można tu utworzyć lub edytować oddzielny słownik wymowy dla każdego profilu
użytkownika.

From NVDA MENU, Preferences -> Speech dictionaries -> Emoticons dictionary, you can open a dialog to add or to edit available emoticons.

Po dostosowaniu dodatku do potrzeb użytkownika i zapisaniu zmian, nowe
ustawienia odczytywania emotikonów będą działać jedynie w aktualnie
edytowanym profilu.

For example, you may wish that NVDA spoken custom emoticons only in XxChat
program, but not in other chat programs: you can do this by creating a
profile for the XxChat application and assign to it a speech dictionary from
Speech dictionaries menu, Emoticons dictionary option. See below for
Emoticons settings in relation to the configuration profiles.

Naciśnij przycisk "Zapisz i eksportuj słownik". Plik słownika o nazwie
emoticons.dic zostanie zapisany w twoim folderze konfiguracji użytkownika, w
podfolderze speechDicts.

Dokładna nazwa i lokalizacja pliku słownika zostanie stworzona na podstawie
aktualnie edytowanego profilu, który będzie wyświetlony w tytule okna
dialogowego słownika emotikonów.

## Emoticons settings ##

From menu Preferences -> Settings -> Emoticons opens a panel to configure the activation of your speech-dictionaries for each profile.

In Emoticons settings panel you can choose whether or not speech-dictionary should automatically activate when  NVDA switches to the   profile you are currently editing. By default it is disabled in normal configuration of NVDA and in all your new profiles.

Jeżeli wolisz nie wprowadzać do swoich folderów konfiguracji żadnych zmian,
możesz określić w tym samym oknie dialogowym, czy nieużywane słowniki
(przypisane do nieistniejących profili) mają zostać usunięte z dodatku po
jego wyłączeniu.

## Skróty klawiszowe: ##

These are the key commands available by default, you can edit those or add
new key to open Emoticons settings panel or Emoticon Dictionary dialog:

* NVDA+E: przełącza między odczytywaniem tekstu tak jak został napisany, a
  odczytywaniem tekstu z emotikonami zastąpionymi przez opisy.
* NVDA+I: wyświetla okno dialogowe wyboru uśmieszku do skopiowania.


## Changes for 7.0 ##

* The Activation settings dialog has been moved to a panel in NVDA settings,
  so that the current profile will be shown in the title of the NVDA
  settings dialog.
* The Manage Emoticons menu has been removed: now Insert emoticon will be
  found under the Tools menu, and Customize Emoticons will be shown under
  Speech dictionaries like Emoticons dictionary.
* Requires NVDA 2018.2 or later.
* If needed, you can download the [last version compatible with NVDA
  2017.3][3].

## Zmiany w wersji 6.0 ##

* Dodano wsparcie dla profili konfiguracji.
* W NVDA 2017.4 i nowszych wersjach, ustawienia konfiguracji oraz słowniki
  użytkownika będą się zmieniać automatycznie, zgodnie z wybranym
  profilem. W wersji 2017.3 i wcześniejszych, możesz wywołać tę zmianę przez
  opcję Przeładuj Wtyczki (naciskając control+NVDA+f3).
* Jeśli zechcesz zaimportować ustawienia przy aktualizacji dodatku,
  nieaktualne pliki (emoticons.ini i emoticons.dic) zostaną usunięte lub
  dostosowane do nowej wersji.

## Zmiany dla wersji 5.0 ##

* Dodane wsparcie dla emoji.
* Usprawnienia dla okna dialogowego wstaw emotikonyy z polem do filtrowania
  i i przyciskami opcji do wyboru wyświetlanych emotek.
* Używanie guiHelper do aktywacji okna dialogowego ustawień i okna
  dialogowego dla wstawiania emotek: wymaga NVDA 2016.4 lub nowsze wersje

## Zmiany dla wersji 4.0 ##

* Jeżeli jest otwarty dialog do wstawiania emotek, gdy się próbuje otworzyć
  inny dialog ustawień, NVDA wyświetli odpowiednią wiadomość o błędzie.


## Zmiany dla wersji 3.0 ##

* W oknie konfiguracji dodatku, , można teraz określić, że wzorzec powinien
  pasować tylko, jeśli jest całym słowem, zgodnie ze słownikami mowy NVDA
  2014.4.


## Zmiany dla wersji 2.0 ##

* Pomoc dodatku dostępna w managerze dodatków.


## Zmiany dla wersji 1.1 ##

* Usunięty powielony emotikon.
* Dodano kilka buź.

## Zmiany dla wersji 1.0 ##

* Pierwsza wersja.




[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=emo

[2]: http://addons.nvda-project.org/files/get.php?file=emo-dev

[3]:
https://github.com/nvdaes/emoticons/releases/download/6.5/emoticons-6.5.nvda-addon
