# Emoticons #
* Autoren: Chris Leo, Noelia Ruiz Martínez, Mesar Hameed, Francisco Javier
  Estrada Martínez
* NVDA-Kompatibilität: 2019.3 oder neuer
* [Stabile Version herunterladen][1]
* [Entwicklerversion herunterladen][2]

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

Press NVDA+I, or from menu Tools -> Emoticons > Insert emoticon, to open a dialog with the provided emoticons or emoji.

Dieser Dialog zeigt Ihnen eine Liste aller Emoticons an. Dort könnenSie ein
Emoticon auswählen und seine zugehörige Beschreibung lesen:

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

## Insert symbol ##

This dialog allows you to choose one of the symbols available in the
Punctuation/symbol pronunciation dialog of NVDA. You can use the Filter edit
box or the arrow keys to select an item from the symbols list. Then, press
OK and the selected emoji or symbol will be copied to your clipboard, ready
for pasting.

## Emoticons-Wörterbuch ##

Die Erweiterung Emoticons ermöglicht die Erstellung verschiedener
Aussprachewörterbücher für unterschiedliche Konfigurationsprofile.

Das heißt Sie können für jedes Ihrer benutzerdefinierten Profile ein
spezielles Sprachwörterbuch erstellen oder bearbeiten.

Über das NVDA-Menü "Einstellungen" -> "Aussprachewörterbücher" -> "Emoticons-Wörterbuch", können Sie einen Dialog öffnen, um verfügbare Emoticons hinzuzufügen oder zu bearbeiten.

Wenn Sie Ihre Anpassungen speichern, gelten die neuen
Ausspracheeinstellungen von Emoticons nur für das gerade aktive Profil.

Zum Beispiel können Sie NVDA nur in XxChat, aber nicht in anderen
Chat-Programmen die Emoticons ansagen lassen: Sie können dies tun, indem Sie
ein Profil für die XxChat-Anwendung erstellen und ihr ein Sprachwörterbuch
aus dem Menü Sprachwörterbücher, Option Emoticons Wörterbuch,
zuweisen. Siehe unten für Emoticons Einstellungen in Bezug auf die
Konfigurationsprofile.

Der Schalter "Wörterbuch speichern und exportieren" legt eine entsprechende
Wörterbuchdatei in Ihrem "User Config"-Verzeichnis unter
"speechDicts/Emoticons" ab.

Der genaue Name und Speicherort der Wörterbuchdatei richtet sich nach dem
Konfigurationsprofil, das im Titel des Emoticons-Dialogs angezeigt wird.

## Emoticons-Einstellungen ##

Über das Menü "Einstellungen" -> "Emoticons" können Sie die Aktivierung Ihrer Sprachwörterbücher für jedes Profil konfigurieren.

In den Einstellungen von Emoticons können Sie auswählen, ob das Sprachwörterbuch automatisch aktiviert werden soll, wenn NVDA zu dem Profil wechselt, das Sie gerade bearbeiten. Standardmäßig ist es in der normalen Konfiguration von NVDA und in allen Ihren neuen Profilen deaktiviert.

Darüberhinaus kann ebenfalls festgelegt werden, ob die Emojis der
Erweiterung angesagt werden soll. Dies ist nützlich, wenn in der
NVDA-Konfiguration Symbole vorkommen.

Wenn Sie Ihre Konfigurationsordner sauber halten möchten, können Sie in
diesem Dialog nicht genutzte Wörterbücher von gelöschten Profilen entfernen.

## Tastenkombinationen: ##

Dies sind die standardmäßig verfügbaren Tastenbefehle. Sie können diese
bearbeiten oder neue Tasten hinzufügen, um das Emoticons-Einstellungsfenster
oder den Emoticon-Wörterbuch-Dialog zu öffnen:

* NVDA+E: Ansage der Emoticons aktivieren oder deaktivieren, legt fest, ob
  Text so gelesen wird, wie er geschrieben wurde oder  ob Emoticons durch
  Beschreibungen ersetzt werden sollen.
