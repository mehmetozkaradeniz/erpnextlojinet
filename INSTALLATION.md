# Lojinet - Detaylı Kurulum Kılavuzu

## Sistem Gereksinimleri

- **ERPNext:** v14 veya üzeri
- **Frappe Framework:** v14 veya üzeri
- **Python:** 3.10+
- **MariaDB:** 10.6+
- **Node.js:** 16+

## Kurulum Adımları

### 1. Modülü İndirme

```bash
cd ~/frappe-bench

# GitHub'dan (yayınlandığında)
bench get-app https://github.com/lojinet/lojinet

# VEYA zip dosyasından
bench get-app /path/to/lojinet.zip
```

### 2. Site'a Kurulum

```bash
# Site'ınızın adını [site-name] ile değiştirin
bench --site [site-name] install-app lojinet
```

### 3. Migrate ve Restart

```bash
# Veritabanı migration
bench --site [site-name] migrate

# Clear cache
bench --site [site-name] clear-cache

# Bench restart
bench restart
```

## Kurulum Sonrası Yapılandırma

### 1. Temel Ayarlar

ERPNext'e giriş yapın ve **Lojinet** modülüne gidin:

#### Seri Tanımları
**Yönetim > Seri Tanımları** menüsünden:
- Mal Kabul: `MK-.YYYY.-.####`
- Yük: `YUK-.YYYY.-.####`
- Sefer: `SFR-.YYYY.-.####`
- Fiyat Anlaşması: `FA-.YYYY.-.####`
- Ödeme/Tahsilat: `OT-.YYYY.-.####`
- Çek: `CEK-.YYYY.-.####`
- Destek Bileti: `TKT-.YYYY.-.####`
- Mutabakat: `MUT-.YYYY.-.####`
- Evrak: `EVR-.YYYY.-.####`
- SaaS Müşteri: `SM-.YYYY.-.####`

### 2. Rol Tanımları

Kullanıcılara uygun rolleri atayın:

- **Lojinet Manager:** Tüm modül yetkileri
- **Lojinet User:** Operasyonel işlemler (Mal Kabul, Yük, Sefer)
- **Lojinet B2B User:** B2B portal erişimi (müşteriler için)
- **System Manager:** Tüm yönetimsel işlemler

### 3. Mail Ayarları

**Ayarlar > E-posta Hesabı** menüsünden SMTP ayarlarınızı yapın:

```
SMTP Sunucusu: smtp.gmail.com (veya kendi sunucunuz)
Port: 587
TLS Kullan: Evet
Kullanıcı Adı: your-email@domain.com
Şifre: *****
```

### 4. İlk Cari Tanımlama

1. **Lojinet > Cari > Yeni Cari**
2. Cari Kodu: `CR-001`
3. Cari Adı: Test Müşteri
4. Cari Tipi: Müşteri
5. Telefon ve E-posta ekleyin
6. **Adresler** bölümünden en az bir adres ekleyin
7. Kaydedin

### 5. İlk Araç ve Şoför Tanımlama

**Araç:**
1. **Lojinet > Araçlar > Yeni Araç**
2. Plaka: `34ABC123`
3. Araç Tipi: Kamyon
4. Kaydedin

**Şoför:**
1. **Lojinet > Şoförler > Yeni Şoför**
2. TC Kimlik No: `12345678901`
3. Ad Soyad: Test Şoför
4. Telefon: 05XXXXXXXXX
5. Kaydedin

## Temel İş Akışı

### 1. Mal Kabul İşlemi

1. **Lojinet > Mal Kabul > Yeni Mal Kabul**
2. Cari seçin
3. Araç plaka ve rampa no girin
4. **Kalemler** bölümünden stok ekleyin:
   - Stok Kodu seçin (Item)
   - Miktar girin
   - Birim, desi, ambalaj türü
5. **Kaydet** ve **Submit**
6. **Mail Gönder** butonuyla müşteriye PDF gönder

### 2. Yük Oluşturma

