# -*- coding: utf-8 -*-
# Copyright (c) 2025, Lojinet Team
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import flt

class LojinetSefer(Document):
    def validate(self):
        self.calculate_total()
    
    def calculate_total(self):
        self.toplam_fiyat = flt(self.navlun_tutar)
    
    def on_submit(self):
        """Yük statülerini güncelle"""
        for yuk_item in self.sefer_yukleri:
            yuk_doc = frappe.get_doc("Lojinet Yuk", yuk_item.yuk)
            yuk_doc.yuk_statusu = "Yolda"
            yuk_doc.yuk_durumu = "Araçta"
            yuk_doc.save(ignore_permissions=True)
