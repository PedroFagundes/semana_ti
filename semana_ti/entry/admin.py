# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Entry


class EntryAdmin(admin.ModelAdmin):
	list_display = ('get_subscribed_name', 'in_out', 'when')

admin.site.register(Entry, EntryAdmin)
