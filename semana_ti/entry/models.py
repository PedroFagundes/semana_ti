# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from subscription.models import Subscription


class Entry(models.Model):
	subscription = models.ForeignKey(Subscription, verbose_name='Nome')
	when = models.DateTimeField('Quando', auto_now_add=True)
	in_out = models.PositiveSmallIntegerField('Saiu/Entrou', choices=[(1, 'Entrou'), (2, 'Saiu')])

	class Meta:
		verbose_name = 'Registro da portaria'
		verbose_name_plural = 'Registros da portaria'

	def __unicode__(self):
		return "%s %s às %s" % (self.subscription.name, self.in_out, self.when)

	def get_subscribed_name(self):
		return self.subscription.name
	get_subscribed_name.short_description = 'Nome'
