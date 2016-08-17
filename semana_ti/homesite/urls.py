from django.conf.urls import url

from homesite import views

urlpatterns = [
    url(r'^$', views.Home.as_view(), name='home'),
]