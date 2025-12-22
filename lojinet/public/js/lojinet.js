// Lojinet Public JS
frappe.provide("lojinet");

lojinet.send_mail_with_pdf = function(doctype, docname) {
    frappe.call({
        method: "lojinet.api.send_mail_with_pdf",
        args: { doctype: doctype, docname: docname },
        callback: function(r) {
            if (r.message) {
                frappe.show_alert({message: __('Mail gönderildi'), indicator: 'green'});
            }
        }
    });
};

lojinet.bulk_import_excel = function(frm) {
    let d = new frappe.ui.Dialog({
        title: 'Excel ile Toplu Ürün Ekle',
        fields: [{label: 'Excel Dosyası', fieldname: 'excel_file', fieldtype: 'Attach'}],
        primary_action_label: 'İçe Aktar',
        primary_action(values) {
            frappe.call({
                method: "lojinet.utils.import_excel",
                args: {file_url: values.excel_file, docname: frm.doc.name},
                callback: function(r) {
                    if (r.message) {
                        frm.reload_doc();
                        frappe.show_alert({message: __('Ürünler eklendi'), indicator: 'green'});
                    }
                }
            });
            d.hide();
        }
    });
    d.show();
};

lojinet.add_yukler_to_sefer = function(frm) {
    frappe.prompt([
        {label: 'Yük Listesi', fieldname: 'yukler', fieldtype: 'MultiSelect', options: [], reqd: 1}
    ], function(values) {
        frappe.call({
            method: "lojinet.api.add_yuk_to_sefer",
            args: {sefer_name: frm.doc.name, yuk_list: values.yukler},
            callback: function(r) {
                frm.reload_doc();
            }
        });
    }, 'Yük Ekle');
};
