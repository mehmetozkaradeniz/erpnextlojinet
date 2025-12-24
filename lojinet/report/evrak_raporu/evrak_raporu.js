frappe.query_reports["Evrak Raporu"] = {
    "filters": [
        {
            "fieldname": "from_date",
            "label": __("Başlangıç"),
            "fieldtype": "Date"
        },
        {
            "fieldname": "to_date",
            "label": __("Bitiş"),
            "fieldtype": "Date"
        },
        {
            "fieldname": "musteri",
            "label": __("Müşteri"),
            "fieldtype": "Link",
            "options": "Lojinet Cari"
        }
    ]
};
