from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^eventos/$', views.index, name='index'),
]