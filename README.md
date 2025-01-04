

# Akıllı Bahçe Sistemi - README

## Proje Hakkında

Bu proje, kullanıcılara bitki türlerine göre çevre koşullarını izleyip önerilerde bulunan bir Akıllı Bahçe Sistemi sağlamaktadır. Bitkilerin büyüme koşullarını en iyi şekilde optimize etmek amacıyla sensör verileri kullanılarak, kullanıcılara sıcaklık, nem, toprak nemi ve ışık seviyeleri hakkında gerçek zamanlı bilgiler verilmektedir. Ayrıca, bitki türlerine göre önerilerde bulunarak, bitkilerin sağlıklı gelişmesini sağlamayı hedeflemektedir.

### Özellikler

- **Bitki Türü Seçimi:** Kullanıcı, önceden tanımlanmış bitki türlerinden birini seçebilir veya yeni bir bitki türü ekleyebilir.
- **Sensör Verileri:** Gerçek zamanlı olarak sıcaklık, nem, toprak nemi ve ışık seviyesi gibi veriler alınır ve kullanıcıya gösterilir.
- **Öneriler:** Kullanıcıya, sensör verileri doğrultusunda bitkilerinin sağlıklı büyümesi için önerilerde bulunulur (örneğin, "Sıcaklık çok düşük, bitkinin sıcaklık seviyesini arttırın").
- **Veri Görselleştirme:** Kullanıcı, sensör verilerini görselleştirmek için bir grafik oluşturabilir.
- **Bitki Profili Yönetimi:** Yeni bitki türleri eklenebilir ve mevcut bitki profilleri güncellenebilir.

### Kullanım

1. **Bitki Türü Seçin:** Akıllı Bahçe Sistemi'ni açtıktan sonra, mevcut bitki türlerinden birini seçebilirsiniz. Eğer yeni bir bitki eklemek isterseniz, "Yeni Ürün Ekle" butonunu kullanabilirsiniz.
2. **Sistemi Başlatın:** "Sistemi Başlat" butonuna tıklayarak sistemi aktif hale getirebilirsiniz. Sistem başladığında, sensör verilerini güncelleyebilir ve önerileri alabilirsiniz.
3. **Sensör Verilerini Güncelleyin:** "Güncelle" butonuna tıklayarak sensör verilerini güncelleyebilir ve yeni verilerle öneriler alabilirsiniz.
4. **Verileri Görselleştir:** "Verileri Görselleştir" butonuna tıklayarak sensör verilerini grafik olarak görüntüleyebilirsiniz.

### Bağımlılıklar

Bu projede kullanılan bazı Python kütüphaneleri:

- **tkinter:** GUI (Grafiksel Kullanıcı Arayüzü) oluşturmak için kullanılır.
- **matplotlib:** Sensör verilerini görselleştirmek için kullanılır.
- **json:** Bitki profillerini kaydetmek ve yüklemek için kullanılır.
- **random:** Sensör verilerini simüle etmek için kullanılır.

### Proje Dosyaları

- **garden_app.py:** Ana uygulama dosyasının bulunduğu Python betiği.
- **plant_profiles.json:** Bitki profillerinin saklandığı dosya. Eğer bu dosya yoksa, varsayılan bitki profilleri kullanılacaktır.

### Kullanıcı Arayüzü

GUI tasarımı, basit ve kullanıcı dostudur:

- **Başlık:** "Akıllı Bahçe Sistemi" yazısı başlık olarak görünür.
- **Bitki Türü Seçimi:** Kullanıcı bir bitki türü seçebilir.
- **Yeni Ürün Ekleme Alanı:** Kullanıcı, yeni bitki türleri ekleyebilir.
- **Sensör Verileri:** Sıcaklık, nem, toprak nemi ve ışık seviyeleri gerçek zamanlı olarak görüntülenir.
- **Sistem Durumu:** Sistem başlatıldığında veya durdurulduğunda kullanıcı bilgilendirilir.
- **Öneriler:** Sistem, bitkinin ihtiyaçlarını karşılamak için önerilerde bulunur.
- **Veri Görselleştirme:** Sensör verilerinin grafik olarak görselleştirilmesi sağlanır.

### Bitki Profilleri

Uygulama varsayılan olarak aşağıdaki bitki profillerini içermektedir:

- **Domates:** Sıcaklık: 20-30°C, Nem: 50-70%, Toprak Nem: 40-70%, Işık Seviyesi: 60-80%
- **Fesleğen:** Sıcaklık: 18-28°C, Nem: 40-60%, Toprak Nem: 50-80%, Işık Seviyesi: 50-70%
- **Biber:** Sıcaklık: 18-32°C, Nem: 50-70%, Toprak Nem: 40-60%, Işık Seviyesi: 70-90%
- **Marul:** Sıcaklık: 15-25°C, Nem: 60-80%, Toprak Nem: 60-90%, Işık Seviyesi: 40-60%

### Bitki Profili Ekleme

Kullanıcı yeni bir bitki türü eklemek istediğinde, bitkinin adı girildikten sonra varsayılan değerlerle birlikte sistemde kaydedilir. Bu yeni bitki profili daha sonra sensör verilerine göre analiz edilir ve önerilerde bulunulur.

### Profil Kaydetme

Bitki profilleri, **plant_profiles.json** dosyasına kaydedilir. Bu dosya kaybolursa, varsayılan profiller kullanılır.
