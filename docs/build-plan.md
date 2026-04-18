# Yapim Plani - Bosanma MVP

Bu belge, projenin artik dokuman asamasindan uygulama asamasina nasil gececegini adim adim tanimlar.

Amac, neyin hangi sirayla yapilacagini netlestirmek ve projeyi kontrol edilebilir parcalara bolmektir.

Bu plan, ilk calisan surume ulasmayi hedefler.

## 1. Genel hedef

Ilk hedefimiz su olacak:

- Windows'ta acilan
- bosanma dosyasi olusturabilen
- kullanicidan bilgi alabilen
- ilgili kaynaklari listeleyebilen
- kaynakli dilekce taslagi olusturabilen

bir MVP uygulamasi cikarmak.

## 2. Genel calisma mantigi

Bu proje tek seferde degil, asama asama yapilmalidir.

Dogru sira su olacaktir:

1. proje iskeleti
2. veri yapisi
3. arayuz iskeleti
4. lokal dosya ve veri kaydi
5. veri kaynaklarinin ilk baglantisi
6. arama ve kaynak secimi
7. AI ile taslak uretimi
8. disa aktarim
9. paketleme

## 3. Faz 1 - Proje iskeleti

Ilk yapilacak is, kod tarafinda bos bir ama duzenli temel kurmaktir.

Bu fazda yapilacaklar:

- proje klasor yapisini kurmak
- temel Python uygulama yapisini kurmak
- PySide6 pencere iskeletini acmak
- SQLite baglantisini hazirlamak
- temel `data/` klasorlerini olusturmak

Bu fazin ciktilari:

- uygulama aciliyor olmali
- ana pencere gorunmeli
- veritabani dosyasi olusmali
- veri klasorleri hazir olmali

## 4. Faz 2 - Dosya mantigi ve veri girisi

Bu fazda artik kullanici bir bosanma dosyasi olusturabilmelidir.

Yapilacaklar:

- yeni dosya olusturma ekrani
- giris formunun ilk surumu
- kaydetme ve yeniden acma
- ozet ve kontrol ekrani

Bu fazin ciktilari:

- kullanici yeni dosya acabilmeli
- formu doldurabilmeli
- bilgiler SQLite'a kaydolmali
- daha sonra ayni dosya tekrar acilabilmeli

## 5. Faz 3 - Ilk veri altyapisi

Bu fazda sistemin hukuk verisiyle bag kurmasi baslar.

Yapilacaklar:

- mevzuat icin ilk veri yapisini kurmak
- ornek karar kaydi yapisini kurmak
- local arsiv klasorlerini netlestirmek
- manuel veri ekleme veya test verisi yukleme

Bu fazda amac, once gercek veri cekmekten cok veri modelini canlandirmaktir.

Bu fazin ciktilari:

- ornek mevzuat kayitlari sisteme eklenmis olmali
- ornek karar kayitlari sisteme eklenmis olmali
- arama ekranlari icin veri tabani hazir olmali

## 6. Faz 4 - Kaynak listeleme ve arama

Bu fazda kullanici girdigi olay bilgisine gore ilgili kaynaklari gorebilmelidir.

Yapilacaklar:

- mevzuat listeleme ekrani
- karar listeleme ekrani
- temel filtreler
- olay ozetine gore basit eslestirme mantigi

Bu fazin ciktilari:

- sistem ilgili mevzuati gostermeli
- sistem ilgili kararlari gostermeli
- kullanici kaynak secimi yapabilmeli

## 7. Faz 5 - AI ile dilekce taslagi

Bu faz, projenin ilk buyuk gorunen ama kontrollu adimidir.

Yapilacaklar:

- AI baglantisini kurmak
- modele gonderilecek veri yapisini belirlemek
- taslak prompt mantigini yazmak
- kaynakli dilekce taslagi uretmek
- ilk duzenleme ekranini yapmak

Bu fazin ciktilari:

- sistem girilen olay bilgisi ve secilen kaynaklarla taslak uretebilmeli
- taslak ekranda duzenlenebilir olmali
- kaynak listesi gorunmeli

## 8. Faz 6 - Disa aktarim

Bu fazda uretilen taslak uygulama disinda kullanilabilir hale gelir.

Yapilacaklar:

- Word export
- PDF export
- dosya kaydetme

Bu fazin ciktilari:

- kullanici olusturdugu metni disa aktarabilmeli
- belgeyi uygulama disinda da kullanabilmeli

## 9. Faz 7 - Test ve duzeltme

Bu faz, ilk kullanimdan once cok onemlidir.

Yapilacaklar:

- 5 ila 10 test senaryosu belirlemek
- anlasmali bosanma testi
- cekismeli bosanma testi
- velayet talepli dosya testi
- nafaka talepli dosya testi
- tazminat talepli dosya testi

Bu fazin ciktilari:

- eksik alanlar gorulmeli
- yanlis akilar duzeltilmeli
- metin kalitesi not edilmeli

## 10. Faz 8 - Windows paketleme

Bu fazda uygulama dagitilabilir hale getirilir.

Yapilacaklar:

- PyInstaller ile exe almak
- veri klasoru yapisini korumak
- temel kurulum veya tasinabilir surum hazirlamak

Bu fazin ciktilari:

- uygulama tek bilgisayarda kurularak calisabilmeli
- uygulama acilisinda temel hata vermemeli

## 11. Onerilen zamanlama

Bu proje icin ilk sade zamanlama su olabilir:

### 1. hafta

- proje klasor yapisi
- temel uygulama iskeleti
- veritabani baglantisi

### 2. hafta

- dosya olusturma
- bilgi giris formu
- kaydetme ve acma

### 3. hafta

- test verisi ile mevzuat ve karar kayitlari
- listeleme ekranlari
- temel eslestirme

### 4. hafta

- AI taslak uretimi
- taslak ekrani
- ilk duzenleme

### 5. hafta

- Word/PDF aktarim
- test senaryolari
- hata duzeltmeleri

### 6. hafta

- exe paketleme
- pilot kullanim
- geri bildirim toplama

## 12. Ilk gelistirme sirasi

Yazilim yazilmaya baslandiginda gorev sirasi su olmalidir:

1. uygulama iskeleti
2. veritabani ve dosya kaydi
3. bilgi giris formu
4. ozet ekrani
5. ornek veri yukleme
6. kaynak listeleme
7. AI baglantisi
8. taslak uretimi
9. export
10. paketleme

## 13. Bu planin en kritik noktasi

Bu projede en onemli hata, AI tarafina cok erken kosmak olur.

Bu nedenle ilk kural sunun etrafinda kurulur:

- once veri ve ekran akisi
- sonra AI

Bu sayede proje daha az riskle ilerler.

## 14. Bu belgeden sonraki adim

Bir sonraki hazirlanacak belge:

- `tasks/todo.md`

Bu belgede artik teorik plan degil, tek tek yapilacak isler gorev listesi haline getirilecektir.
