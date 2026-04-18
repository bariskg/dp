# UI Akisi - Bosanma MVP

Bu belge, kullanicinin uygulama icinde hangi ekranlardan hangi sirayla gececegini tanimlar.

Amac, ilk surumde karmasik olmayan, anlasilir ve hizli bir kullanim akisi kurmaktir.

## 1. Genel ilke

Ilk surumde kullanici, uygulamayi acinca ne yapacagini hemen anlamalidir.

Bu nedenle akisin temel mantigi su olacaktir:

1. dosya olustur
2. olay bilgisini gir
3. ilgili kaynaklari gor
4. dilekce taslagini olustur
5. duzenle ve disa aktar

## 2. Ana ekran

Uygulama acildiginda gorulecek ilk ekran `Ana Ekran` olacaktir.

Bu ekranda kullanici su secenekleri gorecektir:

- yeni bosanma dosyasi olustur
- kayitli dosyayi ac
- son calisilan dosyalar
- veri guncelleme durumu

Bu ekranin amaci:

- kullaniciyi karisik menulerle yormamak
- tek tikla yeni isleme baslatmak

## 3. Yeni dosya olusturma ekrani

Kullanici `yeni bosanma dosyasi olustur` dediginde bu ekrana gelir.

Bu ekranda:

- dosya adi
- dava tipi
- kisa not

gibi temel bilgiler alinabilir.

Bu ekranin amaci:

- calismayi kayitli bir dosya mantigina baglamak
- daha sonra ayni dosyaya geri donulebilmesini saglamak

## 4. Kullanici bilgi giris ekrani

Bu ekran, `docs/input-form.md` belgesindeki sorulari kullanir.

Bu ekranda kullanici asama asama bilgi girer:

- dava tipi
- taraf bilgileri
- evlilik bilgileri
- cocuk ve velayet bilgileri
- nafaka ve tazminat talepleri
- olay ozeti
- delil notlari

Bu ekranin davranisi:

- sadece gerekli alanlari gostermek
- kullanicinin verdigi cevaba gore ek sorular acmak
- formu tek seferde cok agir gostermemek

## 5. Ozet ve kontrol ekrani

Kullanici bilgiler tamamlandiginda once bir `Ozet ve Kontrol` ekranina gelir.

Bu ekranda sistem kullanicidan aldigi bilgileri toplu halde gosterir:

- dava tipi
- talepler
- cocuk ve velayet durumu
- olay ozeti
- delil notlari

Bu ekranin amaci:

- hatali veya eksik bilgiyi taslak olusmadan once fark ettirmek
- kullaniciya geri donup duzeltme imkani vermek

## 6. Kaynak onerileri ekrani

Kullanici ozet ekranini onayladiktan sonra sistem ilgili kaynaklari listeler.

Bu ekranda su bolumler bulunur:

- ilgili mevzuat
- ilgili kararlar
- benzer olay ornekleri
- sistemin neden bunlari sectigine dair kisa aciklama

Bu ekranin amaci:

- kullaniciya sistemin neye dayanarak ilerledigini gostermek
- kararlari ve mevzuati gorunur hale getirmek
- kaynak secimini denetlenebilir yapmak

## 7. Dilekce taslagi ekrani

Kullanici kaynaklari inceledikten sonra `Taslak Olustur` adimina gecer.

Bu ekranda sistem:

- dava basligini kurar
- taraf kisimlarini hazirlar
- olaylari duzenler
- hukuki sebepleri yazar
- talepleri listeler
- sonuc ve istem bolumunu olusturur

Bu ekranin sagladigi imkanlar:

- metni duzenleme
- bolum bazli degistirme
- yeniden taslak olusturma
- farkli uslupla tekrar deneme

## 8. Kaynak baglama ekrani

Taslak olustuktan sonra kullanici isterse hangi paragraf hangi kaynakla destekleniyor gorebilir.

Bu ekran veya yan panel su bilgileri gosterebilir:

- paragraf basligi
- dayanilan mevzuat
- dayanilan kararlar
- eksik kaynak uyarisi

Bu ekran ilk surumde cok detayli olmak zorunda degildir; ama kaynak gorunurlugu mutlaka olmalidir.

## 9. Son duzenleme ve disa aktarim ekrani

Bu ekran, kullanicinin son kontrol yaptigi ekrandir.

Bu ekranda sunlar olmali:

- metni kopyalama
- Word olarak disa aktarma
- PDF olarak disa aktarma
- dosya olarak kaydetme

Bu ekranin amaci:

- taslagi son kullanima hazir hale getirmek
- kullanicinin uygulama disinda da belgeyi kullanabilmesini saglamak

## 10. Kayitli dosyaya geri donme akisi

Kullanici daha once actigi bir dosyaya yeniden donebilmelidir.

Bu akista:

- ana ekrandan dosya secilir
- daha once girilen bilgiler yuklenir
- taslak yeniden acilir
- kullanici isterse guncelleme yapar

Bu ozellik ilk surumde cok degerlidir cunku hukuk dosyalari tek oturumda bitmeyebilir.

## 11. Ilk surumde olmamasi gereken ekranlar

Ilk surumde su yapilar gereksiz karmasa yaratabilir:

- cok ayrintili ayarlar menusu
- cok kullanicili yonetim paneli
- gelismis analiz panelleri
- grafik ve rapor ekranlari
- otomatik risk puani ekranlari

## 12. Ilk surumun sade ekran sirasi

Ilk surumde kullanicinin gorecegi ana akim ekranlar su olmalidir:

1. Ana ekran
2. Yeni dosya olustur
3. Bilgi giris formu
4. Ozet ve kontrol
5. Kaynak onerileri
6. Dilekce taslagi
7. Son duzenleme ve disa aktarim

## 13. Bu belgeden sonraki adim

Bir sonraki hazirlanacak belge:

- `docs/database-schema.md`

Bu belgede uygulamanin hangi bilgileri hangi duzende saklayacagi sade bir dille tanimlanacaktir.
