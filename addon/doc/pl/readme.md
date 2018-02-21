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
ożywić twoje wiadomości błyskawicznei żeby pokazać swoim przyjacielom, jak
się czujesz.

Jeśli nie jesteś pewien znaku dla określonego uśmiechu, ten dodatek pozwala
oznaczyć i dodać smajliki .

Naciśnij NVDA+I, oraz z mini ustawień -> zarządzaj emotikonami -> wstaw emotykon, aby otworzyć dialog z dostępnymi emotikonami lub emoji.

Ten dialog umożliwia wybór emotikonu i przegląd emotikonów interesujących
cie:

*	An editable field allows you to filter the search for the desired emoticon
  among the emoticons available.
*	Poprzez przyciski opcji, można wybrać tylko emoji (alt+E) albo standardowe
  emotykony (alt+s) oraz wszystkie emotykony (alt+A).
*	Na liście emotikonów (alt+L) wyświetlane są trzy kolumny: nazwa emotikonu,
  typ emotikonu (emotikon standardowy lub emoji), i odpowiedni znaczek.

Po naciśnięciu "ok", znaczki dla wybranego emotikonu będą skopiowane do
schowka, już gotowe do wklejenia.

## Dostosuj emotikony ##

Emoticons add-on allows to have differents speech-dictionaries using
configuration profiles.

This means that you can create or edit a specific speech-dictionary for each
your custom profile.

Z pozycji meni NVDA, Ustawienia -> Zarządzaj emotikonami -> dostosuj emotikony, można otworzyć okno dialogowe, w którym można edytować istniejące, lub dodawać nowe emotykony.

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

## Ustawienia aktywacji ##

From menu Preferences -> Manage Emoticons -> Activation-settings opens a dialog to configure the activation of your speech-dictionaries for each profile.

In activation-setting dialog you can choose whether or not speech-dictionary should automatically activate when  NVDA switches to the   profile you are currently editing. By default it is disabled in normal configuration of NVDA and in all your new profiles.

If you may wish to keep clean your configuration folders, in this dialog it
is also possible to choose if dictionaries not used (associated with non
existing profiles) will be removed from the add-on when it is unloaded.

## Skróty klawiszowe: ##

To są domyślnie dostępne skróty klawiszowe, można ich zmienić, albo dodać
nowy skrót do wywołania dialogu aktywacji lub słownika emotikonów:

* NVDA+E: speaking emoticons on/off, toggles between speaking text as it is
  written, or with the emoticons replaced by the human description.
* NVDA+I: wyświetla okno dialogowe wyboru uśmieszku do skopiowania.

## Changes for 6.0 ##

* Added support for configuration profiles.
* In NVDA 2017.4 or later, the configuration settings and custom
  dictionaries will change automatically according with the selected
  profiles. In 2017.3 or earlier, you can apply changes by reloading plugins
  (pressing control+NVDA+f3).
* If you choose to import settings when updating the add-on, deprecated
  files (emoticons.ini and emoticons.dic) will be removed or adapted to this
  version.

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
