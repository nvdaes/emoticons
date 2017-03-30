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

Appuyer sur NVDA+I, ou à partir du menu Préférences -> Gérer les frimousses -> Insérer une frimousse, pour ouvrir un dialogue avec les frimousses ou emoji fournis.

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

## Personnaliser les frimousses ##

À partir du Menu NVDA, Préférences -> Gérer les frimousses -> Personnaliser les frimousses, vous pouvez ouvrir un dialogue paramètre pour ajouter ou modifier les frimousses disponibles.

Ce dialogue vous permet d'enregistrer un dictionnaire de parole avec vos
frimousses personnalisées.

En appuyant sur le bouton "Enregistrer et exporter le dictionnaire" un
fichier de dictionnaire nommé emoticons.dic sera enregistré dans votre
dossier de configuration utilisateur, sous-dossier speechDicts.

## Paramètres d'activation ##

À partir du menu Préférences -> Gérer les frimousses -> Paramètres d'activation Vous pouvez choisir d'activer ou non l'annonce des frimousses lors du démarrage de NVDA. Par défaut, elle est désactivée.

Il est également possible d'enregistrer votre choix pour ce paramètre.

## Raccourcis clavier : ##

Voici les raccourcis clavier par défaut, vous pouvez les modifier ou ajouter
un nouveau raccourci pour ouvrir le dialogue Paramètres d'activation ou le
dialogue Dictionnaire des frimousses :

* NVDA+E : en activant/désactivant la diffusion des frimousses, permet de
  basculer entre la lecture du texte comme il est écrit, ou avec les
  frimousses remplacées par leur description humaine.
* NVDA+I : affiche un dialogue pour choisir la frimousse que vous souhaitez
  copier.


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
