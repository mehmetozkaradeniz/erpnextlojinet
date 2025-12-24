# -*- coding: utf-8 -*-
import frappe
from frappe.utils import flt

def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data

def get_columns():
    return [
        {"fieldname": "yuk_no", "label": "Yük No", "fieldtype": "Link", "options": "Lojinet Yuk", "width": 120},
        {"fieldname": "musteri_irsaliye_no", "label": "Müşteri İrsaliye", "fieldtype": "Data", "width": 130},
        {"fieldname": "musteri", "label": "Müşteri", "fieldtype": "Link", "options": "Lojinet Cari", "width": 150},
        {"fieldname": "islem_tarihi", "label": "Tarih", "fieldtype": "Date", "width": 100},
        {"fieldname": "cikis_ili", "label": "Çıkış", "fieldtype": "Data", "width": 100},
        {"fieldname": "varis_ili", "label": "Varış", "fieldtype": "Data", "width": "100"},
        {"fieldname": "alici_cari", "label": "Alıcı Firma", "fieldtype": "Link", "options": "Lojinet Cari", "width": 150},
        {"fieldname": "alici_adres", "label": "Alıcı Adres", "fieldtype": "Data", "width": 120},
        {"fieldname": "miktar", "label": "Miktar", "fieldtype": "Float", "width": 80},
        {"fieldname": "birim", "label": "Birim", "fieldtype": "Data", "width": 60},
        {"fieldname": "yuk_statusu", "label": "Durum", "fieldtype": "Data", "width": 100},
        {"fieldname": "toplam_fiyat", "label": "Toplam", "fieldtype": "Currency", "width": 120}
    ]

def get_data(filters):
    conditions = "WHERE y.docstatus = 1"
    
    if filters.get("from_date"):
        conditions += f" AND y.islem_tarihi >= '{filters.get('from_date')}'"
    if filters.get("to_date"):
        conditions += f" AND y.islem_tarihi <= '{filters.get('to_date')}'"
    if filters.get("musteri"):
        conditions += f" AND y.musteri = '{filters.get('musteri')}'"
    if filters.get("yuk_statusu"):
        conditions += f" AND y.yuk_statusu = '{filters.get('yuk_statusu')}'"
    
    data = frappe.db.sql(f"""
        SELECT 
            y.name as yuk_no,
            y.musteri_irsaliye_no,
            y.musteri,
            y.islem_tarihi,
            y.cikis_ili,
            y.varis_ili,
            y.alici_cari,
            y.alici_adres,
            (SELECT SUM(yd.miktar) FROM `tabLojinet Yuk Detay` yd WHERE yd.parent = y.name) as miktar,
            (SELECT yd.birim FROM `tabLojinet Yuk Detay` yd WHERE yd.parent = y.name LIMIT 1) as birim,
            y.yuk_statusu,
            y.toplam_fiyat
        FROM `tabLojinet Yuk` y
        {conditions}
        ORDER BY y.islem_tarihi DESC
    """, as_dict=True)
    
    return data
