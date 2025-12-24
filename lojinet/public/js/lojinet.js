// LOJİNET V2.0 - Ana JS Dosyası
console.log("✅ Lojinet v2.0 yüklendi");

// Global helper fonksiyonlar
window.lojinet = {
    version: '2.0.0',
    
    hesapla_toplam: function(miktar, birim_fiyat) {
        return flt(miktar) * flt(birim_fiyat);
    },
    
    format_para: function(tutar) {
        return format_currency(tutar, frappe.defaults.get_default("currency"));
    }
};
