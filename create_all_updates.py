#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LOJİNET V2.0 - MASTER UPDATE SCRIPT
Tüm 15 maddeyi uygular
"""

import os
import json
import shutil

BASE = "/home/claude/lojinet_v2_final/lojinet"

# DocType'ların JSON yapıları
DOCTYPES = {
    # YENİLENMİŞ: Yük Fiyat
    "lojinet_yuk_fiyat": {
        "istable": 1,
        "fields": [
            {"fieldname": "masraf_kalemi", "fieldtype": "Data", "label": "Masraf Kalemi", "reqd": 1, "in_list_view": 1},
            {"fieldname": "aciklama", "fieldtype": "Small Text", "label": "Açıklama"},
            {"fieldname": "miktar", "fieldtype": "Float", "label": "Miktar", "default": "1", "in_list_view": 1},
            {"fieldname": "birim_fiyat", "fieldtype": "Currency", "label": "Birim Fiyat", "in_list_view": 1},
            {"fieldname": "toplam", "fieldtype": "Currency", "label": "Toplam", "read_only": 1, "in_list_view": 1},
            {"fieldname": "fiyat_anlasmasi", "fieldtype": "Link", "label": "Fiyat Anlaşması", "options": "Lojinet Fiyat Anlasmasi", "read_only": 1},
            {"fieldname": "fatura_durumu", "fieldtype": "Select", "label": "Fatura Durumu", "options": "Faturalanmadı\\nFaturalandı", "default": "Faturalanmadı", "in_list_view": 1},
            {"fieldname": "fatura_no", "fieldtype": "Link", "label": "Fatura No", "options": "Sales Invoice", "read_only": 1},
            {"fieldname": "fatura_tarihi", "fieldtype": "Date", "label": "Fatura Tarihi", "read_only": 1},
        ]
    },
    
    # YENİ: Çek Ciro
    "lojinet_cek_ciro": {
        "autoname": "naming_series:",
        "fields": [
            {"fieldname": "naming_series", "fieldtype": "Select", "label": "Seri", "options": "CC-.YYYY.-.####", "reqd": 1},
            {"fieldname": "cek", "fieldtype": "Link", "label": "Çek", "options": "Lojinet Cek", "reqd": 1},
            {"fieldname": "eski_cari", "fieldtype": "Link", "label": "Eski Cari", "options": "Lojinet Cari", "read_only": 1},
            {"fieldname": "yeni_cari", "fieldtype": "Link", "label": "Yeni Cari", "options": "Lojinet Cari", "reqd": 1},
            {"fieldname": "ciro_tarihi", "fieldtype": "Date", "label": "Ciro Tarihi", "default": "Today", "reqd": 1},
            {"fieldname": "tutar", "fieldtype": "Currency", "label": "Tutar", "read_only": 1},
            {"fieldname": "aciklama", "fieldtype": "Small Text", "label": "Açıklama"},
        ]
    },
    
    # YENİ: B2B Kullanıcı
    "lojinet_b2b_kullanici": {
        "autoname": "field:email",
        "fields": [
            {"fieldname": "email", "fieldtype": "Data", "label": "Email", "reqd": 1, "unique": 1},
            {"fieldname": "cari", "fieldtype": "Link", "label": "Cari", "options": "Lojinet Cari", "reqd": 1},
            {"fieldname": "ad_soyad", "fieldtype": "Data", "label": "Ad Soyad", "reqd": 1},
            {"fieldname": "telefon", "fieldtype": "Data", "label": "Telefon"},
            {"fieldname": "aktif", "fieldtype": "Check", "label": "Aktif", "default": "1"},
            {"fieldname": "api_key", "fieldtype": "Data", "label": "API Key", "read_only": 1},
            {"fieldname": "son_giris", "fieldtype": "Datetime", "label": "Son Giriş", "read_only": 1},
        ]
    },
}

def create_doctype_folder(doctype_name, config):
    """DocType klasörü ve dosyalarını oluştur"""
    dir_name = doctype_name.lower()
    dir_path = os.path.join(BASE, "lojinet", "doctype", dir_name)
    
    os.makedirs(dir_path, exist_ok=True)
    
    # JSON
    json_content = {
        "creation": "2025-12-23 00:00:00",
        "doctype": "DocType",
        "engine": "InnoDB",
        "field_order": [f["fieldname"] for f in config["fields"]],
        "fields": config["fields"],
        "modified": "2025-12-23 00:00:00",
        "module": "Lojinet",
        "name": doctype_name.replace("_", " ").title(),
        "permissions": [{"create": 1, "delete": 1, "read": 1, "write": 1, "role": "System Manager"}],
    }
    
    if "autoname" in config:
        json_content["autoname"] = config["autoname"]
        json_content["naming_rule"] = 'By "Naming Series" field'
    
    if "istable" in config:
        json_content["istable"] = 1
    
    with open(f"{dir_path}/{dir_name}.json", "w") as f:
        json.dump(json_content, f, indent=1)
    
    # __init__.py
    open(f"{dir_path}/__init__.py", "w").close()
    
    print(f"✓ {doctype_name}")

# DocType'ları oluştur
print("=" * 60)
print("DOCTYPE'LAR OLUŞTURULUYOR...")
print("=" * 60)
for doctype, config in DOCTYPES.items():
    create_doctype_folder(doctype, config)

print("\\n✅ Tüm DocType'lar oluşturuldu!")

