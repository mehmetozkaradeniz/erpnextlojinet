# -*- coding: utf-8 -*-
import frappe

def execute(filters=None):
    columns = [
        {"fieldname": "cari", "label": "Cari", "fieldtype": "Link", "options": "Lojinet Cari", "width": 200},
        {"fieldname": "telefon", "label": "Telefon", "fieldtype": "Data", "width": 120},
        {"fieldname": "email", "label": "Email", "fieldtype": "Data", "width": 150},
        {"fieldname": "bakiye", "label": "Bakiye", "fieldtype": "Currency", "width": 120}
    ]
    
    data = frappe.db.sql("""
        SELECT 
            name as cari,
            telefon,
            email,
            COALESCE(bakiye, 0) as bakiye
        FROM `tabLojinet Cari`
        ORDER BY bakiye DESC
    """, as_dict=True)
    
    return columns, data
