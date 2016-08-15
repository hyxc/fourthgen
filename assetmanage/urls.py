from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^asset_html/$', views.asset_html, name='asset_html'),
    url(r'^asset_add/$', views.asset_add, name='asset_add'),
    url(r'^asset_del/$', views.asset_del, name='asset_del'),
    url(r'^asset_update/$', views.asset_update, name='asset_update'),
]