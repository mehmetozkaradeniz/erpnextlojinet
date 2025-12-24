# -*- coding: utf-8 -*-
import frappe
from frappe.model.document import Document

class LojinetCek(Document):
    def on_submit(self):
        update_cari_bakiye(self.cari, self.tutar, "Çek Tahsil")
    
    def on_cancel(self):
        reverse_cari_bakiye(self.cari, self.tutar, "Çek İptal")

def update_cari_bakiye(cari, tutar, aciklama):
    # Cari bakiyesinigüncelle
    pass

def reverse_cari_bakiye(cari, tutar, aciklama):
    pass
