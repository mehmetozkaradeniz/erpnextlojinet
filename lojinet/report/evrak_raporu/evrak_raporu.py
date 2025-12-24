# -*- coding: utf-8 -*-
import frappe

def execute(filters=None):
    columns = [
        {"fieldname": "evrak_no", "label": "Evrak No", "fieldtype": "Link", "options": "Lojinet Evrak", "width": 120},
        {"fieldname": "musteri", "label": "Müşteri", "fieldtype": "Link", "options": "Lojinet Cari", "width": 150},
        {"fieldname": "evrak_tarihi", "label": "Tarih", "fieldtype": "Date", "width": 100},
        {"fieldname": "evrak_turu", "label": "Evrak Türü", "fieldtype": "Data", "width": 120},
        {"fieldname": "ay", "label": "Ay", "fieldtype": "Data", "width": 80},
        {"fieldname": "yil", "label": "Yıl", "fieldtype": "Data", "width": 60},
        {"fieldname": "dosya_linki", "label": "Dosya", "fieldtype": "Data", "width": 200}
    ]
    
    conditions = "WHERE e.docstatus < 2"
    
    if filters.get("from_date"):
        conditions += f" AND e.evrak_tarihi >= '{filters.get('from_date')}'"
    if filters.get("to_date"):
        conditions += f" AND e.evrak_tarihi <= '{filters.get('to_date')}'"
    if filters.get("musteri"):
        conditions += f" AND e.musteri = '{filters.get('musteri')}'"
    
    data = frappe.db.sql(f"""
        SELECT 
            e.name as evrak_no,
            e.musteri,
            e.evrak_tarihi,
            e.evrak_turu,
            MONTHNAME(e.evrak_tarihi) as ay,
            YEAR(e.evrak_tarihi) as yil,
            e.dosya as dosya_linki
        FROM `tabLojinet Evrak` e
        {conditions}
        ORDER BY e.evrak_tarihi DESC
    """, as_dict=True)
    
    return columns, data
