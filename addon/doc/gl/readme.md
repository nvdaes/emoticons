# Emoticons #

* Authors: Chris Leo, Noelia Ruiz Martínez, Mesar Hameed, Francisco Javier
  Estrada Martínez
* Descargar [versión estable][1]
* Descargar [versión de desenvolvemento][2]

Using this add-on, spoken text containing emoticon characters will be
replaced by its more human friendly description.

For example: the sequence ":)" will be spoken as "smiling smiley", or for
example NVDA will recognize the meaning of each emoji.

Podes aproveitar as seguintes características:

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

## Persoalizar emoticóns ##

From NVDA MENU, Preferences -> Manage emoticons -> Customize emoticons, you can open a dialog setting to add or to edit available emoticons.

This dialog allows you to save an emoticons speech dictionary with your
customizations.

Premendo o botón "Gardar e exportar diccionario", gardarase unn ficheiro de
diccionario chamado emoticons.dic  no teu  cartafol de configuración de
usuario, subcartafol speechDicts.

## Opcións de activación ##

From menu Preferences -> Manage Emoticons -> Activation settings, you can choose whether to Activate speaking of emoticons when starting NVDA. By default it is disabled.
It is also possible to save your choice for this setting.

## Ordes de teclado: ##

These are the key command available by default, you can edit those or add
new key to open Activation settings dialog or Emoticon Dictionary dialog:

* NVDA+E: conmuta entre falar texto como se escrebe, ou cos emoticóns
  reemplazados pola descripción humána.
* NVDA+I: show a dialog to select an emoticon you want to copy.


## Changes for 5.0 ##

* Added support for emojis.
* Improvements for Insert Emoticon dialog with a filter field and radio
  buttons to choose displayed emoticons.
* Using guiHelper for Activation settings dialog and Insert Emoticon dialog:
  requires NVDA 2016.4 or higher versions

## Cambios para 4.0 ##

* Se o diálogo Insertar emoticón  está aberto cando outro diálogo de opcións
  estea activo, NVDA amosará a mensaxe de erro correspondente.


## Cambios para 3.0 ##

* No diálogo Persoalizar emoticóns, agora é posible especificar que un
  patrón só debería compararse se é unha palabra completa, de acordo cos
  diccionarios da fala do NVDA 2014.4.


## Cambios para 2.0 ##

* A axuda do complemento está dispoñible no Administrador de Complementos.


## Cambios para 1.1 ##

* Borrado un emoticón duplicado.
* Engadidos algúns emoticóns.

## Cambios para 1.0 ##

* Versión inicial.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=emo

[2]: http://addons.nvda-project.org/files/get.php?file=emo-dev
