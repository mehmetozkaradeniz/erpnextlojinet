# -*- coding: utf-8 -*-
import frappe
from frappe.model.document import Document

class LojinetMalKabul(Document):
    def on_submit(self):
        self.durum = "İşlendi"
        # İlgili yüklerin durumunu güncelle
        for item in self.detaylar:
            yukler = frappe.db.sql("""
                SELECT DISTINCT parent
                FROM `tabLojinet Yuk Detay`
                WHERE stok_kodu = %s
            """, item.stok_kodu, as_list=True)
            
            for yuk_name in yukler:
                yuk = frappe.get_doc("Lojinet Yuk", yuk_name[0])
                yuk.yuk_durumu = "Ürün Depoda"
                yuk.save()
