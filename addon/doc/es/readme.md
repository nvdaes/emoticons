# Emoticons #


* Autores: Chris Leo, Noelia Ruiz Martínez, Mesar Hameed, Francisco Javier
  Estrada Martínez
* Descargar [versión estable][1]
* Descargar [versión de desarrollo][2]

Utilizando este complemento, la verbalización de texto que contenga
caracteres emoticonos se reemplazará por su descripción más amigable.

Por ejemplo: la secuencia ":)" se verbalizará como "cara sonriente", o por
ejemplo NVDA reconocerá el significado de cada emoji.

Puedes aprovecharte de las siguientes características:

## Insertar Emoticono ##

A veces una imagen vale más que 1000 palabras: usa el nuevo emoji para
animar tus mensajes instantáneos para que tus amigos sepan cómo te sientes.

Cuando no estés seguro de los caracteres para un emoticono en particular,
este complemento te capacita para seleccionarlos e insertarlos en tu texto
tal como en un chat.

Press NVDA+I, or from menu Tools -> Insert emoticon, to open a dialog with the provided emoticons or emoji.

Este diálogo te permite elegir un emoticono y ver los emoticonos que te
interesen:

*	Un campo editable que te permite filtrar la búsqueda del emoticono deseado
  de entre los emoticonos disponibles.
*	A través de un grupo de botones de opción, puedes elegir ver sólo la
  categoría emoji (alt+E) o ver sólo la categoría de emoticonos estándar
  (alt+s) o ver todos los emoticonos disponibles (alt+A).
*	En la lista de emoticonos (alt+L) se muestran en tres columnas
  respectivamente: los nombres de emoticono, el tipo de emoticono (emoticono
  estándar o emoji), el carácter correspondiente.

Cuando pulses Aceptar, los caracteres para el emoticono elegido se copiarán
en tu portapapeles, listos para pegarse.

## Emoticons dictionary ##

El complemento emoticons permite tener diferentes diccionarios de habla
usando los perfiles de configuración.

Esto significa que puedes crear o editar un diccionario de habla específico
para cada uno de tus perfiles personalizados.

From NVDA MENU, Preferences -> Speech dictionaries -> Emoticons dictionary, you can open a dialog to add or to edit available emoticons.

Al guardar tus personalizaciones, la nueva configuración de lectura de
emoticonos solo se aplicará al perfil que estás editando actualmente.

For example, you may wish that NVDA spoken custom emoticons only in XxChat
program, but not in other chat programs: you can do this by creating a
profile for the XxChat application and assign to it a speech dictionary from
Speech dictionaries menu, Emoticons dictionary option. See below for
Emoticons settings in relation to the configuration profiles.

También puedes exportar cada diccionario de habla personalizado pulsando el
botón "Guardar y exportar diccionario": de esta manera tus diccionarios de
habla se guardarán en tu carpeta de configuración de usuario, subcarpeta
speechDicts/emoticons.

El nombre exacto y la ubicación del archivo de diccionario se basarán en el
perfil de configuración de edición, que se mostrará en el título del diálogo
del Diccionario de Emoticonos.

## Emoticons settings ##

From menu Preferences -> Settings -> Emoticons opens a panel to configure the activation of your speech-dictionaries for each profile.

In Emoticons settings panel you can choose whether or not speech-dictionary should automatically activate when  NVDA switches to the   profile you are currently editing. By default it is disabled in normal configuration of NVDA and in all your new profiles.

Si deseas mantener limpias tus carpetas de configuración, en este diálogo
también es posible elegir si los diccionarios no utilizados (asociados a
perfiles no existentes) se eliminarán del complemento cuando se descarguen.

## Órdenes de teclado: ##

These are the key commands available by default, you can edit those or add
new key to open Emoticons settings panel or Emoticon Dictionary dialog:

* NVDA+E: activando/desactivando la verbalización de los emoticonos, conmuta
  entre verbalizar texto tal Como está escrito:, o con los emoticonos
  reemplazados por la descripción humana.
* NVDA+I: muestra un cuadro de diálogo para seleccionar un emoticono que
  quieras pegar.


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

* Añadido el soporte para los perfiles de configuración.
* En NVDA 2017.4 o superiores, las opciones de configuración y los
  diccionarios personalizados cambiarán automáticamente de acuerdo con los
  perfiles seleccionados. En 2017.3 o anterior, puedes aplicar los cambios
  recargando los complementos (pulsando control+NVDA+f3).
* Si eliges importar las configuraciones al actualizar el complemento, los
  archivos obsoletos (emoticons.ini y emoticons.dic) se eliminarán o
  adaptarán a esta versión.

## Cambios para 5.0 ##

* Añadido el soporte para emojis.
* Mejoras para el diálogo Insertar Emoticones con un campo de filtro y
  botones de opción para elegir los emoticonos mostrados.
* Utilización de guiHelper para el diálogo Opciones de Activación y el
  diálogo Insertar Emoticono: requiere de versiones de NVDA 2016.4 o
  superiores

## Cambios para 4.0 ##

* Si el diálogo Insertar emoticono está abierto cuando esté activo otro
  diálogo de opciones, NVDA mostrará el mensaje de error correspondiente.


## Cambios para 3.0 ##

* En el diálogo Personalizar emoticonos, ahora es posible especificar que un
  patrón sólo debería compararse si es una palabra completa, de acuerdo con
  los diccionarios del habla de NVDA 2014.4.


## Cambios para 2.0 ##

* La ayuda del complemento está disponible en el Administrador de
  Complementos.


## Cambios para 1.1 ##

* Eliminado un emoticono duplicado.
* Añadidos algunos emoticonos.

## Cambios para 1.0 ##

* Versión inicial.




[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=emo

[2]: http://addons.nvda-project.org/files/get.php?file=emo-dev

[3]:
https://github.com/nvdaes/emoticons/releases/download/6.5/emoticons-6.5.nvda-addon
