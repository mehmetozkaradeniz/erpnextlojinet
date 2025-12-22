# Lojinet - Kapsamlı Lojistik Yönetim Sistemi

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![ERPNext](https://img.shields.io/badge/ERPNext-v14%2B-orange)
![License](https://img.shields.io/badge/license-MIT-green)

Lojinet, ERPNext için geliştirilmiş **eksiksiz** bir lojistik, depolama ve SaaS yönetim sistemidir.

## ✨ Özellikler

### 📦 Temel Modüller

#### Cari Yönetimi
- ✅ Detaylı cari kartları
- ✅ Çoklu adres yönetimi
- ✅ Çoklu mail desteği
- ✅ Vergi numarası validasyonu
- ✅ Müşteri temsilcisi atama

#### Lojistik
- ✅ **Mal Kabul**: Depoya gelen ürünlerin sayımı ve kaydı
  - Otomatik toplam hesaplama
  - PDF ile mail gönderme
  - Rampa ve araç bilgileri
- ✅ **Yük Yönetimi**: Müşteri irsaliyelerinin kaydı ve takibi
  - Benzersiz referans numarası
  - **Otomatik stok kontrolü** (Ürün Bekleniyor/Depoda/Araçta)
  - Fiyat modeli entegrasyonu
  - Excel ile toplu ürün ekleme
  - 3 TAB yapısı (Bilgiler/Fiyatlar/Tarihler)
- ✅ **Operasyon**: Sefer yönetimi ve takip
  - Toplu yük ekleme
  - Otomatik statü güncelleme
  - Navlun hesaplama
- ✅ **Araç ve Şoför Yönetimi**
  - Sigorta takibi
  - Ehliyet ve SRC belge kontrolü

#### Depolama
- ✅ Depo kartları
- ✅ Depo giriş/çıkış takibi
- ✅ Stok kontrolü

#### Muhasebe
- ✅ **Fatura Yönetimi**
  - Yükten otomatik fatura oluşturma
  - Faturalandırma durumu takibi
- ✅ **Ödeme/Tahsilat**
  - Nakit, Havale, Çek
  - Çek havuzu yönetimi
- ✅ **Çek İşlemleri**
  - Portföy yönetimi
  - Ciro, tahsil, iade takibi
- ✅ **Fiyat Anlaşmaları**
  - Müşteri bazlı fiyatlandırma
  - Kalem detayları
- ✅ **Online Mutabakat**
  - Link ile onay/red sistemi
  - IP adresi kaydı

#### B2B Müşteri Portalı
- ✅ Kullanıcı oluşturma (API)
- ✅ İrsaliye takibi
- ✅ Destek bileti sistemi
  - 12 saat otomatik kapatma
  - Müşteri temsilcisi atama
- ✅ Evrak galeri
  - Yıl/ay klasörleri
  - Önizlemeli galeri

#### SaaS Yönetimi
- ✅ Paket yönetimi
- ✅ Müşteri kartları
- ✅ Abonelik takibi

### 🚀 Teknik Özellikler

- **22 DocType** (Ana + Child tablolar)
- **Python API fonksiyonları**
- **Client-side JavaScript**
- **Web portal sayfaları** (B2B, Mutabakat)
- **Otomatik hesaplamalar**
- **Scheduler görevleri** (günlük/haftalık)
- **Custom CSS** ve UI iyileştirmeleri
- **Mail entegrasyonu**

## 📋 DocType Listesi

### Ana DocType'lar (22 adet)

| DocType | Açıklama | Submittable |
|---------|----------|-------------|
| Lojinet Cari | Cari kartları | ❌ |
| Lojinet Cari Adres | Adres detayları (Child) | ❌ |
| Lojinet Arac | Araç yönetimi | ❌ |
| Lojinet Sofor | Şoför kartları | ❌ |
| Lojinet Mal Kabul | Mal kabul işlemleri | ✅ |
| Lojinet Mal Kabul Detay | Kalemler (Child) | ❌ |
| Lojinet Yuk | Yük/İrsaliye | ✅ |
| Lojinet Yuk Detay | Kalemler (Child) | ❌ |
| Lojinet Yuk Fiyat | Fiyatlar (Child) | ❌ |
| Lojinet Sefer | Sefer planlama | ✅ |
| Lojinet Sefer Yuk | Sefer yükleri (Child) | ❌ |
| Lojinet Fiyat Anlasmasi | Fiyat anlaşmaları | ❌ |
| Lojinet Fiyat Anlasmasi Detay | Kalemler (Child) | ❌ |
| Lojinet Odeme Tahsilat | Ödeme/Tahsilat | ❌ |
| Lojinet Cek | Çek yönetimi | ❌ |
| Lojinet Destek Bileti | Destek sistemi | ❌ |
| Lojinet Destek Mesaj | Mesajlar (Child) | ❌ |
| Lojinet Online Mutabakat | Mutabakat yönetimi | ❌ |
| Lojinet Evrak | Evrak galeri | ❌ |
| Lojinet Depo | Depo kartları | ❌ |
| Lojinet Saas Paket | SaaS paketleri | ❌ |
| Lojinet Saas Musteri | SaaS müşterileri | ❌ |

## 🛠️ Kurulum

```bash
# 1. Bench'e ekle
bench get-app /path/to/lojinet.zip

# 2. Site'a kur
bench --site [site-name] install-app lojinet

# 3. Migrate
bench --site [site-name] migrate

# 4. Restart
bench restart
```

Detaylı kurulum için: [INSTALLATION.md](INSTALLATION.md)

## 📖 Kullanım

### Temel İş Akışı

```
1. Cari Tanımla
   ↓
2. Araç ve Şoför Tanımla
   ↓
3. Mal Kabul Yap
   ↓
4. Yük Oluştur
   ↓
5. Sefer Planla
   ↓
6. Fatura Oluştur
```

### API Örnekleri

```python
# B2B kullanıcı oluştur
lojinet.api.create_b2b_user(
    customer="CR-001",
    email="user@example.com",
    first_name="Ali",
    last_name="Veli"
)

# Mutabakat gönder
lojinet.api.send_mutabakat(
    customer="CR-001",
    month="12",
    year=2025
)

# Yükten fatura oluştur
lojinet.api.create_invoice_from_yuk(yuk_name="YUK-2025-0001")

# Sefere toplu yük ekle
lojinet.api.add_yuk_to_sefer(
    sefer_name="SFR-2025-0001",
    yuk_list=["YUK-2025-0001", "YUK-2025-0002"]
)
```

## 🎯 Senaryolar

### ✅ Mal Kabul Senaryosu
Müşteriden gelen ürünler → Araç bilgileri → Rampa → Stok kartından ürün seç → Mail gönder (PDF) → Liste

### ✅ Yük Kayıt Senaryosu
Müşteri irsaliyesi → Gönderen/Alıcı adres seç → **Otomatik stok kontrolü** → Yük/Ürün durumu → Fiyat modeli → Excel import → 3 TAB

### ✅ Sefer Senaryosu
Araç/Şoför seç → Toplu yük ekle → Navlun → **Otomatik statü güncelleme**

### ✅ Faturalandırma
Yüklerden faturala → Fatura durumu güncelle → E-Fatura (hazır)

### ✅ Ödeme/Tahsilat
Cari seç → Ödeme türü → Çek havuzu → Cari borç/alacak

### ✅ Online Mutabakat
Ay seç → Müşteri seç → Link gönder → Onay/Red → IP kayıt

### ✅ B2B Portal
Kullanıcı giriş → Yüklerini gör → Destek talebi → Müşteri temsilcisi → Evrak galeri

## 🔧 Geliştirme

### Yeni DocType Ekleme

```bash
bench --site [site-name] new-doctype
```

### Test

```bash
bench --site [site-name] console

import frappe
doc = frappe.get_doc("Lojinet Yuk", "YUK-2025-0001")
print(doc.as_dict())
```

## 📊 Performans

- 22 DocType
- 150+ Field
- 15+ API Fonksiyon
- 2 Web Sayfası (B2B, Mutabakat)
- 2 Scheduler Görevi

## 🤝 Katkıda Bulunma

Pull request'ler memnuniyetle karşılanır!

## 📝 Lisans

MIT License - Detaylar için [license.txt](license.txt)

## 📞 İletişim

- Email: info@lojinet.com
- GitHub: https://github.com/lojinet/lojinet
- Döküman: https://docs.lojinet.com

## 🎉 Teşekkürler

ERPNext ve Frappe ekibine teşekkürler!

---

**Lojinet v1.0.0** - Eksiksiz Lojistik Yönetim Sistemi
