# Emoticons #
* Авторы: Chris Leo, Noelia Ruiz Martínez, Mesar Hameed, Francisco Javier
  Estrada Martínez
* NVDA compatibility: 2019.3 or later
* Загрузить [Стабильную версию][1]
* Загрузить [Разрабатываемую версию][2]

С помощью этого дополнения, в проговариваеммом тексте, содержащиеся символы
эмоций будут заменены на их более подробное описание.

Например: последовательность ":)" произносится как "улыбающийся смайлик",
или, например, NVDA будет распознавать значение каждого эмодзи.

Вы можете воспользоваться следующими возможностями:

## Вставить Смайлик ##

Иногда одно изображение стоит тысячу слов: используйте новые смайлики, чтобы
оживить ваши мгновенные сообщения, и пусть ваши друзья знают, что вы
чувствуете.

Когда вы не уверены в знаке для конкретного смайлика, это дополнение
позволит выбрать и вставить его в текст, например, в чате.

Press NVDA+I, or from menu Tools -> Emoticons > Insert emoticon, to open a dialog with the provided emoticons or emoji.

Этот диалог позволяет выбрать смайлик и отобразить смайлики, которые Вас
интересуют:

*	Поле редактирования позволяет фильтровать поискк нужного смайлика среди
  доступных смайликов.
*	С помощью набора радиокнопок, вы можете выбрать для просмотра только
  эмодзи (alt+З), только стандартные смайлики (alt+С) или все доступные
  смайлики (alt+В).
*	Список смайликов (alt+С) отображается тремя соответствующими столбцами:
  Имя смайлика, тип смайлика (стандартный или эмодзи), соответствующий
  символ.

Когда Вы нажмёте ОК, символы выбранного смайлика будут скопированы в буфер
обмена, готовые к вставке.

## Insert symbol ##

This dialog allows you to choose one of the symbols available in the
Punctuation/symbol pronunciation dialog of NVDA. You can use the Filter edit
box or the arrow keys to select an item from the symbols list. Then, press
OK and the selected emoji or symbol will be copied to your clipboard, ready
for pasting.

## Emoticons dictionary ##

Дополнение Emoticons позволяет иметь разные речевые словари, используя
профили конфигурации.

Это означает, что вы можете создавать и редактировать конкретный речевой
словарь для каждого пользовательского профиля.

From NVDA MENU, Preferences -> Speech dictionaries -> Emoticons dictionary, you can open a dialog to add or to edit available emoticons.

При сохранении ваших настроек, новые параметры чтения смайликов будут
применены только к редактируемому в данный момент профилю.

For example, you may wish that NVDA spoken custom emoticons only in XxChat
program, but not in other chat programs: you can do this by creating a
profile for the XxChat application and assign to it a speech dictionary from
Speech dictionaries menu, Emoticons dictionary option. See below for
Emoticons settings in relation to the configuration profiles.

Вы также можете экспортировать каждый пользовательский речевой словарь,
нажимая кнопку "Сохранить и экспортировать словарь": в этом случае ваши
речевые словари будут сохранены в папке конфигурации пользователя, в
подпапку speechDicts/emoticons.

The exact name and location of the dictionary file will be based on the
editing configuration profile, which will be shown in the title of the
Emoticons dictionary dialog.

## Emoticons settings ##

From menu Preferences -> Settings -> Emoticons opens a panel to configure the activation of your speech-dictionaries for each profile.

In Emoticons settings panel you can choose whether or not speech-dictionary should automatically activate when  NVDA switches to the   profile you are currently editing. By default it is disabled in normal configuration of NVDA and in all your new profiles.

Moreover, it's possible to determine if the add-on emojis should be
spoken. This could be useful to preserve symbols speaking if emojis are
included in NVDA's configuration.

If you may wish to keep clean your configuration folders, in this dialog it
is also possible to choose if dictionaries not used (associated with non
existing profiles) will be removed from the add-on when it is unloaded.

