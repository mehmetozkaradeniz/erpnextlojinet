# -*- coding: utf-8 -*-
import frappe

def get_context(context):
    context.no_cache = 1
    
    if frappe.session.user == "Guest":
        frappe.local.flags.redirect_location = "/login"
        raise frappe.Redirect
    
    customer = frappe.db.get_value("User", frappe.session.user, "lojinet_customer")
    
    if not customer:
        frappe.throw("Bu sayfaya erişim yetkiniz yok")
    
    context.customer = customer
    context.yukler = frappe.get_all("Lojinet Yuk",
        filters={"musteri": customer},
        fields=["name", "musteri_irsaliye_no", "yuk_statusu", "yuk_durumu", "islem_tarihi"],
        order_by="islem_tarihi desc",
        limit=50
    )
    
    context.tickets = frappe.get_all("Lojinet Destek Bileti",
        filters={"musteri": customer},
        fields=["name", "konu", "durum", "creation"],
        order_by="creation desc",
        limit=20
    )
    
    context.temsilci = frappe.db.get_value("Lojinet Cari", customer, "musteri_temsilcisi")
    
    return context
