from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.booking_shell, name='index'),
]
