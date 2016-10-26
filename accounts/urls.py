from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.login, name='init_login'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
]