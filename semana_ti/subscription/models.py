# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Subscription(models.Model):
	PERSON_TYPE_CHOICES = {
		('Academico FASA', 'Academico FASA'),
		('Egresso', 'Egresso'),
		('Professor', 'Professor'),
		('Outro', 'Outro'),
	}

	name = models.CharField('Nome', max_length=80, blank=False, null=False)
	cpf = models.CharField('CPF', max_length=14, blank=False, null=False)
	email = models.EmailField('E-mail', unique=True, blank=False, null=False)
	phone = models.CharField('Telefone', max_length=14, blank=False, null=False)
	person_type = models.CharField('Tipo inscrito', max_length=15, choices=PERSON_TYPE_CHOICES, default='A', blank=False, null=False)
	registration = models.CharField('Matrícula', max_length=6, blank=True, null=True)

	event = models.BooleanField('Partcipar do evento', default=False)
	# day_1 = models.CharField()
	# day_2 = models.CharField()
	# day_3 = models.CharField()
	# day_4 = models.CharField()
	# day_5 = models.CharField()

	checked = models.BooleanField('E-mail válido', default=False)

	class Meta:
		verbose_name = 'Inscrição'
		verbose_name_plural = 'Inscrições'

	def __str__(self):
		return self.name
