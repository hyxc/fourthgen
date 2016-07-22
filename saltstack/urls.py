from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^key_list/$', views.key_list, name='key_list'),
    url(r'^key_accept/$', views.key_accept, name='key_accept'),
    url(r'^$', views.index, name='ba'),
]
