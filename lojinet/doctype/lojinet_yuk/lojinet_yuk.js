frappe.ui.form.on('Lojinet Yuk', {
    refresh: function(frm) {
        if (frm.doc.name) {
            show_tarihler_tablo(frm);
        }
    },
    sefer: function(frm) {
        if (frm.doc.sefer) {
            frappe.call({
                method: 'frappe.client.get',
                args: {doctype: 'Lojinet Sefer', name: frm.doc.sefer},
                callback: function(r) {
                    if (r.message) {
                        frm.set_value('sefer_no_display', r.message.name);
                        if (r.message.arac) {
                            frappe.db.get_value('Lojinet Arac', r.message.arac, 'plaka', (r) => {
                                frm.set_value('arac_plaka_display', r.plaka);
                            });
                        }
                        if (r.message.sofor) {
                            frappe.db.get_value('Lojinet Sofor', r.message.sofor, ['ad','soyad','telefon'], (r) => {
                                frm.set_value('sofor_ad_soyad_display', r.ad + ' ' + r.soyad);
                                frm.set_value('sofor_telefon_display', r.telefon);
                            });
                        }
                    }
                }
            });
        }
    }
});

frappe.ui.form.on('Lojinet Yuk Fiyat', {
    miktar: function(frm, cdt, cdn) {
        let row = locals[cdt][cdn];
        row.toplam = flt(row.miktar) * flt(row.birim_fiyat);
        frm.refresh_field('yuk_fiyatlari');
        frm.set_value('toplam_fiyat', frm.doc.yuk_fiyatlari.reduce((sum, r) => sum + flt(r.toplam), 0));
    },
    birim_fiyat: function(frm, cdt, cdn) {
        frappe.ui.form.trigger('Lojinet Yuk Fiyat', 'miktar', frm, cdt, cdn);
    }
});

function show_tarihler_tablo(frm) {
    let html = `<table class="table table-bordered">
        <tr><td><b>Oluşturma</b></td><td>${frm.doc.olusturma_tarihi || '-'}</td></tr>
        <tr><td><b>Sevk</b></td><td>${frm.doc.sevk_tarihi || '-'}</td></tr>
        <tr><td><b>Teslim</b></td><td>${frm.doc.teslim_tarihi || '-'}</td></tr>
    </table>`;
    if (!$('.tarihler-tablo').length) {
        $('[data-fieldname="olusturma_tarihi"]').parent().before(html);
    }
}