## Комбинации клавиш: ##

These are the key commands available by default, you can edit those or add
new key to open Emoticons settings panel or Emoticon Dictionary dialog:

* NVDA+E: проговаривание смайликов вкл/выкл, переключает между проговаривать
  текст, как написано, или с заменённым дружественным описанием смайликов.
* NVDA+I: показать диалог выбора смайлика, который вы хотите скопировать.
* Not assigned: show a dialog to select an NVDA's symbol you want to copy.
* Not assigned: open a browseable message showing the symbol where the
  review cursor is positioned, so that the whole description can be reviewed
  in browse mode.
* Not assigned: open a browseable message showing the symbol where the caret
  is positioned, so that the whole description can be reviewed in browse
  mode.

Note: On Windows 10, it's also possible to use the built-in emoji panel.

## Changes for 13.0 ##

* Fixed errors in Insert Emoticon dialog.
* Added a dialog to insert a symbol available in the Punctuation/symbol
  pronunciation of NVDA.

## Changes for 12.0 ##

* Requires NVDA 2019.3 or later.

## Changes for 11.0 ##

* When the add-on is updated, dictionaries saved in the previous version of
  the add-on will be automatically copied to the new version, unless you
  prefer to import dictionaries saved in the main dictionaries folder of
  NVDA.
* When showing the symbol where the caret or the review cursor are
  positioned, the words Character and Replacement are used to distinguish
  between the symbol itself and its description in browse mode, useful for
  speech users.

## Changes for 10.0 ##

* Added commands to show the symbol where the review cursor or caret are
  positioned. Gestures for these commands can be assigned from the Input
  gestures dialog, Text review category.

## Changes for 9.0 ##

* Added the possibility of choosing if add-on emojis should be spoken.
* Used appropiate encoding for dictionary names, fixing errors when they
  contain certain characters.
* The translated summary of the add-on is properly used for the title
  presented in add-on help, accessible from the add-on manager.
* Added a note mentioning the emoji panel available on Windows 10.

## Changes for 8.0 ##

* Compatible with NVDA 2018.3 or later (required).

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

## Изменения в версии 6.0 ##

* Добавлена поддержка профилей конфигурации.
* В NVDA 2017.4 или позднее, параметры конфигурации и пользовательские
  словари автоматически изменяются в соответствии с выбранными профилями. В
  2017.3 или ранее, вам нужно применять изменения с помощью перезагрузки
  плагинов (нажатие control+NVDA+f3).
* Если вы выберете импортировать настройки при обновлении дополнения,
  устаревшие файлы (emoticons.ini и emoticons.dic) будут удалены или
  приспособлены для этой версии.

## Изменения в версии 5.0 ##

* Добавлена поддержка эмодзи.
* Улучшен диалог Вставка смайлика с помощью поля фильтра и переключателей
  для выбора отображаемых смайликов.
* Используется guiHelper для диалогов параметры активации и Вставка
  смайлика: требуется NVDA 2016.4 или более поздней версии

## Изменения в версии 4.0 ##

* Если открывать диалог Insert smiley, когда активен другой диалог настроек,
  NVDA покажет соответствующее сообщение об ошибке.


## Изменения в версии 3.0 ##

* В диалоге настроек смайликов emoticons теперь возможно указать, что
  образец будет соответствовать смайлику, если он - только целое слово,
  согласно речевым словарям NVDA 2014.4.


## Изменения в версии 2.0 ##

* Справка дополнения доступна в диспетчере дополнений.


## Изменения в версии 1.1 ##

* Удалён дублирующийся смайлик.
* Добавлено несколько смайликов.

## Изменения в версии 1.0 ##

* Начальная версия.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=emo

[2]: https://addons.nvda-project.org/files/get.php?file=emo-dev

[3]: https://addons.nvda-project.org/files/get.php?file=emo-o
