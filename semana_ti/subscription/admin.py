# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Subscription

class SubscriptionAdmin(admin.ModelAdmin):
	model = Subscription
	list_display = ('name', 'email', 'phone')
	list_filter = ('person_type',)

admin.site.register(Subscription, SubscriptionAdmin)
