# Emoticons #


* Autoren: Chris Leo, Noelia Ruiz Martínez, Mesar Hameed, Francisco Javier
  Estrada Martínez
* [Stabile Version herunterladen][1]
* [Testversion herunterladen][2]

Diese Erweiterung ersetzt Emoticons durch besser verständliche
Beschreibungen.

So wird beispielsweise: ":)" als "Lächelndes Gesicht" oder ":D" als
"Lachendes Gesicht" ausgesprochen.

Diese Erweiterung bietet folgende Funktionen:

## Emoticon einfügen ##

Manchmal sagt ein Bild mehr als 1000 Worte: Sie können die neuen Emojis in
Ihren Nachrichten einfügen und Ihren Freunden dadurch zeigen, wie Sie sich
fühlen.

Wenn Sie sich unsicher sind, welche Zeichen für ein bestimmtes Smiley
verwendet werden, können Sie dieses Smiley mit Hilfe der Erweiterung
auswählen und es in Ihren Text einfügen.

Press NVDA+I, or from menu Tools -> Insert emoticon, to open a dialog with the provided emoticons or emoji.

Dieser Dialog zeigt Ihnen eine Liste aller Emoticons an. Dort könnenSie ein
Emoticon auswählen und seine zugehörige Beschreibung lesen.

*	Ein Eingabefeld ermöglicht es Ihnen, die Suche nach dem gewünschten
  Emoticon unter den verfügbaren Emoticons zu filtern.
*	Über eine Reihe von Kontrollfeldern können Sie wählen, ob Sie nur die
  Emoji-Kategorie (alt+e), nur die Standard-Emoticon-Kategorie (alt+s) oder
  alle verfügbaren Emoticons (alt+a) anzeigen möchten.
*	In der Liste der Emoticons (alt+L) werden jeweils auf drei Spalten
  angezeigt: der Name des Emoticons, der Typ (Standard Emoticon oder Emoji)
  und das entsprechende Zeichen.

Mit Drücken auf "OK" wird die Zeichenfolge für das ausgewählte Emoticon in
die Zwischenablage kopiert.

## Emoticons dictionary ##

Die Erweiterung Emoticons ermöglicht die Erstellung verschiedener
Aussprachewörterbücher für unterschiedliche Konfigurationsprofile.

Das heißt Sie können für jedes Ihrer benutzerdefinierten Profile ein
spezielles Sprachwörterbuch erstellen oder bearbeiten.

From NVDA MENU, Preferences -> Speech dictionaries -> Emoticons dictionary, you can open a dialog to add or to edit available emoticons.

Wenn Sie Ihre Anpassungen speichern, gelten die neuen
Ausspracheeinstellungen von Emoticons nur für das gerade aktive Profil.

For example, you may wish that NVDA spoken custom emoticons only in XxChat
program, but not in other chat programs: you can do this by creating a
profile for the XxChat application and assign to it a speech dictionary from
Speech dictionaries menu, Emoticons dictionary option. See below for
Emoticons settings in relation to the configuration profiles.

Der Schalter "Wörterbuch speichern und exportieren" legt eine entsprechende
Wörterbuchdatei in Ihrem "User Config"-Verzeichnis unter
"speechDicts/Emoticons" ab.

Der genaue Name und Speicherort der Wörterbuchdatei richtet sich nach dem
Konfigurationsprofil, das im Titel des Emoticons-Dialogs angezeigt wird.

## Emoticons settings ##

From menu Preferences -> Settings -> Emoticons opens a panel to configure the activation of your speech-dictionaries for each profile.

In Emoticons settings panel you can choose whether or not speech-dictionary should automatically activate when  NVDA switches to the   profile you are currently editing. By default it is disabled in normal configuration of NVDA and in all your new profiles.

Wenn Sie Ihre Konfigurationsordner sauber halten möchten, können Sie in
diesem Dialog nicht genutzte Wörterbücher von gelöschten Profilen entfernen.

## Tastenkombinationen: ##

These are the key commands available by default, you can edit those or add
new key to open Emoticons settings panel or Emoticon Dictionary dialog:

* NVDA+E: Ansage der Emoticons aktivieren oder deaktivieren, legt fest, ob
  Text so gelesen wird, wie er geschrieben wurde oder  ob Emoticons durch
  Beschreibungen ersetzt werden sollen.
* NVDA+I: Zeigt ein Dialogfeld an, aus dem Sie ein Emoticon zum Einfügen
  auswählen können.


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

## Änderungen in 6.0 ##

* Unterstützt nun auch benutzerdefinierte Konfigurationsprofile in NVDA.
* In NVDA 2017.4 oder höher ändern sich die Konfigurationseinstellungen und
  benutzerdefinierten Wörterbücher automatisch entsprechend den ausgewählten
  Profilen. In 2017.3 oder früher können Sie Änderungen vornehmen, indem Sie
  Plugins neu laden (STRG+NVDA+f3).
* Wenn Sie beim Aktualisieren der Erweiterung "Einstellungen importieren"
  wählen, werden veraltete Dateien (emoticons.ini und emoticons.dic)
  entfernt oder an diese Version angepasst.

## Änderungen in 5.0 ##

* Unterstützung für Emojis hinzugefügt.
* Verbesserungen im Dialogfeld Emoticon einfügen durch Filterfunktionen und
  Kontrollfeldern zur Auswahl der angezeigten Emoticons.
* GuiHelper wird für die Dialoge Aktivierungseinstellungen und Emoticon
  einfügen und verwalten verwendet: erfordert NVDA 2016.4 oder höher

## Änderungen in 4.0 ##

* Wenn der Dialog "Smiley einfügen" geöffnet wird, während ein
  Einstellungsdialog von NVDA aktiv ist, wird die zugehörige Fehlermeldung
  ausgegeben.


## Änderungen in 3.0 ##

* Im Dialog "Emoticons verwalten..." kann nun die Gültigkeit eines Musters
  festgelegt werden, wenn es ein ganzes Wort ist. Dies ist mit den
  Aussprache-Wörterbüchern von NVDA 2014.4 vergleichbar.


## Änderungen in 2.0 ##

* Hilfe zur Erweiterung ist in der Erweiterungsverwaltung verfügbar.


## Änderungen in 1.1 ##

* Doppelte Emoticons wurden entfernt.
* Einige Smileys wurden hinzugefügt.

## Änderungen in 1.0 ##

* Ehrstveröffentlichung




[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=emo

[2]: http://addons.nvda-project.org/files/get.php?file=emo-dev

[3]:
https://github.com/nvdaes/emoticons/releases/download/6.5/emoticons-6.5.nvda-addon
