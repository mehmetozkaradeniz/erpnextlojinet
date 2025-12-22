// Customer Enhancements
frappe.ui.form.on('Customer', {
    refresh: function(frm) {
        if (!frm.is_new()) {
            frm.add_custom_button(__('B2B Kullanıcı Oluştur'), function() {
                create_b2b_user(frm);
            }, __('Lojinet'));
            
            frm.add_custom_button(__('Mutabakat Gönder'), function() {
                send_mutabakat(frm);
            }, __('Lojinet'));
        }
    }
});

function create_b2b_user(frm) {
    frappe.prompt([
        {label: 'E-posta', fieldname: 'email', fieldtype: 'Data', reqd: 1},
        {label: 'İsim', fieldname: 'first_name', fieldtype: 'Data', reqd: 1},
        {label: 'Soyisim', fieldname: 'last_name', fieldtype: 'Data', reqd: 1}
    ], function(values) {
        frappe.call({
            method: 'lojinet.api.create_b2b_user',
            args: {customer: frm.doc.name, ...values},
            callback: function(r) {
                if (r.message) {
                    frappe.msgprint(__('B2B kullanıcı oluşturuldu'));
                }
            }
        });
    }, 'B2B Kullanıcı Oluştur', 'Oluştur');
}

function send_mutabakat(frm) {
    frappe.prompt([
        {label: 'Ay', fieldname: 'month', fieldtype: 'Select', options: '01\n02\n03\n04\n05\n06\n07\n08\n09\n10\n11\n12', reqd: 1},
        {label: 'Yıl', fieldname: 'year', fieldtype: 'Int', default: new Date().getFullYear(), reqd: 1}
    ], function(values) {
        frappe.call({
            method: 'lojinet.api.send_mutabakat',
            args: {customer: frm.doc.name, ...values},
            callback: function(r) {
                if (r.message) {
                    frappe.msgprint(__('Mutabakat gönderildi'));
                }
            }
        });
    }, 'Online Mutabakat Gönder', 'Gönder');
}
