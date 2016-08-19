# -*- coding: utf-8 -*-
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView

from subscription.models import Subscription
from subscription.forms import SubscriptionForm


class Home(SuccessMessageMixin, CreateView):
	template_name = 'homesite/home.html'
	model = Subscription
	form_class = SubscriptionForm
	success_url = '/'
	success_message = 'Sucesso!'
