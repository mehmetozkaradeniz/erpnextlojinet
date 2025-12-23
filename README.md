# 🚀 LOJİNET v2.0

**Profesyonel Lojistik Yönetim Sistemi**

ERPNext için tam entegre lojistik ve nakliye yönetim modülü.

---

## 🎯 Yeni Özellikler (v2.0)

### ✅ 1. Gelişmiş Fiyat Hesaplama
- Miktar × Birim Fiyat = Toplam otomatiği
- Yük detayından otomatik miktar çekme
- Faturaya doğru yansıma

### ✅ 2. Akıllı Seri Numaralama
- YUK-2025-0001 formatı
- Otomatik artan numaralama
- Tüm DocType'larda standardizasyon

### ✅ 3. Otomatik Durum Güncellemeleri
- Mal kabul → Yük durumu güncelleme
- Sefer oluşturma → Yük "Yolda"
- Teslim → Yük "Teslim Edildi"

### ✅ 4. Çek Ciro Sistemi
- Çek tahsilat/ödeme
- Çek ciro hareketleri
- Cari bakiye entegrasyonu
- Çek geçmişi takibi

### ✅ 5. Sefer Kar/Zarar Hesaplama
- Yük toplam - Navlun = Kar/Zarar
- Sefer bazında raporlama
- Tarih aralığı kar/zarar raporu
- Detaylı analiz

### ✅ 6. B2B Portal (YENİ!)
- Müşteri self-servis portalı
- Online yük takibi
- Fiyat teklifi alma
- Canlı sefer bilgileri
- REST API entegrasyonu

### ✅ 7. Gelişmiş Raporlar
- Çek raporu (bekleyen, tahsil, ödeme)
- Yük raporu (detaylı)
- Depo raporu (doluluk oranı)
- Evrak raporu
- Kar/Zarar raporu

### ✅ 8. Liste Görünümleri İyileştirmeleri
- Tüm DocType'larda arama optimizasyonu
- İlgili alanlar listede görünür
- Hızlı filtreleme

---

## 📦 Kurulum

### Yeni Kurulum

```bash
# ERPNext bench'inizde
bench get-app https://github.com/mehmetozkaradeniz/erpnextlojinet

# Site'e kur
bench --site [site-adı] install-app lojinet

# Migrate
bench --site [site-adı] migrate

# Restart
bench restart
```

### Güncelleme (v1.0 → v2.0)

```bash
# 1. YEDEKinizi alın!
bench --site [site-adı] backup

# 2. Git pull
cd ~/frappe-bench/apps/lojinet
git pull origin main

# 3. Migrate
bench --site [site-adı] migrate

# 4. Custom field'leri oluştur
bench --site [site-adı] console
```

**Console'da:**
```python
from lojinet.setup.install import after_install
after_install()
exit()
```

```bash
# 5. Cache temizle
bench --site [site-adı] clear-cache

# 6. Restart
bench restart
```

---

## 🎨 Özellikler

### 📊 Modüller

1. **Cari Yönetimi**
   - Müşteri/Tedarikçi tanımlama
   - Çoklu adres desteği
   - Bakiye takibi
   - B2B kullanıcı tanımlama

2. **Mal Kabul**
   - Hızlı giriş
   - Barkod desteği
   - Otomatik email bildirimi
   - PDF yazdırma

3. **Yük Yönetimi**
   - Otomatik fiyat anlaşması
   - Miktar bazlı hesaplama
   - Sefer entegrasyonu
   - Durum takibi

4. **Sefer Yönetimi**
   - Toplu yük ekleme
   - Kar/Zarar hesaplama
   - Navlun yönetimi
   - Araç ve şoför takibi

5. **Çek Yönetimi**
   - Çek ciro sistemi
   - Tahsilat/Ödeme
   - Vade takibi
   - Portföy yönetimi

6. **Faturalama**
   - Toplu faturalama
   - Excel rapor
   - Email gönderimi
   - Detaylı fatura raporu

7. **B2B Portal**
   - Müşteri girişi
   - Yük takibi
   - Teklif alma
   - API entegrasyonu

8. **Raporlar**
   - Çek raporu
   - Yük raporu
   - Depo raporu
   - Kar/Zarar raporu
   - Evrak raporu

---

## 🔧 Yapılandırma

### 1. Şirket Bilgileri

```
Setup > Company
```

### 2. Seri Numaralama

```
Setup > Settings > Naming Series

Lojinet Cari: CARI-.YYYY.-.####
Lojinet Mal Kabul: MK-.YYYY.-.####
Lojinet Yuk: YUK-.YYYY.-.####
Lojinet Sefer: SFR-.YYYY.-.####
Lojinet Fiyat Anlasmasi: FA-.YYYY.-.####
Lojinet Cek: CEK-.YYYY.-.####
```

### 3. Email Ayarları

```
Setup > Email > Email Account
```

### 4. B2B Ayarları

```
Lojinet > B2B Ayarları
```

---

## 📖 Kullanım

### Yük Oluşturma

