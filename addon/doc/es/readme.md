# Emoticons #
* Autores: Chris Leo, Noelia Ruiz Martínez, Mesar Hameed, Francisco Javier
  Estrada Martínez
* Compatibilidad con NVDA: 2019.3 o posterior
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

Pulsa NVDA+I, o desde el menú Herramientas -> Emoticonos -> Insertar emoticono, para abrir un diálogo con los emoticonos o emojis proporcionados.

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

## Insertar símbolo ##

Este diálogo permite elegir uno de los símbolos disponibles en el diálogo de
pronunciación y símbolos de NVDA. Puedes utilizar el cuadro de edición de
filtro o las flechas para seleccionar un elemento de la lista de símbolos. A
continuación, pulsa Aceptar y se copiará al portapapeles el emoji o símbolo
seleccionado, listo para pegar.

## Diccionario de emoticonos ##

El complemento emoticons permite tener diferentes diccionarios de habla
usando los perfiles de configuración.

Esto significa que puedes crear o editar un diccionario de habla específico
para cada uno de tus perfiles personalizados.

Desde el menú NVDA, Preferencias -> Diccionarios del Habla -> Diccionario de emoticonos, puedes abrir un diálogo para añadir o para editar los emoticonos disponibles.

Al guardar tus personalizaciones, la nueva configuración de lectura de
emoticonos solo se aplicará al perfil que estás editando actualmente.

Por ejemplo, puedes desear que NVDA anuncie los emoticonos personalizados
solo en el programa XxChat, pero no en otros programas de chat: puedes
hacerlo creando un perfil para la aplicación XxChat y asignándole un
diccionario de habla desde el menú Diccionarios del Habla, opción
Diccionario de Emoticonos. Consulta a continuación las Opciones de
activación en relación con los perfiles de configuración.

También puedes exportar cada diccionario de habla personalizado pulsando el
botón "Guardar y exportar diccionario": de esta manera tus diccionarios de
habla se guardarán en tu carpeta de configuración de usuario, subcarpeta
speechDicts/emoticons.

El nombre exacto y la ubicación del archivo de diccionario se basarán en el
perfil de configuración de edición, que se mostrará en el título del diálogo
del Diccionario de Emoticonos.

## Opciones de emoticonos ##

Desde el menú Preferencias -> Opciones -> Emoticonos abre un diálogo para configurar la activación de tus diccionarios de habla para cada perfil.

En el panel Opciones de Emoticonos puedes elegir si el diccionario de habla se activará o no automáticamente cuando NVDA conmute al perfil que estás editando actualmente. de manera predeterminada está desactivado en la configuración normal de NVDA y en todos tus nuevos perfiles.

Aún más, es posible determinar si los emojis del complemento deberían
hablarse. Esto podría ser útil para preservar el habla de símbolos si los
emojis se incluyen en la configuración de NVDA.

Si deseas mantener limpias tus carpetas de configuración, en este diálogo
también es posible elegir si los diccionarios no utilizados (asociados a
perfiles no existentes) se eliminarán del complemento cuando se descarguen.

## Órdenes de teclado: ##

Estas son las teclas de órdenes disponibles por omisión, puedes editarlas o
añadir teclas nuevas para abrir el panel Opciones de Emoticonos o el diálogo
Diccionario de Emoticonos:

* NVDA+E: activando/desactivando la verbalización de los emoticonos, conmuta
  entre verbalizar texto tal Como está escrito:, o con los emoticonos
  reemplazados por la descripción humana.
* NVDA+I: muestra un cuadro de diálogo para seleccionar un emoticono que
  quieras pegar.
* Sin asignar: muestra un diálogo para seleccionar y copiar un símbolo de
  NVDA.
* Sin asignar: Abrir un mensaje navegable mostrando el símbolo donde el
  cursor de revisión está posicionado, de forma que se pueda revisar la
  descripción completa en modo exploración.
* Sin asignar: Abrir un mensaje navegable mostrando el símbolo donde el
  cursor está posicionado, de forma que se pueda revisar la descripción
  completa en modo exploración.

Nota: en Windows 10, también es posible usar el panel de emojis incorporado.

## Cambios para 13.0 ##

* Corregidos errores en el diálogo Insertar emoticono.
* Añadido un diálogo para insertar un símbolo disponible en la pronunciación
  de puntuación y símbolos de NVDA.

## Cambios para 12.0 ##

* Se requiere NVDA 2019.3 o posterior.

## Cambios para 11.0 ##

* Cuando se actualiza el complemento, los diccionarios guardados de la
  versión anterior se copiarán a la nueva versión, a menos que prefieras
  importar los diccionarios guardados en la carpeta principal de
  diccionarios de NVDA.
* Al mostrar el símbolo en el que se encuentran situados el cursor del
  sistema o el cursor de revisión, las palabras carácter y reemplazo se usan
  para distinguir el propio símbolo de su descripción en el modo
  exploración, útil para usuarios de voz.

## Cambios para 10.0 ##

* Añadido comando para mostrar el símbolo donde el cursor de revisión o del
  sistema están posicionados. Se pueden asignar gestos a estos comandos
  desde el diálogo Gestos de entrada, categoría Revisión de texto.

## Cambios para 9.0 ##

* Añadida la posibilidad de elegir si se hablarán los emojis del
  complemento.
* Se usa la codificación apropiada para nombres de diccionario, solucionando
  errores cuando contienen ciertos caracteres.
* El resumen traducido del complemento se usa adecuadamente para el título
  presentado en la ayuda del complemento, accesible desde el administrador
  de complementos.
* Añadida una nota mencionando el panel de emoji disponible en Windows 10.

## Cambios para 8.0 ##

* Compatible con NVDA 2018.3 o posterior (requerido).

## Cambios para 7.0 ##

* El diálogo Opciones de activación se ha movido a un panel en las opciones
  de NVDA, tal que el perfil actual se mostrará en el título del diálogo
  Opciones de NVDA.
* Se ha eliminado el menú Gestionar emoticonos: Ahora Insertar emoticón se
  encontrará en el menú Herramientas, y Personalizar Emoticonos se mostrará
  en Diccionarios del Habla como Diccionario de emoticonos.
* Se requiere NVDA 2018.2 o posterior.
* Si fuese necesario, puedes descargar la [última versión compatible con
  NVDA 2017.3][3].

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

[1]: https://addons.nvda-project.org/files/get.php?file=emo

[2]: https://addons.nvda-project.org/files/get.php?file=emo-dev

[3]: https://addons.nvda-project.org/files/get.php?file=emo-o
