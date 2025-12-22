# -*- coding: utf-8 -*-
import frappe

def get_context(context):
    context.no_cache = 1
    
    mutabakat_name = frappe.form_dict.get("mutabakat")
    if not mutabakat_name:
        frappe.throw("Geçersiz mutabakat linki")
    
    context.mutabakat = frappe.get_doc("Lojinet Online Mutabakat", mutabakat_name)
    
    return context
