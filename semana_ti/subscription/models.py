# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.validators import MinValueValidator
from django.db import models


class Lecture(models.Model):
	title = models.CharField('Título do curso', max_length=50)
	date = models.DateField('Data')
	hour = models.TimeField('Horário')
	value = models.DecimalField('Valor', max_digits=9, decimal_places=2, validators=[MinValueValidator(0.00)])

	class Meta:
		verbose_name = 'Mini-curso'
		verbose_name_plural = 'Mini-cursos'

	def __unicode__(self):
		return '[%s] %s - R$%.2f' % (self.date.strftime('%d/%m/%Y'), self.title, self.value)


class Subscription(models.Model):
	PERSON_TYPE_CHOICES = {
		('Academico FASA', 'Academico FASA'),
		('Egresso', 'Egresso'),
		('Professor', 'Professor'),
		('Outro', 'Outro'),
	}

	LECTURE_CHOICES = {
		(''),
	}

	name = models.CharField('Nome', max_length=80, blank=False, null=False)
	cpf = models.CharField('CPF', max_length=14, blank=False, null=False)
	email = models.EmailField('E-mail', unique=True, blank=False, null=False)
	phone = models.CharField('Telefone', max_length=15, blank=False, null=False)
	person_type = models.CharField('Tipo inscrito', max_length=15, choices=PERSON_TYPE_CHOICES, default='A', blank=False, null=False)
	registration = models.CharField('Matrícula', max_length=6, blank=True, null=True)

	event = models.BooleanField('Partcipar do evento', default=False)

	lecture = models.ManyToManyField(Lecture, verbose_name='Mini-cursos',blank=True, null=True)

	# day_1 = models.CharField()
	# day_2 = models.CharField()
	# day_3 = models.CharField()
	# day_4 = models.CharField()
	# day_5 = models.CharField()

	paid = models.BooleanField('Pago', default=False)

	class Meta:
		verbose_name = 'Inscrição'
		verbose_name_plural = 'Inscrições'

	def __unicode__(self):
		return self.name