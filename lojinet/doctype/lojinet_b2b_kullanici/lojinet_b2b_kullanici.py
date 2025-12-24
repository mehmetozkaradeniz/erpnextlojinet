# -*- coding: utf-8 -*-
import frappe
from frappe.model.document import Document
import hashlib
from frappe.utils import now

class LojinetB2BKullanici(Document):
    def autoname(self):
        self.name = self.email
    
    def validate(self):
        # Şifreyi hashle (basit örnek, production'da daha güvenli olmalı)
        if self.is_new() or self.has_value_changed('sifre'):
            self.sifre = hashlib.sha256(self.sifre.encode()).hexdigest()
    
    def verify_password(self, password):
        """Şifre doğrulama"""
        hashed = hashlib.sha256(password.encode()).hexdigest()
        return self.sifre == hashed
    
    def generate_api_key(self):
        """Yeni API key oluştur"""
        self.api_key = hashlib.md5(f"{self.email}{now()}".encode()).hexdigest()
        self.son_giris = now()
        self.giris_sayisi = (self.giris_sayisi or 0) + 1
        self.save(ignore_permissions=True)
        return self.api_key
