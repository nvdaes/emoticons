# Emoticons #
* Autorzy: Chris Leo, Noelia Ruiz Martínez, Mesar Hameed, Francisco Javier
  Estrada Martínez
* Zgodność z wersjami NVDA: 2018.3 do 2019.2
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

Naciśnij NVDA+I lub z menu Narzędzia-> opcję emotikonów, aby otworzyć okno dialogowe z dostarczonymi emotikonami lub emoji.

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

## Słownik Emotikonów ##

Ten dodatek pozwala korzystać z różnych słowników wymowy używających profili
konfiguracji.

Można tu utworzyć lub edytować oddzielny słownik wymowy dla każdego profilu
użytkownika.

Z Menu NVDA, Ustawienia -> Słowniki Wymowy -> Słownik Emotikonów, można otworzyć okno dialogowe służące do dodawania lub edycji dostępnych emotikonów.

Po dostosowaniu dodatku do potrzeb użytkownika i zapisaniu zmian, nowe
ustawienia odczytywania emotikonów będą działać jedynie w aktualnie
edytowanym profilu.

Jeżeli np. chcesz, żeby NVDA odczytywała emotikony użytkownika tylko w
komunikatorze XxChat , ale w innych komunikatorach już nie, możesz dodać
profil dla aplikacji XxChat i przypisać do niego słownik wymowy z menu
Dostosuj Emotikony. Więcej informacji na temat ustawiania aktywacji
emotikonów w odniesieniu do danego profilu konfiguracji znajdziesz poniżej.

Naciśnij przycisk "Zapisz i eksportuj słownik". Plik słownika o nazwie
emoticons.dic zostanie zapisany w twoim folderze konfiguracji użytkownika, w
podfolderze speechDicts.

Dokładna nazwa i lokalizacja pliku słownika zostanie stworzona na podstawie
aktualnie edytowanego profilu, który będzie wyświetlony w tytule okna
dialogowego słownika emotikonów.

## Ustawienia aktywacji ##

Menu Ustawienia -> Zarządzaj Emotikonami -> Ustawienia Aktywacji otwiera okno dialogowe konfiguracji aktywacji słowników wymowy dla każdego profilu.

W oknie dialogowym ustawień aktywacji, można określić, czy słownik wymowy powinien/niepowinien aktywować się automatycznie, gdy NVDA przełącza się na aktualnie edytowany profil. Jest to domyślnie wyłączone w standardowej konfiguracji NVDA i we wszystkich nowych profilach dodanych przez użytkownika.

Moreover, it's possible to determine if the add-on emojis should be
spoken. This could be useful to preserve symbols speaking if emojis are
included in NVDA's configuration.

Jeżeli wolisz nie wprowadzać do swoich folderów konfiguracji żadnych zmian,
możesz określić w tym samym oknie dialogowym, czy nieużywane słowniki
(przypisane do nieistniejących profili) mają zostać usunięte z dodatku po
jego wyłączeniu.

## Skróty klawiszowe: ##

To domyślnie dostępne skróty klawiszowe, można je zmieniać, albo dodać nowy
skrót służący do wywołania dialogu aktywacji lub słownika emotikonów:

* NVDA+E: przełącza między odczytywaniem tekstu tak jak został napisany, a
  odczytywaniem tekstu z emotikonami zastąpionymi przez opisy.
* NVDA+I: wyświetla okno dialogowe wyboru uśmieszku do skopiowania.
* Not assigned: open a browseable message showing the symbol where the
  review cursor is positioned, so that the whole description can be reviewed
  in browse mode.
* Not assigned: open a browseable message showing the symbol where the caret
  is positioned, so that the whole description can be reviewed in browse
  mode.

Uwaga: w  Windowsie 10, jest także możliwe używanie panelu emoji.

## Zmiany w wersji 11.0 ##

* When the add-on is updated, dictionaries saved in the previous version of
  the add-on will be automatically copied to the new version, unless you
  prefer to import dictionaries saved in the main dictionaries folder of
  NVDA.
* When showing the symbol where the caret or the review cursor are
  positioned, the words Character and Replacement are used to distinguish
  between the symbol itself and its description in browse mode, useful for
  speech users.

## Zmiany w wersji 10.0 ##

* Added commands to show the symbol where the review cursor or caret are
  positioned. Gestures for these commands can be assigned from the Input
  gestures dialog, Text review category.

## Zmiany w wersji 9.0 ##

* Added the possibility of choosing if add-on emojis should be spoken.
* Used appropiate encoding for dictionary names, fixing errors when they
  contain certain characters.
* The translated summary of the add-on is properly used for the title
  presented in add-on help, accessible from the add-on manager.
* Added a note mentioning the emoji panel available on Windows 10.

## Zmiany w wersji 8.0 ##

* zgodne z wersjami NVDA 2018.3 lub nowszymi (wymagane).

## Zmiany w wersji 6.0 ##

* Okno dialogowe ustawień aktywacji zostało przeniesione do oddzielnego
  panelu w ustawieniach NVDA, więc nazwa aktualnie aktywnego profilu będzie
  wyświetlana w tytule okna ustawień NVDA.
* Menu Zarządzaj Emotikonami zostało zastąpione opcją Emotikony dodaną do
  menu Narzędzia. Natomiast Dostosuj Emotikony zostało dodane do Słowników
  Wymowy, np. Słownika Emotikonów.
* Wymaga NVDA w wersji 2018.2 lub nowszej.
* W razie potrzeby, można pobrać [najnowszą wersję dodatku zgodną z NVDA
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

[1]: https://addons.nvda-project.org/files/get.php?file=emo

[2]: https://addons.nvda-project.org/files/get.php?file=emo-dev

[3]: https://addons.nvda-project.org/files/get.php?file=emo-o
