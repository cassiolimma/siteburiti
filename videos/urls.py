from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^videos/$', views.index, name='index'),
]