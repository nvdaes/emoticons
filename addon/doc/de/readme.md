# Emoticons #

* Autoren: Chris Leo, Noelia Ruiz Martínez, Mesar Hameed, Francisco Javier
  Estrada Martínez
* [Stabile Version herunterladen][1]
* [Testversion herunterladen][2]

Wenn Sie diese Erweiterung verwenden, werden Emoticons durch besser
verständliche Beschreibungen ersetzt. 

So wird beispielsweise: ":)" als "Lächelndes Gesicht" oder ":D" als
"Lachendes Gesicht" gesprochen.

Folgende Features:

## Emoticon einfügen ##

Manchmal sagt ein Bild mehr als 1000 Worte: Verwenden Sie die neuen Emojis,
um Ihre Sofortnachrichten zu beleben. Lassen Sie Ihre Freunde wissen, wie
Sie sich fühlen.

Wenn Sie sich unsicher sind, welche Zeichen für ein bestimmtes Smiley
verwendet werden, können Sie dieses Smiley mit Hilfe der Erweiterung
auswählen und es in Ihren Text (bspw. Chat) einfügen.

Drücken Sie NVDA+I, oder aus dem Menü Einstellungen -> Emoticons verwalten -> Emoticons einfügen, um einen Dialog mit den bereitgestellten Emoticons oder Emoji zu öffnen. 

Dieser Dialog zeigt Ihnen eine Liste aller Emoticons an, in der Sie ein
Emoticon auswählen können, um Nähreres über dieses zu erfahren.

*	Ein Eingabefeld ermöglicht es Ihnen, die Suche nach dem gewünschten
  Emoticon unter den verfügbaren Emoticons zu filtern.
*	Über eine Reihe von Kontrollfeldern können Sie wählen, ob Sie nur die
  Emoji-Kategorie (alt+e) oder nur die Standard-Emoticon-Kategorie (alt+s)
  oder alle verfügbaren Emoticons (alt+a) anzeigen möchten.
*	In der Liste der Emoticons (alt+L) werden jeweils auf drei Spalten
  angezeigt: der Name des Emoticons, der Typ des Emoticons (Standard
  Emoticon oder Emoji), das entsprechende Zeichen.

Wenn Sie auf "OK" drücken, wird die Zeichenfolge für das ausgewählte
Emoticon in die Zwischenablage kopiert.

## Benutzerdefinierte Emoticons ##

Emoticons add-on allows to have differents speech-dictionaries using
configuration profiles.

This means that you can create or edit a specific speech-dictionary for each
your custom profile.

Unter Einstellungen -> Emoticons verwalten -> Benutzerdefinierte Emoticons im NVDA-Menü, können Sie ein Dialogfeld öffnen, in dem Sie neue hinzufügen oder bereits eingetragene Emoticons bearbeiten können.
Hier können Sie nach Ihren Wünschen ein Wörterbuch für die Aussprache der Emoticons definieren.

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

## Aktivierungseinstellungen ##

From menu Preferences -> Manage Emoticons -> Activation-settings opens a dialog to configure the activation of your speech-dictionaries for each profile.

In activation-setting dialog you can choose whether or not speech-dictionary should automatically activate when  NVDA switches to the   profile you are currently editing. By default it is disabled in normal configuration of NVDA and in all your new profiles.

If you may wish to keep clean your configuration folders, in this dialog it
is also possible to choose if dictionaries not used (associated with non
existing profiles) will be removed from the add-on when it is unloaded.

## Tastenkombinationen: ##

In diesem Dialogfeld werden alle verfügbaren Standard-Tastenkombinationen
angezeigt. Diese können Sie bei Bedarf bearbeiten oder Neue hinzufügen über
das Dialogfeld der Aktivierungseinstellungen oder auch im Wörterbuch für die
Emoticons:

* NVDA+E: speaking emoticons on/off, toggles between speaking text as it is
  written, or with the emoticons replaced by the human description.
* NVDA+I: Zeigt ein Dialogfeld an, aus dem Sie ein Emoticon zum Einfügen
  auswählen können.

## Changes for 6.0 ##

* Added support for configuration profiles.
* In NVDA 2017.4 or later, the configuration settings and custom
  dictionaries will change automatically according with the selected
  profiles. In 2017.3 or earlier, you can apply changes by reloading plugins
  (pressing control+NVDA+f3).
* If you choose to import settings when updating the add-on, deprecated
  files (emoticons.ini and emoticons.dic) will be removed or adapted to this
  version.

## Änderungen für 5.0 ##

* Unterstützung für Emojis hinzugefügt.
* Verbesserungen im Dialogfeld Emoticon einfügen durch Filterfunktionen und
  Kontrollfeldern zur Auswahl der angezeigten Emoticons.
* Es wird  GuiHelper für die Dialoge Aktivierungseinstellungen und Emoticon
  einfügen und verwalten verwendet: erfordert NVDA 2016.4 oder höhere
  Versionen

## Änderungen bis 4.0 ##

* Wenn der Dialog "Smiley einfügen" geöffnet wird, während ein
  Einstellungsdialog von NVDA aktiv ist, wird die zugehörige Fehlermeldung
  ausgegeben.


## Änderungen bis 3.0 ##

* Im Dialog "Emoticons verwalten..." kann nun festgelegt werden, dass ein
  Muster nur gültig ist, wenn es ein ganzes Wort ist. Vergleichbar mit den
  Aussprache-Wörterbüchern von NVDA 2014.4.


## Änderungen bis 2.0 ##

* Hilfe zur Erweiterung ist in der Erweiterungsverwaltung verfügbar.


## Änderungen bis 1.1 ##

* Doppelte Emoticons entfernt.
* Einige Smileys hinzugefügt.

## Änderungen bis 1.0 ##

* Ehrstveröffentlichung

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=emo

[2]: http://addons.nvda-project.org/files/get.php?file=emo-dev
