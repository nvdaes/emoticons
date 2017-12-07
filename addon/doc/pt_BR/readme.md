# Emoticons #

* Autores: Chris Leo, Noelia Ruiz Martínez, Mesar Hameed, Francisco Javier
  Estrada Martínez
* Baixe a [versão estável][1]
* Baixe a [versão de desenvolvimento][2]

Ao usar este complemento, os textos falados que contenham caracteres de
emoticons serão substituídos por descrições mais amigáveis dos mesmos.

Por exemplo: A seqüência ":)" será falada como "sorriso", ou por exemplo o
NVDA vai reconhecer o significado de cada emoji.

Pode tirar proveito dos seguintes recursos:

## Inserir Emoticon ##

Às vezes uma imagem vale 1000 palavras: use o novo emoji para animar suas
mensagens instantâneas e fazer seus amigos saberem como você está se
sentindo.

Quando você não tiver certeza dos caracteres para uma cara em particular,
este complemento lhe possibilita selecionar e inseri-lo no texto, por
exemplo num chat.

Pressione NVDA+I, ou no menu Preferências -> Gerir emoticons -> Inserir emoticon, para abrir um diálogo com os emoticons ou emojis fornecidos.

Este diálogo possibilita você escolher um emoticon e ver os emoticons que
lhe interessem:

*	Um campo de edição possibilita filtrar a busca pelo emoticon desejado
  entre os disponíveis.
*	Por meio dum conjunto de botões de opção, pode escolher ver somente a
  categoria emoji (alt+E) ou ver somente a categoria emoticons padrão
  (alt+s) ou ver todos os emoticons disponíveis (alt+A).
*	Na lista (alt+L), os emoticons são mostrados em três colunas, a saber:
  Nome do emoticon, tipo (emoticon padrão ou emoji) e o caractere
  correspondente.

Ao pressionar OK, os caracteres do emoticon escolhido serão copiados para a
área de transferência, prontos para colar.

## Personalizar emoticons ##

Emoticons add-on allows to have differents speech-dictionaries using
configuration profiles.

This means that you can create or edit a specific speech-dictionary for each
your custom profile.

No menu do NVDA, em Preferências -> Gerir emoticons -> personalizar emoticons, pode abrir um diálogo de opções para adicionar ou editar os emoticons disponíveis.

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

## Opções de ativação ##

From menu Preferences -> Manage Emoticons -> Activation-settings opens a dialog to configure the activation of your speech-dictionaries for each profile.

In activation-setting dialog you can choose whether or not speech-dictionary should automatically activate when  NVDA switches to the   profile you are currently editing. By default it is disabled in normal configuration of NVDA and in all your new profiles.

If you may wish to keep clean your configuration folders, in this dialog it
is also possible to choose if dictionaries not used (associated with non
existing profiles) will be removed from the add-on when it is unloaded.

## Teclas de comando: ##

Estas são as teclas de comando disponíveis por padrão; você pode editá-las
ou acrescentar uma nova tecla para abrir o diálogo Opções de Ativação ou o
Dicionário de Emoticons:

* NVDA+E: speaking emoticons on/off, toggles between speaking text as it is
  written, or with the emoticons replaced by the human description.
* NVDA+I: mostra um diálogo para selecionar um emoticon que queira copiar.

## Changes for 6.0 ##

* Added support for configuration profiles.
* In NVDA 2017.4 or later, the configuration settings and custom
  dictionaries will change automatically according with the selected
  profiles. In 2017.3 or earlier, you can apply changes by reloading plugins
  (pressing control+NVDA+f3).
* If you choose to import settings when updating the add-on, deprecated
  files (emoticons.ini and emoticons.dic) will be removed or adapted to this
  version.

## Mudanças na 5.0 ##

* Adicionado suporte a emojis.
* Aprimoramentos para o diálogo Inserir Emoticon com um campo de filtro e
  botões de opção para escolher os emoticons mostrados.
* Usa guiHelper para os diálogos Opções de Ativação e Inserir Emoticon:
  requer NVDA 2016.4 ou versões maiores

## Mudanças na 4.0 ##

* Se o diálogo de inserir cara for aberto quando outro diálogo de opções
  estiver ativo, o NVDA mostrará a mensagem de erro correspondente.


## Mudanças na 3.0 ##

* No diálogo Personalizar emoticons, agora é possível determinar que uma
  expressão só deve valer se for uma palavra inteira, conforme os
  dicionários de fala do NVDA 2014.4.


## Mudanças na 2.0 ##

* A ajuda do complemento está disponível no gestor de complementos.


## Mudanças na 1.1 ##

* Removido um emoticon duplicado.
* Adicionadas algumas caras.

## Mudanças na 1.0 ##

* Versão inicial.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=emo

[2]: http://addons.nvda-project.org/files/get.php?file=emo-dev
