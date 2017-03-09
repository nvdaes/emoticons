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

Cuando no estés seguro de los caracteres para un emoticono en particular,
este complemento te capacita para seleccionarlos e insertarlos en tu texto
tal como en un chat.

Pulsa NVDA+I, o desde el menú Preferencias -> Gestionar emoticonos -> Insertar emoticono, para abrir un diálogo con los emoticonos o emojis proporcionados.

Este diálogo te permite elegir un emoticono y ver los emoticonos que te
interesen:

*	Un campo editable que te permite filtrar la búsqueda del emoticono deseado
  de entre los emoticonos disponibles.
*	A través de un grupo de botones de opción, puedes elegir ver sólo la categoría emoji (alt+E) o ver sólo la categoría de emoticonos estándar (alt+s) o ver todos los emoticonos disponibles (alt+A).
*	En la lista de emoticonos (alt+L) se muestran en tres columnas respectivamente: los nombres de emoticono, el tipo de emoticono (emoticono estándar o emoji), el carácter correspondiente.

Cuando pulses Aceptar, los caracteres para el emoticono elegido se copiarán
en tu portapapeles, listos para pegarse.

## Personalizar emoticonos ##

Desde el menú NVDA, Preferencias -> Gestionar emoticonos -> Personalizar emoticonos, puedes abrir un diálogo para añadir o para editar los emoticonos disponibles.

Este diálogo te permite guardar un diccionario de habla de emoticonos con
tus personalizaciones.

Pulsando el botón "Guardar y exportar diccionario", se guardará un fichero
de diccionario llamado emoticons.dic  en tu carpeta de configuración de
usuario, subcarpeta speechDicts.

## Opciones de activación ##

Desde el menú Preferencias -> Gestionar Emoticonos -> Opciones de Activación, puedes elegir activar la verbalización de emoticonos cuando arranque NVDA. de manera predeterminada está desactivado.
También es posible guardar la elección de esta opción.

## Órdenes de teclado: ##

Estas son las teclas de órdenes disponibles por omisión, puedes editarlas o
añadir teclas nuevas para abrir el diálogo Opciones de Activación o el
diálogo Diccionario de Emoticonos:

* NVDA+E: conmuta entre verbalizar texto tal Como está escrito:, o con los
  emoticonos reemplazados por la descripción humana.
* NVDA+I: muestra un cuadro de diálogo para seleccionar un emoticono que
  quieras pegar.


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
