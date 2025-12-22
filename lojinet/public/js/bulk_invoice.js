// Toplu Faturalama Dialog
frappe.ui.form.on('Lojinet Cari', {
    refresh: function(frm) {
        if (!frm.is_new() && frm.doc.cari_tipi && frm.doc.cari_tipi.includes("Müşteri")) {
            frm.add_custom_button(__('Toplu Fatura Oluştur'), function() {
                show_bulk_invoice_dialog(frm);
            }, __('Lojinet'));
        }
    }
});

function show_bulk_invoice_dialog(frm) {
    let d = new frappe.ui.Dialog({
        title: __('Toplu Fatura Oluştur'),
        fields: [
            {
                label: __('Başlangıç Tarihi'),
                fieldname: 'from_date',
                fieldtype: 'Date',
                default: frappe.datetime.add_days(frappe.datetime.get_today(), -30),
                reqd: 1
            },
            {
                label: __('Bitiş Tarihi'),
                fieldname: 'to_date',
                fieldtype: 'Date',
                default: frappe.datetime.get_today(),
                reqd: 1
            },
            {
                fieldtype: 'HTML',
                options: '<div id="yuk_preview"></div>'
            }
        ],
        primary_action_label: __('Fatura Oluştur'),
        primary_action(values) {
            frappe.call({
                method: 'lojinet.api.create_bulk_invoice',
                args: {
                    customer: frm.doc.name,
                    from_date: values.from_date,
                    to_date: values.to_date
                },
                freeze: true,
                freeze_message: __('Fatura oluşturuluyor...'),
                callback: function(r) {
                    if (r.message) {
                        d.hide();
                        frappe.msgprint({
                            title: __('Başarılı'),
                            message: __('Fatura oluşturuldu: {0}<br>Yük Sayısı: {1}<br>Toplam: {2} TL', 
                                [r.message.fatura_no, r.message.yuk_sayisi, r.message.toplam_tutar]),
                            indicator: 'green'
                        });
                        
                        // Fatura detay raporunu göster
                        show_invoice_detail_dialog(r.message.fatura_no);
                    }
                }
            });
        }
    });
    
    // Tarih değiştiğinde önizleme göster
    d.fields_dict.from_date.$input.on('change', function() {
        load_yuk_preview(frm.doc.name, d.get_value('from_date'), d.get_value('to_date'));
    });
    d.fields_dict.to_date.$input.on('change', function() {
        load_yuk_preview(frm.doc.name, d.get_value('from_date'), d.get_value('to_date'));
    });
    
    d.show();
    
    // İlk önizleme
    load_yuk_preview(frm.doc.name, d.get_value('from_date'), d.get_value('to_date'));
}

function load_yuk_preview(customer, from_date, to_date) {
    frappe.call({
        method: 'frappe.client.get_list',
        args: {
            doctype: 'Lojinet Yuk',
            filters: [
                ['musteri', '=', customer],
                ['islem_tarihi', 'between', [from_date, to_date]],
                ['docstatus', '=', 1]
            ],
            fields: ['name', 'musteri_irsaliye_no', 'islem_tarihi', 'toplam_fiyat']
        },
        callback: function(r) {
            if (r.message) {
                let html = '<h4>Faturasız Yükler:</h4>';
                let total = 0;
                
                r.message.forEach(function(yuk) {
                    html += `<div>${yuk.musteri_irsaliye_no} - ${yuk.toplam_fiyat} TL</div>`;
                    total += yuk.toplam_fiyat;
                });
                
                html += `<hr><strong>Toplam: ${total.toFixed(2)} TL</strong>`;
                $('#yuk_preview').html(html);
            }
        }
    });
}

function show_invoice_detail_dialog(invoice_no) {
    let d = new frappe.ui.Dialog({
        title: __('Fatura Detay Raporu'),
        fields: [
            {
                fieldtype: 'HTML',
                options: '<div id="invoice_detail_report" style="max-height: 400px; overflow-y: auto;"></div>'
            }
        ],
        primary_action_label: __('Excel İndir'),
        primary_action() {
            download_invoice_excel(invoice_no);
        },
        secondary_action_label: __('Mail Gönder'),
        secondary_action() {
            send_invoice_email(invoice_no);
        }
    });
    
    d.show();
    
    // Rapor yükle
    frappe.call({
        method: 'lojinet.api.get_invoice_detail_report',
        args: { invoice_no: invoice_no },
        callback: function(r) {
            if (r.message) {
                let html = `
                    <h4>Fatura No: ${r.message.fatura_no}</h4>
                    <p>Tarih: ${r.message.fatura_tarihi}</p>
                    <p>Toplam: ${r.message.toplam_tutar} TL</p>
                    <table class="table table-bordered">
                        <thead>
                            <tr>
                                <th>Yük No</th>
                                <th>İrsaliye No</th>
                                <th>Tarih</th>
                                <th>Tutar</th>
                            </tr>
                        </thead>
                        <tbody>
                `;
                
                r.message.yukler.forEach(function(yuk) {
                    html += `
                        <tr>
                            <td>${yuk.yuk_no}</td>
                            <td>${yuk.musteri_irsaliye_no}</td>
                            <td>${yuk.islem_tarihi}</td>
                            <td>${yuk.tutar} TL</td>
                        </tr>
                    `;
                });
                
                html += '</tbody></table>';
                $('#invoice_detail_report').html(html);
            }
        }
    });
}

function download_invoice_excel(invoice_no) {
    frappe.call({
        method: 'lojinet.api.export_invoice_detail_excel',
        args: { invoice_no: invoice_no },
        callback: function(r) {
            if (r.message) {
                // Base64 veriyi blob'a çevir ve indir
                const linkSource = `data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,${r.message.file_data}`;
                const downloadLink = document.createElement("a");
                downloadLink.href = linkSource;
                downloadLink.download = r.message.filename;
                downloadLink.click();
                
                frappe.show_alert({message: __('Excel indirildi'), indicator: 'green'});
            }
        }
    });
}

function send_invoice_email(invoice_no) {
    frappe.prompt([
        {
            label: __('E-posta Adresleri'),
            fieldname: 'recipients',
            fieldtype: 'Small Text',
            description: __('Virgülle ayırarak birden fazla adres girebilirsiniz')
        }
    ], function(values) {
        let recipients = values.recipients ? values.recipients.split(',').map(e => e.trim()) : null;
        
        frappe.call({
            method: 'lojinet.api.send_invoice_detail_email',
            args: {
                invoice_no: invoice_no,
                recipients: recipients
            },
            freeze: true,
            freeze_message: __('Mail gönderiliyor...'),
            callback: function(r) {
                if (r.message) {
                    frappe.show_alert({message: __('Mail gönderildi'), indicator: 'green'});
                }
            }
        });
    }, __('Mail Gönder'), __('Gönder'));
}
