frappe.query_reports["Yuk Raporu"] = {
    "filters": [
        {
            "fieldname": "from_date",
            "label": __("Başlangıç Tarihi"),
            "fieldtype": "Date",
            "default": frappe.datetime.month_start()
        },
        {
            "fieldname": "to_date",
            "label": __("Bitiş Tarihi"),
            "fieldtype": "Date",
            "default": frappe.datetime.month_end()
        },
        {
            "fieldname": "musteri",
            "label": __("Müşteri"),
            "fieldtype": "Link",
            "options": "Lojinet Cari"
        },
        {
            "fieldname": "yuk_statusu",
            "label": __("Durum"),
            "fieldtype": "Select",
            "options": "\nBeklemede\nHazırlanıyor\nYolda\nTeslim Edildi"
        }
    ]
};
