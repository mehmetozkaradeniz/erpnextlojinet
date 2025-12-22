#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lojinet DocType Generator
Tüm eksik DocType'ları otomatik oluşturur
"""

import os
import json

BASE_DIR = "/home/claude/lojinet/lojinet/lojinet/doctype"

# DocType tanımlamaları
DOCTYPES = {
    # Temel Modüller
    "Lojinet Cari": {
        "is_submittable": 0,
        "autoname": "field:cari_kodu",
        "fields": [
            {"fieldname": "cari_kodu", "fieldtype": "Data", "label": "Cari Kodu", "reqd": 1, "unique": 1},
            {"fieldname": "cari_adi", "fieldtype": "Data", "label": "Cari Adı", "reqd": 1, "in_list_view": 1},
            {"fieldname": "cari_tipi", "fieldtype": "Select", "label": "Cari Tipi", "options": "Müşteri\nTedarikçi\nHer İkisi", "reqd": 1},
            {"fieldname": "vergi_dairesi", "fieldtype": "Data", "label": "Vergi Dairesi"},
            {"fieldname": "vergi_numarasi", "fieldtype": "Data", "label": "Vergi Numarası"},
            {"fieldname": "telefon", "fieldtype": "Data", "label": "Telefon"},
            {"fieldname": "email", "fieldtype": "Data", "label": "E-posta"},
            {"fieldname": "website", "fieldtype": "Data", "label": "Website"},
            {"fieldname": "adresler", "fieldtype": "Table", "label": "Adresler", "options": "Lojinet Cari Adres"},
            {"fieldname": "ek_mail_adresleri", "fieldtype": "Small Text", "label": "Ek Mail Adresleri"},
            {"fieldname": "odeme_vadesi", "fieldtype": "Int", "label": "Ödeme Vadesi (Gün)"},
            {"fieldname": "kredi_limiti", "fieldtype": "Currency", "label": "Kredi Limiti"},
            {"fieldname": "musteri_temsilcisi", "fieldtype": "Link", "label": "Müşteri Temsilcisi", "options": "User"},
        ]
    },
    
    "Lojinet Cari Adres": {
        "istable": 1,
        "fields": [
            {"fieldname": "adres_adi", "fieldtype": "Data", "label": "Adres Adı", "reqd": 1, "in_list_view": 1},
            {"fieldname": "adres_tipi", "fieldtype": "Select", "label": "Adres Tipi", "options": "Fatura\nGönderi\nTeslimat\nDiğer", "in_list_view": 1},
            {"fieldname": "varsayilan", "fieldtype": "Check", "label": "Varsayılan", "in_list_view": 1},
            {"fieldname": "adres_satiri_1", "fieldtype": "Data", "label": "Adres"},
            {"fieldname": "il", "fieldtype": "Data", "label": "İl"},
            {"fieldname": "ilce", "fieldtype": "Data", "label": "İlçe"},
            {"fieldname": "posta_kodu", "fieldtype": "Data", "label": "Posta Kodu"},
            {"fieldname": "yetkili_kisi", "fieldtype": "Data", "label": "Yetkili Kişi"},
            {"fieldname": "telefon", "fieldtype": "Data", "label": "Telefon"},
            {"fieldname": "email", "fieldtype": "Data", "label": "E-posta"},
        ]
    },
    
    # Araç ve Şoför
    "Lojinet Arac": {
        "autoname": "field:plaka",
        "fields": [
            {"fieldname": "plaka", "fieldtype": "Data", "label": "Plaka", "reqd": 1, "unique": 1, "in_list_view": 1},
            {"fieldname": "arac_tipi", "fieldtype": "Select", "label": "Araç Tipi", "options": "Çekici\nKamyon\nKamyonet\nDorse", "reqd": 1, "in_list_view": 1},
            {"fieldname": "marka", "fieldtype": "Data", "label": "Marka"},
            {"fieldname": "model", "fieldtype": "Data", "label": "Model"},
            {"fieldname": "yil", "fieldtype": "Int", "label": "Yıl"},
            {"fieldname": "kapasite_ton", "fieldtype": "Float", "label": "Kapasite (Ton)"},
            {"fieldname": "arac_sahibi", "fieldtype": "Data", "label": "Araç Sahibi"},
            {"fieldname": "navlun_odenecek_cari", "fieldtype": "Link", "label": "Navlun Ödenecek Cari", "options": "Lojinet Cari"},
            {"fieldname": "arac_durumu", "fieldtype": "Select", "label": "Araç Durumu", "options": "Aktif\nBakımda\nPasif\nYolda", "default": "Aktif", "in_list_view": 1},
            {"fieldname": "sigorta_bitis_tarihi", "fieldtype": "Date", "label": "Sigorta Bitiş Tarihi"},
        ]
    },
    
    "Lojinet Sofor": {
        "autoname": "field:tc_kimlik_no",
        "fields": [
            {"fieldname": "tc_kimlik_no", "fieldtype": "Data", "label": "TC Kimlik No", "reqd": 1, "unique": 1},
            {"fieldname": "ad_soyad", "fieldtype": "Data", "label": "Ad Soyad", "reqd": 1, "in_list_view": 1},
            {"fieldname": "telefon", "fieldtype": "Data", "label": "Telefon", "reqd": 1, "in_list_view": 1},
            {"fieldname": "email", "fieldtype": "Data", "label": "E-posta"},
            {"fieldname": "ehliyet_no", "fieldtype": "Data", "label": "Ehliyet No"},
            {"fieldname": "src_belge_no", "fieldtype": "Data", "label": "SRC Belge No"},
            {"fieldname": "src_gecerlilik_tarihi", "fieldtype": "Date", "label": "SRC Geçerlilik Tarihi"},
            {"fieldname": "durum", "fieldtype": "Select", "label": "Durum", "options": "Aktif\nPasif\nGörevde", "default": "Aktif", "in_list_view": 1},
        ]
    },
    
    # Mal Kabul
    "Lojinet Mal Kabul": {
        "is_submittable": 1,
        "autoname": "naming_series:",
        "fields": [
            {"fieldname": "naming_series", "fieldtype": "Select", "label": "Seri", "options": "MK-.YYYY.-.####", "reqd": 1},
            {"fieldname": "cari", "fieldtype": "Link", "label": "Cari", "options": "Lojinet Cari", "reqd": 1, "in_list_view": 1},
            {"fieldname": "tarih", "fieldtype": "Date", "label": "Tarih", "default": "Today", "reqd": 1, "in_list_view": 1},
            {"fieldname": "saat", "fieldtype": "Time", "label": "Saat", "default": "Now", "reqd": 1},
            {"fieldname": "arac_plaka", "fieldtype": "Link", "label": "Araç Plaka", "options": "Lojinet Arac"},
            {"fieldname": "rampa_no", "fieldtype": "Data", "label": "Rampa No"},
            {"fieldname": "mal_kabul_kalemleri", "fieldtype": "Table", "label": "Kalemler", "options": "Lojinet Mal Kabul Detay"},
            {"fieldname": "toplam_miktar", "fieldtype": "Float", "label": "Toplam Miktar", "read_only": 1},
            {"fieldname": "durum", "fieldtype": "Select", "label": "Durum", "options": "Taslak\nOnaylandı\nİptal", "default": "Taslak"},
        ]
    },
    
    "Lojinet Mal Kabul Detay": {
        "istable": 1,
        "fields": [
            {"fieldname": "stok_kodu", "fieldtype": "Link", "label": "Stok Kodu", "options": "Item", "reqd": 1, "in_list_view": 1},
            {"fieldname": "miktar", "fieldtype": "Float", "label": "Miktar", "reqd": 1, "in_list_view": 1},
            {"fieldname": "birim", "fieldtype": "Link", "label": "Birim", "options": "UOM", "in_list_view": 1},
            {"fieldname": "desi", "fieldtype": "Float", "label": "Desi", "in_list_view": 1},
            {"fieldname": "ambalaj_turu", "fieldtype": "Select", "label": "Ambalaj", "options": "Koli\nPalet\nÇuval", "in_list_view": 1},
        ]
    },
    
    # Yük
    "Lojinet Yuk": {
        "is_submittable": 1,
        "autoname": "naming_series:",
        "fields": [
            {"fieldname": "naming_series", "fieldtype": "Select", "label": "Seri", "options": "YUK-.YYYY.-.####", "reqd": 1},
            {"fieldname": "musteri", "fieldtype": "Link", "label": "Müşteri", "options": "Lojinet Cari", "reqd": 1, "in_list_view": 1},
            {"fieldname": "musteri_irsaliye_no", "fieldtype": "Data", "label": "Müşteri İrsaliye No", "reqd": 1, "in_list_view": 1},
            {"fieldname": "islem_tarihi", "fieldtype": "Date", "label": "İşlem Tarihi", "default": "Today", "reqd": 1},
            {"fieldname": "yuk_statusu", "fieldtype": "Select", "label": "Yük Statüsü", "options": "Beklemede\nYolda\nTeslim Edildi\nİptal", "default": "Beklemede", "in_list_view": 1},
            {"fieldname": "yuk_durumu", "fieldtype": "Select", "label": "Yük Durumu", "options": "Ürün Bekleniyor\nÜrün Depoda\nAraçta", "default": "Ürün Bekleniyor"},
            {"fieldname": "sefer", "fieldtype": "Link", "label": "Sefer", "options": "Lojinet Sefer"},
            {"fieldname": "yuk_kalemleri", "fieldtype": "Table", "label": "Kalemler", "options": "Lojinet Yuk Detay"},
            {"fieldname": "yuk_fiyatlari", "fieldtype": "Table", "label": "Fiyatlar", "options": "Lojinet Yuk Fiyat"},
            {"fieldname": "toplam_fiyat", "fieldtype": "Currency", "label": "Toplam Fiyat", "read_only": 1},
        ]
    },
    
    "Lojinet Yuk Detay": {
        "istable": 1,
        "fields": [
            {"fieldname": "stok_kodu", "fieldtype": "Link", "label": "Stok", "options": "Item", "reqd": 1, "in_list_view": 1},
            {"fieldname": "miktar", "fieldtype": "Float", "label": "Miktar", "reqd": 1, "in_list_view": 1},
            {"fieldname": "birim", "fieldtype": "Link", "label": "Birim", "options": "UOM"},
        ]
    },
    
    "Lojinet Yuk Fiyat": {
        "istable": 1,
        "fields": [
            {"fieldname": "masraf_kalemi", "fieldtype": "Data", "label": "Masraf Kalemi", "reqd": 1, "in_list_view": 1},
            {"fieldname": "tutar", "fieldtype": "Currency", "label": "Tutar", "reqd": 1, "in_list_view": 1},
            {"fieldname": "fatura_durumu", "fieldtype": "Select", "label": "Fatura Durumu", "options": "Faturalanmadı\nFaturalandı", "default": "Faturalanmadı"},
            {"fieldname": "fatura_no", "fieldtype": "Link", "label": "Fatura No", "options": "Sales Invoice"},
        ]
    },
    
    # Sefer
    "Lojinet Sefer": {
        "is_submittable": 1,
        "autoname": "naming_series:",
        "fields": [
            {"fieldname": "naming_series", "fieldtype": "Select", "label": "Seri", "options": "SFR-.YYYY.-.####", "reqd": 1},
            {"fieldname": "islem_tarihi", "fieldtype": "Date", "label": "İşlem Tarihi", "default": "Today", "reqd": 1, "in_list_view": 1},
            {"fieldname": "arac_plaka", "fieldtype": "Link", "label": "Araç", "options": "Lojinet Arac", "reqd": 1, "in_list_view": 1},
            {"fieldname": "sofor", "fieldtype": "Link", "label": "Şoför", "options": "Lojinet Sofor"},
            {"fieldname": "sefer_yukleri", "fieldtype": "Table", "label": "Yükler", "options": "Lojinet Sefer Yuk"},
            {"fieldname": "navlun_tutar", "fieldtype": "Currency", "label": "Navlun"},
            {"fieldname": "toplam_fiyat", "fieldtype": "Currency", "label": "Toplam", "read_only": 1},
        ]
    },
    
    "Lojinet Sefer Yuk": {
        "istable": 1,
        "fields": [
            {"fieldname": "yuk", "fieldtype": "Link", "label": "Yük", "options": "Lojinet Yuk", "reqd": 1, "in_list_view": 1},
            {"fieldname": "irsaliye_no", "fieldtype": "Data", "label": "İrsaliye No", "in_list_view": 1},
        ]
    },
    
    # Fiyat Anlaşması
    "Lojinet Fiyat Anlasmasi": {
        "autoname": "naming_series:",
        "fields": [
            {"fieldname": "naming_series", "fieldtype": "Select", "label": "Seri", "options": "FA-.YYYY.-.####"},
            {"fieldname": "cari", "fieldtype": "Link", "label": "Cari", "options": "Lojinet Cari", "reqd": 1},
            {"fieldname": "baslangic_tarihi", "fieldtype": "Date", "label": "Başlangıç"},
            {"fieldname": "bitis_tarihi", "fieldtype": "Date", "label": "Bitiş"},
            {"fieldname": "fiyat_kalemleri", "fieldtype": "Table", "label": "Kalemler", "options": "Lojinet Fiyat Anlasmasi Detay"},
        ]
    },
    
    "Lojinet Fiyat Anlasmasi Detay": {
        "istable": 1,
        "fields": [
            {"fieldname": "masraf_kalemi", "fieldtype": "Data", "label": "Kalem", "reqd": 1, "in_list_view": 1},
            {"fieldname": "birim_fiyat", "fieldtype": "Currency", "label": "Birim Fiyat", "reqd": 1, "in_list_view": 1},
        ]
    },
    
    # Ödeme Tahsilat
    "Lojinet Odeme Tahsilat": {
        "autoname": "naming_series:",
        "fields": [
            {"fieldname": "naming_series", "fieldtype": "Select", "label": "Seri", "options": "OT-.YYYY.-.####"},
            {"fieldname": "islem_tipi", "fieldtype": "Select", "label": "İşlem Tipi", "options": "Ödeme\nTahsilat", "reqd": 1},
            {"fieldname": "cari", "fieldtype": "Link", "label": "Cari", "options": "Lojinet Cari", "reqd": 1},
            {"fieldname": "tarih", "fieldtype": "Date", "label": "Tarih", "default": "Today", "reqd": 1},
            {"fieldname": "odeme_turu", "fieldtype": "Select", "label": "Ödeme Türü", "options": "Nakit\nHavale\nÇek", "reqd": 1},
            {"fieldname": "tutar", "fieldtype": "Currency", "label": "Tutar", "reqd": 1},
            {"fieldname": "cek", "fieldtype": "Link", "label": "Çek", "options": "Lojinet Cek"},
        ]
    },
    
    # Çek
    "Lojinet Cek": {
        "autoname": "naming_series:",
        "fields": [
            {"fieldname": "naming_series", "fieldtype": "Select", "label": "Seri", "options": "CEK-.YYYY.-.####"},
            {"fieldname": "cek_no", "fieldtype": "Data", "label": "Çek No", "reqd": 1},
            {"fieldname": "banka", "fieldtype": "Data", "label": "Banka"},
            {"fieldname": "sube", "fieldtype": "Data", "label": "Şube"},
            {"fieldname": "tutar", "fieldtype": "Currency", "label": "Tutar", "reqd": 1},
            {"fieldname": "vade_tarihi", "fieldtype": "Date", "label": "Vade Tarihi"},
            {"fieldname": "cek_durumu", "fieldtype": "Select", "label": "Durum", "options": "Portföyde\nCiro Edildi\nTahsil Edildi\nİade", "default": "Portföyde"},
        ]
    },
    
    # Destek Bileti
    "Lojinet Destek Bileti": {
        "autoname": "naming_series:",
        "fields": [
            {"fieldname": "naming_series", "fieldtype": "Select", "label": "Seri", "options": "TKT-.YYYY.-.####"},
            {"fieldname": "musteri", "fieldtype": "Link", "label": "Müşteri", "options": "Lojinet Cari", "reqd": 1},
            {"fieldname": "yuk", "fieldtype": "Link", "label": "Yük", "options": "Lojinet Yuk"},
            {"fieldname": "konu", "fieldtype": "Data", "label": "Konu", "reqd": 1},
            {"fieldname": "aciklama", "fieldtype": "Text", "label": "Açıklama", "reqd": 1},
            {"fieldname": "durum", "fieldtype": "Select", "label": "Durum", "options": "Açık\nİşlemde\nKapalı", "default": "Açık"},
            {"fieldname": "mesajlar", "fieldtype": "Table", "label": "Mesajlar", "options": "Lojinet Destek Mesaj"},
        ]
    },
    
    "Lojinet Destek Mesaj": {
        "istable": 1,
        "fields": [
            {"fieldname": "mesaj", "fieldtype": "Text", "label": "Mesaj", "reqd": 1, "in_list_view": 1},
            {"fieldname": "gonderici", "fieldtype": "Link", "label": "Gönderici", "options": "User", "in_list_view": 1},
            {"fieldname": "tarih", "fieldtype": "Datetime", "label": "Tarih", "default": "Now", "in_list_view": 1},
        ]
    },
    
    # Online Mutabakat
    "Lojinet Online Mutabakat": {
        "autoname": "naming_series:",
        "fields": [
            {"fieldname": "naming_series", "fieldtype": "Select", "label": "Seri", "options": "MUT-.YYYY.-.####"},
            {"fieldname": "cari", "fieldtype": "Link", "label": "Cari", "options": "Lojinet Cari", "reqd": 1},
            {"fieldname": "ay", "fieldtype": "Select", "label": "Ay", "options": "01\n02\n03\n04\n05\n06\n07\n08\n09\n10\n11\n12", "reqd": 1},
            {"fieldname": "yil", "fieldtype": "Int", "label": "Yıl", "reqd": 1},
            {"fieldname": "durum", "fieldtype": "Select", "label": "Durum", "options": "Cevap Bekleniyor\nOnaylandı\nReddedildi", "default": "Cevap Bekleniyor"},
            {"fieldname": "onay_tarihi", "fieldtype": "Datetime", "label": "Onay Tarihi"},
            {"fieldname": "ip_adresi", "fieldtype": "Data", "label": "IP Adresi"},
            {"fieldname": "red_aciklamasi", "fieldtype": "Text", "label": "Red Açıklaması"},
        ]
    },
    
    # Evrak
    "Lojinet Evrak": {
        "autoname": "naming_series:",
        "fields": [
            {"fieldname": "naming_series", "fieldtype": "Select", "label": "Seri", "options": "EVR-.YYYY.-.####"},
            {"fieldname": "musteri", "fieldtype": "Link", "label": "Müşteri", "options": "Lojinet Cari", "reqd": 1},
            {"fieldname": "yuk", "fieldtype": "Link", "label": "Yük", "options": "Lojinet Yuk"},
            {"fieldname": "yil", "fieldtype": "Int", "label": "Yıl", "reqd": 1},
            {"fieldname": "ay", "fieldtype": "Select", "label": "Ay", "options": "01\n02\n03\n04\n05\n06\n07\n08\n09\n10\n11\n12", "reqd": 1},
            {"fieldname": "dosya", "fieldtype": "Attach", "label": "Dosya"},
        ]
    },
    
    # Depo
    "Lojinet Depo": {
        "autoname": "field:depo_kodu",
        "fields": [
            {"fieldname": "depo_kodu", "fieldtype": "Data", "label": "Depo Kodu", "reqd": 1, "unique": 1},
            {"fieldname": "depo_adi", "fieldtype": "Data", "label": "Depo Adı", "reqd": 1},
            {"fieldname": "adres", "fieldtype": "Small Text", "label": "Adres"},
            {"fieldname": "kapasite", "fieldtype": "Float", "label": "Kapasite (m³)"},
        ]
    },
    
    # SaaS
    "Lojinet Saas Paket": {
        "autoname": "field:paket_adi",
        "fields": [
            {"fieldname": "paket_adi", "fieldtype": "Data", "label": "Paket Adı", "reqd": 1, "unique": 1},
            {"fieldname": "aylik_fiyat", "fieldtype": "Currency", "label": "Aylık Fiyat"},
            {"fieldname": "yillik_fiyat", "fieldtype": "Currency", "label": "Yıllık Fiyat"},
            {"fieldname": "kullanici_sayisi", "fieldtype": "Int", "label": "Kullanıcı Sayısı"},
        ]
    },
    
    "Lojinet Saas Musteri": {
        "autoname": "naming_series:",
        "fields": [
            {"fieldname": "naming_series", "fieldtype": "Select", "label": "Seri", "options": "SM-.YYYY.-.####"},
            {"fieldname": "firma_adi", "fieldtype": "Data", "label": "Firma Adı", "reqd": 1},
            {"fieldname": "paket", "fieldtype": "Link", "label": "Paket", "options": "Lojinet Saas Paket"},
            {"fieldname": "baslangic_tarihi", "fieldtype": "Date", "label": "Başlangıç"},
            {"fieldname": "bitis_tarihi", "fieldtype": "Date", "label": "Bitiş"},
            {"fieldname": "durum", "fieldtype": "Select", "label": "Durum", "options": "Aktif\nPasif\nDeneme", "default": "Deneme"},
        ]
    },
}

def create_doctype_files(doctype_name, config):
    """DocType için JSON ve PY dosyalarını oluştur"""
    # Dizin adı
    dir_name = doctype_name.lower().replace(" ", "_")
    dir_path = os.path.join(BASE_DIR, dir_name)
    
    # Dizin oluştur
    os.makedirs(dir_path, exist_ok=True)
    
    # JSON dosyası
    json_content = {
        "actions": [],
        "creation": "2025-01-01 00:00:00.000000",
        "doctype": "DocType",
        "engine": "InnoDB",
        "field_order": [f["fieldname"] for f in config["fields"]],
        "fields": config["fields"],
        "index_web_pages_for_search": 1,
        "links": [],
        "modified": "2025-01-01 00:00:00.000000",
        "modified_by": "Administrator",
        "module": "Lojinet",
        "name": doctype_name,
        "owner": "Administrator",
        "sort_field": "modified",
        "sort_order": "DESC",
        "states": [],
        "track_changes": 1,
    }
    
    # Ek alanlar
    if "is_submittable" in config:
        json_content["is_submittable"] = config["is_submittable"]
    if "autoname" in config:
        json_content["autoname"] = config["autoname"]
        json_content["naming_rule"] = "By \"Naming Series\" field" if config["autoname"] == "naming_series:" else "By fieldname"
    if "istable" in config:
        json_content["istable"] = config["istable"]
    else:
        json_content["permissions"] = [
            {
                "create": 1, "delete": 1, "email": 1, "export": 1,
                "print": 1, "read": 1, "report": 1, "role": "System Manager",
                "share": 1, "write": 1
            }
        ]
        if config.get("is_submittable"):
            json_content["permissions"][0]["submit"] = 1
    
    # JSON dosyasını yaz
    json_file = os.path.join(dir_path, f"{dir_name}.json")
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(json_content, f, indent=1, ensure_ascii=False)
    
    # PY dosyası
    py_content = f"""# -*- coding: utf-8 -*-
# Copyright (c) 2025, Lojinet Team
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class {doctype_name.replace(' ', '')}(Document):
    pass
"""
    
    py_file = os.path.join(dir_path, f"{dir_name}.py")
    with open(py_file, 'w', encoding='utf-8') as f:
        f.write(py_content)
    
    # __init__.py
    init_file = os.path.join(dir_path, "__init__.py")
    with open(init_file, 'w', encoding='utf-8') as f:
        f.write("# -*- coding: utf-8 -*-\nfrom __future__ import unicode_literals\n")
    
    print(f"✓ {doctype_name} oluşturuldu")

# Tüm DocType'ları oluştur
print("DocType'lar oluşturuluyor...")
for doctype_name, config in DOCTYPES.items():
    create_doctype_files(doctype_name, config)

print(f"\n✓ Toplam {len(DOCTYPES)} DocType oluşturuldu!")
