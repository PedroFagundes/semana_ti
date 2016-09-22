# -*- coding: utf-8 -*-
from django.contrib import admin

from import_export import resources
from import_export.admin import ExportMixin

from .models import Lecture, Subscription

class LectureAdmin(admin.ModelAdmin):
	list_display = ('title', 'get_subscriptions_total')

admin.site.register(Lecture, LectureAdmin)

class SubscriptionResource(resources.ModelResource):
	class Meta:
		model = Subscription
		# list_display = ('name', 'email', 'phone')
		# list_filter = ('person_type',)

class SubscriptionAdmin(ExportMixin, admin.ModelAdmin):
	list_display = ('name', 'email', 'phone', 'paid')
	list_filter = ('person_type', 'event', 'lecture', 'paid')
	search_fields = ('name',)

admin.site.register(Subscription, SubscriptionAdmin)
