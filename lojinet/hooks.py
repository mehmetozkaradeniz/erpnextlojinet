# -*- coding: utf-8 -*-
from . import __version__ as app_version

app_name = "lojinet"
app_title = "Lojinet"
app_publisher = "Lojinet Team"
app_description = "Comprehensive Logistics, Warehouse Management and SaaS System"
app_email = "info@lojinet.com"
app_license = "MIT"

# CSS/JS includes
app_include_css = "/assets/lojinet/css/lojinet.css"
app_include_js = [
    "/assets/lojinet/js/lojinet.js",
    "/assets/lojinet/js/bulk_invoice.js"
]

# DocType JS
doctype_js = {
    "Customer": "public/js/customer.js",
    "Lojinet Yuk": "lojinet/doctype/lojinet_yuk/lojinet_yuk.js",
    "Lojinet Fiyat Anlasmasi": "lojinet/doctype/lojinet_fiyat_anlasmasi/lojinet_fiyat_anlasmasi.js",
}

# Document Events
doc_events = {
    "Customer": {
        "validate": "lojinet.api.validate_customer"
    }
}

# Scheduled Tasks
scheduler_events = {
    "daily": [
        "lojinet.api.auto_close_tickets",
        "lojinet.api.check_insurance_expiry",
    ],
    "weekly": [
        "lojinet.api.send_weekly_reports",
    ]
}

# Portal Settings
has_website_permission = {
    "Lojinet Yuk": "lojinet.api.has_yuk_permission",
    "Lojinet Destek Bileti": "lojinet.api.has_ticket_permission",
}

# Boot session
boot_session = "lojinet.api.boot_session"

# Fixtures
fixtures = [
    {"doctype": "Role", "filters": [["name", "in", ["Lojinet User", "Lojinet Manager", "Lojinet B2B User"]]]},
]
