# Emoticons #

* Autores: Chris Leo, Noelia Ruiz Martínez, Mesar Hameed, Francisco Javier
  Estrada Martínez

Ao usar este complemento, os textos falados que contenham caracteres de
emoticons serão substituídos por descrições mais amigáveis dos mesmos.

Por exemplo: A seqüência ":)" será falada como "carinha sorridente", ou por
exemplo o NVDA vai reconhecer o significado de cada emoji.

Pode tirar proveito dos seguintes recursos:

## Inserir Emoticon ##

Às vezes uma imagem vale que 1000 palavras: use o novo emoji para animar
suas mensagens instantâneas e fazer seus amigos saberem como você está se
sentindo.

Quando você não tiver certeza dos caracteres para uma carinha em particular,
este complemento lhe possibilita selecionar e inseri-lo no texto, por
exemplo num bate-papo (chat).

Pressione NVDA+I, ou no menu Ferramentas -> Emoticons > Inserir emoticon, para abrir um diálogo com os emoticons ou emojis fornecidos.

Este diálogo possibilita você escolher um emoticon e ver os emoticons que
lhe interessem:

*	Um campo de edição possibilita filtrar a pesquisa do emoticon desejado
  entre os disponíveis.
*	Por meio dum conjunto de botões de opção, pode escolher ver somente a
  categoria emoji (alt+E) ou ver somente a categoria emoticons padrão
  (alt+s) ou ver todos os emoticons disponíveis (alt+A).
*	Na lista (alt+L), os emoticons são mostrados em três colunas, a saber:
  Nome do emoticon, tipo (emoticon padrão ou emoji) e o caractere
  correspondente.

Ao pressionar OK, os caracteres do emoticon escolhido serão copiados para a
área de transferência, prontos para colar.

## Inserir símbolo ##

Esta caixa de diálogo permite que você escolha um dos símbolos disponíveis
no diálogo Pronúncia de pontuação/símbolos do NVDA. Pode usar a caixa de
edição Filtro ou as teclas de setas para selecionar um item da lista de
símbolos. Em seguida, pressione OK e o emoji ou símbolo selecionado será
copiado para sua área de transferência, pronto para colar.

Se você quiser copiar vários símbolos, use o botão Adicionar para anexá-los
à caixa de edição Símbolos a serem copiados.

Em seguida, pressione OK e o emoji ou símbolo selecionado, ou os símbolos
contidos na caixa de edição mencionada, serão copiados para a área de
transferência, prontos para serem colados.

## Associar gestos a símbolos ##

No menu do NVDA, submenu Preferências, caixa de diálogo Gestos de entrada,
categoria Inserir símbolos, você pode configurar o NVDA para digitar
símbolos por meio de gestos associados.

Você pode usar a caixa de edição Editar campo para reduzir o número de
símbolos apresentados, de modo que essa categoria possa ser expandida mais
rapidamente.

## Dicionário de emoticons ##

O Complemento Emoticons permite ter diferentes dicionários de fala usando
perfis de configuração.

Isso significa que você pode criar ou editar um dicionário de fala
específico para cada perfil personalizado.

No MENU DO NVDA, em Preferências -> Dicionários -> Dicionário de Emoticons, pode abrir um diálogo de opções para adicionar ou editar os emoticons disponíveis.

Salvando suas personalizações, as novas configurações de leitura de
emoticons só se aplicam ao perfil que você está editando no momento.

Por exemplo, você pode desejar que o NVDA fale emoticons personalizados
apenas no programa XxBate-papo, mas não em outros programas de bate-papo:
você pode criar um perfil para o aplicativo XxBate-papo e atribuir um
dicionário de fala no menu Dicionários, opção de Dicionário de
Emoticons. Veja abaixo as configurações dos Emoticons em relação aos perfis
de configuração.

Você também pode exportar cada dicionário de fala personalizado pressionando
o botão "Salvar e exportar dicionário": dessa forma, seus dicionários de
fala serão salvos em sua pasta de configuração do usuário, subpasta
speechDicts/emoticons.

O nome e a localização exatos do arquivo de dicionário serão baseados no
perfil de configuração em edição, que será mostrado no título do diálogo do
dicionário de Emoticons.

## Configurações de emoticons ##

No menu Preferências -> Configurações -> Emoticons abre um painel para configurar a ativação de seus dicionários de fala para cada perfil.

No painel de configurações de Emoticons, você pode escolher se o dicionário de fala deve ou não ser ativado automaticamente quando o NVDA alterna para o perfil que você está editando no momento. Por padrão está desabilitado na configuração normal do NVDA e em todos os seus novos perfis.

Outrossim, pode-se determinar se os emojis do complemento devem ser
falados. Isso pode ser útil para preservar símbolos de serem falados caso os
emojis estejam inclusos na configuração do NVDA.

If symbols inserted using associated gestures aren't spoken in your system,
even when NVDA is configured to speak typed characters, you can try to
enable a checkbox to ensure the speaking of inserted symbols.


Se você desejar manter limpas suas pastas de configuração, nesta caixa de
diálogo também é possível escolher se os dicionários não utilizados
(associados a perfis não existentes) serão removidos do complemento quando
ele for descarregado.

## Teclas de Comando: ##

Estes são os comandos de teclas disponíveis por padrão, você pode editá-los
ou adicionar uma nova tecla para abrir o painel de configurações de
Emoticons ou o diálogo Dicionário de Emoticons:

