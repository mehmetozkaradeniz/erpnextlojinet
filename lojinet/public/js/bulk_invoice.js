// Toplu Faturalama
function create_bulk_invoice_dialog(customer) {
    let d = new frappe.ui.Dialog({
        title: 'Toplu Fatura Oluştur',
        fields: [
            {fieldname: 'customer', fieldtype: 'Link', options: 'Lojinet Cari', label: 'Müşteri', default: customer, read_only: 1},
            {fieldname: 'from_date', fieldtype: 'Date', label: 'Başlangıç'},
            {fieldname: 'to_date', fieldtype: 'Date', label: 'Bitiş'}
        ],
        primary_action_label: 'Oluştur',
        primary_action(values) {
            frappe.call({
                method: 'lojinet.api.create_bulk_invoice',
                args: values,
                callback: function(r) {
                    if (r.message) {
                        frappe.msgprint('✅ Fatura: ' + r.message);
                        d.hide();
                    }
                }
            });
        }
    });
    d.show();
}
