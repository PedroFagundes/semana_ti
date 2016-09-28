# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages

from subscription.models import Subscription


def entry(request):
	if request.method == 'GET':
		return HttpResponse(render(request, 'entry.html'))

	if request.method == 'POST':
		wrong_cpf = request.POST['cpf']
		cpf = wrong_cpf[0:2] + wrong_cpf[3:4] + '.' + wrong_cpf[4:6] + wrong_cpf[7:8] + '.' + wrong_cpf[8:10] + wrong_cpf[11:12] + '-' + wrong_cpf[12:14]
		try:
			subscription = Subscription.objects.get(cpf=cpf)
			if subscription.paid == True:
				messages.add_message(request, messages.SUCCESS, subscription.name + '!')
			else:
				messages.add_message(request, messages.WARNING, 'Inscrição com problema (NP). Verifique sua inscrição com um organizador.')
			return HttpResponse(render(request, 'entry.html'))
		except:
			messages.add_message(request, messages.ERROR, u'Não encontramos uma inscrição com este CPF (' + cpf + ')')
			return HttpResponse(render(request, 'entry.html'))
