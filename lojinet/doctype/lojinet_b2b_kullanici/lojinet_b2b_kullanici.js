frappe.ui.form.on('Lojinet B2B Kullanici', {
    refresh: function(frm) {
        if (!frm.is_new()) {
            // API Key yenile butonu
            frm.add_custom_button(__('API Key Yenile'), function() {
                frappe.call({
                    method: 'generate_api_key',
                    doc: frm.doc,
                    callback: function(r) {
                        frm.reload_doc();
                        frappe.msgprint('✅ Yeni API Key oluşturuldu');
                    }
                });
            });
            
            // Test login butonu
            frm.add_custom_button(__('Test Login'), function() {
                frappe.prompt({
                    label: 'Şifre',
                    fieldname: 'password',
                    fieldtype: 'Password'
                }, function(values) {
                    frappe.call({
                        method: 'lojinet.api.b2b_login',
                        args: {
                            email: frm.doc.email,
                            password: values.password
                        },
                        callback: function(r) {
                            if (r.message) {
                                frappe.msgprint('✅ Giriş başarılı! API Key: ' + r.message.api_key);
                            } else {
                                frappe.msgprint('❌ Giriş başarısız!');
                            }
                        }
                    });
                }, 'Test Login');
            });
        }
    }
});
