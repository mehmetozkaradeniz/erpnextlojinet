frappe.ui.form.on('Lojinet Mal Kabul', {
    refresh: function(frm) {
        if (frm.doc.docstatus === 1) {
            frm.set_value('durum', 'İşlendi');
        }
    }
});
