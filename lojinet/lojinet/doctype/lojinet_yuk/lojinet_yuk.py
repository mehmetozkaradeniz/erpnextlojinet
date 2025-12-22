# -*- coding: utf-8 -*-
# Copyright (c) 2025, Lojinet Team
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import flt, now

class LojinetYuk(Document):
    def before_save(self):
        if not self.olusturma_tarihi:
            self.olusturma_tarihi = now()
        self.guncelleme_tarihi = now()
    
    def validate(self):
        self.apply_price_agreement()
        self.check_stock_availability()
        self.calculate_total_price()
    
    def apply_price_agreement(self):
        """Kriter bazlı fiyat anlaşması eşleştirmesi"""
        # Eğer faturalanan fiyat varsa ekleme yapma
        if any(f.fatura_durumu == "Faturalandı" for f in self.yuk_fiyatlari):
            return
        
        # Eğer zaten anlaşma fiyatı varsa tekrar ekleme
        if any(f.fiyat_anlasmasi for f in self.yuk_fiyatlari):
            return
        
        if not self.musteri or not self.islem_tarihi:
            return
        
        # SQL ile gelişmiş kriter eşleştirme
        agreements = frappe.db.sql("""
            SELECT 
                fa.name,
                fa.birim_fiyat,
                (
                    CASE WHEN fa.cari = %(musteri)s THEN 10 ELSE 0 END +
                    CASE WHEN fa.cikis_ili = %(cikis_ili)s THEN 5 ELSE 0 END +
                    CASE WHEN fa.varis_ili = %(varis_ili)s THEN 5 ELSE 0 END +
                    CASE WHEN fa.alici_cari = %(alici_cari)s THEN 5 ELSE 0 END +
                    CASE WHEN fa.alici_adres = %(alici_adres)s THEN 3 ELSE 0 END
                ) as match_score
            FROM `tabLojinet Fiyat Anlasmasi` fa
            WHERE 
                (fa.cari = %(musteri)s OR fa.cari IS NULL)
                AND (fa.baslangic_tarihi IS NULL OR fa.baslangic_tarihi <= %(islem_tarihi)s)
                AND (fa.bitis_tarihi IS NULL OR fa.bitis_tarihi >= %(islem_tarihi)s)
                AND (fa.cikis_ili IS NULL OR fa.cikis_ili = %(cikis_ili)s)
                AND (fa.varis_ili IS NULL OR fa.varis_ili = %(varis_ili)s)
                AND (fa.alici_cari IS NULL OR fa.alici_cari = %(alici_cari)s)
                AND (fa.alici_adres IS NULL OR fa.alici_adres = %(alici_adres)s)
                AND fa.docstatus != 2
            HAVING match_score > 0
            ORDER BY match_score DESC, fa.creation DESC
            LIMIT 1
        """, {
            "musteri": self.musteri,
            "islem_tarihi": self.islem_tarihi,
            "cikis_ili": self.cikis_ili or "",
            "varis_ili": self.varis_ili or "",
            "alici_cari": self.alici_cari or "",
            "alici_adres": self.alici_adres or ""
        }, as_dict=True)
        
        if not agreements:
            return
        
        agreement = agreements[0]
        
        # Anlaşma fiyatını ekle
        self.append("yuk_fiyatlari", {
            "masraf_kalemi": "Nakliye Bedeli",
            "aciklama": f"Anlaşma: {agreement.name}",
            "tutar": agreement.birim_fiyat,
            "fiyat_anlasmasi": agreement.name,
            "fatura_durumu": "Faturalanmadı"
        })
        
        frappe.msgprint(
            f"Fiyat anlaşması uygulandı: {agreement.name}",
            indicator="green",
            alert=True
        )
    
    def check_stock_availability(self):
        """Otomatik stok kontrolü"""
        all_available = True
        for item in self.yuk_kalemleri:
            available_qty = frappe.db.sql("""
                SELECT SUM(mkd.miktar)
                FROM `tabLojinet Mal Kabul Detay` mkd
                JOIN `tabLojinet Mal Kabul` mk ON mk.name = mkd.parent
                WHERE mkd.stok_kodu = %s AND mk.cari = %s AND mk.docstatus = 1
            """, (item.stok_kodu, self.musteri))
            
            if flt(available_qty[0][0] if available_qty else 0) < flt(item.miktar):
                all_available = False
                break
        
        if all_available and self.yuk_statusu != "Yolda":
            self.yuk_durumu = "Ürün Depoda"
        elif not all_available:
            self.yuk_durumu = "Ürün Bekleniyor"
    
    def calculate_total_price(self):
        total = 0
        for price in self.yuk_fiyatlari:
            total += flt(price.tutar)
        self.toplam_fiyat = total
