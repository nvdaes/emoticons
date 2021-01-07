# Emoticons #
* Autores: Chris Leo, Noelia Ruiz Martínez, Mesar Hameed, Francisco Javier
  Estrada Martínez
* Compatibilidade con NVDA: 2019.3 ou posterior
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

Press NVDA+I, or from menu Tools -> Emoticons > Insert emoticon, to open a dialog with the provided emoticons or emoji.

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

## Insert symbol ##

This dialog allows you to choose one of the symbols available in the
Punctuation/symbol pronunciation dialog of NVDA. You can use the Filter edit
box or the arrow keys to select an item from the symbols list. Then, press
OK and the selected emoji or symbol will be copied to your clipboard, ready
for pasting.

## Diccionario de emoticóns ##

O complemento Emoticons permite ter diferentes diccionarios da fala usando
perfís de configuración.

Esto significa que podes crear ou editar un diccionario da fala específico
para cada perfil personalizado.

Dende o menú NVDA, Preferencias -> Diccionarios da Fala -> Diccionario de Emoticóns, podes abrir un diálogo para engadir ou editar os emoticóns dispoñibles.

Gardando as túas persoalizacións, a nova lectura de configuración dos
emoticóns só se aplicará ao perfil que estés a editar actualmente.

Por exemplo, poderás desexar que o NVDA falara emoticóns persoalizados só no
programa XxChat, pero non noutros programas de chat: podes facer esto
creando un perfil para a aplicación XxChat e asignar a el un diccionario da
fala dende o menú Diccionarios da Fala, Opción Diccionario de
Emoticóns. Consulta abaixo para opcións de activación en relación cos perfís
de configuración.

Tamén podes exportar cada diccionario personalizado da fala premendo o botón
"Gardar e exportar diccionario": deste xeito o teu diccionario da fala
gardarase no teu cartafol de configuración do usuario, subcartafol
speechDicts/emoticons.

O nomme e localización exacta do ficheiro de diccionario basearáse no perfil
de configuración en edición, que se amosará no título do diálogo de
diccionario do Emoticons.

## Opcións de emoticóns ##

Dende o menú Preferencias -> Opciones -> Emoticóns abre un diálogo para configurar a activación do teu diccionario da fala para cada perfil.

No panel Opcións de emoticóns podes escoller se o diccionario da fala deberíasse activar ou non automáticamente cando o NVDA cambia ao perfil que estás a editar actualmente. Por defecto está deshabilitado na configuración normal do NVDA e en todos os novos perfís.

Aínda máis, é posible determinar se se deberían falar os emojis do
complemento. Isto podería ser útil para preservar a fala de símbolos se os
emojis están incluídos na configuración do NVDA.

Se desexases manter limpos os teus cartafois de configuración, neste diálogo
é posible tamén escoller se os dicionarios non usados (asociados con perfís
non existentes) borraranse do complemento cando se descargue.

## Ordes de teclado: ##

Estas son as teclas de ordes dispoñibles por omisión, podes editalas ou
engadir teclas novas para abrir o panel Opcións de Emoticóns ou o diálogo
Diccionario de Emoticóns:

* NVDA+E: activando e desactivando a difusión dos emoticonos, conmuta entre
  falar texto segundo estea escrito, ou cos emoticonos remprazados pola
  descripción humana.
* NVDA+I: amosa un cadro de diálogo para seleccionar un emoticón que queras
  pegar.
* Not assigned: show a dialog to select an NVDA's symbol you want to copy.
* Non asignada: abrir unha mensaxe de modo exploración amosando o símbolo
  onde o cursor de revisión está posicionado, de modo que se poida examinar
  en modo exploración a descrición completa.
* Non asignada: abrir mensaxe de modo exploración amosando o símbolo onde o
  cursor está posicionado, de modo que se poida revisar en modo exploración
  a descrición completa.

Nota: En Windows 10, tamén é posible utilizar o panel de emoji integrado.

## Changes for 13.0 ##

* Fixed errors in Insert Emoticon dialog.
* Added a dialog to insert a symbol available in the Punctuation/symbol
  pronunciation of NVDA.

## Cambios para 12.0 ##

* Require NVDA 2019.3 ou posterior.

## Cambios para 11.0 ##

* Cando o complemento se actualice, os dicionarios gardados na versión
  anterior do complemento copiaranse automaticamente á nova versión, a menos
  que prefiras importar os dicionarios gardados no cartafol principal de
  dicionarios de NVDA.
* Ao amosar o símbolo sobre o que están posicionados o cursor ou o cursor de
  revisión, utilízanse as palabras Carácter e Reemprazo para distinguir
  entre o símbolo en sí e a súa descrición en modo exploración, útil para
  usuarios de fala.

## Cambios para 10.0 ##

* Engadidos atallos para amosar o símbolo onde estea posicionado o cursor de
  revisión ou do sistema. Os xestos para estes atallos pódense asignar dende
  o diálogo Xestos de entrada, categoría Revisión de texto.

## Cambios para 9.0 ##

* Engadida a posibilidad de elixir se se falarán os emojis do omplemento.
* Utilízase a codificación apropiada para nomes de dicionario, arranxando
  errores cando conteñen certos caracteres.
* O resumo do complemento traducido úsase adecuadamente para o título
  presentado na axuda do complemento, accesible dende o administrador de
  complementos.
* Engadida unha nota mencionando que está dispoñible o panel de emoji en
  Windows 10.

## Cambios para 8.0 ##

* Compatible co NVDA 2018.3 ou posterior (requerido).

## Cambios para 7.0 ##

* O diálogo Opcións de activación moveuse a un panel nas opcións do NVDA,
  así que o perfil actual amosarase no título do diálogo Opcións do NVDA.
* Borrouse o menú Xestionar emoticóns: Agora Insertar emoticón atoparase no
  menú Ferramentas e Personalizar Emoticóns amosarase en Diccionarios da
  Fala como Diccionario de emoticóns.
* Requírese do NVDA 2018.2 ou posterior.
* Se fora necesario, podes descargar a [derradeira versión compatible co
  NVDA 2017.3][3].

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

[1]: https://addons.nvda-project.org/files/get.php?file=emo

[2]: https://addons.nvda-project.org/files/get.php?file=emo-dev

[3]: https://addons.nvda-project.org/files/get.php?file=emo-o
