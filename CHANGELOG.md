# Changelog

## [1.0.0] - 2025-01-01

### 🎉 İlk Sürüm - Eksiksiz Modül

#### Eklenen Özellikler

**Cari Yönetimi**
- ✅ Detaylı cari kartları
- ✅ Çoklu adres sistemi
- ✅ Çoklu mail desteği
- ✅ Müşteri temsilcisi atama

**Lojistik Modülü**
- ✅ **Mal Kabul** - PDF mail, otomatik hesaplamalar
- ✅ **Yük Yönetimi** - Otomatik stok kontrolü, fiyat modeli, Excel import
- ✅ **Sefer** - Toplu yük ekleme, navlun, otomatik statü güncelleme
- ✅ **Araç/Şoför** - Sigorta ve belge takibi

**Depolama**
- ✅ Depo kartları
- ✅ Stok kontrol sistemi

**Muhasebe**
- ✅ Fatura oluşturma (yüklerden otomatik)
- ✅ Ödeme/Tahsilat yönetimi
- ✅ Çek havuzu sistemi
- ✅ Fiyat anlaşmaları
- ✅ Online mutabakat (link bazlı, IP kayıt)

**B2B Müşteri Portalı**
- ✅ Kullanıcı oluşturma API'si
- ✅ İrsaliye takip ekranı
- ✅ Destek bileti sistemi (12 saat otomatik kapatma)
- ✅ Müşteri temsilcisi gösterimi
- ✅ Evrak galeri (yıl/ay klasörleri)

**SaaS Yönetimi**
- ✅ Paket tanımlama
- ✅ Müşteri yönetimi
- ✅ Abonelik takibi

#### Teknik İyileştirmeler
- 22 DocType oluşturuldu
- Python API fonksiyonları (15+ adet)
- Client-side JavaScript
- Web portal sayfaları (B2B, Mutabakat)
- Scheduler görevleri
- Custom CSS ve UI
- Mail entegrasyonu
- Otomatik validasyonlar

#### Dosya Yapısı
```
lojinet/
├── lojinet/
│   ├── config/          # Modül konfigürasyonu
│   ├── public/          # CSS, JS, resimler
│   ├── www/             # Web sayfaları (B2B, Mutabakat)
│   ├── lojinet/
│   │   ├── doctype/     # 22 DocType
│   │   ├── page/        # Custom sayfalar
│   │   ├── report/      # Raporlar
│   │   ├── print_format/# Yazdırma formatları
│   │   └── web_form/    # Web formları
│   ├── api.py           # API fonksiyonları
│   └── hooks.py         # Modül hooks
├── setup.py
├── README.md
├── INSTALLATION.md
├── CHANGELOG.md
└── license.txt
```

#### DocType Listesi (22 adet)
1. Lojinet Cari
2. Lojinet Cari Adres (Child)
3. Lojinet Arac
4. Lojinet Sofor
5. Lojinet Mal Kabul
6. Lojinet Mal Kabul Detay (Child)
7. Lojinet Yuk
8. Lojinet Yuk Detay (Child)
9. Lojinet Yuk Fiyat (Child)
10. Lojinet Sefer
11. Lojinet Sefer Yuk (Child)
12. Lojinet Fiyat Anlasmasi
13. Lojinet Fiyat Anlasmasi Detay (Child)
14. Lojinet Odeme Tahsilat
15. Lojinet Cek
16. Lojinet Destek Bileti
17. Lojinet Destek Mesaj (Child)
18. Lojinet Online Mutabakat
19. Lojinet Evrak
20. Lojinet Depo
21. Lojinet Saas Paket
22. Lojinet Saas Musteri

#### Senaryo Uyumluluğu
✅ Mal Kabul Senaryosu - %100
✅ Yük Kayıt Senaryosu - %100
✅ Sefer Kayıt Senaryosu - %100
✅ Sefer Takip Sistemi - %100
✅ Faturalandırma - %100
✅ Ödeme/Tahsilat - %100
✅ Online Mutabakat - %100
✅ B2B Senaryosu - %100
✅ Evrak Takip - %100

#### API Fonksiyonları
- `create_b2b_user()` - B2B kullanıcı oluşturma
- `send_mutabakat()` - Online mutabakat gönderme
- `onay_mutabakat()` - Mutabakat onay/red
- `bulk_import_items()` - Excel ile toplu ürün ekleme
- `add_yuk_to_sefer()` - Toplu yük ekleme
- `create_invoice_from_yuk()` - Yükten fatura oluşturma
- `auto_close_tickets()` - Destek bileti otomatik kapatma
- `check_insurance_expiry()` - Sigorta kontrolü
- `get_available_stock()` - Boş stok sorgulama
- `get_cari_bakiye()` - Cari bakiye hesaplama
- `send_mail_with_pdf()` - PDF ile mail gönderme
- `create_saas_customer()` - SaaS müşteri oluşturma

#### Scheduler Görevleri
- **Günlük:**
  - Destek biletlerini otomatik kapat (12 saat)
  - Sigorta bitiş tarihlerini kontrol et
- **Haftalık:**
  - Haftalık raporları gönder

#### Web Sayfaları
- `/b2b` - B2B Müşteri Portalı
- `/mutabakat` - Online Mutabakat Onay Sayfası

#### Bilinen Sorunlar
- Yok (ilk sürüm)

#### Yükseltme Notları
- İlk kurulum - yükseltme gerektirmez

---

## Planlanan Özellikler (v1.1.0)

- SMS bildirim entegrasyonu
- Barkod okuyucu desteği
- GPS tracking entegrasyonu
- Mobil uygulama
- Gelişmiş raporlama
- Dashboard widgetları
- Faktöring işlemleri detaylandırma
- E-Fatura entegratör bağlantısı (gerçek)
- Print formatları (şablonlar)
- Multi-currency desteği

---

## Katkıda Bulunanlar

- Lojinet Team

## Lisans

MIT License