1. **Lojinet > Yük > Yeni**
2. Müşteri seç
3. İrsaliye no gir
4. Çıkış/Varış ili seç
5. Kalemler ekle
6. **Otomatik:** Fiyat anlaşması uygulanır
7. Kaydet

### Sefer Oluşturma

1. **Lojinet > Sefer > Yeni**
2. Araç ve şoför seç
3. Yükleri toplu seç
4. Navlun bilgileri gir
5. **Otomatik:** Kar/Zarar hesaplanır
6. Submit

### Çek Ciro

1. **Lojinet > Çek > [Çek Seç]**
2. **İşlemler > Çek Ciro Et**
3. Yeni cari seç
4. **Otomatik:** Bakiyeler güncellenir

### Toplu Faturalama

1. **Lojinet > Cari > [Müşteri Seç]**
2. **İşlemler > Toplu Fatura Oluştur**
3. Tarih aralığı seç
4. **Otomatik:** Tek fatura oluşur
5. Excel indir / Mail gönder

---

## 🌐 B2B Portal

### Müşteri Girişi

```
https://your-site.com/b2b
```

### API Kullanımı

```python
import requests

# Login
response = requests.post("https://your-site.com/api/method/lojinet.api.b2b_login", data={
    "email": "musteri@firma.com",
    "password": "****"
})

api_key = response.json()["message"]["api_key"]

# Yükleri getir
yukler = requests.get("https://your-site.com/api/method/lojinet.api.b2b_get_yukler", params={
    "api_key": api_key
})

print(yukler.json())
```

---

## 📊 Raporlar

### Kar/Zarar Raporu

```
Lojinet > Raporlar > Sefer Kar/Zarar Raporu

Filtreler:
- Başlangıç Tarihi
- Bitiş Tarihi

Çıktı:
- Sefer bazında detaylar
- Yük toplam
- Navlun toplam
- Kar/Zarar
```

### Çek Raporu

```
Lojinet > Raporlar > Çek Raporu

Filtreler:
- Durum (Portföy, Tahsil, Ödeme, Ciro)
- Tarih aralığı
- Cari

Çıktı:
- Çek detayları
- Kimden geldi
- Kime gitti
- Vade tarihi
```

---

## 🛠️ Geliştirici

### API Endpoints

```python
# Çek Ciro
@frappe.whitelist()
def cek_ciro(cek_id, yeni_cari, aciklama=None)

# Kar/Zarar
@frappe.whitelist()
def hesapla_sefer_kar_zarar(sefer_id)

# Kar/Zarar Raporu
@frappe.whitelist()
def sefer_kar_zarar_raporu(from_date, to_date)

# B2B Login
@frappe.whitelist(allow_guest=True)
def b2b_login(email, password)

# B2B Yükler
@frappe.whitelist()
def b2b_get_yukler(api_key)

# B2B Yük Talebi
@frappe.whitelist()
def b2b_create_yuk_talebi(api_key, data)
```

### Hooks

```python
# Scheduler
scheduler_events = {
    "daily": ["lojinet.tasks.check_vade_tarihleri"],
    "weekly": ["lojinet.tasks.send_weekly_reports"]
}

# Boot Session
boot_session = "lojinet.api.boot_session"
```

---

## 🐛 Sorun Giderme

### Fiyat Anlaşması Uygulanmıyor

**Kontrol edin:**
- Fiyat anlaşması tarih aralığı doğru mu?
- Kriterler yüke uyuyor mu?
- Zaten fiyat eklenmiş mi?

### Seri Numaralama Çalışmıyor

```bash
# Console'da
bench --site [site] console

frappe.db.sql("UPDATE `tabDocType` SET autoname='naming_series:' WHERE name='Lojinet Yuk'")
frappe.db.commit()
exit()
```

### B2B Portal Açılmıyor

**Kontrol edin:**
- Nginx yapılandırması
- DNS ayarları
- B2B ayarları aktif mi?

---

## 📞 Destek

- **GitHub:** https://github.com/mehmetozkaradeniz/erpnextlojinet
- **Issues:** https://github.com/mehmetozkaradeniz/erpnextlojinet/issues
- **Email:** info@ixirbilisim.com

---

## 📜 Lisans

MIT License - Detaylar için `license.txt` dosyasına bakın.

---

## 🙏 Katkıda Bulunanlar

- İXİR Bilişim Ekibi
- Community Contributors

---

## 📝 Changelog

### v2.0.0 (2025-12-23)
- ✅ 15 maddelik kapsamlı güncelleme
- ✅ B2B modülü
- ✅ Çek ciro sistemi
- ✅ Kar/Zarar raporları
- ✅ Gelişmiş fiyat hesaplama
- ✅ Otomatik durum güncellemeleri

### v1.0.0 (2025-12-22)
- İlk sürüm
- 22 DocType
- Temel lojistik yönetimi

---

**⚡ Lojinet v2.0 - Profesyonel Lojistik Yönetimi**

**Powered by ERPNext & İXİR Bilişim**
