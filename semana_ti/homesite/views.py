from django.views.generic import CreateView

from subscription.models import Subscription
from subscription.forms import SubscriptionForm


class Home(CreateView):
	template_name = 'homesite/home.html'
	model = Subscription
	form_class = SubscriptionForm
	success_url = '/'
