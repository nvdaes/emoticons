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

Appuyer sur NVDA+I, ou à partir du menu Outils ->Insérer une frimousse, pour ouvrir un dialogue avec les frimousses ou emoji fournis.

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

## Dictionnaire des frimousses ##

Le module complémentaire emoticons permet d'avoir différents dictionnaires
de parole en utilisant des profils de configuration.

Cela signifie que vous pouvez créer ou modifier un dictionnaire de parole
spécifique pour chaque profil personnalisé.

À partir du Menu NVDA, Préférences -> Dictionnaires de prononciation -> Dictionnaire des frimousses, vous pouvez ouvrir un dialogue pour ajouter ou modifier les frimousses disponibles.

En sauvegardant vos personnalisations, les nouveaux paramètres de lecture
des frimousses ne s'appliqueront qu'au profil que vous êtes en train
d'éditer.

Par exemple, vous pouvez souhaiter que NVDA ne annonce des  frimousses
personnalisées que dans le programme XxChat, mais pas dans les autres
programmes de conversation: vous pouvez créer un profil pour l'application
XxChat et lui attribuer un dictionnaire de parole à partir du menu
Dictionnaires de prononciation, option du Dictionnaires  des
frimousses. Voir ci-dessous pour les Paramètres des Frimousses par rapport
aux profils de configuration.

Vous pouvez également exporter chaque dictionnaire de parole personnalisé en
appuyant sur le bouton "Enregistrer et exporter le dictionnaire": de cette
façon, vos dictionnaires de parole  seront enregistrés dans votre dossier de
configuration utilisateur, sous-dossier speechDicts/emoticons.

Le nom exact et l'emplacement du fichier de dictionnaire seront basés sur le
profil de configuration d'édition, qui sera affiché dans le titre du
dialogue Dictionnaire des frimousses.

## Paramètres des Frimousses ##

À partir du menu Préférences -> Paramètres -> Frimousses ouvre un panneau pour configurer l'activation de vos dictionnaires de parole pour chaque profil.

Dans le panneau  Paramètres des Frimousses, vous pouvez choisir si le dictionnaire de parole doit ou non être activé automatiquement lorsque NVDA bascule sur le profil que vous êtes en train d'éditer. Par défaut, il est désactivé dans la configuration normale de NVDA et dans tous vos nouveaux profils.

Si vous souhaitez garder propres vos dossiers de configuration, vous pouvez
également choisir dans ce dialogue si les dictionnaires non utilisés
(associés à des profils non existants) seront supprimés du module
complémentaire lorsqu'il est déchargé.

Also, it's possible to enable Settings only in normal configuration (not
recommended). This is intended to disable settings changes in case of speed
issues when switching profiles.

## Raccourcis clavier : ##

Voici les raccourcis clavier par défaut, vous pouvez les modifier ou ajouter
un nouveau raccourci pour ouvrir le panneau Paramètres des Frimousses ou le
dialogue Dictionnaire des frimousses :

* NVDA+E : en activant/désactivant l'annonce des frimousses, permet de
  basculer entre la lecture du texte comme il est écrit, ou avec les
  frimousses remplacées par leur description humaine.
* NVDA+I : affiche un dialogue pour choisir la frimousse que vous souhaitez
  copier.



## Changes for 8.0 ##

* Compatible with NVDA 2018.3 or later (required).

## Changements pour la version 7.0 ##

* Le dialogue Paramètres d'activation a été déplacée vers un panneau dans
  les Paramètres NVDA, de sorte que le profil actuel s'affiche dans le titre
  du dialogue des Paramètres NVDA.
* Le menu Gérer les frimousses a été supprimé: maintenant, pour Insérer une
  frimousse se trouve dans le menu Outils et pour Personnaliser les
  frimousses s'affichent sous le Dictionnaires de prononciation comme le
  Dictionnaire des frimousses.
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
