# Emoticons #

* Authors: Chris Leo, Noelia Ruiz Martínez, Mesar Hameed, Francisco Javier
  Estrada Martínez
* Télécharger [version stable][1]
* Télécharger [version de développement][2]

Using this add-on, spoken text containing emoticon characters will be
replaced by its more human friendly description.

For example: the sequence ":)" will be spoken as "smiling smiley", or for
example NVDA will recognize the meaning of each emoji.

Vous pouvez profiter des fonctionnalités suivantes :

## Insert Emoticon ##

When you are unsure of the characters for a particular smiley, this addon
enables you to select and insert it into your text such as in a chat.

Press NVDA+I, or from menu Preferences -> Manage emoticons -> Insert emoticon, to open a dialog with the provided emoticons or emoji.

This dialog allows you to choose an emoticon and to view the emoticons that
interest you:

*	An editable field allows you to filter the search for the desired emoticon
  among the emoticons available.
*	Through a set of radio buttons, you can choose to view    only emoji category (alt+E) or view only standard emoticon category (alt+s) or view all emoticons available (alt+A).
*	In the list of emoticons (alt+L) are displayed  on three columns respectively: the name of emoticon, the type of emoticon (standard emoticon or emoji), the  corresponding character.

When you press OK, the characters for the chosen emoticon will be copied to
your clipboard, ready for pasting.

## Personnaliser les frimousses ##

From NVDA MENU, Preferences -> Manage emoticons -> Customize emoticons, you can open a dialog setting to add or to edit available emoticons.

This dialog allows you to save an emoticons speech dictionary with your
customizations.

En appuyant sur le bouton "Enregistrer et exporter le dictionnaire" un
fichier de dictionnaire nommé emoticons.dic sera enregistré dans votre
dossier de configuration utilisateur, sous-dossier speechDicts.

## Paramètres d'activation ##

From menu Preferences -> Manage Emoticons -> Activation settings, you can choose whether to Activate speaking of emoticons when starting NVDA. By default it is disabled.
It is also possible to save your choice for this setting.

## Raccourcis clavier : ##

These are the key command available by default, you can edit those or add
new key to open Activation settings dialog or Emoticon Dictionary dialog:

* NVDA+E: permet de basculer entre la lecture du texte comme il est écrit,
  ou avec les frimousses remplacées par leur description humaine.
* NVDA+I: show a dialog to select an emoticon you want to copy.


## Changes for 5.0 ##

* Added support for emojis.
* Improvements for Insert Emoticon dialog with a filter field and radio
  buttons to choose displayed emoticons.
* Using guiHelper for Activation settings dialog and Insert Emoticon dialog:
  requires NVDA 2016.4 or higher versions

## Changements pour la version 4.0 ##

* Si la boîte de dialogue Insérer une frimousse est ouverte lorsqu'une autre
  boîte de dialogue de paramètres est actif, NVDA affichera le message
  d'erreur correspondant.


## Changements pour la version 3.0 ##

* Dans la boîte de dialogue Personnaliser les frimousses, il est maintenant
  possible de spécifier qu'un modèle doit correspondre uniquement si c'est
  un mot entier, selon les dictionnaires de paroles de NVDA 2014.4.


## Changements pour la version 2.0 ##

* L'aide du module complémentaire est disponible à partir du Gestionnaire de
  modules complémentaires.


## Changements pour la version 1.1 ##

* Suppression des frimousses dupliqué.
* Ajouté quelques frimousses.

## Changements pour la version 1.0 ##

* Première version.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=emo

[2]: http://addons.nvda-project.org/files/get.php?file=emo-dev
