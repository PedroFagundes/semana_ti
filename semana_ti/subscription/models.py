# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.validators import MinValueValidator
from django.db import models


class Lecture(models.Model):
	title = models.CharField('Título do curso', max_length=150)
	date = models.DateField('Data')
	hour = models.TimeField('Horário')
	value = models.DecimalField('Valor', max_digits=9, decimal_places=2, validators=[MinValueValidator(0.00)])
	vacancies = models.PositiveSmallIntegerField('Número de vagas')

	class Meta:
		verbose_name = 'Mini-curso'
		verbose_name_plural = 'Mini-cursos'

	def __unicode__(self):
		return '[%s] %s' % (self.date.strftime('%d/%m/%Y'), self.title)

	def reached_max_subscriptions(self):
		if len(Subscription.objects.filter(lecture=self)) >= self.vacancies:
			return True
		else:
			return False


class Subscription(models.Model):
	PERSON_TYPE_CHOICES = {
		('1', 'Acadêmico FASA'),
		('2', 'Acadêmico outra instituição'),
		('3', 'Profissional'),
	}

	name = models.CharField('Nome', max_length=80, blank=False, null=False)
	cpf = models.CharField('CPF', max_length=14, blank=False, null=False)
	email = models.EmailField('E-mail', unique=True, blank=False, null=False)
	phone = models.CharField('Telefone', max_length=15, blank=False, null=False)
	person_type = models.CharField('Tipo inscrito', max_length=15, choices=PERSON_TYPE_CHOICES, default='1', blank=False, null=False)
	registration = models.CharField('Matrícula', max_length=6, blank=True, null=True)

	event = models.BooleanField('Partcipar do evento', default=False)

	lecture = models.ManyToManyField(Lecture, verbose_name='Mini-cursos')

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
