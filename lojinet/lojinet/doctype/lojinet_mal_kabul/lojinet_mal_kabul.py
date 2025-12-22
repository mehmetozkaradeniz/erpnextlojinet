# -*- coding: utf-8 -*-
# Copyright (c) 2025, Lojinet Team
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import flt

class LojinetMalKabul(Document):
    def validate(self):
        self.calculate_totals()
    
    def calculate_totals(self):
        self.toplam_miktar = sum([flt(item.miktar) for item in self.mal_kabul_kalemleri])
    
    def on_submit(self):
        """Onaylandığında mail gönder"""
        self.send_mail()
    
    def send_mail(self):
        """PDF ile mail gönder"""
        cari_doc = frappe.get_doc("Lojinet Cari", self.cari)
        recipients = [cari_doc.email] if cari_doc.email else []
        
        if cari_doc.ek_mail_adresleri:
            for email in cari_doc.ek_mail_adresleri.split("\n"):
                if email.strip():
                    recipients.append(email.strip())
        
        if recipients:
            frappe.sendmail(
                recipients=recipients,
                subject=f"Mal Kabul - {self.name}",
                message=f"<p>Mal kabul işleminiz tamamlanmıştır. Toplam: {self.toplam_miktar}</p>"
            )
