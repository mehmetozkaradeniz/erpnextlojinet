# -*- coding: utf-8 -*-
import frappe

def execute(filters=None):
    columns = [
        {"fieldname": "cek_no", "label": "Çek No", "fieldtype": "Data", "width": 100},
        {"fieldname": "cari", "label": "Cari", "fieldtype": "Link", "options": "Lojinet Cari", "width": 150},
        {"fieldname": "tutar", "label": "Tutar", "fieldtype": "Currency", "width": 120},
        {"fieldname": "vade_tarihi", "label": "Vade", "fieldtype": "Date", "width": 100},
        {"fieldname": "durum", "label": "Durum", "fieldtype": "Data", "width": 100}
    ]
    
    conditions = "WHERE docstatus = 1"
    if filters.get("durum"):
        conditions += f" AND durum = '{filters.get('durum')}'"
    
    data = frappe.db.sql(f"""
        SELECT cek_no, cari, tutar, vade_tarihi, durum
        FROM `tabLojinet Cek`
        {conditions}
        ORDER BY vade_tarihi
    """, as_dict=True)
    
    return columns, data
