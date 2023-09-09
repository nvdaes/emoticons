# İfadeler #

* Geliştiriciler: Chris Leo, Noelia Ruiz Martínez, Mesar Hameed, Francisco
  Javier Estrada Martínez

Bu eklenti, metinlerde bulunan ifadeleri açıklamalarıyla değiştirerek onları
daha anlaşılabilir kılar.

Örneğin: ":)" dizisi "gülen yüz" olarak söylenecek veya örneğin NVDA her
emojinin anlamını tanıyacaktır.

Aşağıdaki özelliklerden yararlanabilirsiniz:

## İfade ekle ##

Bazen bir emoji 1000 kelimeye bedeldir: Anlık mesajınızı canlandırmak ve
arkadaşlarınıza nasıl hissettiğinizi bildirmek için yeni emojiyi
kullanabilirsiniz.

Belirli bir suratları (smiley) oluşturmak için gereken karakterlerden emin
değilseniz, bu eklenti  bir sohbete emojiyi olduğu gibi metninize seçip
eklemenizi sağlar.

NVDA+i tuşuna basarak veya nvda menusu+araşlar+ifadeler alt menüsünden ifade ekle öğesini etkinleştirerek ifadeler ve emojilerin bulunduğu iletişim kutusuna ulaşabilirsiniz. 

Bu iletişim kutusu, bir ifade seçmenizi veya ilginizi çeken ifadeleri
görüntülemenizi sağlar:

*	Düzenlenebilir bir alan, mevcut ifadeler arasından istenen ifadeyi aramayı
  filtrelemenizi sağlar.
*	Seçim düğmelerini kullanarak sadece emoji kategorisini (alt+İ), sadece
  standart ifade kategorisini (alt+s) veya mevcut tüm ifadeleri (alt+T)
  görüntülemeyi seçebilirsiniz.
*	İfade listesinde (alt+L) sırasıyla üç sütunda görüntülenir: ifadenin adı,
  ifadenin türü (standart ifade veya emoji), karşılık gelen karakter.

Tamam'a bastığınızda, seçilen ifadenin karakterleri yapıştırmaya hazır
olarak panonuza kopyalanacaktır.

## Sembol ekle ##

Bu iletişim kutusu, NVDA'nın Noktalama/sembol telaffuz iletişim kutusunda
bulunan simgelerden birini seçmenizi sağlar. Sembol listesinden bir öğe
seçmek için Filtre düzenleme kutusunu veya ok tuşlarını kullanabilirsiniz.

Çeşitli sembolleri kopyalamak istiyorsanız, bunları Kopyalanacak Semboller
düzenleme kutusuna eklemek için Ekle düğmesini kullanın.

Ardından, Tamam'a basın ve seçilen emoji veya sembol veya söz konusu
düzenleme kutusunda bulunan semboller, yapıştırmaya hazır olarak panonuza
kopyalanacaktır.

## Hareketleri sembollerle ilişkilendirin ##

NVDA menüsü, Tercihler alt menüsü, Girdi hareketleri iletişim kutusunda,
İfadeler kategorisinden, NVDA'yı ilgili hareketlerle sembolleri yazacak
şekilde yapılandırabilirsiniz.

Bu kategorinin daha hızlı genişletilebilmesi için sunulan sembol sayısını
azaltmak üzere Alanı düzenle düzenleme kutusunu kullanabilirsiniz.

## İfadeler sözlüğü ##

İfadeler eklentisi, yapılandırma profillerini kullanarak farklı konuşma
sözlüklerine kullanmanızı sağlar.

Bu,her bir özel profil için belirli bir konuşma sözlüğü oluşturabileceğiniz
veya düzenleyebileceğiniz anlamına gelir.

NVDA MENÜSÜ, Tercihler -> Konuşma sözlükleri -> İfadeler sözlüğünden, mevcut ifadeleri eklemek veya düzenlemek için bir iletişim kutusu açabilirsiniz.

Özelleştirmelerinizi kaydederken, ifadelerin yeni okuma ayarları yalnızca şu
anda düzenlemekte olduğunuz profile uygulanacaktır.

