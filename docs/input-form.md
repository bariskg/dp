# Kullanici Giris Formu - Bosanma

Bu belge, kullanicidan bosanma dilekcesi taslagi uretmek icin hangi bilgilerin alinacagini tanimlar.

Amac, kullaniciyi yormayan ama sistemin dogru taslak uretebilmesi icin yeterli bilgi veren bir form yapisi kurmaktir.

## 1. Form tasarim ilkesi

Ilk surumde form:

- kisa olacak
- sade olacak
- zorunlu ve opsiyonel alanlari ayiracak
- hukuki jargon kullanmadan da doldurulabilecek
- sonradan gelistirilmeye uygun olacak

## 2. Formun genel akisi

Ilk surumde form 5 bolumden olusacaktir:

1. dava tipi
2. taraf ve aile bilgileri
3. cocuk ve velayet bilgileri
4. talepler
5. olay ozeti

## 3. Zorunlu alanlar

Bu alanlar ilk surumde zorunlu olmalidir.

### 3.1 Dava tipi

- anlasmali bosanma
- cekismeli bosanma

Bu soru onemlidir cunku sistemin kullanacagi dil ve taslak yapisi buna gore degisecektir.

### 3.2 Taraf bilgileri

- davaci kim
- davali kim

Not:

Ilk surumde ad soyad zorunlu olmayabilir. Sistem, taslak uretirken `Davaci` ve `Davali` gibi yer tutucular kullanabilir.

### 3.3 Evlilik bilgisi

- evlilik tarihi
- taraflar su an fiilen ayri mi

### 3.4 Olay ozeti

Kullanicidan serbest metin olarak su bilgi alinmalidir:

- bosanma gerekcesi nedir
- temel anlasmazliklar nelerdir
- surec nasil gelisti

Bu alan, sistemin karar ve mevzuat secimi icin en kritik alanlardan biridir.

## 4. Yari zorunlu alanlar

Bu alanlar her dosyada gerekmeyebilir; ancak ilgili durum varsa sorulmalidir.

### 4.1 Cocuk bilgisi

- ortak cocuk var mi
- cocuk sayisi
- cocuklarin yaslari

### 4.2 Velayet

- velayet talebi var mi
- velayet kime verilsin isteniyor
- karsi tarafla kisisel iliski talebi var mi

### 4.3 Nafaka

- tedbir nafakasi talebi var mi
- yoksulluk nafakasi talebi var mi
- istirak nafakasi talebi var mi

### 4.4 Tazminat

- maddi tazminat talebi var mi
- manevi tazminat talebi var mi

## 5. Opsiyonel alanlar

Bu alanlar ilk surumde istege bagli olabilir.

- ayrilik tarihi
- siddet iddiasi var mi
- aldatma iddiasi var mi
- ekonomik destek saglanmadigi iddiasi var mi
- evden ayrilma veya terk iddiasi var mi
- sosyal medya, mesaj, tanik gibi delil var mi
- daha once acilmis dava veya uzaklastirma karari var mi
- kullanicinin ozel notlari

Bu alanlar sonraki surumlerde daha akilli soru akisi icin kullanilabilir.

## 6. Ilk surumde formun davranisi

Form, kullaniciyi tek seferde cok soruyla bogmamali.

Bu nedenle ilk davranis soyle olmalidir:

- once temel sorular sorulur
- kullanicinin secimine gore ek alanlar acilir

Ornek:

- kullanici `ortak cocuk var` derse cocuk ve velayet alanlari acilir
- kullanici `nafaka talebi var` derse nafaka turleri sorulur
- kullanici `tazminat talebi var` derse maddi ve manevi secenekleri acilir

## 7. Formdan beklenen teknik cikti

Bu formun sonunda sistem asagidaki gibi yapilandirilmis bilgiye sahip olmalidir:

- dava tipi
- aile yapisi
- cocuk durumu
- velayet talebi
- nafaka talepleri
- tazminat talepleri
- olay ozeti
- delil notlari

Bu yapi daha sonra:

- karar arama
- mevzuat eslestirme
- dilekce taslagi uretimi

icin kullanilacaktir.

## 8. Ilk surum icin sade soru listesi

Kullanicinin gorecegi ilk soru listesi su sekilde olabilir:

1. Dava tipi nedir
2. Bosanma talebi anlasmali mi, cekismeli mi
3. Taraflarin rol dagilimi nedir
4. Evlilik tarihi nedir
5. Taraflar fiilen ayri mi
6. Ortak cocuk var mi
7. Velayet talebiniz var mi
8. Nafaka talebiniz var mi
9. Maddi veya manevi tazminat talebiniz var mi
10. Olayi kisaca anlatin
11. Elinizde hangi deliller var
12. Eklemek istediginiz ozel bir not var mi

## 9. Ilk surumde formun yapmayacagi seyler

Ilk surumde form:

- kullanicidan asiri ayrintili hukuki analiz istemeyecek
- otomatik kusur puanlamasi yapmayacak
- belge yukleme zorunlulugu getirmeyecek
- ilk ekranda 30 farkli soru gostermeyecek

## 10. Bu belgeden sonraki adim

Bir sonraki hazirlanacak belge:

- `docs/ui-flow.md`

Bu belgede kullanicinin uygulama icinde hangi ekranlardan hangi sirayla gececegi anlatilacaktir.
