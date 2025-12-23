# 🚀 LOJİNET V2.0 KURULUM TALIMATLARI

## 📋 ÖNEMLİ NOTLAR

Bu **v2.0 güncellemesi** şunları içerir:
- ✅ 15 maddelik kapsamlı güncelleme
- ✅ Yeni DocType'lar (Çek Ciro, B2B Kullanıcı)
- ✅ API genişletmeleri
- ✅ Rapor eklemeleri
- ✅ B2B portal

---

## 🔄 MEVCUT SİSTEMİ GÜNCELLEME

### 1. Yedek Alın (Kritik!)

```bash
bench --site lojinet.ixirbilisim.com backup
```

### 2. Uygulamayı Güncelleyin

```bash
cd ~/frappe-bench/apps/lojinet

# Mevcut değişiklikleri kaydet
git stash

# GitHub'dan çek
git pull origin main

# Veya zip'i kopyalayın
cp /path/to/lojinet_v2.zip .
unzip -o lojinet_v2.zip
```

### 3. Bağımlılıkları Kurun

```bash
pip install --upgrade -e ~/frappe-bench/apps/lojinet
```

### 4. Migrate Yapın

```bash
bench --site lojinet.ixirbilisim.com migrate
```

### 5. Custom Field'leri Oluşturun

```bash
bench --site lojinet.ixirbilisim.com console
```

**Console'da:**
```python
import frappe

# Yük Fiyat - Miktar alanı
frappe.get_doc({
    "doctype": "Custom Field",
    "dt": "Lojinet Yuk Fiyat",
    "fieldname": "miktar",
    "label": "Miktar",
    "fieldtype": "Float",
    "default": "1",
    "insert_after": "aciklama"
}).insert(ignore_if_duplicate=True)

# Yük Fiyat - Toplam alanı
frappe.get_doc({
    "doctype": "Custom Field",
    "dt": "Lojinet Yuk Fiyat",
    "fieldname": "toplam",
    "label": "Toplam",
    "fieldtype": "Currency",
    "read_only": 1,
    "insert_after": "birim_fiyat"
}).insert(ignore_if_duplicate=True)

# Cari - Bakiye alanı
frappe.get_doc({
    "doctype": "Custom Field",
    "dt": "Lojinet Cari",
    "fieldname": "bakiye",
    "label": "Bakiye",
    "fieldtype": "Currency",
    "default": "0"
}).insert(ignore_if_duplicate=True)

frappe.db.commit()
print("✅ Custom Field'ler oluşturuldu!")

exit()
```

### 6. Cache Temizle ve Restart

```bash
bench --site lojinet.ixirbilisim.com clear-cache
bench restart
```

---

## 🎯 YENİ KURULUM

### GitHub'dan

```bash
bench get-app https://github.com/mehmetozkaradeniz/erpnextlojinet
bench --site lojinet.ixirbilisim.com install-app lojinet
bench --site lojinet.ixirbilisim.com migrate
bench restart
```

### Zip'ten

```bash
# Zip'i apps dizinine kopyala
cp lojinet_v2.zip ~/frappe-bench/apps/

cd ~/frappe-bench/apps/
unzip lojinet_v2.zip
mv lojinet_v2_final lojinet

# Kur
bench --site lojinet.ixirbilisim.com install-app lojinet
bench --site lojinet.ixirbilisim.com migrate
bench restart
```

---

## ✅ KURULUM SONRASI KONTROLLER

### 1. Workspace Kontrol

**Tarayıcıda:**
- Sol menüde "Lojinet" görünüyor mu?
- Awesome Bar'da "Lojinet Yuk" arattığınızda buluyor mu?

### 2. Yeni DocType'lar

```bash
bench --site lojinet.ixirbilisim.com console
```

```python
import frappe
print(frappe.db.exists("DocType", "Lojinet Cek Ciro"))  # True olmalı
print(frappe.db.exists("DocType", "Lojinet B2B Kullanici"))  # True olmalı
exit()
```

### 3. API Test

```bash
bench --site lojinet.ixirbilisim.com console
```

```python
import frappe
from lojinet.api import hesapla_sefer_kar_zarar

# API fonksiyonu mevcut mu?
print("API yüklendi!" if hasattr(frappe.get_module("lojinet.api"), "hesapla_sefer_kar_zarar") else "API YOK!")

exit()
```

### 4. Test Verisi

**Tarayıcıda test edin:**

1. **Cari oluştur**
   - Lojinet > Cari > Yeni
   - Cari Adı: Test Müşteri
   - Kaydet

2. **Fiyat Anlaşması**
   - Lojinet > Fiyat Anlaşması > Yeni
   - Cari: Test Müşteri
   - Çıkış: İstanbul
   - Varış: Ankara
   - Birim Fiyat: 2000
   - Kaydet

3. **Yük Oluştur**
   - Lojinet > Yük > Yeni
   - Müşteri: Test Müşteri
   - İrsaliye No: TEST-001
   - Çıkış: İstanbul
   - Varış: Ankara
   - Kalemler > Stok: TEST, Miktar: 10
   - **Kaydet → Fiyatlar sekmesi kontrol:**
     - Miktar: 10 (otomatik)
     - Birim Fiyat: 2000 (anlaşmadan)
     - Toplam: 20000 (10 × 2000) ✅

---

## 🐛 SORUN GİDERME

### Hata: "DocType not found"

```bash
bench --site lojinet.ixirbilisim.com migrate --force
bench restart
```

### Hata: "Table doesn't exist"

```bash
bench --site lojinet.ixirbilisim.com console
```

```python
import frappe
frappe.db.sql("SHOW TABLES LIKE '%Lojinet%'")
exit()
```

Tablolar yoksa:
```bash
bench --site lojinet.ixirbilisim.com reinstall
```

### Hata: "API method not found"

```bash
cd ~/frappe-bench/apps/lojinet
git status  # Dosyalar güncel mi?

bench restart
```

---

## 📞 DESTEK

**Sorun yaşarsanız:**

1. Log dosyalarını kontrol edin:
```bash
tail -f ~/frappe-bench/logs/web.error.log
```

2. GitHub'da issue açın:
https://github.com/mehmetozkaradeniz/erpnextlojinet/issues

3. Email gönderin:
info@ixirbilisim.com

---

**BAŞARILAR!** 🎉
