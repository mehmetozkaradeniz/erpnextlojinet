frappe.ui.form.on('Lojinet Sefer', {
    refresh: function(frm) {
        if (!frm.is_new()) {
            frm.add_custom_button(__('Toplu Yük Ekle'), function() {
                toplu_yuk_ekle(frm);
            });
        }
    }
});

function toplu_yuk_ekle(frm) {
    let d = new frappe.ui.Dialog({
        title: 'Yük Seç',
        fields: [
            {
                fieldname: 'yukler',
                fieldtype: 'MultiCheck',
                label: 'Yükler',
                options: []
            }
        ],
        primary_action_label: 'Ekle',
        primary_action(values) {
            // Seçilen yükleri tabloya ekle
            d.hide();
        }
    });
    d.show();
}
