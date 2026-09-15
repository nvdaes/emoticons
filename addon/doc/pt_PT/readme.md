# &Emoticons

* Autores: Chris Leo, Noelia Ruiz Martínez, Mesar Hameed, Francisco Javier Estrada Martínez

Usando este extra, o texto falado que contém caracteres emoticon será substituído por uma descrição mais fácil de entender.

Por exemplo: a sequência “:)” será lida como “smiley sorridente”; ou, por exemplo, o NVDA reconhecerá o significado de cada emoji.

Pode aproveitar os seguintes recursos:

## Inserir emoticon ##

Às vezes, uma imagem vale mais que mil palavras: use os novos emojis para animar as suas mensagens instantâneas e mostrar aos seus amigos como se está a sentir.

Quando não tiver a certeza dos caracteres de um smiley específico, este extra permite que o selecione e insira no seu texto, por exemplo, numa conversa.

Pressione NVDA+I ou, no menu, selecione Ferramentas -> Emoticons > Inserir emoticon para abrir uma caixa de diálogo com os emoticons ou emojis disponíveis.

Esta caixa de diálogo permite-lhe escolher um emoticon e visualizar os emoticons que lhe interessam:

*	Um campo editável permite filtrar a busca pelo emoticon desejado entre os emoticons disponíveis.
*	Por meio de um conjunto de botões de opção, pode optar por visualizar apenas a categoria de emojis (Alt+E), apenas a categoria de emoticons padrão (Alt+S) ou todos os emoticons disponíveis (Alt+A).
*	Na lista de emoticons (Alt+L), os itens são exibidos em três colunas, respectivamente: o nome do emoticon, o tipo de emoticon (emoticon padrão ou emoji) e o caractere correspondente.

Ao clicar em OK, os caracteres do emoticon escolhido serão copiados para a sua área de transferência, prontos para serem colados.

## Inserir o símbolo ##

Esta caixa de diálogo permite-lhe escolher um dos símbolos disponíveis na caixa de diálogo “Pontuação/pronúncia de símbolos” do NVDA. pode usar a caixa de texto “Filtro” ou as setas do teclado para selecionar um item da lista de símbolos.

Se quiser copiar vários símbolos, use o botão “Adicionar” para os inserir na caixa de texto “Símbolos a serem copiados”.

Em seguida, pressione OK e o emoji ou símbolo selecionado, ou os símbolos contidos na caixa de edição mencionada, serão copiados para a sua área de transferência, prontos para serem colados.

## Associar atalhos a símbolos ##

No menu do NVDA, no submenu “Preferências”, na caixa de diálogo “definir comandos”, nas categorias “Inserir símbolos” ou “Copiar símbolos”, é possível configurar o NVDA para digitar símbolos por meio de gestos associados.

Pode usar a caixa de texto do campo “Editar” para reduzir o número de símbolos exibidos, de modo que essa categoria possa ser expandida mais rapidamente.

## dicionário de Emoticons ##

O extra de emoticons permite utilizar diferentes dicionários de fala por meio de perfis de configuração.

Isto significa que pode criar ou editar um dicionário de voz específico para cada um dos seus perfis personalizados.

No MENU do NVDA, em Preferências -> Dicionários de fala -> Dicionário de emoticons, pode abrir uma caixa de diálogo para adicionar ou editar os emoticons disponíveis.

Ao guardar as suas personalizações, as novas configurações de exibição dos emoticons se aplicarão apenas ao perfil que está editando no momento.

Por exemplo, talvez queira que o NVDA leia em voz alta os emoticons personalizados apenas no programa XxChat, mas não em outros programas de bate-papo: para isso, crie um perfil para o aplicativo XxChat e atribua a ele um dicionário de voz no menu “Dicionários de voz”, na opção “Dicionário de emoticons”. Veja a seguir as configurações de emoticons em relação aos perfis de configuração.

