# Emoticons #

* Authors: Chris Leo, Noelia Ruiz Martínez, Mesar Hameed, Francisco Javier
  Estrada Martínez

Ao usar este extra, o texto do emoticon que contenha caracteres será
substituído por uma descrição mais humana e amigável.

Por exemplo: a seqüência ":)" será falada como "smiley sorridente", ou, por
exemplo, o NVDA reconhecerá o significado de cada emoji.

Neste extra, pode aproveitar os seguintes recursos:

## Inserir Emoticon ##

Sometimes an image is worth a 1000 words: use the new emoji to liven up your
instant message and to let your friends know how you’re feeling.

Quando não tiver a certeza dos caracteres para um determinado smiley, este
extra permite-lhe seleccioná-lo e inseri-lo no seu texto, como numa
conversa.

Pressione NVDA+I, ou no menu Ferramentas -> Emoticons > Inserir emoticon, para abrir um diálogo com os emoticons ou emoji fornecidos.

Esta caixa de diálogo permite-lhe escolher um emoticon e ver os emoticons
que o interessam:

*	Um campo de edição permite-lhe filtrar a busca do emoticon desejado entre
  os emoticons disponíveis.
*	Através de um conjunto de botões de rádio, pode optar por ver apenas a
  categoria emoji (alt + E) ou visualizar apenas a categoria padrão de
  emoticon (alt + s) ou visualizar todos os emoticons disponíveis (alt + A).
*	Na lista de emoticons (alt + L) cada Emoticom é mostrado em três colunas
  respectivamente: o nome do emoticon, o tipo de emoticon (emoticon padrão
  ou emoji) e o conjunto de caracteres que o representam.

Quando pressiona OK, os caracteres do emoticon escolhido serão copiados para
a área de transferência, ficando prontos para colar na sua conversa.

## Inserir símbolo ##

This dialog allows you to choose one of the symbols available in the
Punctuation/symbol pronunciation dialog of NVDA. You can use the Filter edit
box or the arrow keys to select an item from the symbols list.

If you want to copy various symbols, use the Add button to append them to
the Symbols to copy edit box.

Then, press OK and the selected emoji or symbol, or the symbols contained in
the mentioned edit box, will be copied to your clipboard, ready for pasting.

## Associate gestures to symbols ##

From NVDA's menu, Preferences submenu, Input gestures dialog, category
Insert symbols, you can configure NVDA to type symbols through associated
gestures.

You can use the Edit field edit box to reduce the number of symbols
presented, so that this category can be expanded faster.

## Dicionário de emoticons ##

Este extra permite-lhe ter diferentes dicionários de descrição de Emoticons,
para usar com diferentes perfis.

Isto significa que pode criar ou editar um dicionário de descrição
específico para cada perfil personalizado.

A partir do menu do NVDA, Preferências -> dicionários de fala -> dicionário de emoticons, pode abrir uma caixa de diálogo para adicionar ou editar emoticons disponíveis.

Guardar as suas personalizações, as novas configurações de leitura dos
emoticons só se aplicam ao perfil que está a editar no momento.

Por exemplo, pode desejar que o NVDA fale os emoticons personalizados apenas
no programa XxChat, mas não em outros programas de chat: pode fazer isso
criando um perfil para o aplicativo XxChat e atribuindo-lhe um dicionário no
menu Personalizar Emoticons. Veja abaixo a configuração de activação em
relação aos perfis de configuração.

Neste extra, também pode exportar cada dicionário personalizado pressionando
o botão "Guardar e exportar dicionário": desta forma, os seus dicionários
serão salvos na sua pasta de configuração do utilizador, subpasta
speechDicts / emoticons.

O nome exacto e a localização do ficheiro de dicionário serão baseados no
perfil de configuração de edição, que será mostrado no título da caixa de
diálogo do dicionário de Emoticons.

## Configurações de emoticons ##

A partir do menu de Preferências -> Gerenciar Emoticons -> Configurações de activação abra uma caixa de diálogo para configurar a activação dos seus dicionários de voz para cada perfil.

No painel de configurações do extra, pode escolher se o dicionário de descrição deve ou não ser activado automaticamente quando o NVDA muda para o perfil que está a editar no momento. Por padrão, está desactivado na configuração normal do NVDA e em todos os seus novos perfis.

Além disso, é possível determinar se os emojis complementares devem ser
falados. Isto pode ser útil para preservar os símbolos falados, se os emojis
estiverem incluídos na configuração do NVDA.

Se quiser manter limpas as suas pastas de configuração, nesta caixa de
diálogo também é possível escolher se os dicionários não utilizados
(associados a perfis não existentes) serão removidos do extra quando
estiverem descarregados.

## Teclas de Comando: ##

Estas são as teclas de comando disponíveis por padrão, pode editá-las ou
adicionar uma nova tecla para abrir o painel de configurações do extra ou o
diálogo do dicionário do Emoticon:

* NVDA + E: falar emoticons on / off, alterna entre o texto falar como está
  escrito, ou com os emoticons substituídos pela descrição humana.
