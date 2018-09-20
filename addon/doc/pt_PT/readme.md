# Emoticons #

* Autores: Chris Leo, Noelia Ruiz Martínez, Mesar Hameed, Francisco Javier
  Estrada Martínez
* Baixar [versão estável] [1]
* Baixar [versão de desenvolvimento] [2]

Ao usar este extra, o texto do emoticon que contenha caracteres será
substituído por uma descrição mais humana e amigável.

Por exemplo: a seqüência ":)" será falada como "smiley sorridente", ou, por
exemplo, o NVDA reconhecerá o significado de cada emoji.

Neste extra, pode aproveitar os seguintes recursos:

## Inserir Emoticon ##

Por vezes, uma imagem vale 1000 palavras: use o novo emoji para animar a sua
mensagem instantânea e deixar os seus amigos saberem como se está a sentir,
naquele momento.

Quando não tiver a certeza dos caracteres para um determinado smiley, este
extra permite-lhe seleccioná-lo e inseri-lo no seu texto, como numa
conversa.

Pressione NVDA + I, ou a partir do menu ferramentas -> Gerir emoticons -> Inserir emoticon, abra uma caixa de diálogo com os emoticons ou emoji fornecidos.

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

Se quiser manter limpas as suas pastas de configuração, nesta caixa de
diálogo também é possível escolher se os dicionários não utilizados
(associados a perfis não existentes) serão removidos do extra quando
estiverem descarregados.

Also, it's possible to enable Settings only in normal configuration (not
recommended). This is intended to disable settings changes in case of speed
issues when switching profiles.

## Teclas de Comando: ##

Estas são as teclas de comando disponíveis por padrão, pode editá-las ou
adicionar uma nova tecla para abrir o painel de configurações do extra ou o
diálogo do dicionário do Emoticon:

* NVDA + E: falar emoticons on / off, alterna entre o texto falar como está
  escrito, ou com os emoticons substituídos pela descrição humana.
* NVDA + I: mostra uma caixa de diálogo para seleccionar um emoticon que
  deseja copiar.



## Changes for 8.0 ##

* Compatible with NVDA 2018.3 or later (required).

## Alterações para 7.0 ##

* A caixa de diálogo Configurações de ativação foi movida para um painel nas
  configurações do NVDA, para que o perfil actual seja mostrado no título da
  caixa de diálogo de configurações do NVDA.
* O menu Gerir Emoticons foi removido: agora o extra foi Inserido no menu
  Ferramentas e os Emoticons Personalizados serão exibidos em dicionários de
  fala, como o dicionário de Emoticons.
* Requer o NVDA 2018.2 ou posterior.
* Se for necessário, pode fazer o download da [última versão compatível com
  o NVDA 2017.3] [3].

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

[1]: http://addons.nvda-project.org/files/get.php?file=emo

[2]: http://addons.nvda-project.org/files/get.php?file=emo-dev

[3]:
https://github.com/nvdaes/emoticons/releases/download/6.5/emoticons-6.5.nvda-addon
