#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Yeni Fiyat Anlaşması DocType Generator
Gelişmiş kriter bazlı fiyat anlaşması
"""

import os
import json

BASE_DIR = "/home/claude/lojinet/lojinet/lojinet/doctype"

# Yeni Fiyat Anlaşması yapısı
NEW_FIYAT_ANLASMASI = {
    "Lojinet Fiyat Anlasmasi": {
        "autoname": "naming_series:",
        "fields": [
            {"fieldname": "naming_series", "fieldtype": "Select", "label": "Seri", "options": "FA-.YYYY.-.####", "reqd": 1},
            {"fieldname": "section_break_1", "fieldtype": "Section Break", "label": "Temel Bilgiler"},
            {"fieldname": "cari", "fieldtype": "Link", "label": "Cari (Gönderen)", "options": "Lojinet Cari", "in_list_view": 1},
            {"fieldname": "column_break_1", "fieldtype": "Column Break"},
            {"fieldname": "baslangic_tarihi", "fieldtype": "Date", "label": "Başlangıç Tarihi"},
            {"fieldname": "bitis_tarihi", "fieldtype": "Date", "label": "Bitiş Tarihi"},
            
            {"fieldname": "section_break_2", "fieldtype": "Section Break", "label": "Kriter Detayları"},
            {"fieldname": "cikis_ili", "fieldtype": "Data", "label": "Çıkış İli"},
            {"fieldname": "varis_ili", "fieldtype": "Data", "label": "Varış İli", "in_list_view": 1},
            {"fieldname": "column_break_2", "fieldtype": "Column Break"},
            {"fieldname": "urun_karti", "fieldtype": "Link", "label": "Ürün Kartı", "options": "Item"},
            {"fieldname": "birim", "fieldtype": "Link", "label": "Birim", "options": "UOM"},
            
            {"fieldname": "section_break_3", "fieldtype": "Section Break", "label": "Alıcı Bilgileri"},
            {"fieldname": "alici_cari", "fieldtype": "Link", "label": "Alıcı Cari", "options": "Lojinet Cari"},
            {"fieldname": "alici_adres", "fieldtype": "Link", "label": "Alıcı Adres", "options": "Lojinet Cari Adres"},
            {"fieldname": "column_break_3", "fieldtype": "Column Break"},
            {"fieldname": "desi", "fieldtype": "Float", "label": "Desi"},
            
            {"fieldname": "section_break_4", "fieldtype": "Section Break", "label": "Fiyat"},
            {"fieldname": "birim_fiyat", "fieldtype": "Currency", "label": "Birim Fiyat", "reqd": 1, "in_list_view": 1},
            {"fieldname": "aciklama", "fieldtype": "Small Text", "label": "Açıklama"},
        ]
    }
}

def update_doctype(doctype_name, config):
    """DocType'ı güncelle"""
    dir_name = doctype_name.lower().replace(" ", "_")
    dir_path = os.path.join(BASE_DIR, dir_name)
    
    os.makedirs(dir_path, exist_ok=True)
    
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
        "permissions": [
            {
                "create": 1, "delete": 1, "email": 1, "export": 1,
                "print": 1, "read": 1, "report": 1, "role": "System Manager",
                "share": 1, "write": 1
            }
        ],
        "sort_field": "modified",
        "sort_order": "DESC",
        "states": [],
        "track_changes": 1,
    }
    
    if "autoname" in config:
        json_content["autoname"] = config["autoname"]
        json_content["naming_rule"] = "By \"Naming Series\" field"
    
    json_file = os.path.join(dir_path, f"{dir_name}.json")
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(json_content, f, indent=1, ensure_ascii=False)
    
    print(f"✓ {doctype_name} güncellendi")

print("Fiyat Anlaşması DocType'ı güncelleniyor...")
for doctype_name, config in NEW_FIYAT_ANLASMASI.items():
    update_doctype(doctype_name, config)

print("\n✓ Yeni Fiyat Anlaşması yapısı oluşturuldu!")