* NVDA + I: mostra uma caixa de diálogo para seleccionar um emoticon que
  deseja copiar.
* Não atribuído: mostra um diálogo para seleccionar um símbolo do NVDA que
  deseja copiar.
* Não atribuído: abre uma mensagem navegável mostrando o símbolo onde o
  cursor de revisão está posicionado, para que toda a descrição possa ser
  revisada no modo de navegação.
* Não atribuído: abre uma mensagem navegável mostrando o símbolo onde o
  cursor está posicionado, para que toda a descrição possa ser revisada no
  modo de navegação.

Note: On Windows 10 and higher, it's also possible to use the built-in emoji
panel.

## Changes for 33.0.0

* Fixed bug in Save and export dictionaries.
* Added copy and close buttons to messages presented in browse mode.

## Changes for 22.0.0 ##

* Requires NVDA 2023.2 or later.

## Changes for 17.0 ##

* Added ability to associate gestures to type symbols.
* Added ability to copy various symbols at the same time.

## Changes for 16.0 ##

* Compatible with NVDA 2023.1.

## Changes for 15.0 ##

* Requires NVDA 2022.1 or later.
* Cannot be used in secure mode.

## Alterações para 14.0 ##

* Compatível com a NVDA 2021.1.

## Alterações para 13.0 ##

* Erros corrigidos no diálogo Inserir Emoticon.
* Adicionado um diálogo para inserir um símbolo disponível na Pronúncia de
  Pontuação/Símbolo do NVDA.

## Alterações para 12.0 ##

* Requer o NVDA 2019.3 ou posterior.

## Alterações para 11.0 ##

* Quando o extra é actualizado, os dicionários guardados na versão anterior
  do extra serão automaticamente copiados para a nova versão, a menos que
  prefira importar dicionários guardados na pasta principal de dicionários
  do NVDA.
* Ao mostrar o símbolo onde o cursor ou o cursor de revisão estão
  posicionados, as palavras Caracter e Substituição são usadas para
  distinguir entre o próprio símbolo e a sua descrição no modo de navegação,
  útil para os utilizadores de voz.

## Alterações para 10.0 ##

* Adicionados comandos para mostrar o símbolo onde o cursor de revisão ou o
  cursor estão posicionados. Teclas para esses comandos podem ser atribuídas
  a partir da caixa de diálogo definir comandos, na categoria Revisão de
  texto.

## Alterações para 9.0 ##

* Adicionada a possibilidade de escolher se os emojis do extra devem ser
  falados.
* Usada a codificação apropriada para nomes de dicionários, corrigindo erros
  quando eles contêm certos caracteres.
* O resumo traduzido do extra é, agora,  usado correctamente para o título
  apresentado na ajuda do extra, acessível a partir do gestor de extras.
* Adicionada uma nota mencionando o painel de emojis disponível no Windows
  10.

## Alterações para 8.0 ##

* Compatível com o NVDA 2018.3 ou posterior

## Alterações para 7.0 ##

* A caixa de diálogo Configurações de ativação foi movida para um painel nas
  configurações do NVDA, para que o perfil actual seja mostrado no título da
  caixa de diálogo de configurações do NVDA.
* O menu Gerir Emoticons foi removido: agora o extra foi Inserido no menu
  Ferramentas e os Emoticons Personalizados serão exibidos em dicionários de
  fala, como o dicionário de Emoticons.
* Requer o NVDA 2018.2 ou posterior.

## Alterações para 6.0 ##

* Adicionado suporte para perfis de configuração.
* No NVDA 2017.4 ou posterior, as configurações e os dicionários
  personalizados serão alterados automaticamente de acordo com os perfis
  seleccionados. No 2017.3 ou anteriores, pode aplicar alterações
  recarregando plugins (pressionando controle + NVDA + f3).
* Se optar por importar configurações ao actualizar o extra, os ficheiros
  obsoletos (emoticons.ini e emoticons.dic) serão removidos ou adaptados a
  esta versão.

## Alterações para 5.0 ##

* Adicionado suporte para emojis.
* Melhorias para o diálogo inserir Emoticon com um campo de filtro e botões
  de rádio para escolher os emoticons a mostrar.
* Usar o guiHelper para o diálogo Configurações de Activação e diálogo
  Inserir Emoticon: requer versões do NVDA 2016.4 ou superiores

## Alterações para 4.0 ##

* Se a caixa de diálogo inserir smiley for aberta quando outra caixa de
  diálogo de configurações estiver activa, o NVDA mostrará a mensagem de
  erro correspondente.


## Alterações para 3.0 ##

* Na caixa de diálogo Personalizar emoticons, agora é possível especificar
  que um padrão deve corresponder apenas se for uma palavra inteira, de
  acordo com os dicionários do NVDA 2014.4.


## Mudanças para 2.0 ##

* A ajuda adicional está disponível no Gestor de extras.


## Alterações para 1.1 ##

* O emoticon duplicado foi removido.
* Adicionados alguns smileys.

## Alterações para 1.0 ##

* Versão inicial.

[[!tag dev stable]]
