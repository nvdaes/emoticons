# Emoticons #
* Auteurs : Chris Leo, Noelia Ruiz Martínez, Mesar Hameed, Francisco Javier
  Estrada Martínez
* NVDA compatibility: 2019.3 or later
* Télécharger [version stable][1]
* Télécharger [version de développement][2]

En utilisant cette extension, la verbalisation du texte contenant les
caractères de l'émoticône seront remplacés par leur description humaine plus
conviviale.

Par exemple : la séquence ":)" sera prononcé comme "Émoticône Sourire", ou
par exemple NVDA Reconnaîtra la signification de chaque emoji.

Vous pouvez profiter des fonctionnalités suivantes :

## Insérer une émoticône ##

Parfois, une image vaut 1000 mots : utilisez le nouvel emoji pour animer vos
messages instantanés pour indiquer à vos contacts ce que vous ressentez.

Lorsque vous n'êtes pas sûr des caractères pour une émoticône particulière,
cette extension vous permet de sélectionner et insérer dans votre texte
comme dans une conversation.

Press NVDA+I, or from menu Tools -> Emoticons > Insert emoticon, to open a dialog with the provided emoticons or emoji.

Ce dialogue vous permet de choisir une émoticône et d'afficher les
émoticônes qui vous intéressent :

*	Un champ éditable vous permet de filtrer la recherche de l'émoticône
  souhaitée parmi les émoticônes disponibles.
*	Grâce à un ensemble de boutons radio, vous pouvez choisir d'afficher
  uniquement la catégorie emoji (alt+E) ou afficher uniquement la catégorie
  émoticône standard (alt+s) ou afficher toutes les émoticônes disponibles
  (alt+A).
*	Dans la liste des émoticônes (alt+L) sont affichés respectivement sur
  trois colonnes : le nom de l'émoticône, le type d'émoticône (émoticône
  standard ou emoji), le  caractère correspondant.

Lorsque vous appuyez sur OK, les caractères pour l'émoticône choisie sont
copiés dans le presse-papiers, prêts à être collés.

## Insert symbol ##

This dialog allows you to choose one of the symbols available in the
Punctuation/symbol pronunciation dialog of NVDA. You can use the Filter edit
box or the arrow keys to select an item from the symbols list. Then, press
OK and the selected emoji or symbol will be copied to your clipboard, ready
for pasting.

## Dictionnaire des émoticônes ##

L'extension emoticons permet d'avoir différents dictionnaires de parole en
utilisant des profils de configuration.

Cela signifie que vous pouvez créer ou modifier un dictionnaire de parole
spécifique pour chaque profil personnalisé.

À partir du Menu NVDA, Préférences -> Dictionnaires de prononciation -> Dictionnaire des émoticônes, vous pouvez ouvrir un dialogue pour ajouter ou modifier les émoticônes disponibles.

En sauvegardant vos personnalisations, les nouveaux paramètres de lecture
des émoticônes ne s'appliqueront qu'au profil que vous êtes en train
d'éditer.

Par exemple, vous pouvez souhaiter que NVDA ne annonce des émoticônes
personnalisées que dans le programme XxChat, mais pas dans les autres
programmes de conversation: vous pouvez créer un profil pour l'application
XxChat et lui attribuer un dictionnaire de parole à partir du menu
Dictionnaires de prononciation, option du Dictionnaires des émoticônes. Voir
ci-dessous pour les Paramètres des émoticônes par rapport aux profils de
configuration.

Vous pouvez également exporter chaque dictionnaire de parole personnalisé en
appuyant sur le bouton "Enregistrer et exporter le dictionnaire": de cette
façon, vos dictionnaires de parole  seront enregistrés dans votre dossier de
configuration utilisateur, sous-dossier speechDicts/emoticons.

Le nom exact et l'emplacement du fichier de dictionnaire seront basés sur le
profil de configuration d'édition, qui sera affiché dans le titre du
dialogue Dictionnaire des émoticônes.

## Paramètres des émoticônes ##

À partir du menu Préférences -> Paramètres -> émoticônes ouvre un panneau pour configurer l'activation de vos dictionnaires de parole pour chaque profil.

Dans le panneau Paramètres des émoticônes, vous pouvez choisir si le dictionnaire de parole doit ou non être activé automatiquement lorsque NVDA bascule sur le profil que vous êtes en train d'éditer. Par défaut, il est désactivé dans la configuration normale de NVDA et dans tous vos nouveaux profils.

Moreover, it's possible to determine if the add-on emojis should be
spoken. This could be useful to preserve symbols speaking if emojis are
included in NVDA's configuration.

Si vous souhaitez garder propres vos dossiers de configuration, vous pouvez
également choisir dans ce dialogue si les dictionnaires non utilisés
(associés à des profils non existants) seront supprimés de l'extension
lorsqu'il est déchargé.

## Raccourcis clavier : ##

