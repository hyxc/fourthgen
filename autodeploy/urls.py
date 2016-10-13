from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^app_deploy_html/$', views.app_deploy_html, name='app_deploy_html'),
    url(r'^app_deploy/$', views.app_deploy, name='app_deploy'),
]
