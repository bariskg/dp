# Veritabani Semasi - Bosanma MVP

Bu belge, uygulamanin ilk surumde hangi bilgileri saklayacagini sade bir dille tanimlar.

Amac, yazilim gelistirilirken hangi bilgi nereye kaydedilecek sorusunu en bastan netlestirmektir.

Bu belge teknik kod seviyesinde degil; urun mantigi seviyesinde bir veri semasidir.

## 1. Genel ilke

Uygulama ilk surumde asagidaki veri turlerini saklayacaktir:

- kullanicinin actigi dosyalar
- kullanicinin girdigi olay bilgileri
- sistemin buldugu mevzuat
- sistemin buldugu kararlar
- olusturulan dilekce taslaklari
- kullanilan kaynak baglantilari

Ilk surumde amac, az ama duzenli veri tutmaktir.

## 2. Ana veri yapilari

Ilk surum icin temel tablolar veya veri gruplari sunlar olmalidir:

1. dosyalar
2. taraf bilgileri
3. cocuk bilgileri
4. talepler
5. olay ozeti ve notlar
6. mevzuat kayitlari
7. karar kayitlari
8. kaynak eslestirmeleri
9. dilekce taslaklari

## 3. Dosyalar

Her calisma bir `dosya` mantigi ile tutulmalidir.

Bu yapida asgari alanlar:

- dosya kimligi
- dosya adi
- dava tipi
- olusturma tarihi
- son guncelleme tarihi
- durum

Durum alanina ornekler:

- taslak
- incelemede
- tamamlandi

Bu yapi neden onemli:

- kullanici ayni anda birden fazla dosya uzerinde calisabilir
- kayitli dosyaya sonradan geri donulebilir

## 4. Taraf bilgileri

Her dosyada taraflara ait temel bilgiler saklanmalidir.

Asgari alanlar:

- dosya kimligi
- davaci tipi veya etiketi
- davali tipi veya etiketi
- evlilik tarihi
- fiili ayrilik durumu
- ayrilik tarihi

Ilk surumde taraf isimleri zorunlu olmayabilir.

Sistem ilk asamada su sekilde de calisabilir:

- Davaci
- Davali

yer tutuculari ile taslak uretmek.

## 5. Cocuk bilgileri

Her dosyada cocuk bilgileri ayri tutulmalidir.

Asgari alanlar:

- dosya kimligi
- ortak cocuk var mi
- cocuk sayisi
- cocuklarin yas bilgileri
- ozel not

Bu yapi neden ayri tutulmali:

- her dosyada cocuk bilgisi olmayabilir
- velayet ve nafaka talepleriyle kolayca bag kurulur

## 6. Talepler

Bu tablo veya veri grubu, kullanicinin ne istedigini saklar.

Asgari alanlar:

- dosya kimligi
- velayet talebi var mi
- velayet talebinin yonu
- kisisel iliski talebi var mi
- tedbir nafakasi talebi var mi
- yoksulluk nafakasi talebi var mi
- istirak nafakasi talebi var mi
- maddi tazminat talebi var mi
- manevi tazminat talebi var mi

Bu yapi neden onemli:

- sistemin hangi mevzuati ve hangi kararlari one cikaracagini belirler
- dilekce sonuc ve istem bolumunu otomatik kurmayi kolaylastirir

## 7. Olay ozeti ve notlar

Her dosya icin kullanicidan gelen serbest metinler ayri tutulmalidir.

Asgari alanlar:

- dosya kimligi
- olay ozeti
- delil notlari
- kullanici ozel notu

Bu alanlar daha sonra:

- karar arama
- konu tespiti
- AI taslak uretimi

icin kullanilacaktir.

## 8. Mevzuat kayitlari

Sistem tarafindan bulunan mevzuat kayitlari ayri tutulmalidir.

Asgari alanlar:

- mevzuat kimligi
- kaynak adi
- kanun veya mevzuat adi
- madde numarasi
- baslik
- metin
- belge linki
- guncellenme tarihi

Bu yapi neden onemli:

- ayni mevzuat birden fazla dosyada tekrar kullanilabilir
- guncellik kontrolu daha kolay yapilir

## 9. Karar kayitlari

Sistem tarafindan bulunan kararlar ayri tutulmalidir.

Asgari alanlar:

- karar kimligi
- kaynak adi
- mahkeme veya daire bilgisi
- karar tarihi
- esas numarasi
- karar numarasi
- konu etiketi
- kisa ozet
- tam metin veya temiz metin
- belge linki
- anonimlestirme durumu

Bu yapi neden onemli:

- ayni karar birden fazla dosyada kullanilabilir
- kararlari etiketleyip aramak kolaylasir

## 10. Kaynak eslestirmeleri

Bu yapi, hangi dosyada hangi kaynaklarin kullanildigini saklar.

Asgari alanlar:

- dosya kimligi
- kaynak tipi
- kaynak kimligi
- secilme nedeni
- kullanici onayi var mi

Kaynak tipi ornekleri:

- mevzuat
- karar

Bu yapi neden onemli:

- her dosyanin hangi dayanaklarla olusturuldugu izlenebilir
- taslak ile kaynaklar arasinda bag kurulur

## 11. Dilekce taslaklari

Uretilen her taslak ayri kayit olarak tutulmalidir.

Asgari alanlar:

- taslak kimligi
- dosya kimligi
- surum numarasi
- taslak metni
- olusturma tarihi
- son duzenleme tarihi
- durum

Durum ornekleri:

- ilk taslak
- duzenlenmis taslak
- son cikti

Bu yapi neden onemli:

- kullanici farkli taslak versiyonlarini gorebilir
- eski metinlere geri donulebilir

## 12. Iliski mantigi

Ilk surumde veri iliskileri sade olmalidir.

Ana baglar su sekilde dusunulmelidir:

- bir dosyanin bir taraf bilgi kaydi olur
- bir dosyanin sifir veya bir cocuk bilgi kaydi olur
- bir dosyanin bir talep kaydi olur
- bir dosyanin bir olay ozeti kaydi olur
- bir dosyanin birden fazla kaynak eslestirmesi olabilir
- bir dosyanin birden fazla taslagi olabilir

Bu sade yapi, ilk surum icin yeterlidir.

## 13. Ilk surumde saklanmamasi gerekenler

Ilk surumde su veri tiplerini zorunlu tutmamak daha dogrudur:

- gelismis kullanici hesap sistemi
- ayrintili rol ve yetki yapisi
- tum islem loglari
- otomatik risk puanlari
- performans istatistikleri

Bunlar sonraki asamalarda eklenebilir.

## 14. Dosya bazli dusunme mantigi

Bu projede en onemli tasarim karari `dosya bazli` calismaktir.

Yani her sey bir dosyanin etrafinda toplanir:

- girilen bilgiler
- secilen kaynaklar
- olusturulan taslaklar

Bu yaklasim, hukuk burolarinin gercek is akisina daha uygundur.

## 15. Bu belgeden sonraki adim

Bir sonraki hazirlanacak belge:

- `docs/tech-stack.md`

Bu belgede bu urunu kurmak icin hangi teknoloji seceneklerinin uygun oldugu yazilim bilmeyen biri icin sade bir dille anlatilacaktir.