Também pode exportar cada dicionário de voz personalizado clicando no botão “Guardar e exportar dicionário”: dessa forma, os seus dicionários de voz serão salvos na pasta de configuração do usuário, na subpasta speechDicts/emoticons.

O nome exato e a localização do arquivo do dicionário dependerão do perfil de configuração de edição, que será exibido no título da caixa de diálogo “Dicionário de emoticons”.

## Configurações de emoticons

No menu Preferências -> Configurações -> Emoticons, abre-se um painel para configurar a ativação dos seus dicionários de voz para cada perfil.

No painel de configurações de Emoticons, pode escolher se o dicionário de fala deve ou não ser ativado automaticamente quando o NVDA alternar para o perfil que está a editar no momento. Por padrão, essa opção está desativada na configuração normal do NVDA e em todos os seus novos perfis.

Além disso, é possível definir se os emojis adicionais devem ser lidos em voz alta. Isso pode ser útil para garantir que os símbolos continuem sendo lidos em voz alta caso haja emojis incluídos na configuração do NVDA.

Se os símbolos inseridos por meio de atalhos associados não forem lidos em voz alta no seu sistema, mesmo quando o NVDA estiver configurado para ler em voz alta os caracteres digitados, pode tentar marcar uma caixa de seleção para garantir que os símbolos inseridos sejam lidos em voz alta.


Caso deseje manter as suas pastas de configuração organizadas, nesta caixa de diálogo também é possível definir se os dicionários não utilizados (associados a perfis inexistentes) serão removidos do extra, quando ele for desativado.

## Teclas de atalho

Estes são os atalhos de teclado disponíveis por padrão; pode editá-los ou adicionar novos atalhos para abrir o painel de configurações de emoticons ou a caixa de diálogo do dicionário de emoticons:

* NVDA+E: ativa/desativa a leitura em voz alta dos emoticons; alterna entre a leitura do texto conforme ele é escrito e a leitura com os emoticons substituídos por descrições verbais.
* NVDA+I: exibe uma caixa de diálogo para selecionar o emoticon que você deseja copiar.
* Não atribuído: mostra um diálogo para seleccionar um símbolo do NVDA que deseja copiar.
* Não atribuído: abrir uma mensagem navegável que mostre o símbolo no local onde o cursor de revisão está posicionado, para que toda a descrição possa ser revisada no modo de navegação.
* Não atribuído: abre uma mensagem navegável exibindo o símbolo no local onde o cursor está posicionado, para que toda a descrição possa ser revisada no modo de navegação.

Observação: No Windows 10 e versões posteriores, também é possível usar o painel de emojis integrado.

## Alterações na versão 34.0.0

* Foi adicionada a funcionalidade de copiar para a área de transferência e colar símbolos individualmente, o que é útil quando os gestos associados aos scripts de inserção de símbolos não funcionam.


## Alterações na versão 33.0.0

* Corrigimos um erro no recurso “Salvar e exportar dicionários”.
* Foram adicionados botões “Copiar” e “Fechar” às mensagens exibidas no modo de navegação.
* Ao usar comandos para inserir símbolos, estes podem ser lidos em voz alta, de acordo com a opção “ler em voz alta os caracteres digitados”.

## Alterações na versão 22.0.0 ##

* Requer o NVDA 2023.2 ou versão posterior.

## Alterações na versão 17.0 ##

* Foi adicionada a funcionalidade de associar gestos à digitação de símbolos.
* Foi adicionada a funcionalidade de copiar vários símbolos ao mesmo tempo.

## Alterações na versão 16.0 ##

* Compatível com NVDA 2023.1.

## Alterações na versão 15.0 ##

* Requer o NVDA 2022.1 ou versão posterior.
* Não pode ser usado no modo seguro.

## Alterações na versão 14.0 ##

* Compatível com o NVDA 2021.1.

## Alterações na versão 13.0 ##

