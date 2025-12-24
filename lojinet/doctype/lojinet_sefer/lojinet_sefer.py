# -*- coding: utf-8 -*-
import frappe
from frappe.model.document import Document
from frappe.utils import flt

class LojinetSefer(Document):
    def validate(self):
        self.calculate_kar_zarar()
    
    def calculate_kar_zarar(self):
        # Yük toplam
        yuk_toplam = 0
        for yuk_row in self.yukler:
            if yuk_row.yuk:
                yuk = frappe.get_doc("Lojinet Yuk", yuk_row.yuk)
                yuk_toplam += flt(yuk.toplam_fiyat)
        
        # Navlun toplam
        navlun_toplam = sum(flt(n.toplam) for n in self.navlun_fiyatlari)
        
        self.yuk_toplam = yuk_toplam
        self.navlun_toplam = navlun_toplam
        self.kar_zarar = yuk_toplam - navlun_toplam
    
    def on_submit(self):
        # Yüklerin durumunu "Yolda" yap
        for yuk_row in self.yukler:
            if yuk_row.yuk:
                frappe.db.set_value("Lojinet Yuk", yuk_row.yuk, "yuk_statusu", "Yolda")

def calculate_kar_zarar(doc, method):
    doc.calculate_kar_zarar()

def update_yukler_status(doc, method):
    for yuk_row in doc.yukler:
        if yuk_row.yuk:
            frappe.db.set_value("Lojinet Yuk", yuk_row.yuk, {
                "yuk_statusu": "Yolda",
                "sefer": doc.name
            })
