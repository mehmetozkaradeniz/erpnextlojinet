# 🎯 LOJİNET V2.0 - KOMPLE GÜNCELLEME

## 📋 UYGULANAN 15 MADDE

### ✅ 1. YÜK FİYAT HESAPLAMA SİSTEMİ
**Değişiklikler:**
- `Lojinet Yuk Fiyat` DocType güncellendi
- Yeni alanlar: `miktar`, `birim_fiyat`, `toplam`
- Otomatik hesaplama: `toplam = miktar × birim_fiyat`
- Fiyat anlaşması uygulanırken yük detayından miktar çekilir
- Fatura toplam tutarına yansıma

**Dosyalar:**
- `lojinet/doctype/lojinet_yuk_fiyat/lojinet_yuk_fiyat.json`
- `lojinet/doctype/lojinet_yuk/lojinet_yuk.py` (apply_price_agreement fonksiyonu)
- `lojinet/doctype/lojinet_yuk_fiyat/lojinet_yuk_fiyat.js`

---

### ✅ 2. YÜK LİSTESİ VE SERİ NUMARALAMA
**Değişiklikler:**
- Müşteri irsaliye no ile arama öncelikli
- Müşteri adı ile arama
- Seri numaralama düzeltildi: `YUK-2025-0001` formatı
- İşlendi durumunda da düzenlenebilir
- Mal kabul yapıldığında yük durumu otomatik güncellenir
- Kalemler sekmesinde: stok kodu, stok adı, miktar, birim

**Dosyalar:**
- `lojinet/doctype/lojinet_yuk/lojinet_yuk.json` (search_fields, title_field)
- `lojinet/doctype/lojinet_yuk/lojinet_yuk.py` (on_update_after_submit)
- `lojinet/doctype/lojinet_yuk/lojinet_yuk.js`

---

### ✅ 3. MAL KABUL LİSTESİ VE DURUM
**Değişiklikler:**
- Liste: cari adı, mal kabul tarihi, ürün adı, miktar, birim
- Submit sonrası durum "İşlendi" olarak gösteriliyor
- Bağlı yüklerin durumu otomatik güncelleniyor

**Dosyalar:**
- `lojinet/doctype/lojinet_mal_kabul/lojinet_mal_kabul.json`
- `lojinet/doctype/lojinet_mal_kabul/lojinet_mal_kabul.py`

---

### ✅ 4. DEPO LİSTESİ
**Değişiklikler:**
- Depo adı, kapasite bilgileri listede görünür

**Dosyalar:**
- `lojinet/doctype/lojinet_depo/lojinet_depo.json`

---

### ✅ 5. ÇEK SİSTEMİ (TAM YENİLEME)
**Yeni Özellikler:**
- Çek Ciro sistemi eklendi
- Cari bakiye entegrasyonu
- Tahsilat/Ödeme çek işlemleri
- Çek durumu: Portföy, Ciro, Tahsil, Ödeme
- Çek geçmişi takibi

**Yeni DocType:**
- `Lojinet Cek Ciro` (Çek ciro hareketleri)
- `Lojinet Cek Hareket` (Çek geçmişi)

**Değişiklikler:**
- `Lojinet Cek`: cari, tutar, vade_tarihi, durum, ciro_edilebilir
- `Lojinet Odeme Tahsilat`: cek seçiminde sadece müsait çekler

**Dosyalar:**
- `lojinet/doctype/lojinet_cek/lojinet_cek.json`
- `lojinet/doctype/lojinet_cek/lojinet_cek.py`
- `lojinet/doctype/lojinet_cek_ciro/` (yeni)
- `lojinet/api.py` (cek_ciro, update_cari_bakiye fonksiyonları)

---

### ✅ 6. YÜK-SEFER BİLGİLERİ GÖRÜNTÜLEME
**Değişiklikler:**
- Yük ekranında "Sefer Bilgileri" bölümü
- Sefer numarası, araç plaka, şoför ad-soyad, telefon
- Read-only alanlar

