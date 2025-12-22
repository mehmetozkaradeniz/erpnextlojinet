// Lojinet Yuk Client Script
frappe.ui.form.on('Lojinet Yuk', {
    refresh: function(frm) {
        if (!frm.is_new()) {
            // Fiyat anlaşması uygula butonu
            frm.add_custom_button(__('Fiyat Anlaşmasını Uygula'), function() {
                apply_price_agreement(frm);
            }, __('İşlemler'));
            
            // Mail gönder butonu
            frm.add_custom_button(__('Mail Gönder'), function() {
                frappe.call({
                    method: 'lojinet.api.send_mail_with_pdf',
                    args: {
                        doctype: 'Lojinet Yuk',
                        docname: frm.doc.name
                    },
                    callback: function(r) {
                        frappe.show_alert({message: __('Mail gönderildi'), indicator: 'green'});
                    }
                });
            }, __('İşlemler'));
        }
    },
    
    musteri: function(frm) {
        // Müşteri değiştiğinde otomatik fiyat anlaşması uygula
        if (frm.doc.musteri && frm.doc.islem_tarihi) {
            apply_price_agreement(frm);
        }
    },
    
    islem_tarihi: function(frm) {
        // Tarih değiştiğinde otomatik fiyat anlaşması uygula
        if (frm.doc.musteri && frm.doc.islem_tarihi) {
            apply_price_agreement(frm);
        }
    },
    
    cikis_ili: function(frm) {
        if (frm.doc.musteri && frm.doc.islem_tarihi) {
            apply_price_agreement(frm);
        }
    },
    
    varis_ili: function(frm) {
        if (frm.doc.musteri && frm.doc.islem_tarihi) {
            apply_price_agreement(frm);
        }
    },
    
    alici_cari: function(frm) {
        if (frm.doc.musteri && frm.doc.islem_tarihi) {
            apply_price_agreement(frm);
        }
    }
});

// Fatura koruması
frappe.ui.form.on('Lojinet Yuk Fiyat', {
    yuk_fiyatlari_remove: function(frm, cdt, cdn) {
        let row = locals[cdt][cdn];
        if (row.fatura_durumu === 'Faturalandı') {
            frappe.msgprint(__('Faturalanmış satır silinemez!'));
            frappe.validated = false;
            return false;
        }
    },
    
    tutar: function(frm, cdt, cdn) {
        let row = locals[cdt][cdn];
        if (row.fatura_durumu === 'Faturalandı') {
            frappe.msgprint(__('Faturalanmış satır değiştirilemez!'));
            frappe.model.set_value(cdt, cdn, 'tutar', row.__unsaved.tutar || row.tutar);
            return false;
        }
    }
});

function apply_price_agreement(frm) {
    if (!frm.doc.musteri) {
        frappe.msgprint(__('Lütfen önce müşteri seçin'));
        return;
    }
    
    // Faturalanan fiyat var mı kontrol et
    let has_invoiced = frm.doc.yuk_fiyatlari.some(f => f.fatura_durumu === 'Faturalandı');
    if (has_invoiced) {
        frappe.msgprint(__('Bu yükte faturalanmış fiyatlar var, yeni anlaşma eklenemez'));
        return;
    }
    
    // Zaten anlaşma fiyatı var mı kontrol et
    let has_agreement = frm.doc.yuk_fiyatlari.some(f => f.fiyat_anlasmasi);
    if (has_agreement) {
        frappe.confirm(
            __('Bu yükte zaten anlaşma fiyatı var. Yeniden uygulamak ister misiniz?'),
            function() {
                // Mevcut anlaşma fiyatlarını temizle
                frm.doc.yuk_fiyatlari = frm.doc.yuk_fiyatlari.filter(f => !f.fiyat_anlasmasi);
                frm.refresh_field('yuk_fiyatlari');
                // Form'u kaydet (validate otomatik çalışacak)
                frm.save();
            }
        );
        return;
    }
    
    // Form'u kaydet (validate içinde apply_price_agreement otomatik çalışacak)
    frm.save();
}
