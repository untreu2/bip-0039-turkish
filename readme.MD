Orjinali İngilizce olan, Bitcoin özel anahtar yaratım sürecinde kullanılan kelimelerin Türkçe versiyonudur.

Kurallar:

1. Kelimeler en az 3, en fazla 8 harften oluşmalı. (okul✅, yol✅, anahtar✅, su🚫, ornitorenk🚫)
2. Kelimelerin ilk 3 harfi şu an ki İngilizce, Türkçe ve diğer dillerdeki seed kelimelerden farklı olmalı. (artist🚫, atom🚫, yemek✅)
3. Kelimelerde simge, büyük harf, Türkçe'ye özgü harf ve semboller olmamalıdır. (çşöüığâ) (okul ✅, içecek 🚫, hâla 🚫, öğretmen 🚫)
4. Eğer kullanılacak kelime fiil ise, emir kipi kullanılmalı ve -yapmak -etmek gibi iki kelimeden oluşan fiiller kullanılmamalıdır.
5. Harflerin arasında boşluk olmamalıdır.  (piyasa✅, ucundan tut🚫)
6. Eş anlamlı kelimeler olabildiğince kullanılmamalıdır.
7. Türkçe kelimelerde en az 2 harf farklı olacaktır.(keman✅ - kemer✅ - kenar✅, tepe✅ - tepki✅ - terfi✅ - tere🚫 )
8. Özel isim kullanılmamalıdır.
9. İyelik eki kullanılmamalıdır.

- Diğer dillerdeki kelimelere ve İngilizce dilindeki orjinal kelimelere other_languages klasöründen ulaşılabilir: https://github.com/efecini-plentific/bip-0039-turkish/tree/master/other_languages

- Eklenmiş kelimelerin son haline final isimli dosyadan ulaşılabilir: https://github.com/efecini-plentific/bip-0039-turkish/blob/master/HELPER_FILES/final.txt

- Kelimelerin daha önceki versiyonlarına şuradan ulaşabilirsiniz. https://github.com/efecini-plentific/bip-0039-turkish/tree/master/do_not_change


2048 kelime bulunduktan sonra yapılacak son kontroller
- Son kontrollerde şunları her harfle başlayan kelimeler için bulk olarak şunları yap:
(Google Sheet Belgesi aç. Tüm harfler için ayrı sayfalar aç, başta Kaan ve Emir olmak üzere, kontrol etmek isteyenlere izin ver.
Kontrolleri yapanlar check koyabilir. En az 1 fail olursa yeni kelime ekle. Dağıtık iş kanıtı.)

1. TDK'dan imla ve anlam kontrolü. Uymayan harf kontrolü
2. Eş anlamlı başka bir kelime var mı?
3. Bilinen bir kelime mi? Çok fazla İngilizce veya Arapçaya mı kayıyor?
4. Kötü/argo/şiddet içeren kelime kontrolü.(Örn:tosuncuk, pezevenk)
5. Aynı harfte işk 4 kelime kontrolü.
6. Hayat görüşümüze ters kelimeler var mı? (Örnek:nihilist)
7. Özel isim kontrolü
