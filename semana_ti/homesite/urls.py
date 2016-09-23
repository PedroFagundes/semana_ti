from django.conf.urls import url

from homesite import views

urlpatterns = [
    url(r'^$', views.Home.as_view(), name='home'),
    url(r'^send-mails$', views.send_confirmation_mail_to_all, name='send_mails'),
]