Örneğin, NVDA'nın özel ifadeleri yalnızca XxChat programında konuşmasını
ancak diğer sohbet programlarında kullanmamasını isteyebilirsiniz: bunu
XxChat uygulaması için bir profil oluşturarak ve ona Konuşma sözlükleri
menüsünden, İfadeler sözlüğü seçeneğinden bir konuşma sözlüğü atayarak
yapabilirsiniz. . Konfigürasyon profilleriyle ilgili İfadeler ayarları için
aşağıya bakın.

Ayrıca "Sözlüğü kaydet ve dışa aktar" düğmesine basarak her özel
konuşma-sözlüğünü dışa aktarabilirsiniz: bu şekilde konuşma sözlükleriniz,
kullanıcı yapılandırma klasörünüz, speechDicts/ifadeler alt klasörüne
kaydedilecektir.

Sözlük dosyasının tam adı ve konumu, İfadeler sözlüğü iletişim kutusunun
başlığında gösterilecek olan düzenleme yapılandırma profiline dayalı
olacaktır.

## İfade ayarları ##

Tercihler -> Ayarlar -> İfadeler menüsünden, her profil için konuşma sözlüklerinizin aktivasyonunu yapılandırmak üzere bir panel açar.

İfade ayarları panelinde, NVDA düzenlemekte olduğunuz profile geçtiğinde konuşma sözlüğünün otomatik olarak etkinleştirilip etkinleştirilmeyeceğini seçebilirsiniz. Varsayılan olarak, NVDA'nın normal konfigürasyonunda ve tüm yeni profillerinizde devre dışıdır.

Üstelik eklenti emojilerinin konuşulup söylenmemesi gerektiğini de
belirlemek mümkün. Bu, NVDA'nın yapılandırmasına emojiler dahil edilmişse,
konuşan sembolleri korumak için faydalı olabilir.

Konfigürasyon klasörlerinizi temiz tutmak istiyorsanız, bu iletişim
kutusunda, kullanılmayan sözlüklerin (mevcut olmayan profillerle ilişkili)
eklenti kaldırıldığında eklentiden kaldırılıp kaldırılmayacağını da
seçebilirsiniz.

## Kısayol Komutları: ##

Bunlar, varsayılan olarak İfade ayarları panelini veya İfade Sözlüğü
iletişim kutusunu açmak için kullanılabilen kısayol komutlarıdır. bunları
düzenleyebilir VEYA YENİkısayol komutları ekleyebilirsiniz:

* NVDA+E: ifadenin yazıldığı şekilde mi yoksa tanımlandığı haliyle mi
  seslendirileceği ile ilgili ayarı değiştirir.
* NVDA + I: yapıştırmak istediğiniz ifadeyi seçmeniz için bir iletişim
  kutusu açar.
* Atanmamış: kopyalamak istediğiniz bir sembolü seçmeniz için bir iletişim
  kutusu gösterir.
* Atanmamış: tüm açıklamanın göz atma modunda gözden geçirilebilmesi için
  inceleme imlecinin konumlandığı sembolü gösteren göz atılabilir bir mesaj
  açar.
* Atanmamış: şapka işaretinin yerleştirildiği sembolü gösteren göz
  atılabilir bir mesaj açar. böylece tüm açıklama tarama kipi modunda gözden
  geçirilebilir.

Not: Windows 10 ve üzeri sürümlerde yerleşik emoji panelini kullanmak da
mümkündür.

## 17.0 için değişiklikler ##

* Sembolleri yazmak için hareketleri ilişkilendirme yeteneği eklendi.
* Çeşitli sembolleri aynı anda kopyalama özelliği eklendi.

## 16.0 için değişiklikler ##

* NVDA 2023.1 ile uyumludur.

## 15.0 için değişiklikler ##

* NVDA 2022.1 veya sonraki sürümünü gerektirir.
* Güvenli modda kullanılamaz.

## 14.0 için değişiklikler ##

* NVDA 2021.1 ile uyumludur.

## 13.0 için değişiklikler ##

* İfade Ekle iletişim kutusundaki hatalar düzeltildi.
* NVDA'nın Noktalama/imla sözlüğünde bulunan bir sembolü eklemek için bir
  iletişim kutusu eklendi.

## 12.0 için değişiklikler ##

* NVDA 2019.3 veya sonraki bir sürümü gerektirir.

## 11.0 için değişiklikler ##

