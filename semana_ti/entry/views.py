# -*- coding: utf-8 -*-
from django.utils.timezone import now
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages

from subscription.models import Subscription

from .models import Entry


def entry(request):
	if request.method == 'GET':
		return HttpResponse(render(request, 'entry.html'))

	if request.method == 'POST':
		wrong_cpf = request.POST['cpf']
		cpf = wrong_cpf[0:2] + wrong_cpf[3:4] + '.' + wrong_cpf[4:6] + wrong_cpf[7:8] + '.' + wrong_cpf[8:10] + wrong_cpf[11:12] + '-' + wrong_cpf[12:14]
		try:
			subscription = Subscription.objects.get(Q(cpf=cpf) | Q(cpf=wrong_cpf))
			if subscription.paid == True and Entry.objects.filter(subscription=subscription).exists():
				if Entry.objects.filter(subscription=subscription).order_by('-when').first().in_out == 1:
					Entry(subscription=subscription, when=now(), in_out=2).save()
					messages.add_message(request, messages.SUCCESS, u'Até mais, ' + subscription.name + '!')
				else:
					Entry(subscription=subscription, when=now(), in_out=1).save()
					messages.add_message(request, messages.SUCCESS, 'Bem-vindo, ' + subscription.name + '!')
			elif subscription.paid == True and not Entry.objects.filter(subscription=subscription).exists():
				Entry(subscription=subscription, when=now(), in_out=1).save()
				messages.add_message(request, messages.SUCCESS, 'Bem-vindo, ' + subscription.name + '!')				
			else:
				messages.add_message(request, messages.WARNING, 'Inscrição com problema (NP). Verifique sua inscrição com um organizador.')
			return HttpResponse(render(request, 'entry.html'))
		except:
			messages.add_message(request, messages.ERROR, u'Não encontramos uma inscrição com este CPF (' + cpf + ')')
			return HttpResponse(render(request, 'entry.html'))
