# -*- coding: utf-8 -*-
import frappe
from frappe.model.document import Document
from frappe.utils import flt

class LojinetOdemeTahsilat(Document):
    def validate(self):
        # Çek seçildiyse bilgileri doldur
        if self.odeme_yontemi == "Çek" and self.cek:
            cek = frappe.get_doc("Lojinet Cek", self.cek)
            self.cek_no_display = cek.cek_no
            self.cek_tutar_display = cek.tutar
            self.cek_vade_display = cek.vade_tarihi
            
            # Tutar çek tutarı ile uyumlu olmalı
            if flt(self.tutar) != flt(cek.tutar):
                frappe.msgprint(f"⚠️ Uyarı: Tutar ({self.tutar}) çek tutarından ({cek.tutar}) farklı!")
    
    def on_submit(self):
        # Cari bakiye güncelle
        if self.islem_turu == "Tahsilat":
            update_cari_bakiye(self.cari, -self.tutar, f"Tahsilat: {self.name}")
        else:  # Ödeme
            update_cari_bakiye(self.cari, self.tutar, f"Ödeme: {self.name}")
        
        # Çek durumunu güncelle
        if self.odeme_yontemi == "Çek" and self.cek:
            cek = frappe.get_doc("Lojinet Cek", self.cek)
            if self.islem_turu == "Tahsilat":
                cek.durum = "Tahsil Edildi"
            else:
                cek.durum = "Ödendi"
            cek.save()

def update_cari_bakiye(cari, tutar, aciklama):
    """Cari bakiye güncelle"""
    cari_doc = frappe.get_doc("Lojinet Cari", cari)
    
    if not hasattr(cari_doc, 'bakiye'):
        cari_doc.bakiye = 0
    
    cari_doc.bakiye = flt(cari_doc.bakiye) + flt(tutar)
    cari_doc.add_comment("Comment", f"{aciklama}: {tutar}")
    cari_doc.save(ignore_permissions=True)