* NVDA+I: Zeigt ein Dialogfeld an, aus dem Sie ein Emoticon zum Einfügen
  auswählen können.
* Not assigned: show a dialog to select an NVDA's symbol you want to copy.
* Nicht zugewiesen: Öffnet eine (wie im Internet) lesbare Meldung, die das
  Symbol anzeigt, an dem sich der NVDA-cursor befindet, damit die gesamte
  Beschreibung Lese-Modus gelesen werden kann.
* Nicht zugewiesen: Öffnet eine (wie im Internet) lesbare Meldung, die das
  Symbol anzeigt, an dem sich die Schreibmarke befindet, damit die gesamte
  Beschreibung im Lese-Modus gelesen werden kann.

Hinweis: Unter Windows 10 ist es auch möglich, das integrierte Emoji-Panel
zu verwenden.

## Changes for 13.0 ##

* Fixed errors in Insert Emoticon dialog.
* Added a dialog to insert a symbol available in the Punctuation/symbol
  pronunciation of NVDA.

## Änderungen für 12.0 ##

* Erfordert NVDA 2019.3 oder höher.

## Änderungen in 11.0 ##

* Bei der Aktualisierung dieser Erweiterung werden die in der vorherigen
  Version gespeicherten Wörterbücher automatisch in die neue Version
  kopiert, es sei denn, Sie möchten ausdrücklich, dass diese aus dem
  Hauptkonfigurationsordner von NVDA importiert werden.
* Beim Anzeigen eines Symbols, auf dem sich der Systemcursor oder der
  NVDA-Cursor befindet, werden die Wörter, Zeichen und die Ersetzung
  verwendet, um zwischen dem Symbol selbst und seiner Beschreibung im
  Lesemodus zu unterscheiden. Dies ist nützlich für Anwender, die
  ausschließlich mit Sprachausgabe arbeiten, i.e. keine Braillezeile
  verwenden.

## Änderungen in 10.0 ##

* Es wurden Befehle hinzugefügt, um das Symbol anzuzeigen, an dem sich der
  NVDA-cursor oder die Schreibmarke befinden. Gesten für diese Befehle
  können im Dialogfeld Eingaben, Kategorie "Befehle zum Betrachten von
  Text", zugewiesen werden.

## Änderungen für 9.0 ##

* Man kann nun zu wählen, ob Emojis (die in der Erweiterung enthalten sind)
  gesprochen werden sollen.
* Adäquates encoding für Wörterbuchnamen verwendet, dies behebt Fehler, wenn
  diese bestimmte Zeichen enthalten.
* Die übersetzte Zusammenfassung der Erweiterung wird ordnungsgemäß für den
  Titel verwendet, der in der Erweiterungshilfe angezeigt wird und auf den
  über den Erweiterungs-Verwalter zugegriffen werden kann.
* Es wurde eine Notiz hinzugefügt, in der das Emoji-Panel unter Windows 10
  erwähnt wird.

## Änderungen für 8.0 ##

* Kompatibel mit NVDA 2018.3 oder neuer (erforderlich).

## Änderungen für 7.0 ##

* Der Dialog Aktivierungseinstellungen wurde in ein Fenster in den
  NVDA-Einstellungen verschoben, so dass das aktuelle Profil im Titel des
  NVDA-Einstellungsdialogs angezeigt wird.
* Das Menü Emoticons verwalten wurde entfernt: Jetzt wird Emoticon einfügen
  unter dem Menü Extras und Emoticons anpassen unter Sprachwörterbücher wie
  Emoticons Wörterbuch angezeigt.
* Benötigt NVDA 2018.2 oder höher.
* Bei Bedarf können Sie die[letzte Version, die mit NVDA 2017.3 kompatibel
  ist][3] herunterladen.

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

* Ehrstveröffentlichung.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=emo

[2]: https://addons.nvda-project.org/files/get.php?file=emo-dev

[3]: https://addons.nvda-project.org/files/get.php?file=emo-o
