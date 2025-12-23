# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "lojinet"
app_title = "Lojinet"
app_publisher = "İXİR Bilişim"
app_description = "Profesyonel Lojistik Yönetim Sistemi v2.0"
app_icon = "octicon octicon-package"
app_color = "#3498db"
app_email = "info@ixirbilisim.com"
app_license = "MIT"
app_version = "2.0.0"

# Dokümantasyon
docs_app = "lojinet"

# CSS/JS
app_include_css = "/assets/lojinet/css/lojinet.css"
app_include_js = [
    "/assets/lojinet/js/lojinet.js",
    "/assets/lojinet/js/bulk_invoice.js"
]

# DocType JS
doctype_js = {
    "Lojinet Yuk": "lojinet/doctype/lojinet_yuk/lojinet_yuk.js",
    "Lojinet Sefer": "lojinet/doctype/lojinet_sefer/lojinet_sefer.js",
    "Lojinet Cek": "lojinet/doctype/lojinet_cek/lojinet_cek.js",
    "Lojinet Cari": "lojinet/doctype/lojinet_cari/lojinet_cari.js"
}

# Scheduler Events
scheduler_events = {
    "daily": [
        "lojinet.tasks.check_vade_tarihleri"
    ],
    "weekly": [
        "lojinet.tasks.send_weekly_reports"
    ]
}

# Fixtures
fixtures = [
    {
        "doctype": "Custom Field",
        "filters": [["dt", "in", ["User", "Customer", "Supplier"]]]
    }
]

# Permissions
permission_query_conditions = {
    "Lojinet Yuk": "lojinet.permissions.yuk_query",
    "Lojinet Cari": "lojinet.permissions.cari_query"
}

# Whitelisted methods
override_whitelisted_methods = {
    "frappe.desk.search.search_link": "lojinet.overrides.search_link"
}

# Web routes
website_route_rules = [
    {"from_route": "/b2b/<path:app_path>", "to_route": "b2b"},
]

# Boot session
boot_session = "lojinet.api.boot_session"

