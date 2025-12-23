# -*- coding: utf-8 -*-
"""
LOJİNET YÜK V2.0
Tüm düzeltmeler uygulandı
"""

import frappe
from frappe.model.document import Document
from frappe.utils import flt, now

class LojinetYuk(Document):
    def before_save(self):
        if not self.olusturma_tarihi:
            self.olusturma_tarihi = now()
        self.guncelleme_tarihi = now()
    
    def validate(self):
        # Fiyat anlaşmasını uygula
        self.apply_price_agreement()
        
        # Stok kontrolü
        self.check_stock_availability()
        
        # Toplam fiyat hesapla
        self.calculate_total_price()
        
        # Fiyat satırlarında miktar x birim_fiyat = toplam
        for price in self.yuk_fiyatlari:
            price.toplam = flt(price.miktar) * flt(price.birim_fiyat)
    
    def on_update_after_submit(self):
        """Submit sonrası da düzenlenebilir - Madde 2"""
        # İşlendi durumunda bile düzenlemeye izin ver
        pass
    
    def apply_price_agreement(self):
        """Fiyat anlaşması - Madde 1: Miktar çarpımı ile"""
        # Faturalanan varsa ekleme
        if any(f.fatura_durumu == "Faturalandı" for f in self.yuk_fiyatlari):
            return
        
        # Zaten anlaşma varsa ekleme
        if any(f.fiyat_anlasmasi for f in self.yuk_fiyatlari):
            return
        
        if not self.musteri or not self.islem_tarihi:
            return
        
        # Kriterlere göre anlaşma bul
        agreement = frappe.db.sql("""
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
                AND (fa.baslangic_tarihi IS NULL OR fa.baslangic_tarihi <= %(tarih)s)
                AND (fa.bitis_tarihi IS NULL OR fa.bitis_tarihi >= %(tarih)s)
                AND (fa.cikis_ili IS NULL OR fa.cikis_ili = %(cikis_ili)s)
                AND (fa.varis_ili IS NULL OR fa.varis_ili = %(varis_ili)s)
                AND (fa.alici_cari IS NULL OR fa.alici_cari = %(alici_cari)s)
                AND fa.docstatus != 2
            HAVING match_score > 0
            ORDER BY match_score DESC
            LIMIT 1
        """, {
            "musteri": self.musteri,
            "tarih": self.islem_tarihi,
            "cikis_ili": self.cikis_ili or "",
            "varis_ili": self.varis_ili or "",
            "alici_cari": self.alici_cari or "",
            "alici_adres": self.alici_adres or ""
        }, as_dict=True)
        
        if not agreement:
            return
        
        ag = agreement[0]
        
        # Yük detayından toplam miktarı al - Madde 1
        total_miktar = sum(flt(item.miktar) for item in self.yuk_kalemleri)
        
        # Fiyat ekle
        self.append("yuk_fiyatlari", {
            "masraf_kalemi": "Nakliye Bedeli",
            "aciklama": f"Anlaşma: {ag.name}",
            "miktar": total_miktar,
            "birim_fiyat": ag.birim_fiyat,
            "toplam": total_miktar * ag.birim_fiyat,
            "fiyat_anlasmasi": ag.name,
            "fatura_durumu": "Faturalanmadı"
        })
        
        frappe.msgprint(f"Fiyat anlaşması uygulandı: {ag.name}", indicator="green")
    
    def check_stock_availability(self):
        """Stok kontrolü"""
        all_available = True
        for item in self.yuk_kalemleri:
            available = frappe.db.sql("""
                SELECT SUM(mkd.miktar)
                FROM `tabLojinet Mal Kabul Detay` mkd
                JOIN `tabLojinet Mal Kabul` mk ON mk.name = mkd.parent
                WHERE mkd.stok_kodu = %s AND mk.cari = %s AND mk.docstatus = 1
            """, (item.stok_kodu, self.musteri))
            
            if flt(available[0][0] if available else 0) < flt(item.miktar):
                all_available = False
                break
        
        # Otomatik durum güncelle - Madde 2
        if all_available and self.yuk_statusu != "Yolda":
            self.yuk_durumu = "Ürün Depoda"
        elif not all_available:
            self.yuk_durumu = "Ürün Bekleniyor"
    
    def calculate_total_price(self):
        """Toplam fiyat hesapla"""
        total = 0
        for price in self.yuk_fiyatlari:
            total += flt(price.toplam)
        self.toplam_fiyat = total

