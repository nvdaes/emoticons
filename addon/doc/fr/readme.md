# Emoticons #

* Auteurs : Chris Leo, Noelia Ruiz Martínez, Mesar Hameed, Francisco Javier
  Estrada Martínez

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

Appuyer sur NVDA+I, ou à partir du menu Outils -> Émoticônes > Insérer une émoticône, pour ouvrir un dialogue avec les émoticônes et emoji fournis.

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

## Insérer un symbole ##

Ce dialogue vous permet de choisir l'un des symboles disponibles dans le
dialogue Prononciation des ponctuations et symboles de NVDA. Vous pouvez
utiliser la zone d'édition  Filtrer ou les touches fléchées pour
sélectionner un élément dans la liste des symboles.

Si vous souhaitez copier divers symboles, utilisez le bouton Ajouter pour
les ajouter à la suite des symboles à être copier dans la zone d'édition.

Ensuite, appuyez sur OK et l'emoji ou le symbole sélectionné, ou les
symboles contenus dans la zone d'édition mentionnée, seront copiés dans
votre presse-papiers, prêts à être collés.

## Associer des gestes aux symboles ##

À partir du menu NVDA, Préférences sous-menu, dialogue Gestes de commandes,
catégorie Insert symbols,vous pouvez configurer NVDA pour taper des symboles
via des gestes associés.

Vous pouvez utiliser  un champ d'édition pour réduire le nombre de symboles
présentés, afin que cette catégorie puisse être développé plus rapidement.

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
appuyant sur le bouton "Sauvegarder et exporter le dictionnaire": de cette
façon, vos dictionnaires de parole  seront Sauvegardés dans votre dossier de
configuration utilisateur, sous-dossier speechDicts/emoticons.

Le nom exact et l'emplacement du fichier de dictionnaire seront basés sur le
profil de configuration d'édition, qui sera affiché dans le titre du
dialogue Dictionnaire des émoticônes.

## Paramètres des émoticônes ##

À partir du menu Préférences -> Paramètres -> Émoticônes ouvre un panneau pour configurer l'activation de vos dictionnaires de parole pour chaque profil.

Dans le panneau Paramètres des émoticônes, vous pouvez choisir si le dictionnaire de parole doit ou non être activé automatiquement lorsque NVDA bascule sur le profil que vous êtes en train d'éditer. Par défaut, il est désactivé dans la configuration normale de NVDA et dans tous vos nouveaux profils.

De plus, il est possible de déterminer si les emojis de cette extension
doivent être verbalisés. Cela pourrait être utile pour préserver les
symboles verbaliser si des emojis sont inclus dans la configuration de NVDA.

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
* Non assigné: affiche un dialogue pour choisir le symbole de NVDA  que vous
  souhaitez copier.
* Non assigné: ouvre un message navigable affichant le symbole où le curseur
  de revue est positionné , de sorte que toute la description puisse être
  révisé en Mode navigation.
* Non assigné: ouvre un message navigable affichant le symbole où le curseur
  est positionné , de sorte que toute la description puisse être révisé en
  Mode navigation.

Note : Sous Windows 10 et supérieure, il est également possible d’utiliser
le panneau emoji intégré.

## Changements pour la version 17.0 ##

* Ajout de la capacité d'associer des gestes pour taper des symboles.
* Ajout de la capacité de copier divers symboles en même temps.

## Changements pour la version 16.0 ##

* Compatible avec NVDA 2023.1.

## Changements pour la version 15.0 ##

* Nécessite NVDA 2022.1 ou ultérieur.
* Ne peut pas être utilisé en mode sécurisé.

## Changements pour la version 14.0 ##

* Compatible avec NVDA 2021.1.

## Changements pour la version 13.0 ##

* Erreurs corrigées dans le dialogue Insérer une frimousse.
* Ajout d'un dialogue pour insérer un symbole disponible dans le dialogue
  Prononciation des ponctuations et symboles de NVDA.

## Changements pour la version 12.0 ##

* Nécessite NVDA 2019.3 ou ultérieur.

## Changements pour la version 11.0 ##

* Lorsque l'extension est mise à jour, les dictionnaires sauvegardés dans la
  version précédente de l'extension seront automatiquement copiés dans la
  nouvelle version, sauf si vous préférez importer des dictionnaires
  sauvegardés dans le dossier principal des dictionnaires de NVDA.
* Lors de l'affichage le symbole où le curseur de revue ou le curseur sont
  positionnés, les mots Caractère et Remplacement sont utilisés pour
  distinguer le symbole lui-même et sa description dans le Mode navigation,
  utiles pour les utilisateurs de la parole.

## Changements pour la version 10.0 ##

* Ajout de commandes pour afficher le symbole où le curseur de revue ou le
  curseur sont positionnés. Les gestes de ces commandes peuvent être
  assignés à partir du dialogue Gestes de commandes, de la catégorie  Revue
  de texte.

## Changements pour la version 9.0 ##

* Ajout de la possibilité de choisir si des emojis  de l'extension doivent
  être verbalisés.
* Codage approprié pour les noms de dictionnaire utilisés lors de la
  correction des erreurs lorsqu'ils contiennent certains caractères.
* La traduction du summary de l'extensions est correctement utilisé pour le
  titre présenté dans l'aide de l'extension, accessible à partir du
  Gestionnaire d'Extensions.
* Ajout d'une note mentionnant le panneau Emoji disponible sur Windows 10.

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
  les modifications en rechargeant les extensions (en appuyant sur
  contrôle+NVDA+f3).
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

[3]: https://www.nvaccess.org/addonStore/legacy?file=emo-o
