# -*- coding: utf-8 -*-
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string
from django.views.generic import CreateView

from subscription.models import Subscription
from subscription.forms import SubscriptionForm
from subscription.utils import send_html_mail


class Home(SuccessMessageMixin, CreateView):
	template_name = 'homesite/home.html'
	model = Subscription
	form_class = SubscriptionForm
	success_url = '/'
	success_message = 'Sucesso!'


def send_confirmation_mail_to_all(request):
	subscriptions = Subscription.objects.all()[:5]
	import pdb; pdb.set_trace()
	for subscription in subscriptions:
		html_message = render_to_string('mail/e-mail.html', {'subscription': subscription})
		send_html_mail('Confirmacao de inscricao', html_message, ['pedrofagundesb@gmail.com'])
	return HttpResponseRedirect(reverse_lazy('home'))

