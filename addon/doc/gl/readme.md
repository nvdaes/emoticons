# Emoticons #

* Autores: Chris Leo, Noelia Ruiz Martínez, Mesar Hameed, Francisco Javier
  Estrada Martínez
* Descargar [versión estable][1]
* Descargar [versión de desenvolvemento][2]

Ó se utilizar este complemento, o texto falado que conteña carácteres de
emoticón reemprazarase pola súa descripción máis amigable.

Por exemplo: a secuencia ":)" falarase como "cara sorinte", ou por exemplo
NVDA recoñecerá o significado de cada emoji.

Podes aproveitar as seguintes características:

## Insertar Emoticón ##

Ás veces unha imaxen vale máis que 1000 palabras: usa o novo emoji para
animar a túa mensaxe instantánea e para que os teus amigos sepan cómo te
sintes.

Cando non esteas seguro dos caracteres para un emoticón en particular, este
complemento capacítache para selecionalos e insertalos no teu texto como nun
chat.

Preme NVDA+I, ou dende o menú Preferencias -> Xestionar emoticóns -> Insertar emoticón, para abrir un diálogo cos emoticóns ou emojis proporcionados.

Este diálogo permíteche escoller un emoticón e ver os emoticóns que che
interesen:

*	Un campo editable que che permite filtrar a procura do emoticón desexado
  de entre os emoticóns dispoñibles.
*	A través dun grupo de botóns de opción, podes escoller ver só a categoría
  emoji (alt+E) ou ver só a categoría de emoticonos estándar (alt+s) ou ver
  todos os emoticonos dispoñibles (alt+A).
*	Na listaxe de emoticonos (alt+L) amósanse en tres columnas
  respectivamente: os nomes de emoticono, o tipo de emoticono (emoticono
  estándar ou emoji), o carácter correspondente.

Cando premas Aceptar, os caracteres para o emoticón escollido copiaranse no
teu portapapeis, listos para se pegar.

## Persoalizar emoticóns ##

Emoticons add-on allows to have differents speech-dictionaries using
configuration profiles.

This means that you can create or edit a specific speech-dictionary for each
your custom profile.

Dende o menú NVDA, Preferencias -> Xestionar emoticóns -> Persoalizar emoticóns, podes abrir un diálogo para engadir ou editar os emoticóns dispoñibles.

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

## Opcións de activación ##

From menu Preferences -> Manage Emoticons -> Activation-settings opens a dialog to configure the activation of your speech-dictionaries for each profile.

In activation-setting dialog you can choose whether or not speech-dictionary should automatically activate when  NVDA switches to the   profile you are currently editing. By default it is disabled in normal configuration of NVDA and in all your new profiles.

If you may wish to keep clean your configuration folders, in this dialog it
is also possible to choose if dictionaries not used (associated with non
existing profiles) will be removed from the add-on when it is unloaded.

## Ordes de teclado: ##

Estas son as teclas de ordes dispoñibles por omisión, podes editalas ou
engadir teclas novas para abrir o diálogo Opcións de Activación ou o diálogo
Diccionario de Emoticóns:

* NVDA+E: speaking emoticons on/off, toggles between speaking text as it is
  written, or with the emoticons replaced by the human description.
* NVDA+I: amosa un cadro de diálogo para seleccionar un emoticón que queras
  pegar.

## Changes for 6.0 ##

* Added support for configuration profiles.
* In NVDA 2017.4 or later, the configuration settings and custom
  dictionaries will change automatically according with the selected
  profiles. In 2017.3 or earlier, you can apply changes by reloading plugins
  (pressing control+NVDA+f3).
* If you choose to import settings when updating the add-on, deprecated
  files (emoticons.ini and emoticons.dic) will be removed or adapted to this
  version.

## Cambios para 5.0 ##

* Engadido o soporte para emojis.
* Melloras para o diálogo Insertar Emoticón cun campo de filtro e botóns de
  opción para escoller os emoticonos amosados.
* Uso do guiHelper para o diálogo Opcións de Activación e o diálogo Insertar
  Emoticón: require de versións do NVDA 2016.4 ou superiores

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
