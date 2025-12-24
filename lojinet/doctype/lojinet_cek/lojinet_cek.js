frappe.ui.form.on('Lojinet Cek', {
    refresh: function(frm) {
        if (!frm.is_new() && frm.doc.durum === 'Portföy' && frm.doc.ciro_edilebilir) {
            frm.add_custom_button(__('Çek Ciro Et'), function() {
                cek_ciro(frm);
            });
        }
    }
});

function cek_ciro(frm) {
    frappe.prompt({
        label: 'Yeni Cari',
        fieldname: 'yeni_cari',
        fieldtype: 'Link',
        options: 'Lojinet Cari',
        reqd: 1
    }, function(values) {
        frappe.call({
            method: 'lojinet.api.cek_ciro',
            args: {
                cek_id: frm.doc.name,
                yeni_cari: values.yeni_cari
            },
            callback: function(r) {
                if (r.message) {
                    frappe.msgprint('✅ Çek ciro edildi');
                    frm.reload_doc();
                }
            }
        });
    }, 'Çek Ciro', 'Ciro Et');
}
