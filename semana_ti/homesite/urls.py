from django.conf.urls import url

from homesite import views
from entry.views import entry

urlpatterns = [
    url(r'^$', views.Home.as_view(), name='home'),
    url(r'^entry$', entry, name='entry'),
    url(r'^send-mails$', views.send_confirmation_mail_to_all, name='send_mails'),
]