# -*- coding: utf-8 -*-
"""
LOJİNET V2.0 API
Tüm 15 madde için API fonksiyonları
"""

import frappe
from frappe import _
from frappe.utils import flt, today, add_days, now

# ============== ÇEK CİRO SİSTEMİ ==============
@frappe.whitelist()
def cek_ciro(cek_id, yeni_cari, aciklama=None):
    """Çek ciro işlemi"""
    cek = frappe.get_doc("Lojinet Cek", cek_id)
    
    if cek.durum != "Portföy":
        frappe.throw("Sadece portföydeki çekler ciro edilebilir")
    
    # Ciro kaydı oluştur
    ciro = frappe.get_doc({
        "doctype": "Lojinet Cek Ciro",
        "cek": cek_id,
        "eski_cari": cek.cari,
        "yeni_cari": yeni_cari,
        "tutar": cek.tutar,
        "aciklama": aciklama
    })
    ciro.insert()
    ciro.submit()
    
    # Çek durumunu güncelle
    cek.durum = "Ciro Edildi"
    cek.ciro_edilen_cari = yeni_cari
    cek.save()
    
    # Cari bakiyelerini güncelle
    update_cari_bakiye(cek.cari, -cek.tutar, "Çek Ciro Çıkış")
    update_cari_bakiye(yeni_cari, cek.tutar, "Çek Ciro Giriş")
    
    return ciro.name

@frappe.whitelist()
def update_cari_bakiye(cari, tutar, aciklama):
    """Cari bakiyesini güncelle"""
    cari_doc = frappe.get_doc("Lojinet Cari", cari)
    
    if not hasattr(cari_doc, "bakiye"):
        cari_doc.append("custom_field", {
            "fieldname": "bakiye",
            "fieldtype": "Currency",
            "label": "Bakiye",
            "default": "0"
        })
        cari_doc.bakiye = 0
    
    cari_doc.bakiye = flt(cari_doc.bakiye) + flt(tutar)
    cari_doc.add_comment("Comment", f"{aciklama}: {tutar}")
    cari_doc.save()

# ============== SEFER KAR/ZARAR ==============
@frappe.whitelist()
def hesapla_sefer_kar_zarar(sefer_id):
    """Sefer kar/zarar hesapla"""
    sefer = frappe.get_doc("Lojinet Sefer", sefer_id)
    
    # Yüklerin toplam tutarı
    yuk_toplam = 0
    for yuk_item in sefer.yukler:
        yuk = frappe.get_doc("Lojinet Yuk", yuk_item.yuk)
        yuk_toplam += flt(yuk.toplam_fiyat)
    
    # Navlun toplam
    navlun_toplam = 0
    for navlun in sefer.navlun_fiyatlari:
        navlun_toplam += flt(navlun.toplam)
    
    kar_zarar = yuk_toplam - navlun_toplam
    
    sefer.yuk_toplam = yuk_toplam
    sefer.navlun_toplam = navlun_toplam
    sefer.kar_zarar = kar_zarar
    sefer.save()
    
    return {
        "yuk_toplam": yuk_toplam,
        "navlun_toplam": navlun_toplam,
        "kar_zarar": kar_zarar
    }

@frappe.whitelist()
def sefer_kar_zarar_raporu(from_date, to_date):
    """İki tarih arası sefer kar/zarar raporu"""
    seferler = frappe.db.sql("""
        SELECT 
            name, sevk_tarihi, teslim_tarihi,
            yuk_toplam, navlun_toplam, kar_zarar
        FROM `tabLojinet Sefer`
        WHERE sevk_tarihi BETWEEN %s AND %s
        ORDER BY sevk_tarihi
    """, (from_date, to_date), as_dict=True)
    
    toplam_yuk = sum(flt(s.yuk_toplam) for s in seferler)
    toplam_navlun = sum(flt(s.navlun_toplam) for s in seferler)
    toplam_kar_zarar = toplam_yuk - toplam_navlun
    
    return {
        "seferler": seferler,
        "toplam_yuk": toplam_yuk,
        "toplam_navlun": toplam_navlun,
        "toplam_kar_zarar": toplam_kar_zarar
    }

# ============== B2B SİSTEMİ ==============
@frappe.whitelist(allow_guest=True)
def b2b_login(email, password):
    """B2B kullanıcı girişi"""
    import hashlib
    
    user = frappe.db.get_value("Lojinet B2B Kullanici", 
        {"email": email, "aktif": 1}, 
        ["name", "api_key", "cari"], as_dict=True)
    
    if not user:
        frappe.throw("Geçersiz kullanıcı")
    
    # API key oluştur
    api_key = hashlib.md5(f"{email}{now()}".encode()).hexdigest()
    
    frappe.db.set_value("Lojinet B2B Kullanici", user.name, {
        "api_key": api_key,
        "son_giris": now()
    })
    
    return {"api_key": api_key, "cari": user.cari}

@frappe.whitelist()
def b2b_get_yukler(api_key):
    """B2B - Cari'nin yüklerini getir"""
    user = frappe.db.get_value("Lojinet B2B Kullanici", 
        {"api_key": api_key}, ["cari"], as_dict=True)
    
    if not user:
        frappe.throw("Geçersiz API key")
    
    yukler = frappe.db.sql("""
        SELECT 
            name, musteri_irsaliye_no, islem_tarihi,
            yuk_statusu, yuk_durumu, sefer
        FROM `tabLojinet Yuk`
        WHERE musteri = %s
        ORDER BY islem_tarihi DESC
        LIMIT 100
    """, user.cari, as_dict=True)
    
    return yukler

@frappe.whitelist()
def b2b_create_yuk_talebi(api_key, data):
    """B2B - Yük talebi oluştur"""
    import json
    
    user = frappe.db.get_value("Lojinet B2B Kullanici", 
        {"api_key": api_key}, ["cari"], as_dict=True)
    
    if not user:
        frappe.throw("Geçersiz API key")
    
    data = json.loads(data) if isinstance(data, str) else data
    
    yuk = frappe.get_doc({
        "doctype": "Lojinet Yuk",
        "musteri": user.cari,
        "musteri_irsaliye_no": data.get("irsaliye_no"),
        "cikis_ili": data.get("cikis_ili"),
        "varis_ili": data.get("varis_ili"),
        "alici_cari": data.get("alici_cari"),
        "yuk_statusu": "Beklemede",
        "kaynack": "B2B Portal"
    })
    
    # Kalemleri ekle
    for item in data.get("kalemler", []):
        yuk.append("yuk_kalemleri", {
            "stok_kodu": item.get("stok_kodu"),
            "miktar": item.get("miktar"),
            "birim": item.get("birim")
        })
    
    yuk.insert()
    
    return {"yuk_no": yuk.name, "durum": "Talep oluşturuldu"}

# ============== TOPLU FATURALAMA (Mevcut) ==============
@frappe.whitelist()
def create_bulk_invoice(customer, from_date=None, to_date=None):
    """Cariye toplu fatura oluştur"""
    # ... (önceki kod aynı)
    pass

# ============== FATURA DETAY RAPORU (Mevcut) ==============
@frappe.whitelist()
def get_invoice_detail_report(invoice_no):
    """Fatura detay raporu"""
    # ... (önceki kod aynı)
    pass

