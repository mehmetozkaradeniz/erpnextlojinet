frappe.ui.form.on('Lojinet Odeme Tahsilat', {
    onload: function(frm) {
        // Çek seçimini özelleştir - SADECE müsait çekler
        frm.set_query('cek', function() {
            return {
                filters: {
                    'durum': 'Portföy',
                    'ciro_edilebilir': 1
                }
            };
        });
    },
    
    cek: function(frm) {
        if (frm.doc.cek) {
            // Çek bilgilerini getir
            frappe.call({
                method: 'frappe.client.get',
                args: {
                    doctype: 'Lojinet Cek',
                    name: frm.doc.cek
                },
                callback: function(r) {
                    if (r.message) {
                        let cek = r.message;
                        frm.set_value('cek_no_display', cek.cek_no);
                        frm.set_value('cek_tutar_display', cek.tutar);
                        frm.set_value('cek_vade_display', cek.vade_tarihi);
                        frm.set_value('tutar', cek.tutar);
                        
                        frappe.show_alert({
                            message: `✅ Çek: ${cek.cek_no}, Tutar: ${cek.tutar}, Vade: ${cek.vade_tarihi}`,
                            indicator: 'green'
                        });
                    }
                }
            });
        }
    },
    
    odeme_yontemi: function(frm) {
        // Çek değilse çek alanlarını temizle
        if (frm.doc.odeme_yontemi != 'Çek') {
            frm.set_value('cek', '');
            frm.set_value('cek_no_display', '');
            frm.set_value('cek_tutar_display', '');
            frm.set_value('cek_vade_display', '');
        }
    }
});
