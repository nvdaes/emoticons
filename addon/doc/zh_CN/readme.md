# 表情符号插件 #
* 作者：Chris Leo，NoeliaRuizMartínez，Mesar Hameed，Francisco
  JavierEstradaMartínez
* NVDA兼容版本: 2019.3或更高版本
* 下载[稳定版][1]
* 下载[开发版][2]

启用表情名称朗读来代替原字符朗读。

例如：序列“:)”将被称为“微笑表情”，或者例如NVDA将识别每个表情符号的正确含意。

您可以利用以下功能：

## 插入表情 ##

有时一张图片胜过千言万语：使用表情符号来加入到你的即时消息并让你的朋友知道你现在的想法吧。

如果您不确定特定表情的字符，可以使用此插件选择并将其插入到你的文本，例如聊天编辑框。

Press NVDA+I, or from menu Tools -> Emoticons > Insert emoticon, to open a dialog with the provided emoticons or emoji.

此对话框允许您选择表情符号并浏览您感兴趣的表情符号：

*	可编辑字段允许您在可用的表情符号中过滤搜索所需表情符号。
*	通过一组单选按钮，您可以选择仅查看表情符号类别（alt + E）或仅查看标准表情符号类别（alt + s）或查看所有可用的表情符号（alt +
  A）。
*	表情符号列表（alt + L）分别显示在三列上：表情符号的名称，表情符号的类型（标准表情符号或表情符号），相应的字符。

按确认后，所选表情符号的字符将被复制到剪贴板，准备粘贴。

## Insert symbol ##

This dialog allows you to choose one of the symbols available in the
Punctuation/symbol pronunciation dialog of NVDA. You can use the Filter edit
box or the arrow keys to select an item from the symbols list. Then, press
OK and the selected emoji or symbol will be copied to your clipboard, ready
for pasting.

## 表情词典 ##

表情符号插件允许使用配置文件使用不同的语音词典。

这意味着您可以为每个自定义配置文件创建或编辑特定的语音字典。

从NVDA菜单，首选项 - >语音词典 - >表情词典，您可以打开一个对话框来添加或编辑可用的表情。

保存自定义项，表情符号的新阅读设置仅适用于您当前正在编辑的配置文件。

例如，您可能希望NVDA仅在XxChat程序中使用自定义表情符号，而不是在其他聊天程序中：您可以通过为XxChat应用程序创建配置文件并从语音词典菜单中分配语音词典，表情符号词典选项来完成此操作。请参阅下面有关配置配置文件的表情符号设置。

您还可以按“保存并导出词典”按钮导出每个自定义语音词典：这样您的语音词典将保存在您的用户配置文件夹，speechDicts /
emoticons子文件夹中。

字典文件的确切名称和位置将基于编辑配置配置文件，该配置文件将显示在“表情符号”字典对话框的标题中。

## 表情符号设置 ##

从菜单首选项 - >设置 - >表情符号打开一个面板，为每个配置文件配置语音词典的激活。

在“表情符号设置”面板中，您可以选择在NVDA切换到当前正在编辑的配置文件时是否应自动激活语音字典。默认情况下，它在NVDA的正常配置和所有新配置文件中都被禁用。

此外, 还可以确定是否应该读出插件内的表情。如果在 NVDA 的配置中包含表情符号, 这可能会很有用。

如果您可能希望保持清洁配置目录，则在此对话框中还可以选择是否在卸载时从插件中删除未使用的字典（与非现有配置文件关联）。

## 快捷键： ##

这些是默认情况下可用的常见快捷键，您可以编辑这些快捷键或添加新键以打开“表情符号”设置面板或“表情词典”对话框：

* NVDA + E：开启/关闭表情符号朗读。
* NVDA + I：显示对话框，用于选择要复制的表情。
* Not assigned: show a dialog to select an NVDA's symbol you want to copy.
* 未分配: 打开显示浏览光标所在位置的符号的可浏览消息, 以便可以在浏览模式下浏览整个描述。
* 未分配: 打开显示插入符号所在位置的符号的可浏览消息, 以便可以在浏览模式下查看整个描述。

注意：在Windows 10上，也可以使用内置表情符号面板。

## Changes for 13.0 ##

* Fixed errors in Insert Emoticon dialog.
* Added a dialog to insert a symbol available in the Punctuation/symbol
  pronunciation of NVDA.

## 版本 12.0 ##

* 需要NVDA 2019.3或更高版本。

## 版本 11.0 ##

* 更新插件后，保存在以前版本插件中的词典将自动复制到新版本，除非您更喜欢导入保存在NVDA主词典文件夹中的词典。
* 当显示插入符号或浏览光标所在的符号时，单词Character和Replacement用于区分符号本身及其在浏览模式下的描述，对语音用户有用。

## 10.0更新日志 ##

* 添加了命令, 以显示浏览光标或插入符号所在的符号。可以从 "输入手势" 对话框 "文本浏览分类分配这些命令的手势。

## 9.0更新日志 ##

* 新增选择是否应该朗读插件内的表情。
* 对字典名称使用适当的编码, 在错误包含某些字符时修复错误。
* 插件的翻译摘要被正确地用于插件帮助中提供的标题, 可从插件管理器访问。
* 添加了一个提示, 其中提到了 Windows 10 上提供的表情符号面板。

## 8.0更新日志 ##

* 兼容NVDA 2018.3或更高版本（必需）。

## 7.0更新日志 ##

* 激活设置对话框已移至NVDA设置，现在配置文件将显示在NVDA设置对话框的标题中。
* 管理表情符号菜单已被删除：现在可以在“工具”菜单下找到“插入表情符号”，“自定义表情符号”将显示在“表情词典”下的“语音词典”中。
* 现在需要NVDA 2018.2或更高版本。
* 如果需要使用旧版本，您可以下载[与NVDA 2017.3兼容的最新版本] [3]。

## 6.0更新日志 ##

* 添加了对配置文件的支持。
* 在NVDA
  2017.4或更高版本中，配置设置和自定义词典将根据所选配置文件自动更改。在2017.3或更早版本中，您可以通过重新加载插件来应用更改（按下ctrl+
  NVDA + f3）。
* 如果您在更新插件时选择导入设置，则会删除或已弃用此版本的（emoticons.ini和emoticons.dic）文件。

## 5.0更新日志 ##

* 添加了对表情符号的支持。
* Insert Emoticon对话框的改进，带有过滤器字段和单选按钮，用于选择显示的表情符号。
* 使用guiHelper激活设置对话框和插入表情符号对话框：需要NVDA 2016.4或更高版本

## 4.0更新日志 ##

* 如果在另一个设置对话框处于活动状态时打开了“插入表情”对话框，NVDA将显示相应的错误消息。


## 3.0更新日志 ##

* 根据NVDA 2014.4的语音词典，在“自定义表情符号”对话框中，现在可以指定模式只应匹配，如果它是一个完整的单词。


## 2.0更新日志 ##

* 插件管理器现在提供了插件帮助。


## 1.1更新日志 ##

* 删除了重复的表情符号。
* 添加了一些表情。

## 1.0更新日志 ##

* 发布初始版本。

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=emo

[2]: https://addons.nvda-project.org/files/get.php?file=emo-dev

[3]: https://addons.nvda-project.org/files/get.php?file=emo-o
