# Emoticons #


* Auteurs : Chris Leo, Noelia Ruiz Martínez, Mesar Hameed, Francisco Javier
  Estrada Martínez
* Télécharger [version stable][1]
* Télécharger [version de développement][2]

En utilisant ce module complémentaire, la verbalisation du texte contenant
les caractères de la frimousse seront remplacés par leur description humaine
plus conviviale.

Par exemple : la séquence ":)" sera prononcé comme "Frimousse Sourire", ou
par exemple NVDA Reconnaîtra la signification de chaque emoji.

Vous pouvez profiter des fonctionnalités suivantes :

## Insérer une frimousse ##

Parfois, une image vaut 1000 mots : utilisez le nouvel emoji pour animer vos
messages instantanés pour indiquer à vos contacts ce que vous ressentez.

Lorsque vous n'êtes pas sûr des caractères pour une frimousse particulière,
ce module complémentaire vous permet de sélectionner et insérer dans votre
texte comme dans une conversation.

Press NVDA+I, or from menu Tools -> Insert emoticon, to open a dialog with the provided emoticons or emoji.

Ce dialogue vous permet de choisir une frimousse et d'afficher les
frimousses qui vous intéressent :

*	Un champ éditable vous permet de filtrer la recherche de la frimousse
  souhaitée parmi les frimousses disponibles.
*	Grâce à un ensemble de boutons radio, vous pouvez choisir d'afficher
  uniquement la catégorie emoji (alt+E) ou afficher uniquement la catégorie
  frimousse standard (alt+s) ou afficher toutes les frimousses  disponibles
  (alt+A).
*	Dans la liste des frimousses (alt+L) sont affichés respectivement sur
  trois colonnes : le nom de la frimousse, le type de frimousse (frimousse
  standard ou emoji), le  caractère correspondant.

Lorsque vous appuyez sur OK, les caractères pour la frimousse choisie sont
copiés dans le presse-papiers, prêts à être collés.

## Emoticons dictionary ##

Le module complémentaire emoticons permet d'avoir différents dictionnaires
de parole en utilisant des profils de configuration.

Cela signifie que vous pouvez créer ou modifier un dictionnaire de parole
spécifique pour chaque profil personnalisé.

From NVDA MENU, Preferences -> Speech dictionaries -> Emoticons dictionary, you can open a dialog to add or to edit available emoticons.

En sauvegardant vos personnalisations, les nouveaux paramètres de lecture
des frimousses ne s'appliqueront qu'au profil que vous êtes en train
d'éditer.

For example, you may wish that NVDA spoken custom emoticons only in XxChat
program, but not in other chat programs: you can do this by creating a
profile for the XxChat application and assign to it a speech dictionary from
Speech dictionaries menu, Emoticons dictionary option. See below for
Emoticons settings in relation to the configuration profiles.

Vous pouvez également exporter chaque dictionnaire de parole personnalisé en
appuyant sur le bouton "Enregistrer et exporter le dictionnaire": de cette
façon, vos dictionnaires de parole  seront enregistrés dans votre dossier de
configuration utilisateur, sous-dossier speechDicts/emoticons.

Le nom exact et l'emplacement du fichier de dictionnaire seront basés sur le
profil de configuration d'édition, qui sera affiché dans le titre du
dialogue Dictionnaire des frimousses.

## Emoticons settings ##

From menu Preferences -> Settings -> Emoticons opens a panel to configure the activation of your speech-dictionaries for each profile.

In Emoticons settings panel you can choose whether or not speech-dictionary should automatically activate when  NVDA switches to the   profile you are currently editing. By default it is disabled in normal configuration of NVDA and in all your new profiles.

Si vous souhaitez garder propres vos dossiers de configuration, vous pouvez
également choisir dans ce dialogue si les dictionnaires non utilisés
(associés à des profils non existants) seront supprimés du module
complémentaire lorsqu'il est déchargé.

## Raccourcis clavier : ##

These are the key commands available by default, you can edit those or add
new key to open Emoticons settings panel or Emoticon Dictionary dialog:

* NVDA+E : en activant/désactivant l'annonce des frimousses, permet de
  basculer entre la lecture du texte comme il est écrit, ou avec les
  frimousses remplacées par leur description humaine.
* NVDA+I : affiche un dialogue pour choisir la frimousse que vous souhaitez
  copier.


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

## Changements pour la version 6.0 ##

* Ajout du support pour les profils de configuration.
* Dans NVDA 2017.4 ou version ultérieure, les paramètres de configuration et
  les dictionnaires personnalisés changent automatiquement en fonction des
  profils sélectionnés. Dans la  2017.3 ou précédente, vous pouvez appliquer
  les modifications en rechargeant les modules complémentaires  (en appuyant
  sur  contrôle+NVDA+f3).
* Si vous choisissez d'importer les paramètres lors de la mise à jour du
  module complémentaire, les fichiers obsolètes (emoticons.ini et
  emoticons.dic) seront supprimés ou adaptés à cette version.

## Changements pour la version 5.0 ##

* Ajout du support pour les emojis.
* Améliorations du dialogue Insérer une frimousse avec un champ pour filtrer
  et des boutons radio pour choisir les frimousses affichées.
* En utilisant le dialogue GuiHelper pour le dialogue Paramètres
  d'activation et le dialogue Insérer une frimousse : nécessite NVDA 2016.4
  ou versions supérieures

## Changements pour la version 4.0 ##

* Si le dialogue Insérer une frimousse est ouvert lorsqu'un autre dialogue
  de paramètres est actif, NVDA affichera le message d'erreur correspondant.


## Changements pour la version 3.0 ##

* Dans le dialogue Personnaliser les frimousses, il est maintenant possible
  de spécifier qu'un modèle doit correspondre uniquement si c'est un mot
  entier, selon les dictionnaires de paroles de NVDA 2014.4.


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

[3]:
https://github.com/nvdaes/emoticons/releases/download/6.5/emoticons-6.5.nvda-addon