Voici les raccourcis clavier par défaut, vous pouvez les modifier ou ajouter
un nouveau raccourci pour ouvrir le panneau Paramètres des émoticônes ou le
dialogue Dictionnaire des émoticônes :

* NVDA+E : en activant/désactivant l'annonce des émoticônes, permet de
  basculer entre la lecture du texte comme il est écrit, ou avec les
  émoticônes remplacées par leur description humaine.
* NVDA+I : affiche un dialogue pour choisir l'émoticône que vous souhaitez
  copier.
* Not assigned: show a dialog to select an NVDA's symbol you want to copy.
* Not assigned: open a browseable message showing the symbol where the
  review cursor is positioned, so that the whole description can be reviewed
  in browse mode.
* Not assigned: open a browseable message showing the symbol where the caret
  is positioned, so that the whole description can be reviewed in browse
  mode.

Note : Sous Windows 10, il est également possible d’utiliser le panneau
emoji intégré.

## Changes for 13.0 ##

* Fixed errors in Insert Emoticon dialog.
* Added a dialog to insert a symbol available in the Punctuation/symbol
  pronunciation of NVDA.

## Changes for 12.0 ##

* Requires NVDA 2019.3 or later.

## Changes for 11.0 ##

* When the add-on is updated, dictionaries saved in the previous version of
  the add-on will be automatically copied to the new version, unless you
  prefer to import dictionaries saved in the main dictionaries folder of
  NVDA.
* When showing the symbol where the caret or the review cursor are
  positioned, the words Character and Replacement are used to distinguish
  between the symbol itself and its description in browse mode, useful for
  speech users.

## Changes for 10.0 ##

* Added commands to show the symbol where the review cursor or caret are
  positioned. Gestures for these commands can be assigned from the Input
  gestures dialog, Text review category.

## Changes for 9.0 ##

* Added the possibility of choosing if add-on emojis should be spoken.
* Used appropiate encoding for dictionary names, fixing errors when they
  contain certain characters.
* The translated summary of the add-on is properly used for the title
  presented in add-on help, accessible from the add-on manager.
* Added a note mentioning the emoji panel available on Windows 10.

## Changements pour la version 8.0 ##

* Compatible avec NVDA 2018.3 ou version ultérieure (requis).

## Changements pour la version 7.0 ##

* Le dialogue Paramètres d'activation a été déplacée vers un panneau dans
  les Paramètres NVDA, de sorte que le profil actuel s'affiche dans le titre
  du dialogue des Paramètres NVDA.
* Le menu Gérer les émoticônes a été supprimé: maintenant, pour Insérer une
  émoticône se trouve dans le menu Outils et pour Personnaliser les
  émoticônes s'affichent sous le Dictionnaires de prononciation comme le
  Dictionnaire des émoticônes.
* Nécessite NVDA 2018.2 ou ultérieur.
* Si nécessaire, vous pouvez télécharger la [dernière version compatible
  avec NVDA 2017.3][3].

## Changements pour la version 6.0 ##

* Ajout du support pour les profils de configuration.
* Dans NVDA 2017.4 ou version ultérieure, les paramètres de configuration et
  les dictionnaires personnalisés changent automatiquement en fonction des
  profils sélectionnés. Dans la  2017.3 ou précédente, vous pouvez appliquer
  les modifications en rechargeant les modules complémentaires  (en appuyant
  sur  contrôle+NVDA+f3).
* Si vous choisissez d'importer les paramètres lors de la mise à jour de
  l'extension, les fichiers obsolètes (emoticons.ini et emoticons.dic)
  seront supprimés ou adaptés à cette version.

## Changements pour la version 5.0 ##

* Ajout du support pour les emojis.
* Améliorations du dialogue Insérer une émoticône avec un champ pour filtrer
  et des boutons radio pour choisir les émoticônes affichées.
* En utilisant le dialogue GuiHelper pour le dialogue Paramètres
  d'activation et le dialogue Insérer une émoticône : nécessite NVDA 2016.4
  ou versions supérieures

## Changements pour la version 4.0 ##

* Si le dialogue Insérer une émoticône est ouvert lorsqu'un autre dialogue
  de paramètres est actif, NVDA affichera le message d'erreur correspondant.


## Changements pour la version 3.0 ##

* Dans le dialogue Personnaliser les émoticônes, il est maintenant possible
  de spécifier qu'un modèle doit correspondre uniquement si c'est un mot
  entier, selon les dictionnaires de paroles de NVDA 2014.4.


## Changements pour la version 2.0 ##

* L'aide de l'extension est disponible à partir du Gestionnaire
  d'Extensions.


## Changements pour la version 1.1 ##

* Suppression des émoticônes dupliquées.
* Ajout de quelques émoticônes.

## Changements pour la version 1.0 ##

* Première version.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=emo

[2]: https://addons.nvda-project.org/files/get.php?file=emo-dev

[3]: https://addons.nvda-project.org/files/get.php?file=emo-o