* NVDA+E: Liga/desliga a fala de emoticons, alterna entre falar o texto como
  está escrito ou com os emoticons substituídos por descrições amigáveis.
* NVDA+I: mostra um diálogo para selecionar um emoticon que queira copiar.
* Não atribuído: mostra um diálogo para selecionar um símbolo do NVDA que
  queira copiar.
* Não atribuído: Abre uma mensagem navegável mostrando o símbolo onde o
  cursor de exploração está posicionado, de modo que a descrição inteira
  possa ser explorada em modo de navegação.
* Não atribuído: Abre uma mensagem navegável mostrando o símbolo onde o
  cursor está posicionado, de modo que a descrição inteira possa ser
  explorada em modo de navegação.

Nota: No Windows 10, também é possível usar o painel de emojis integrado.

## Changes for 33.0.0

* Fixed bug in Save and export dictionaries.
* Added copy and close buttons to messages presented in browse mode.
* When using commands to insert symbols, they may be spoken according to the
  speak typed characters option.

## Mudanças na 22.0.0 ##

* Requer o NVDA 2023.2 ou posterior.

## Mudanças na 17.0 ##

* Adicionada a capacidade de associar gestos a símbolos de digitação.
* Foi adicionada a capacidade de copiar vários símbolos ao mesmo tempo.

## Mudanças na 16.0 ##

* Compatível com o NVDA 2023.1.

## Mudanças na 15.0 ##

* Requer NVDA 2022.1 ou posterior.
* Não pode ser usado no modo seguro.

## Mudanças na 14.0 ##

* Compatível com o NVDA 2021.1.

## Mudanças na 13.0 ##

* Erros corrigidos no diálogo Inserir Emoticon.
* Adicionado um diálogo para inserir um símbolo disponível na Pronúncia de
  pontuação/símbolos do NVDA.

## Mudanças na 12.0 ##

* Requer NVDA 2019.3 ou posterior.

## Mudanças na 11.0 ##

* Quando o complemento é atualizado, os dicionários salvos na versão
  anterior do complemento serão automaticamente copiados para a nova versão,
  a não ser que você prefira importar dicionários salvos na pasta principal
  de dicionários do NVDA.
* Ao mostrar o símbolo onde o cursor do sistema ou o de exploração está
  posicionado, são usadas as palavras caractere e substituto para distinguir
  entre o próprio símbolo e a descrição dele no modo de navegação, útil para
  usuários de fala.

## Mudanças na 10.0 ##

* Adicionados comandos para mostrar o símbolo onde o cursor de exploração ou
  o do sistema está posicionado. Gestos para esses comandos podem ser
  atribuídos no diálogo Definir Comandos, categoria Exploração de Texto.

## Mudanças na 9.0 ##

* Adicionada a possibilidade de escolher se os emojis do complemento devem
  ser falados.
* Usada codificação adequada nos nomes dos dicionários, o que corrige erros
  quando estes contêm certos caracteres.
* O resumo traduzido do complemento é usado adequadamente no título
  apresentado na ajuda do complemento, acessível no Gestor de Complementos.
* Adicionada uma nota mencionando o painel de emojis disponível em Windows
  10.

## Mudanças na 8.0 ##

* Compatível com o NVDA 2018.3 ou posterior (requerido).

## Mudanças na 7.0 ##

* A caixa de diálogo Configurações de ativação foi movida para um painel nas
  configurações do NVDA, para que o perfil atual seja exibido no título da
  caixa de diálogo de configurações do NVDA.
* O menu Gerir Emoticons foi removido: agora Inserir emoticon será
  encontrado no menu Ferramentas e Personalizar Emoticons será mostrado em
  dicionários como o dicionário de emoticons.
* Requer o NVDA 2018.2 ou posterior.

## Mudanças na 6.0 ##

* Adicionado suporte para perfis de configurações.
* No NVDA 2017.4 ou posterior, as definições de configuração e os
  dicionários personalizados serão alterados automaticamente de acordo com
  os perfis selecionados. Em 2017.3 ou anterior, você pode aplicar
  alterações recarregando plugins (pressionando control+NVDA+f3).
* Se você optar por importar as configurações ao atualizar o complemento, os
  arquivos preteridos (emoticons.ini e emoticons.dic) serão removidos ou
  adaptados a esta versão.

## Mudanças na 5.0 ##

* Adicionado suporte a emojis.
* Aprimoramentos para o diálogo Inserir Emoticon com um campo de filtro e
  botões de opção para escolher os emoticons mostrados.
* Usa guiHelper para os diálogos Opções de Ativação e Inserir Emoticon:
  requer NVDA 2016.4 ou versões maiores

## Mudanças na 4.0 ##

* Se o diálogo de inserir carinha for aberto quando outro diálogo de opções
  estiver ativo, o NVDA mostrará a mensagem de erro correspondente.


## Mudanças na 3.0 ##

* No diálogo Personalizar emoticons, agora é possível determinar que uma
  expressão só deve valer se for uma palavra inteira, conforme os
  dicionários de fala do NVDA 2014.4.


## Mudanças na 2.0 ##

* A ajuda do complemento está disponível no gestor de complementos.


## Mudanças na 1.1 ##

* Removido um emoticon duplicado.
* Adicionadas algumas carinhas.

## Mudanças na 1.0 ##

* Versão inicial.

[[!tag dev stable]]
