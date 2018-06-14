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

Press NVDA+I, or from menu Tools -> Insert emoticon, to open a dialog with the provided emoticons or emoji.

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

## Emoticons dictionary ##

O complemento Emoticons permite ter diferentes diccionarios da fala usando
perfís de configuración.

Esto significa que podes crear ou editar un diccionario da fala específico
para cada perfil personalizado.

From NVDA MENU, Preferences -> Speech dictionaries -> Emoticons dictionary, you can open a dialog to add or to edit available emoticons.

Gardando as túas persoalizacións, a nova lectura de configuración dos
emoticóns só se aplicará ao perfil que estés a editar actualmente.

For example, you may wish that NVDA spoken custom emoticons only in XxChat
program, but not in other chat programs: you can do this by creating a
profile for the XxChat application and assign to it a speech dictionary from
Speech dictionaries menu, Emoticons dictionary option. See below for
Emoticons settings in relation to the configuration profiles.

Tamén podes exportar cada diccionario personalizado da fala premendo o botón
"Gardar e exportar diccionario": deste xeito o teu diccionario da fala
gardarase no teu cartafol de configuración do usuario, subcartafol
speechDicts/emoticons.

O nomme e localización exacta do ficheiro de diccionario basearáse no perfil
de configuración en edición, que se amosará no título do diálogo de
diccionario do Emoticons.

## Emoticons settings ##

From menu Preferences -> Settings -> Emoticons opens a panel to configure the activation of your speech-dictionaries for each profile.

In Emoticons settings panel you can choose whether or not speech-dictionary should automatically activate when  NVDA switches to the   profile you are currently editing. By default it is disabled in normal configuration of NVDA and in all your new profiles.

Se desexases manter limpos os teus cartafois de configuración, neste diálogo
é posible tamén escoller se os dicionarios non usados (asociados con perfís
non existentes) borraranse do complemento cando se descargue.

## Ordes de teclado: ##

These are the key commands available by default, you can edit those or add
new key to open Emoticons settings panel or Emoticon Dictionary dialog:

* NVDA+E: activando e desactivando a difusión dos emoticonos, conmuta entre
  falar texto segundo estea escrito, ou cos emoticonos remprazados pola
  descripción humana.
* NVDA+I: amosa un cadro de diálogo para seleccionar un emoticón que queras
  pegar.


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

## Cambios para 6.0 ##

* Engadido o soporte para perfís de configuración.
* No NVDA 2017.4 ou posterior, as opción de configuración e os diccionarios
  persoalizados cambiarán automáticamente de acordó cos perfís
  selecionados. No 2017.3 ou anteriores, podes aplicar cambios recargando
  plugins (premendos control+NVDA+f3).
* Se escolles importar opcións cando actualizas o complemento, os ficheiros
  deprecados (emoticons.ini e emoticons.dic) borraranse ou adaptaránse a
  esta versión.

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

[3]:
https://github.com/nvdaes/emoticons/releases/download/6.5/emoticons-6.5.nvda-addon
