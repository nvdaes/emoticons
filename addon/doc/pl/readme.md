# Emoticons #

* Autorzy: Chris Leo, Noelia Ruiz Martínez, Mesar Hameed, Francisco Javier
  Estrada Martínez

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

Naciśnij NVDA+I lub z menu Narzędzia -> Emotikony > Wstaw emotikon, aby otworzyć okno dialogowe z dostarczonymi emotikonami lub emotikonami.

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

## Wstaw symbol ##

To okno dialogowe pozwala wybrać jeden z symboli dostępnych w oknie
dialogowym Interpunkcja/wymowa symbolu NVDA. Możesz użyć pola edycji Filtr
lub strzałek, aby wybrać element z listy symboli.

Jeśli chcesz skopiować różne symbole, użyj przycisku Dodaj, aby dołączyć je
do pola edycji Symbole do skopiowania.

Następnie naciśnij OK, a wybrane emoji lub symbol lub symbole zawarte we
wspomnianym polu edycji zostaną skopiowane do schowka, gotowe do wklejenia.

## Kojarzenie gestów z symbolami ##

Z menu NVDA, podmenu Preferencje, okna dialogowego Gesty wprowadzania,
kategorii Wstaw symbole, możesz skonfigurować NVDA do wpisywania symboli
poprzez powiązane gesty.

Za pomocą pola edycji Edytuj pole można zmniejszyć liczbę prezentowanych
symboli, dzięki czemu można szybciej rozwinąć tę kategorię.

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

Przede wszystkim, można regulować wymowę emoji dodatku. To jest użyteczne
gdy chcemy zachować wymowe emoji przez NVDA.

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
* Nie przypisano: pokaż okno dialogowe, aby wybrać symbol NVDA, który chcesz
  skopiować.
* Nieprzydzielone: Otwiera opis znaku pod kursorem przeglądu jako wiadomość
  HTML, aby było możliwe przeczytanie opisu znaku w trybie przeglądania.
* Nieprzydzielone: otwiera wiadomość w oknie HTML, aby było możliwe
  przeczytanie opisu znaku w trybie przeglądania.

Uwaga: W systemie Windows 10 i nowszych można również korzystać z
wbudowanego panelu emoji.

## Zmiany w wersji 17.0 ##

* Dodano możliwość kojarzenia gestów z symbolami wpisywania.
* Dodano możliwość kopiowania różnych symboli w tym samym czasie.

## Zmiany w wersji 16.0 ##

* Kompatybilny z NVDA 2023.1.

## Zmiany w wersji 15.0 ##

* Wymaga NVDA 2022.1 lub nowszego.
* Nie można używać w trybie bezpiecznym.

## Zmiany w wersji 14.0 ##

* Kompatybilny z NVDA 2021.1.

## Zmiany w wersji 13.0  ##

* Naprawiono błędy w oknie dialogowym Wstaw emotikon.
* Dodano okno dialogowe do wstawiania symbolu dostępnego w wymowie
  interpunkcyjnej/symbolu NVDA.

## Zmiany dla wersji 12.0 ##

* Wymaga NVDA w wersji 2019.3 lub nowszej.

## Zmiany w wersji 11.0 ##

* Przy aktualizacji dodatku, stare słowniki będą kopiowane do nowej wersji,
  jednak użytkownik może używać głównych słowników w folderze.
* Przy pokazywaniu znaku, słowa znak i zamiana są korzystane aby pokazać
  różnice w trybie czytania, przydatne dla użytkowników którzy używają mowy.

## Zmiany w wersji 10.0 ##

* Dodano polecenie które pokazuje gdzie znajduje się określony znak. Gesty
  dla tego polecenia można zmienić z poziomu dialogu zdarzenia wejścia,
  kategoria przegląd tekstu.

## Zmiany w wersji 9.0 ##

* Dodano możliwość wymawiania emoji dodatku.
* Używane oczekiwane kodowanie dla słowników, poprawiając błąd przy
  napotkanych znakach niewspieranych.
* Opis dodatku jest prawidłowo wykorzystywany dla pokazywanego tytułu w
  pomocy dodatku, dostępnej z menedżera dodatku.
* Dodano notatkę uwzględniającą emoji panel w Windowsie 10.

## Zmiany w wersji 8.0 ##

* Kompatybilny z NVDA 2018.3 lub nowszym (wymagane).

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

[3]: https://www.nvaccess.org/addonStore/legacy?file=emo-o
