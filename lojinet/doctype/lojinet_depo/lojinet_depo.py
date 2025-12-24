# -*- coding: utf-8 -*-
import frappe
from frappe.model.document import Document
from frappe.utils import flt

class LojinetDepo(Document):
    def validate(self):
        self.calculate_doluluk()
    
    def calculate_doluluk(self):
        """Depo doluluk hesaplama"""
        # Mal kabullerden mevcut stoğu hesapla
        stok_data = frappe.db.sql("""
            SELECT 
                mkd.stok_kodu,
                mkd.urun_adi,
                SUM(mkd.miktar) as toplam_miktar,
                mkd.birim
            FROM `tabLojinet Mal Kabul Detay` mkd
            JOIN `tabLojinet Mal Kabul` mk ON mk.name = mkd.parent
            WHERE mk.depo = %s AND mk.docstatus = 1
            GROUP BY mkd.stok_kodu, mkd.birim
        """, self.depo_adi, as_dict=True)
        
        # Stok detaylarını güncelle
        self.stok_detaylari = []
        total_desi = 0
        
        for stok in stok_data:
            self.append("stok_detaylari", {
                "stok_kodu": stok.stok_kodu,
                "stok_adi": stok.urun_adi,
                "miktar": stok.toplam_miktar,
                "birim": stok.birim
            })
            
            # Basit desi hesabı (örnek: 1 adet = 0.1 m³)
            if stok.birim == "Adet":
                total_desi += flt(stok.toplam_miktar) * 0.1
            elif stok.birim == "M3":
                total_desi += flt(stok.toplam_miktar)
            elif stok.birim == "Kg":
                total_desi += flt(stok.toplam_miktar) * 0.001
        
        self.mevcut_doluluk = total_desi
        
        # Doluluk yüzdesi
        if self.kapasite > 0:
            self.doluluk_yuzdesi = (self.mevcut_doluluk / self.kapasite) * 100
        else:
            self.doluluk_yuzdesi = 0
