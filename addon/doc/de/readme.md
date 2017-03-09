# Smileys #

* Autoren: Chris Leo, Noelia Ruiz Martínez, Mesar Hameed, Francisco Javier
  Estrada Martínez
* [Stabile Version herunterladen][1]
* [Testversion herunterladen][2]

Using this add-on, spoken text containing emoticon characters will be
replaced by its more human friendly description.

So wird beispielsweise: ":)" als "Lächelndes Smiley" oder ":D" als
"Lachendes Smiley" gesprochen.

Folgende Features:

## Smiley einfügen ##

Sometimes an image is worth a 1000 words: use the new emoji to liven up your
instant message and to let your friends know how you’re feeling.

When you are unsure of the characters for a particular smiley, this addon
enables you to select and insert it into your text such as in a chat.

Press NVDA+I, or from menu Preferences -> Manage emoticons -> Insert emoticon, to open a dialog with the provided emoticons or emoji.

Dieser Dialog zeigt Ihnen eine Liste aller Smileys an, in der Sie ein Smiley
auswählen können, um Nähreres über dieses zu erfahren.

*	An editable field allows you to filter the search for the desired emoticon
  among the emoticons available.
*	Through a set of radio buttons, you can choose to view    only emoji category (alt+E) or view only standard emoticon category (alt+s) or view all emoticons available (alt+A).
*	In the list of emoticons (alt+L) are displayed  on three columns respectively: the name of emoticon, the type of emoticon (standard emoticon or emoji), the  corresponding character.

Wenn Sie auf "OK" drücken, wird die Zeichenfolge für das ausgewählte Smiley
in die Zwischenablage kopiert.

## Benutzerdefinierte Smileys ##

Unter Einstellungen -> Smileys verwalten -> Benutzerdefinierte Emoticons im NVDA-Menü, können Sie ein Dialogfeld öffnen, in dem Sie neue hinzufügen oder bereits eingetragene Emoticons bearbeiten können.
Hier können Sie nach Ihren Wünschen ein Wörterbuch für die Aussprache der Emoticons definieren.

Dieser Dialog speichert die zuvor eingegebene Textbeschreibung für das
entsprechende Smiley.

Der Schalter "Wörterbuch speichern und exportieren" legt eine Datei namens
"Emoticons.dic" in Ihrem "User Config"-Verzeichnis unterhalb von
"speechDicts" ab.

## Aktivierungseinstellungen ##

Sie können beim NVDA-Start die Aussprache der Smileys gleich aktivieren. Standardmäßig ist diese Option deaktiviert. Außerdem können Sie sie auch für diese Einstellung speichern.

Sie können zudem Ihre Einstellungen abspeichern.

## Tastenkombinationen: ##

In diesem Dialogfeld werden alle verfügbaren Standard-Tastenkombinationen
angezeigt. Diese können Sie bei Bedarf bearbeiten oder Neue hinzufügen über
das Dialogfeld der Aktivierungseinstellungen oder auch im Wörterbuch für die
Smileys:

* NVDA+E: Legt fest, ob Text so gelesen wird, wie er geschrieben wurde oder
  ob Smileys durch Beschreibung ersetzt werden sollen.
* NVDA+I: Zeigt ein Dialogfeld an, aus dem Sie ein Smiley zum Einfügen
  auswählen können.


## Änderungen in 5.0 ##

* Unterstützung für Emojis hinzugefügt.
* Improvements for Insert Emoticon dialog with a filter field and radio
  buttons to choose displayed emoticons.
* Using guiHelper for Activation settings dialog and Insert Emoticon dialog:
  requires NVDA 2016.4 or higher versions

## Änderungen in 4.0 ##

* Wenn der Dialog "Smiley einfügen" geöffnet wird, während ein
  Einstellungsdialog von NVDA aktiv ist, wird die zugehörige Fehlermeldung
  ausgegeben.


## Änderungen in 3.0 ##

* Im Dialog "Smileys verwalten..." kann nun festgelegt werden, dass ein
  Muster nur gültig ist, wenn es ein ganzes Wort ist. Vergleichbar mit den
  Aussprache-Wörterbüchern von NVDA 2014.4.


## Änderungen in 2.0 ##

* Eine Hilfe für diese Erweiterung ist in der Erweiterungsverwaltung
  verfügbar.


## Änderungen in 1.1 ##

* Doppelte Smileys entfernt.
* Einige Smileys hinzugefügt.

## Änderungen in 1.0 ##

* Ehrstveröffentlichung

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=emo

[2]: http://addons.nvda-project.org/files/get.php?file=emo-dev
