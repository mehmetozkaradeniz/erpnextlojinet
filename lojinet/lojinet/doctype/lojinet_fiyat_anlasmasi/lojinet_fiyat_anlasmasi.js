// Lojinet Fiyat Anlasmasi Client Script
frappe.ui.form.on('Lojinet Fiyat Anlasmasi', {
    refresh: function(frm) {
        if (!frm.is_new()) {
            frm.add_custom_button(__('Bu Anlaşmayı Kullan'), function() {
                frappe.msgprint({
                    title: __('Fiyat Anlaşması'),
                    message: __('Bu anlaşma tarihleri içinde oluşturulan yüklere otomatik olarak uygulanacaktır.'),
                    indicator: 'blue'
                });
            });
        }
    },
    
    cari: function(frm) {
        // Müşteri seçildiğinde bilgi mesajı
        if (frm.doc.cari) {
            frappe.db.get_value('Lojinet Cari', frm.doc.cari, 'cari_adi').then(r => {
                frappe.show_alert({
                    message: __('Müşteri: {0}', [r.message.cari_adi]),
                    indicator: 'blue'
                });
            });
        }
    },
    
    validate: function(frm) {
        // Tarih kontrolü
        if (frm.doc.baslangic_tarihi && frm.doc.bitis_tarihi) {
            if (frm.doc.bitis_tarihi < frm.doc.baslangic_tarihi) {
                frappe.msgprint(__('Bitiş tarihi başlangıç tarihinden önce olamaz!'));
                frappe.validated = false;
            }
        }
    }
});

frappe.ui.form.on('Lojinet Fiyat Anlasmasi Detay', {
    birim_fiyat: function(frm, cdt, cdn) {
        // Toplam hesaplama (isteğe bağlı)
        calculate_total(frm);
    },
    
    fiyat_kalemleri_remove: function(frm) {
        calculate_total(frm);
    }
});

function calculate_total(frm) {
    let total = 0;
    frm.doc.fiyat_kalemleri.forEach(function(item) {
        total += flt(item.birim_fiyat);
    });
    
    // Toplam bilgisi göster (custom field gerekirse eklenebilir)
    if (total > 0) {
        frm.set_intro(__('Toplam Fiyat: {0}', [format_currency(total)]), 'blue');
    }
}
