# Teknoloji Secimi - Bosanma MVP

Bu belge, projenin ilk surumunu hangi teknolojilerle gelistirmenin en mantikli oldugunu sade bir dille anlatir.

Amac, yazilim bilmeyen bir kurucu olarak hangi secimin neden yapildigini anlayabilmendir.

Bu belgede hedef, en teknik veya en modern secimi degil; ilk surum icin en guvenli ve en uygulanabilir secimi yapmaktir.

## 1. Genel prensip

Bu proje icin teknoloji secimi su 4 ihtiyaca gore yapilmalidir:

- Windows'ta calismasi
- masaustu uygulama olarak paketlenebilmesi
- lokal veri saklayabilmesi
- AI ile entegre olabilmesi

Bu nedenle ilk surumde karmasik ve agir mimarilerden kacmak daha dogrudur.

## 2. Ilk surum icin en mantikli teknoloji secimi

Ilk surum icin onerilen yapi:

- arayuz: Python + PySide6
- uygulama mantigi: Python
- lokal veritabani: SQLite
- belge ve ham veri depolama: yerel klasor yapisi
- AI baglantisi: API tabanli model kullanimi
- Windows paketleme: PyInstaller

Bu secim, ilk MVP icin en dengeli secimdir.

## 3. Neden Python

Python bu proje icin en uygun baslangic seceneklerinden biridir.

Nedenleri:

- veri toplama icin cok uygundur
- metin isleme icin cok uygundur
- AI entegrasyonlari kolaydir
- masaustu uygulama tarafinda yeterlidir
- prototip ve MVP hizli gelisir

Bu projede zaten su ihtiyaclar var:

- kaynaklardan veri cekmek
- metin temizlemek
- karar ve mevzuat aramak
- AI ile metin olusturmak

Python bunlarin hepsi icin guclu bir secenektir.

## 4. Neden PySide6

PySide6, Python ile masaustu uygulama yapmak icin uygun bir secenektir.

Avantajlari:

- Windows masaustu uygulamasi icin uygundur
- form ekranlari yapmak kolaydir
- klasik uygulama mantigina yakindir
- exe olarak paketlenebilir

Bu proje icin neden uygundur:

- veri giris formlari gerekir
- sonuc listeleri gerekir
- belge ekrani gerekir
- Word/PDF aktarma adimlari gerekir

Yani ilk surumde web sitesi yerine yerel masaustu uygulama daha anlamlidir.

## 5. Neden SQLite

SQLite, ilk surum icin en pratik veritabani secimidir.

Avantajlari:

- ayri bir sunucu gerekmez
- Windows uygulamasina kolay gomulur
- kurulum yukunu azaltir
- tek kullanicili veya kucuk kullanim icin yeterlidir

Bu projede ilk ihtiyac:

- dosyalari saklamak
- kullanici bilgilerini saklamak
- karar ve mevzuat kayitlarini baglamak
- taslaklari saklamak

Ilk surum icin bunlar icin SQLite yeterlidir.

## 6. Neden API tabanli AI

Ilk surumde buyuk AI modelini bilgisayarda lokal calistirmak onerilmez.

Neden onerilmez:

- guclu donanim ister
- kurulum karmasik olur
- bakim zorlasir
- kaliteyi istikrarli tutmak zorlasir

Ilk surumde daha mantikli yol:

- lokal veri sende olur
- AI modeli bir API uzerinden cagrilir
- modele sadece gerekli kaynaklar gonderilir

Bu yaklasim neden iyi:

- daha hizli baslanir
- daha iyi sonuc alma ihtimali yuksektir
- modeli guncel tutmak daha kolaydir

## 7. Neden yerel klasor yapisi da gerekir

Bu projede sadece veritabani yetmez.

Cunku sunlari da saklamak gerekir:

- ham karar metinleri
- ham mevzuat metinleri
- PDF belgeler
- temizlenmis metin kopyalari
- disa aktarılan dosyalar

Bu nedenle su mantik uygundur:

- metadata ve iliskiler SQLite'ta
- buyuk metin ve belgeler klasorlerde

## 8. Windows paketleme secimi

Ilk surumde Windows'a kurulan uygulama hedeflendigi icin paketleme onemlidir.

Onerilen secim:

- PyInstaller

Neden:

- Python projelerini exe haline getirmek icin yaygin kullanilir
- MVP icin yeterince pratiktir
- ilk surumde hiz kazandirir

Sonraki asamada su secenekler de dusunulebilir:

- Inno Setup ile installer
- daha profesyonel kurulum paketi

Ama ilk asamada zorunlu degildir.

## 9. Simdilik onerilmeyen secenekler

Ilk surumde asagidaki secenekler gereksiz karmasa yaratabilir:

### 9.1 Electron

Artisi:

- guclu arayuz imkanlari sunar

Eksisi:

- ilk MVP icin daha agir olabilir
- Python ile iki katmanli kurgu gerekir

### 9.2 Tauri

Artisi:

- hafif olabilir

Eksisi:

- teknik kurulum ve gelistirme sureci daha zor olabilir

### 9.3 Postgres

Artisi:

- buyuk sistemler icin gucludur

Eksisi:

- ilk surumde gereksiz kurulum yuk getirir

### 9.4 Tam lokal LLM

Artisi:

- veri cihazdan cikmadan calisma imkani olabilir

Eksisi:

- donanim ve kalite problemi cikabilir
- ilk MVP'yi yavaslatir

## 10. Onerilen ilk teknik yapi

Bu proje icin ilk uygulama yapisi sade sekilde su olabilir:

- masaustu arayuz
- dosya kayit sistemi
- veri toplama ve arsivleme modulu
- karar ve mevzuat arama modulu
- AI ile taslak uretim modulu
- Word/PDF aktarma modulu

Teknik olarak bu su anlama gelir:

- PySide6 ekranlari
- Python servis mantigi
- SQLite veritabani
- yerel `data/` klasoru
- API ile AI cagrisi

## 11. Gelecekte nasil buyur

Uygulama basarili olursa sonraki fazlarda su gelisimler yapilabilir:

- Postgres'e gecis
- gelismis arama motoru
- web paneli ekleme
- ekip kullanimi
- daha guclu raporlama
- lokal model destegi

Ama bunlar ilk surumde zorunlu degildir.

## 12. Son karar onerisi

Bu proje icin ilk surumde resmi onerim su:

- Python
- PySide6
- SQLite
- yerel dosya klasorleri
- API tabanli AI
- PyInstaller

Bu kombinasyon, maliyet, hiz ve uygulanabilirlik acisindan ilk surum icin en guvenli secimdir.

## 13. Bu belgeden sonraki adim

Bir sonraki hazirlanacak belge:

- `docs/build-plan.md`

Bu belgede artik dokuman asamasindan uygulama asamasina gecip, hangi sirayla neyin yapilacagi haftalik ve somut bir plan olarak yazilacaktir.
