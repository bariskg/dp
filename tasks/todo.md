# Gorev Listesi - Bosanma MVP

Bu belge, projenin uygulama asamasinda tek tek yapilacak isleri listeler.

Amac, teorik plani somut gorevlere cevirmek ve nereden baslayacagimizi netlestirmektir.

## 1. Calisma kurali

Bu listede gorevler su mantikla yazilmistir:

- once temel sistem
- sonra veri ve ekranlar
- sonra AI
- sonra paketleme

Her gorev mumkun oldugunca kucuk tutulmalidir.

## 2. Faz 1 - Proje kurulumu

### Yapilacaklar

- [ ] proje klasor yapisini olustur
- [ ] `app/` klasorunu olustur
- [ ] `data/` klasorunu olustur
- [ ] `docs/` klasorunu koru
- [ ] `tasks/` klasorunu koru
- [ ] temel Python giris dosyasini ekle
- [ ] temel PySide6 pencere iskeletini olustur
- [ ] temel SQLite baglantisini kur
- [ ] ilk veritabani dosyasini olustur
- [ ] `requirements.txt` dosyasini olustur

### Tamamlanma olcutu

- uygulama pencere aciyor olmali
- veritabani dosyasi olusuyor olmali

## 3. Faz 2 - Dosya mantigi

### Yapilacaklar

- [ ] yeni dosya olusturma ekranini yap
- [ ] dosya listesi ekranini yap
- [ ] dosya kaydetme mantigini ekle
- [ ] dosya acma mantigini ekle
- [ ] dosya guncelleme mantigini ekle
- [ ] dosya durum alanini ekle

### Tamamlanma olcutu

- kullanici yeni bosanma dosyasi olusturabilmeli
- dosya tekrar acilabilmeli

## 4. Faz 3 - Giris formu

### Yapilacaklar

- [ ] dava tipi alanini ekle
- [ ] taraf bilgileri alanlarini ekle
- [ ] evlilik bilgileri alanlarini ekle
- [ ] cocuk bilgileri alanlarini ekle
- [ ] velayet alanlarini ekle
- [ ] nafaka alanlarini ekle
- [ ] tazminat alanlarini ekle
- [ ] olay ozeti alanini ekle
- [ ] delil notlari alanini ekle
- [ ] kosullu alan acma davranisini ekle

### Tamamlanma olcutu

- form doldurulup veritabanina kaydedilebilmeli

## 5. Faz 4 - Ozet ekrani

### Yapilacaklar

- [ ] kullanici girdilerini tek ekranda goster
- [ ] duzenle butonu ekle
- [ ] eksik bilgi uyarisi ekle
- [ ] onayla ve devam et akisini ekle

### Tamamlanma olcutu

- kullanici taslaga gecmeden once girdilerini kontrol edebilmeli

## 6. Faz 5 - Ornek veri ve veri modeli testi

### Yapilacaklar

- [ ] ornek mevzuat kayitlari ekle
- [ ] ornek karar kayitlari ekle
- [ ] mevzuat tablosunu test et
- [ ] karar tablosunu test et
- [ ] dosya ile kaynak bagini test et

### Tamamlanma olcutu

- sistem test verisiyle kaynak gosterebilmeli

## 7. Faz 6 - Kaynak listeleme

### Yapilacaklar

- [ ] ilgili mevzuat listesini goster
- [ ] ilgili karar listesini goster
- [ ] temel filtreleme ekle
- [ ] secilen kaynagi dosyaya bagla
- [ ] kullanicinin kaynak secmesini sagla

### Tamamlanma olcutu

- kullanici bosanma dosyasina uygun kaynaklari gorebilmeli

## 8. Faz 7 - AI entegrasyonu

### Yapilacaklar

- [ ] AI baglanti katmanini olustur
- [ ] API anahtari yapisini belirle
- [ ] istem gonderme fonksiyonunu yaz
- [ ] prompt yapisini hazirla
- [ ] secilen kaynaklari prompt icine koy
- [ ] ilk dilekce taslagi uretimini calistir

### Tamamlanma olcutu

- sistem secilen bilgiler ve kaynaklarla taslak uretebilmeli

## 9. Faz 8 - Taslak duzenleme ekrani

### Yapilacaklar

- [ ] taslak metin ekranini yap
- [ ] metin duzenleme ozelligi ekle
- [ ] yeniden taslak olustur butonu ekle
- [ ] kaynak listesini yan panelde goster

### Tamamlanma olcutu

- kullanici taslagi okuyup duzenleyebilmeli

## 10. Faz 9 - Disa aktarim

### Yapilacaklar

- [ ] Word export ekle
- [ ] PDF export ekle
- [ ] metni kopyalama ekle
- [ ] cikti dosyasini klasore kaydet

### Tamamlanma olcutu

- kullanici belgeyi uygulama disina alabilmeli

## 11. Faz 10 - Testler

### Yapilacaklar

- [ ] anlasmali bosanma senaryosu test et
- [ ] cekismeli bosanma senaryosu test et
- [ ] velayet talepli senaryoyu test et
- [ ] nafaka talepli senaryoyu test et
- [ ] tazminat talepli senaryoyu test et
- [ ] eksik veriyle form test et
- [ ] kaynak secilmeden taslak testi yap

### Tamamlanma olcutu

- kritik akislarda uygulama hata vermemeli

## 12. Faz 11 - Paketleme

### Yapilacaklar

- [ ] PyInstaller konfigurasyonunu yap
- [ ] exe olustur
- [ ] temiz bilgisayarda acilis testi yap
- [ ] veri klasoru erisimini test et

### Tamamlanma olcutu

- uygulama exe olarak acilabilmeli

## 13. Ilk yapilacak 10 is

Projeye hemen baslamak icin ilk 10 gorev:

1. [ ] `app/` klasorunu olustur
2. [ ] `data/` klasorunu olustur
3. [ ] temel Python uygulama dosyasini ekle
4. [ ] temel PySide6 pencereyi ac
5. [ ] `requirements.txt` olustur
6. [ ] SQLite baglantisini kur
7. [ ] ilk veritabani dosyasini olustur
8. [ ] ana ekran iskeletini yap
9. [ ] yeni dosya olustur ekranini yap
10. [ ] bosanma giris formunun ilk ekranini yap

## 14. Bu belgeden sonraki adim

Bir sonraki en gerekli adim:

- repo icinde gercek uygulama klasor yapisini olusturmak

Yani artik dokuman yazmayi birakip kod tabanini kurmaya baslayabiliriz.
