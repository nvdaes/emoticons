# İfadeler #

* Yazarlar: Chris Leo, Noelia Ruiz Martínez, Mesar HameedYazarlar: Chris,
  Noelia Ruiz Martínez, Mesar Hameed
* İndir [kararlı sürüm][1]
* İndir [geliştirme sürümü][2]

bu eklentiyle , ifade karakterlerini içeren metin onun insan dostu
açıklamasıyla değiştirilerek seslendirilecektir. 86 ifade tanımlanmıştır.

For example: ":)" will be spoken as "smiling smiley", or ":D" will be spoken
as "laughing smiley"

Aşağıdaki özelliklerden yararlanabilirsiniz:

## İfade ekle ##

Belirli bir ifadenin hangi karakterlerden oluştuğundan emin değilseniz, Bu eklenti sohbet ettiğiniz ekranlar gibi metinler için surat seçmenizi ve eklemenizi sağlar.
NVDA + I tuşlarına basın ya da tercihler menüsünden ifadeleri yönet altından ifade ekle seçeneğiyle
mevcut ifadelerin listesinin bulunduğu iletişim kutusunu açın.
Tamam düğmesine bastığınızda, seçilen ifadeyle ilgili karakterler panoya kopyalanmış olacak.


## İfadeleri özelleştir ##

NVDA menüsü altından, Tercihler -> ifadeleri yönet -> ifadeleri özelleştir seçeneğiyle, kullanılabilir ifadeleri eklemek veya düzenlemek için bir iletişim kutusu açabilirsiniz.
Bu iletişim kutusu özelleştirmelerinizle birlikte bir ifade konuşma sözlüğü kaydetmenize olanak verir.

"Sözlüğü kaydet ve dışa aktar" düğmesine basarsanız, Kullanıcı konfigürasyon
klasöründe, speechDicts alt klasörüne emoticons.dic adlı bir sözlük dosyası
kaydedilir.


## Etkinleştirme ayarları ##

NVDA başlayınca ifade eklentisinin etkin olup olmayacağını
belirleyebilirsiniz. Varsayılan olarak devre dışıdır.  Bu ayar için
seçiminizi kalıcı olarak kaydetmek mümkündür.

## Tuş Komutları: ##

*	NVDA+E: ifadenin yazıldığı şekilde mi yoksa tanımlandığı haliyle mi
  seslendirileceği ile ilgili ayarı değiştirir.
*	NVDA + I: yapıştırmak istediğiniz bir ifade seçmek için bir iletişim
  kutusu açar.


## Changes for 4.0 ##

* If the Insert smiley dialog is opened when another settings dialog is
  active, NVDA will show the corresponding error message.


## 3.0 için değişiklikler ##

* In the Customize emoticons dialog, it is now possible to specify that a
  pattern should only match if it is a whole word, according to speech
  dictionaries of NVDA 2014.4.


## 2.0 için değişiklikler ##

* Eklenti yardımına Eklenti Yöneticisi altından ulaşılabilir.


## 1.1 için değişiklikler ##

* Tekrar eden ifade silindi.
* Bazı smileyler eklendi.

## 1.0 için değişiklikler ##

* İlk sürüm.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=emo

[2]: http://addons.nvda-project.org/files/get.php?file=emo-dev