**Dosyalar:**
- `lojinet/doctype/lojinet_yuk/lojinet_yuk.json`
- `lojinet/doctype/lojinet_yuk/lojinet_yuk.js` (sefer değiştiğinde bilgileri çek)

---

### ✅ 7. SEFER SİSTEMİ VE KAR/ZARAR
**Değişiklikler:**
- Liste: nereden, nereye, şoför, navlun firması, sevk/teslim tarihleri
- Yükler sekmesi: müşteri irsaliye, müşteri adı, miktar, birim, sefer durumu
- Toplu yük seçimi ve ekleme
- Fiyatlar sekmesi (navlun detayları)
- Kalemler sekmesi (yükler)
- Tarihler sekmesi
- **Kar/Zarar Hesaplama:** Yük toplam - Navlun toplam
- **Kar/Zarar Raporu:** İki tarih arası tüm seferler

**Yeni Rapor:**
- `Sefer Kar Zarar Raporu`

**Dosyalar:**
- `lojinet/doctype/lojinet_sefer/lojinet_sefer.json`
- `lojinet/doctype/lojinet_sefer/lojinet_sefer.py`
- `lojinet/doctype/lojinet_sefer/lojinet_sefer.js`
- `lojinet/report/sefer_kar_zarar_raporu/`

---

### ✅ 8. ÇEK RAPORU
**Yeni Rapor:**
- Bekleyen çekler
- Kimden geldi, kime gitti
- Gelme tarihi, gitme tarihi
- Vade tarihi
- Çek geçmişi

**Dosyalar:**
- `lojinet/report/cek_raporu/cek_raporu.py`
- `lojinet/report/cek_raporu/cek_raporu.js`
- `lojinet/report/cek_raporu/cek_raporu.json`

---

### ✅ 9. YÜK RAPORU
**Değişiklikler:**
- Miktar, birim
- Varış ili
- Alıcı firma
- Alıcı adres adı
- Gönderen firma

**Dosyalar:**
- `lojinet/report/yuk_raporu/yuk_raporu.py`

---

### ✅ 10. DEPO RAPORU
**Detaylı rapor:**
- Depo doluluk oranı
- Stok detayları
- Cari bazında stoklar

**Dosyalar:**
- `lojinet/report/depo_raporu/depo_raporu.py`

---

### ✅ 11. EVRAK LİSTESİ
**Değişiklikler:**
- Müşteri, ay, yıl, eklenme tarihi
- Önizleme linki (göz ikonu)

**Dosyalar:**
- `lojinet/doctype/lojinet_evrak/lojinet_evrak.json`
- `lojinet/doctype/lojinet_evrak/lojinet_evrak.js`

---

### ✅ 12. ŞOFÖR LİSTESİ
**Değişiklikler:**
- Bağlı olduğu nakliye firması görüntüleniyor

**Dosyalar:**
- `lojinet/doctype/lojinet_sofor/lojinet_sofor.json`

---

### ✅ 13. EVRAK RAPORU
**Detaylı rapor:**
- Müşteri bazında
- Tarih aralığı
- Evrak türü filtreleme

**Dosyalar:**
- `lojinet/report/evrak_raporu/evrak_raporu.py`

---

### ✅ 14. ÖDEME TAHSİLAT DÜZELTMELERİ
**Değişiklikler:**
- Çek türü seçildiğinde: çek numarası ile listeleme
- Ciro edilen çekler görünmez
- Otomatik cari bakiye güncellemesi

**Dosyalar:**
- `lojinet/doctype/lojinet_odeme_tahsilat/lojinet_odeme_tahsilat.json`
- `lojinet/doctype/lojinet_odeme_tahsilat/lojinet_odeme_tahsilat.js`
- `lojinet/doctype/lojinet_odeme_tahsilat/lojinet_odeme_tahsilat.py`

---

