# Emotikony #

* Autori: Chris Leo, Noelia Ruiz Martínez, Mesar Hameed, Francisco Javier
  Estrada Martínez

Tento doplnok interpretuje grafické emotikony slovným popisom.

napríklad: ":)" bude prečítané ako "úsmev". NVDA navyše bude rozpoznávať aj
emoji.

Ďalšie vlastnosti:

## Vloženie emotikonu ##

Namiesto tisíc slov môžete použiť jediný obrázok. Použite emoji a dajte
vašim priateľom vedieť, ako sa cítite a čo robíte.

Ak si nie ste istý, ako napísať správne smailíka, tento doplnok vám umožní
vybrať požadovaný symbol zo zoznamu.

Press NVDA+I, or from menu Tools -> Emoticons > Insert emoticon, to open a dialog with the provided emoticons or emoji.

V dialógu uvidíte emotikony na vloženie a tiež tie, ktoré často vkladáte:

*	Pomocou editačného poľa filter môžete rýchlo vyhľadať príslušný emotikon.
*	Pomocou prepínača môžete zvoliť všetky emotikony (alt+v), emoji (alt+i)
  alebo len štandardné emotikony (alt+š).
*	V zozname (alt+z) sa pri každej položke zobrazuje textový popis, tip a
  symbol.

Stlačením OK sa príslušný emotikon uloží do schránky. Následne ho môžete
kamkoľvek prilepiť.

## Insert symbol ##

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

## Slovník emotikonov ##

Môžete mať rôzne slovníky pre rôzne konfiguračné profily.

V každom konfiguračnom profile NVDA tak môžete mať vlastný slovník
emotikonov.

V menu NVDA >možnosti >emotikony >pridať /upraviť môžete vytvoriť nové, alebo upraviť existujúce emotikony.
V tomto dialógu môžete uložiť vlastný používateľský slovník s emotikonmi.

Keď uložíte zmeny v doplnku pri aktivovanom konfiguračnom profile, zmeny sa
prejavia len v práve aktívnom profile.

Napríklad: Chceme, aby NVDA oznamovalo emotikony v programe Miranda, ale nie
v ostatných aplikáciách. Vytvoríme preto profil pre Mirandu a priradíme k
nemu slovník z rečových slovníkov.

po stlačení tlačidla "Ulož a exportuj slovník" sa používateľský slovník
uloží v priečinku s nastaveniami NVDA, v priečinku speechDicts/emoticons.

Názov slovníka sa určí podľa názvu profilu. Názov sa zobrazí aj v názve okna
pri úprave slovníka.

## Nastavenia ##

Aktiváciu slovníka aktivujete v strome s nastaveniami NVDA, vetva emotikony.

Tu môžete určiť, či sa použije slovník s emotikonmi pre práve upravovaný profil. Predvolene je toto nastavenie vypnuté.

Takisto môžete zapnúť a vypnúť oznamovanie emoji. Toto je užitočné v
prípade, že sú emoji súčasťou NVDA.

Tiež môžete z tohto dialógu odstrániť slovníky, ktoré sa viac nepoužívajú a
nie ú asociované so žiadnym profilom.

## Klávesové skratky: ##

Klávesové skratky môžete upraviť v dialógu klávesové skratky, vetva
prezeranie textu. Dostupné sú tieto možnosti:

* NVDA+E: prepína medzi vyslovovaním znakov a popisov emotikonov. Určuje, či
  budú oznamované jednotlivé časti emotikonu alebo slovný popis.
* NVDA+I: zobrazí dialóg na vloženie požadovaného emotikonu.
* Not assigned: show a dialog to select an NVDA's symbol you want to copy.
* Nedefinované: Zobraz emotikon pod prezeracím kurzorom režime prehliadania.
* Nedefinované: Zobraz emotikon pod systémovým kurzorom v režime
  prehliadania.

Note: On Windows 10 and higher, it's also possible to use the built-in emoji
panel.

## Changes for 17.0 ##

* Added ability to associate gestures to type symbols.
* Added ability to copy various symbols at the same time.

## Changes for 16.0 ##

* Compatible with NVDA 2023.1.

## Changes for 15.0 ##

* Requires NVDA 2022.1 or later.
* Cannot be used in secure mode.

## Changes for 14.0 ##

* Compatible with NVDA 2021.1.

## Changes for 13.0 ##

* Fixed errors in Insert Emoticon dialog.
* Added a dialog to insert a symbol available in the Punctuation/symbol
  pronunciation of NVDA.

## Zmeny vo verzii 12.0 ##

* Vyžaduje NVDA od verzie 2019.3.

## Zmeny vo verzii 11.0 ##

* Slovníky z predošlých verzií sa automaticky importujú pri aktualizácii do
  novej verzie, ak nepreferujete ukladanie slovníkov do hlavného adresára s
  nastaveniami NVDA.
* V režime prehliadania sa pri popise symbolu zobrazujú aj slová znak a
  popis, aby bolo možné ľahšie rozlíšiť reprezentáciu a popis symbolov.

## Zmeny vo verzii 10.0 ##

* Pridané skratky na zobrazenie symbolov v režime prehliadania. Nastavujú sa
  v dialógu klávesové skratky, vetva prezeranie textu.

## Zmeny vo verzii 9.0 ##

* Pridaná možnosť zapnúť a vypnúť oznamovanie emotikonov.
* Prerobené kódovanie a odstránené problémy s kódovaním.
* Odteraz je možné preložiť popis doplnku.
* Pridaná informácia o panely emoji v systéme Windows 10.

## Zmeny vo verzii 8.0 ##

* Vyžaduje NVDA od verzie 2018.3.

## Zmeny vo verzii 7.0 ##

* Dialóg s nastaveniami presunutý do nastavení NVDA.
* Odstránené menu doplnku: Pridanie emotikonu vykonáte z menu nástroje,
  slovníky sú v menu rečové slovníky.
* Vyžaduje NVDA od verzie 2018.2.
* Môžete si [stiahnuť verziu pre NVDA 2017.3][3].

## Zmeny vo verzii 6.0 ##

* Pridaná podpora pre konfiguračné profily.
* Od NVDA 2017.4 sa nastavenia načítavajú podľa použitého profilu. V
  starších verziách je potrebné načítať pluginy (ctrl+nvda+F3).
* Pri aktualizácii na novú verziu sa odstránia nepoužívané súbory
  (emoticons.ini a emoticons.dic).

## Zmeny vo verzii 5.0 ##

* Pridaná podpora emoji.
* Do dialógu na vloženie emotikonu pridaný filter a kategórie.
* Vyžaduje NVDA 2016.4. Pridaný modul guiHelper na zobrazenie dialógov.

## Zmeny vo verzii 4.0 ##

* Nie je viac možné otvoriť dialóg na vkladanie emotikonov, ak je už
  otvorený iný dialóg NVDA.


## Zmeny vo verzii 3.0 ##

* v dialógu s nastavením emotikonov môžete odteraz určiť, či sa má reťazec
  zmeniť len ak je ako celé slovo, alebo v ľubovoľnom kontexte (rovnako ako
  v rečových slovníkoch NVDA od verzie 2014.4).


## Zmeny vo verzii 2.0 ##

* Návod k doplnku môžete nájsť v správcovi doplnkov.


## Zmeny vo verzii 1.1 ##

* odstránené duplicitné emotikony.
* pridané nové emotikony.

## Zmeny vo verzii 1.0 ##

* prvé vydanie.

[[!tag dev stable]]

[3]: https://www.nvaccess.org/addonStore/legacy?file=emo-o