* Eklenti güncellendiğinde, NVDA'nın ana sözlükler klasöründe kayıtlı
  sözlükleri içe aktarmayı tercih etmediğiniz sürece, eklentinin önceki
  sürümünde kaydedilen sözlükler otomatik olarak yeni sürüme
  kopyalanacaktır.
* Sembol, düzeltme işaretinin veya inceleme imlecinin konumlandığı yerde
  gösterilirken, karakter ve Değiştirme sözcükleri, sembolün kendisi ile
  tarama kipi modundaki açıklaması arasında ayrım yapmak için kullanılır ve
  bu, konuşma kullanıcıları için yararlıdır.

## 10.0 için değişiklikler ##

* İnceleme imlecinin veya şapka işaretinin konumlandığı sembolü göstermek
  için komutlar eklendi. Bu komutlar için hareketler, Girdi hareketleri
  iletişim kutusundaki Metin inceleme kategorisinden atanabilir.

## 9.0 için değişiklikler ##

* Eklenti emojilerinin konuşulup konuşulmayacağını seçme imkanı eklendi.
* Sözlük adları için uygun kodlama kullanıldı, belirli karakterler
  içerdiğinde hatalar düzeltildi.
* Eklentinin çevrilmiş özeti, eklenti yöneticisinden erişilebilen eklenti
  yardımında sunulan başlık için uygun şekilde kullanılır.
* Windows 10'da bulunan emoji panelinden bahseden bir not eklendi.

## 8.0 için değişiklikler ##

* NVDA 2018.3 veya sonraki bir sürümü gerektirir. (gerekli)

## 7.0 için değişiklikler ##

* Aktivasyon ayarları iletişim kutusu NVDA ayarlarındaki bir panele taşındı,
  böylece mevcut profil NVDA ayarları iletişim kutusunun başlığında
  gösterilebilecek.
* İfadeleri Yönet menüsü kaldırıldı: Artık İfade ekle Araçlar menüsünde
  bulunacak ve İfadeleri Özelleştir, İfadeler sözlüğü gibi Konuşma
  sözlükleri altında gösterilecek.
* NVDA 2018.2 veya sonraki bir sürümü gerektirir.
* Gerekirse [NVDA 2017.3 ile uyumlu son sürümü][3] indirebilirsiniz.

## 6.0 için değişiklikler ##

* Farklı profiller için destek eklendi.
* NVDA 2017.4 veya sonraki sürümlerde, yapılandırma ayarları ve özel
  sözlükler, seçilen profillere göre otomatik olarak değişecektir. 2017.3
  veya önceki sürümlerde, eklentileri yeniden yükleyerek (kontrol+NVDA+f3
  tuşlarına basarak) değişiklikleri uygulayabilirsiniz.
* Eklentiyi güncellerken ayarları içe aktarmayı seçerseniz, kullanımdan
  kaldırılan dosyalar (emoticons.ini ve emoticons.dic) kaldırılacak veya bu
  sürüme uyarlanacaktır.

## 5.0 için değişiklikler ##

* Emojiler için destek eklendi.
* Görüntülenen ifadeleri seçmek için bir filtre alanı ve seçim düğmeleri
  eklenerek İfade Ekle iletişim kutusu iyileştirildi.
* Etkinleştirme ayarları iletişim kutusu ve İfade Ekle iletişim kutusu için
  guiHelper'ı kullanma: NVDA 2016.4 veya daha yüksek sürümleri gerektirir

## 4.0 için değişiklikler ##

* Başka bir ayarlar iletişim kutusu etkinken emoji ekle iletişim kutusu
  açılırsa, NVDA ilgili hata mesajını gösterecektir.


## 3.0 için değişiklikler ##

* İfadeleri özelleştir iletişim kutusunda, NVDA 2014.4'ün konuşma
  sözlüklerine göre, bir kalıbın yalnızca tam bir kelime olması durumunda
  eşleşmesi gerektiğini belirtmek artık mümkün.


## 2.0 için değişiklikler ##

* Eklenti yardımına Eklenti Yöneticisi altından ulaşılabilir.


## 1.1 için değişiklikler ##

* Tekrar eden ifade silindi.
* Bazı smileyler eklendi.

## 1.0 için değişiklikler ##

* İlk sürüm.

[[!tag dev stable]]

[3]: https://www.nvaccess.org/addonStore/legacy?file=emo-o
