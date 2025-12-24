frappe.ui.form.on('Lojinet Depo', {
    refresh: function(frm) {
        if (!frm.is_new()) {
            // Doluluk göstergesi
            show_doluluk_indicator(frm);
            
            // Stok yenile butonu
            frm.add_custom_button(__('Stok Yenile'), function() {
                frm.save();
                frappe.show_alert({
                    message: '✅ Stok bilgileri güncellendi',
                    indicator: 'green'
                });
            });
        }
    }
});

function show_doluluk_indicator(frm) {
    let doluluk = flt(frm.doc.doluluk_yuzdesi);
    let color = 'green';
    let message = 'Normal';
    
    if (doluluk > 90) {
        color = 'red';
        message = 'Kritik Seviye!';
    } else if (doluluk > 70) {
        color = 'orange';
        message = 'Yüksek Doluluk';
    }
    
    frm.dashboard.add_indicator(__('Doluluk: {0}% - {1}', [doluluk.toFixed(1), message]), color);
}
