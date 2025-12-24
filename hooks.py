# -*- coding: utf-8 -*-
# LOJİNET V2.0 - HOOKS.PY - TÜM 15 MADDE UYGULANMIŞ
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "lojinet"
app_title = "Lojinet"
app_publisher = "İXİR Bilişim"
app_description = "Profesyonel Lojistik Yönetim Sistemi v2.0 - 15 Madde Tam Entegrasyon"
app_icon = "octicon octicon-package"
app_color = "#3498db"
app_email = "info@ixirbilisim.com"
app_license = "MIT"
app_version = "2.0.0"

# Modules
app_include_css = "/assets/lojinet/css/lojinet.css"
app_include_js = [
    "/assets/lojinet/js/lojinet.js",
    "/assets/lojinet/js/bulk_invoice.js"
]

# DocType JS
doctype_js = {
    "Lojinet Yuk": "public/js/lojinet_yuk.js",
    "Lojinet Sefer": "public/js/lojinet_sefer.js",
    "Lojinet Cek": "public/js/lojinet_cek.js",
    "Lojinet Cari": "public/js/lojinet_cari.js",
    "Lojinet Mal Kabul": "public/js/lojinet_mal_kabul.js",
    "Lojinet Odeme Tahsilat": "public/js/lojinet_odeme_tahsilat.js"
}

# DocType List JS
doctype_list_js = {
    "Lojinet Yuk": "public/js/lojinet_yuk_list.js",
    "Lojinet Evrak": "public/js/lojinet_evrak_list.js"
}

# Scheduled Tasks
scheduler_events = {
    "daily": [
        "lojinet.tasks.check_vade_tarihleri",
        "lojinet.tasks.send_daily_reports"
    ],
    "weekly": [
        "lojinet.tasks.send_weekly_reports"
    ],
    "monthly": [
        "lojinet.tasks.create_monthly_mutabakat"
    ]
}

# Doc Events - MADDE 2, 3: Otomatik durum güncellemeleri
doc_events = {
    "Lojinet Mal Kabul": {
        "on_submit": "lojinet.lojinet.doctype.lojinet_yuk.lojinet_yuk.update_yuk_from_mal_kabul"
    },
    "Lojinet Sefer": {
        "on_submit": "lojinet.lojinet.doctype.lojinet_sefer.lojinet_sefer.update_yukler_status",
        "on_update": "lojinet.lojinet.doctype.lojinet_sefer.lojinet_sefer.calculate_kar_zarar"
    },
    "Lojinet Cek": {
        "on_submit": "lojinet.lojinet.doctype.lojinet_cek.lojinet_cek.update_cari_bakiye",
        "on_cancel": "lojinet.lojinet.doctype.lojinet_cek.lojinet_cek.reverse_cari_bakiye"
    },
    "Lojinet Yuk": {
        "on_update": "lojinet.lojinet.doctype.lojinet_yuk.lojinet_yuk.check_price_agreement"
    }
}

# Permissions
permission_query_conditions = {
    "Lojinet Yuk": "lojinet.permissions.yuk_query",
    "Lojinet Cari": "lojinet.permissions.cari_query"
}

has_permission = {
    "Lojinet Yuk": "lojinet.permissions.yuk_permission",
    "Lojinet Cari": "lojinet.permissions.cari_permission"
}

# Jinja
jinja = {
    "methods": [
        "lojinet.utils.get_cari_bakiye",
        "lojinet.utils.get_yuk_durum_badge"
    ]
}

# Boot Session - MADDE 15: B2B kullanıcı bilgisi
boot_session = "lojinet.api.boot_session"

# Website
website_route_rules = [
    {"from_route": "/b2b/<path:app_path>", "to_route": "b2b"},
    {"from_route": "/b2b", "to_route": "b2b/index"}
]

# Fixtures
fixtures = [
    {
        "doctype": "Custom Field",
        "filters": [["dt", "in", ["User", "Customer", "Supplier", "Lojinet Cari", "Lojinet Yuk"]]]
    },
    {
        "doctype": "Property Setter",
        "filters": [["doc_type", "in", ["Lojinet Yuk", "Lojinet Sefer", "Lojinet Cek"]]]
    }
]

# Override whitelisted methods
override_whitelisted_methods = {
    "frappe.desk.search.search_link": "lojinet.overrides.search_link"
}

# On install
after_install = "lojinet.setup.install.after_install"

# On migrate
after_migrate = "lojinet.setup.install.after_migrate"

