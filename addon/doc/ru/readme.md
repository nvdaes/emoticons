# Emoticons #

* Авторы: Chris Leo, Noelia Ruiz Martínez, Mesar Hameed, Francisco Javier
  Estrada Martínez
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

Нажмите NVDA+I, или из меню Параметры -> Управление смайликами -> Вставить смайлик, чтобы открыть диалог с предоставленными смайликами или эмодзи.

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

## Настройки смайликов ##

Emoticons add-on allows to have differents speech-dictionaries using
configuration profiles.

This means that you can create or edit a specific speech-dictionary for each
your custom profile.

В меню NVDA, Параметры -> Управление смайликами -> Настройка смайликов, можно открыть диалог настроек, чтобы добавить или редактировать имеющиеся смайлики.

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

## Настройки активации ##

From menu Preferences -> Manage Emoticons -> Activation-settings opens a dialog to configure the activation of your speech-dictionaries for each profile.

In activation-setting dialog you can choose whether or not speech-dictionary should automatically activate when  NVDA switches to the   profile you are currently editing. By default it is disabled in normal configuration of NVDA and in all your new profiles.

If you may wish to keep clean your configuration folders, in this dialog it
is also possible to choose if dictionaries not used (associated with non
existing profiles) will be removed from the add-on when it is unloaded.

## Комбинации клавиш: ##

Это основные команды клавиш, доступные по умолчанию, вы можете изменить
существующие или добавить новые клавиши для открытия диалогов настройки
активации и словаря смайликов:

* NVDA+E: speaking emoticons on/off, toggles between speaking text as it is
  written, or with the emoticons replaced by the human description.
* NVDA+I: показать диалог выбора смайлика, который вы хотите скопировать.

## Changes for 6.0 ##

* Added support for configuration profiles.
* In NVDA 2017.4 or later, the configuration settings and custom
  dictionaries will change automatically according with the selected
  profiles. In 2017.3 or earlier, you can apply changes by reloading plugins
  (pressing control+NVDA+f3).
* If you choose to import settings when updating the add-on, deprecated
  files (emoticons.ini and emoticons.dic) will be removed or adapted to this
  version.

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

[1]: http://addons.nvda-project.org/files/get.php?file=emo

[2]: http://addons.nvda-project.org/files/get.php?file=emo-dev