* Corrigimos erros na caixa de diálogo “Inserir Emoticon”.
* Adicionado um diálogo para inserir um símbolo disponível na Pronúncia de Pontuação/Símbolo do NVDA.

## Alterações na versão 12.0 ##

* Requer NVDA 2019.3 ou superiores.

## Alterações na versão 11.0 ##

* Quando o extra é actualizado, os dicionários guardados na versão anterior do extra serão automaticamente copiados para a nova versão, a menos que prefira importar dicionários guardados na pasta principal de dicionários do NVDA.
* Ao exibir o símbolo no local onde o cursor de edição ou o cursor de revisão estão posicionados, os termos “Caractere” e “Substituição” são utilizados para distinguir entre o próprio símbolo e sua descrição no modo de navegação, o que é útil para usuários de sintetizadores de voz.

## Alterações na versão 10.0 ##

* Foram adicionados comandos para exibir o símbolo no local onde o cursor de revisão ou o marcador estão posicionados. Os gestos para esses comandos podem ser atribuídos na caixa de diálogo “Gestos de entrada”, na categoria “Revisão de texto”.

## Alterações na versão 9.0 ##

* Foi adicionada a opção de escolher se os emojis adicionais devem ser lidos em voz alta.
* Utilizou a codificação adequada para os nomes dos dicionários, corrigindo erros quando estes continham determinados caracteres.
* O resumo traduzido do complemento é utilizado corretamente no título apresentado na ajuda do complemento, acessível a partir do gerenciador de complementos.
* Adicionamos uma nota informando sobre o painel de emojis disponível no Windows 10.

## Alterações na versão 8.0 ##

* Compatível com o NVDA 2018.3 ou versões posteriores (obrigatório).

## Alterações na versão 7.0 ##

* A caixa de diálogo “Configurações de ativação” foi movida para um painel nas configurações do NVDA, de modo que o perfil atual seja exibido no título da caixa de diálogo de configurações do NVDA.
* O menu “Gerenciar Emoticons” foi removido: agora, a opção “Inserir emoticon” estará disponível no menu “Ferramentas”, e a opção “Personalizar Emoticons” será exibida na seção “Dicionários de fala”, junto com o “Dicionário de Emoticons”.
* Requer o NVDA 2018.2 ou versão posterior.

## Alterações na versão 6.0 ##

* Foi adicionado suporte a perfis de configuração.
* No NVDA 2017.4 ou versões posteriores, as configurações e os dicionários personalizados serão alterados automaticamente de acordo com os perfis selecionados. Na versão 2017.3 ou anteriores, você pode aplicar as alterações recarregando os plug-ins (pressionando Ctrl+NVDA+F3).
* Se você optar por importar as configurações ao atualizar o complemento, os arquivos obsoletos (emoticons.ini e emoticons.dic) serão removidos ou adaptados para esta versão.

## Alterações na versão 5.0 ##

* Foi adicionado suporte para emojis.
* Melhorias na caixa de diálogo “Inserir Emoticon”, com um campo de filtro e botões de opção para selecionar os emoticons exibidos.
* Uso do guiHelper nas caixas de diálogo “Configurações de ativação” e “Inserir emoticon”: requer o NVDA 2016.4 ou versões posteriores

## Alterações na versão 4.0 ##

* Se a caixa de diálogo “Inserir smiley” for aberta enquanto outra caixa de diálogo de configurações estiver ativa, o NVDA exibirá a mensagem de erro correspondente.


## Alterações na versão 3.0 ##

* Na caixa de diálogo “Personalizar emoticons”, agora é possível especificar que um padrão só deve corresponder se for uma palavra inteira, de acordo com os dicionários de fala do NVDA 2014.4.


## Alterações na versão 2.0 ##

* A ajuda sobre complementos está disponível no Gerenciador de Complementos.


## Alterações na versão 1.1 ##

* Removi o emoticon duplicado.
* Adicionei alguns emoticons.

## Alterações na versão 1.0 ##

* Versão inicial.
