# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from app.models import SystemIP

class SystemAdmin(admin.ModelAdmin):
    list_display = ["__unicode__","nombre","nombrecell","ipv4"]
    search_fields = ["nombre", "ipv4"]
    list_editable = ["ipv4"]
    class Meta:
        model = SystemIP

admin.site.register(SystemIP, SystemAdmin)