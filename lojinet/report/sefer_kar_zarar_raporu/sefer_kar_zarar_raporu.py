# -*- coding: utf-8 -*-
import frappe
from frappe.utils import flt

def execute(filters=None):
    columns = [
        {"fieldname": "sefer", "label": "Sefer", "fieldtype": "Link", "options": "Lojinet Sefer", "width": 120},
        {"fieldname": "sevk_tarihi", "label": "Sevk", "fieldtype": "Date", "width": 100},
        {"fieldname": "sofor", "label": "Şoför", "fieldtype": "Link", "options": "Lojinet Sofor", "width": 150},
        {"fieldname": "yuk_toplam", "label": "Yük Toplam", "fieldtype": "Currency", "width": 120},
        {"fieldname": "navlun_toplam", "label": "Navlun", "fieldtype": "Currency", "width": 120},
        {"fieldname": "kar_zarar", "label": "Kar/Zarar", "fieldtype": "Currency", "width": 120}
    ]
    
    conditions = ""
    if filters.get("from_date"):
        conditions += f" AND sevk_tarihi >= '{filters.get('from_date')}'"
    if filters.get("to_date"):
        conditions += f" AND sevk_tarihi <= '{filters.get('to_date')}'"
    
    data = frappe.db.sql(f"""
        SELECT 
            name as sefer,
            sevk_tarihi,
            sofor,
            yuk_toplam,
            navlun_toplam,
            kar_zarar
        FROM `tabLojinet Sefer`
        WHERE docstatus = 1 {conditions}
        ORDER BY sevk_tarihi DESC
    """, as_dict=True)
    
    return columns, data
