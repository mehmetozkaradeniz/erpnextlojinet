# -*- coding: utf-8 -*-
import frappe
from frappe.utils import flt

def execute(filters=None):
    columns = [
        {"fieldname": "depo_adi", "label": "Depo", "fieldtype": "Link", "options": "Lojinet Depo", "width": 150},
        {"fieldname": "kapasite", "label": "Kapasite (m³)", "fieldtype": "Float", "width": 120},
        {"fieldname": "mevcut_doluluk", "label": "Doluluk (m³)", "fieldtype": "Float", "width": 120},
        {"fieldname": "doluluk_yuzdesi", "label": "Doluluk %", "fieldtype": "Percent", "width": 100},
        {"fieldname": "stok_kodu", "label": "Stok Kodu", "fieldtype": "Data", "width": 120},
        {"fieldname": "stok_adi", "label": "Stok Adı", "fieldtype": "Data", "width": 200},
        {"fieldname": "cari", "label": "Cari", "fieldtype": "Link", "options": "Lojinet Cari", "width": 150},
        {"fieldname": "miktar", "label": "Miktar", "fieldtype": "Float", "width": 80},
        {"fieldname": "birim", "label": "Birim", "fieldtype": "Data", "width": 60}
    ]
    
    # Depo bazında stok detayları
    data = frappe.db.sql("""
        SELECT 
            mk.depo as depo_adi,
            d.kapasite,
            d.mevcut_doluluk,
            d.doluluk_yuzdesi,
            mkd.stok_kodu,
            mkd.urun_adi as stok_adi,
            mk.cari,
            SUM(mkd.miktar) as miktar,
            mkd.birim
        FROM `tabLojinet Mal Kabul` mk
        JOIN `tabLojinet Mal Kabul Detay` mkd ON mkd.parent = mk.name
        LEFT JOIN `tabLojinet Depo` d ON d.name = mk.depo
        WHERE mk.docstatus = 1
        GROUP BY mk.depo, mkd.stok_kodu, mk.cari, mkd.birim
        ORDER BY mk.depo, mkd.stok_kodu
    """, as_dict=True)
    
    return columns, data