### ✅ 15. B2B SİSTEMİ (YENİ MODÜL)
**Yeni Özellikler:**
- B2B Portal kullanıcıları
- Cari bazlı B2B ayarları
- Web portal (müşteri self-servis)
- API entegrasyonu
- Otomatik yük takibi
- Online fiyat teklifi
- Canlı sefer takibi

**Yeni DocType'lar:**
- `Lojinet B2B Ayarlari` (Cari Child Table)
- `Lojinet B2B Kullanici`
- `Lojinet B2B Log`
- `Lojinet B2B Portal Settings`

**Web Pages:**
- `b2b_portal.html` (Ana portal)
- `b2b_yuk_takip.html` (Yük takip)
- `b2b_teklif_al.html` (Fiyat teklifi)

**API Endpoints:**
- `/api/method/lojinet.b2b.get_yukler`
- `/api/method/lojinet.b2b.create_yuk_talebi`
- `/api/method/lojinet.b2b.track_sefer`

**Dosyalar:**
- `lojinet/b2b/` (yeni modül klasörü)
- `lojinet/doctype/lojinet_cari/lojinet_cari.json` (b2b alanları)
- `lojinet/www/b2b/` (web sayfaları)

---

## 📊 İSTATİSTİKLER

| Kategori | Önceki | Yeni | Değişim |
|----------|--------|------|---------|
| **DocType Sayısı** | 22 | 28 | +6 |
| **API Fonksiyonu** | 16 | 35 | +19 |
| **Rapor Sayısı** | 5 | 10 | +5 |
| **Web Sayfası** | 0 | 3 | +3 |
| **JS Dosyası** | 4 | 15 | +11 |
| **Python Controller** | 22 | 28 | +6 |
| **Email Template** | 4 | 6 | +2 |
| **Print Format** | 3 | 5 | +2 |

---

## 🚀 KURULUM

```bash
# Mevcut Lojinet'i güncelle
cd ~/frappe-bench/apps/lojinet
git pull origin main

# Veya yeni kurulum
bench get-app https://github.com/mehmetozkaradeniz/erpnextlojinet

# Migrate
bench --site [site-name] migrate

# Restart
bench restart
```

---

## 🔄 UPGRADE ADIMLARI (Mevcut Sistemler İçin)

```bash
# 1. Yedek al
bench --site [site-name] backup

# 2. Migrate
bench --site [site-name] migrate

# 3. Custom Field'leri oluştur
bench --site [site-name] console
```

**Console'da:**
```python
import frappe
from lojinet.setup.install import after_install
after_install()
exit()
```

```bash
# 4. Cache temizle
bench --site [site-name] clear-cache

# 5. Restart
bench restart
```

---

## ⚠️ BREAKING CHANGES

### Yük Fiyat Yapısı Değişti
**Eski:** Sadece `tutar` alanı  
**Yeni:** `miktar`, `birim_fiyat`, `toplam` alanları

**Migration:** Mevcut `tutar` değerleri `toplam`'a kopyalanır, `miktar` otomatik `1` olur.

### Çek Sistemi Yeniden Tasarlandı
**Yeni alanlar:** `durum`, `ciro_edilebilir`, `ciro_edilen_cari`

**Migration:** Mevcut çeklerin durumu "Portföy" olarak ayarlanır.

---

## 📞 DESTEK

**GitHub:** https://github.com/mehmetozkaradeniz/erpnextlojinet  
**Issues:** https://github.com/mehmetozkaradeniz/erpnextlojinet/issues

---

## 📝 VERSİYON GEÇMİŞİ

### v2.0.0 (2025-12-23)
- ✅ 15 maddelik kapsamlı güncelleme
- ✅ B2B modülü eklendi
- ✅ Çek ciro sistemi
- ✅ Kar/Zarar raporları
- ✅ Gelişmiş fiyat hesaplama
- ✅ Otomatik durum güncellemeleri

### v1.0.0 (2025-12-22)
- İlk sürüm
- 22 DocType
- Temel lojistik yönetimi

---

**⚡ Lojinet v2.0 - Profesyonel Lojistik Yönetim Sistemi**
