frappe.query_reports["Sefer Kar Zarar Raporu"] = {
    "filters": [
        {
            "fieldname": "from_date",
            "label": __("Başlangıç"),
            "fieldtype": "Date",
            "default": frappe.datetime.month_start()
        },
        {
            "fieldname": "to_date",
            "label": __("Bitiş"),
            "fieldtype": "Date",
            "default": frappe.datetime.month_end()
        }
    ]
};
