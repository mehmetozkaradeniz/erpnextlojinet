# -*- coding: utf-8 -*-
import frappe
from frappe.model.document import Document
from frappe.utils import flt, now

class LojinetYuk(Document):
    def before_save(self):
        if not self.olusturma_tarihi:
            self.olusturma_tarihi = now()
    
    def validate(self):
        self.apply_price_agreement()
        self.calculate_total_price()
        for price in self.yuk_fiyatlari:
            price.toplam = flt(price.miktar) * flt(price.birim_fiyat)
    
    def on_update(self):
        if self.sefer:
            self.update_sefer_bilgileri()
    
    def apply_price_agreement(self):
        if any(f.fatura_durumu == "Faturalandı" for f in self.yuk_fiyatlari):
            return
        if any(f.fiyat_anlasmasi for f in self.yuk_fiyatlari):
            return
        
        total_miktar = sum(flt(item.miktar) for item in self.yuk_kalemleri) or 1
        
        agreement = frappe.db.sql("""
            SELECT name, birim_fiyat
            FROM `tabLojinet Fiyat Anlasmasi`
            WHERE (cari = %(musteri)s OR cari IS NULL)
              AND (cikis_ili = %(cikis)s OR cikis_ili IS NULL)
              AND (varis_ili = %(varis)s OR varis_ili IS NULL)
              AND docstatus = 1
            LIMIT 1
        """, {"musteri": self.musteri, "cikis": self.cikis_ili, "varis": self.varis_ili}, as_dict=True)
        
        if agreement:
            ag = agreement[0]
            self.append("yuk_fiyatlari", {
                "masraf_kalemi": "Nakliye",
                "miktar": total_miktar,
                "birim_fiyat": ag.birim_fiyat,
                "toplam": total_miktar * flt(ag.birim_fiyat),
                "fiyat_anlasmasi": ag.name,
                "fatura_durumu": "Faturalanmadı"
            })
    
    def calculate_total_price(self):
        self.toplam_fiyat = sum(flt(p.toplam) for p in self.yuk_fiyatlari)
    
    def update_sefer_bilgileri(self):
        if not self.sefer:
            return
        sefer = frappe.get_doc("Lojinet Sefer", self.sefer)
        self.sefer_no_display = sefer.name
        if sefer.arac:
            self.arac_plaka_display = frappe.db.get_value("Lojinet Arac", sefer.arac, "plaka")
        if sefer.sofor:
            sofor = frappe.db.get_value("Lojinet Sofor", sefer.sofor, ["ad", "soyad", "telefon"], as_dict=True)
            self.sofor_ad_soyad_display = f"{sofor.ad} {sofor.soyad}"
            self.sofor_telefon_display = sofor.telefon
