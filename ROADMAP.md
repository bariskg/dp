# dp Yol Haritasi

Bu belge, yazilim bilgisi olmayan bir kurucu gozuyle projenin adim adim nasil ilerleyecegini tanimlar.

## 1. Vizyon

Amac, Turk mahkeme kararlari ve mevzuat kaynaklarini inceleyip kullaniciya kaynakli dilekce taslagi hazirlayan bir Windows uygulamasi gelistirmektir.

Uygulama sunlari yapmalidir:

- kullanicidan olay ozeti almak
- ilgili mevzuati bulmak
- benzer karar ve emsal kararlari listelemek
- kararlarin neden ilgili oldugunu aciklamak
- dilekce taslagi uretmek
- kullanilan kaynaklari gostermek
- Word/PDF cikti vermek

## 2. Temel prensipler

- Ilk surum kucuk olacak
- Her cikti kaynakli olacak
- Guncel mevzuat kontrol edilecek
- Kisisel veri ve anonimlestirme zorunlu olacak
- Son hukuki karar her zaman insanda olacak

## 3. Ilk kapsam

Ilk surumde tum hukuk alanlari hedeflenmeyecek.

Baslangic icin sadece 1 veya 2 dava turu secilecek.

Onerilen baslangic alanlari:

- iscilik alacagi
- kira alacagi veya tahliye
- icra takibine itiraz
- tuketici uyusmazliklari

Ilk karar:

- Bu listedeki alanlardan birini secmek

## 4. Veri kaynaklari

Ilk asamada takip edilecek temel kaynaklar:

- Mevzuat Bilgi Sistemi
- Resmi Gazete
- UYAP Emsal Karar Arama
- UYAP KYB karar arama
- Anayasa Mahkemesi Kararlar Bilgi Bankasi

Daha sonra eklenebilecek kaynaklar:

- Yargitay karar arama
- Danistay karar arsivi
- BAM karar kaynaklari
- ofis ici dilekce ve karar arsivi

## 5. Neden once veri

Bu proje once bir veri ve arama projesidir.

Ilk hedef "AI egitmek" degil, su altyapiyi kurmaktir:

- belgeleri toplamak
- lokalde saklamak
- temizlemek
- anonimlestirmek
- aranabilir hale getirmek
- ilgili kaynaklari secip AI'a vermek

## 6. AI yaklasimi

Ilk asamada buyuk bir modeli bastan egitmek hedeflenmeyecek.

Dogru ilk yontem:

- lokal veri havuzu
- metin arama
- benzer karar bulma
- RAG yaklasimi ile AI taslak uretimi

Daha sonra gerekiyorsa:

- iyi dilekce ornekleri ile ince ayar
- ozel hukuk dili stili icin ek egitim

## 7. Ilk MVP ozellikleri

Ilk surumde olmasi gerekenler:

- olay ozeti giris ekrani
- mevzuat arama
- karar arama
- secilen kaynaklari listeleme
- AI ile taslak dilekce olusturma
- Word veya PDF disa aktarma

Ilk surumde olmamasi gerekenler:

- tum hukuk alanlari
- mobil uygulama
- tam otomatik UYAP entegrasyonu
- kendi buyuk lokal modelini calistirma
- kurum ici coklu kullanici yonetimi

## 8. Teknik urun sekli

Uygulama hedefi:

- Windows'a kurulan masaustu uygulama
- exe veya installer ile dagitim

Ilk teknik yon:

- masaustu uygulama arayuzu
- lokal veritabani
- veri toplama modulu
- arama modulu
- AI taslak olusturma modulu

## 9. Fazlar

### Faz 1 - Strateji ve kapsam

Hedef:

- dava turunu secmek
- kullanici tipini tanimlamak
- MVP sinirlarini cizmek

Cikti:

- urun tanimi
- ilk ozellik listesi
- oncelik sirasi

### Faz 2 - Veri toplama

Hedef:

- resmi kaynaklardan veri cekme planini kurmak
- belge metadata yapisini belirlemek
- lokal klasor ve veritabani yapisini kurmak

Cikti:

- veri adapter listesi
- belge semasi
- ilk veri arsivi

### Faz 3 - Arama ve eslestirme

Hedef:

- mevzuat ve kararlar arasinda arama yapmak
- konuya gore karar onermek
- dava turune gore filtrelemek

Cikti:

- arama ekrani
- sonuc listesi
- karar detay gorunumu

### Faz 4 - Dilekce uretimi

Hedef:

- secilen olay ozeti ve kaynaklara gore taslak olusturmak
- kaynakli paragraf yapisi kurmak
- istenen formatta cikti vermek

Cikti:

- dilekce taslagi
- kaynak listesi
- Word/PDF export

### Faz 5 - Paketleme ve pilot kullanim

Hedef:

- Windows uygulamasini paketlemek
- gercek kullanici ile test etmek
- hatalari ve eksikleri toplamak

Cikti:

- ilk exe surumu
- test geri bildirimleri
- ikinci faz listesi

## 10. Ilk 30 gun

Bu repo uzerinden ilerlemek icin ilk 30 gunde yapilacaklar:

1. Baslangic dava turunu secmek
2. Uygulamanin hedef kullanicisini netlestirmek
3. MVP ozelliklerini kesinlestirmek
4. Veri kaynaklarini onceliklendirmek
5. Veri yapisini yazmak
6. Teknik mimariyi secmek
7. Ilk ekranlarin taslagini cikarmak

## 11. Bu repoda nasil ilerleyecegiz

Her yeni adim ayri belge veya gorev olarak eklenecek.

Ornek takip duzeni:

- `docs/vision.md`
- `docs/mvp.md`
- `docs/data-sources.md`
- `docs/database-schema.md`
- `docs/ui-flow.md`
- `tasks/todo.md`

## 12. Siradaki adim

Bu repo icin ilk net karar:

- Hangi dava turu ile baslayacagiz?

Bu soru cevaplandiktan sonra bir sonraki belge olarak `docs/mvp.md` hazirlanacak.