1. **Lojinet > Yük > Yeni Yük**
2. Müşteri ve irsaliye no girin
3. **Kalemler** sekmesinden ürünleri ekleyin
4. **Fiyatlar** sekmesinden masraf kalemlerini girin
5. Sistem otomatik olarak stok durumunu kontrol eder:
   - ✅ Depoda varsa: "Ürün Depoda"
   - ⏳ Yoksa: "Ürün Bekleniyor"
6. **Kaydet** ve **Submit**

### 3. Sefer Planlama

1. **Lojinet > Sefer > Yeni Sefer**
2. Araç seçin (şoför otomatik gelir)
3. **Yükler** sekmesinden yük ekleyin
4. Navlun tutarı girin
5. **Kaydet** ve **Submit**
6. Submit edildiğinde yükler otomatik olarak "Yolda" olur

### 4. Faturalandırma

1. **Lojinet > Muhasebe > Fatura Oluştur**
2. API fonksiyonu: `create_invoice_from_yuk(yuk_name)`
3. Sistem yük fiyatlarını Sales Invoice'a aktarır
4. Fatura kalemlerini "Faturalandı" olarak işaretler

## B2B Portal Kurulumu

### 1. B2B Kullanıcı Oluşturma

1. **Customer** formunu açın
2. Sağ üstteki **Lojinet > B2B Kullanıcı Oluştur**
3. E-posta, İsim, Soyisim girin
4. Kullanıcı otomatik oluşturulur ve karşılama maili gider

### 2. Portal Erişimi

Müşteriler şu URL'den portal'e erişir:
```
https://your-domain.com/b2b
```

Giriş yapınca:
- Yüklerini görür
- Destek talebi oluşturabilir
- Müşteri temsilcisi bilgilerini görür

## Online Mutabakat Kullanımı

1. **Lojinet > Online Mutabakat**
2. Cari seçin, ay/yıl girin
3. **Mutabakat Gönder**
4. Müşteriye link gider
5. Link'e tıklayınca onay/red butonu görür
6. IP adresi kaydedilir

## Sorun Giderme

### Modül Görünmüyorsa

```bash
bench --site [site-name] clear-cache
bench --site [site-name] migrate
bench restart
```

### DocType Hataları

```bash
bench --site [site-name] console

# Python console'da:
import frappe
frappe.db.sql("show tables like 'tabLojinet%'")
```

### Log Kontrol

```bash
# Hata logları
tail -f ~/frappe-bench/sites/[site-name]/logs/web.error.log

# Worker logları
tail -f ~/frappe-bench/sites/[site-name]/logs/worker.error.log
```

### Cache Temizleme

```bash
bench --site [site-name] clear-cache
bench --site [site-name] clear-website-cache
```

## Gelişmiş Ayarlar

### E-Fatura Entegrasyonu

1. **Lojinet > Ayarlar > E-Fatura**
2. Entegratör seçin (Foriba, İnteraktif, vb.)
3. API bilgilerini girin
4. Test edin

### Scheduler Görevleri

Günlük çalışan görevler:
- `auto_close_tickets`: 12 saat yanıt alınmayan biletleri kapatır
- `check_insurance_expiry`: Sigorta bitiş tarihlerini kontrol eder

### Custom Fields

Eğer ERPNext'in standart Customer DocType'ını kullanıyorsanız:
- `lojinet_customer_code`
- `lojinet_representative`

alanları otomatik eklenir.

## Güvenlik

### Yedekleme

```bash
# Manuel yedek
bench --site [site-name] backup

# Otomatik yedek (cron)
# bench/config/crontab ekleyin:
0 2 * * * cd /home/frappe/frappe-bench && bench --site [site-name] backup
```

### SSL Kurulumu

```bash
bench setup lets-encrypt [site-name]
```

## Destek

- Email: info@lojinet.com
- Dökümantasyon: https://docs.lojinet.com
- GitHub: https://github.com/lojinet/lojinet/issues

## Lisans

MIT License - Detaylar için license.txt
