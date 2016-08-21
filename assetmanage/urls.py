from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^asset_table/$', views.asset_table, name='asset_table'),
    url(r'^asset_table_detail/$', views.asset_table_detail, name='asset_table_detail'),
    url(r'^asset_add_html/$', views.asset_add_html, name='asset_add_html'),
    url(r'^asset_add/$', views.asset_add, name='asset_add'),
    url(r'^asset_del_html/$', views.asset_del_html, name='asset_del_html'),
    url(r'^asset_del/$', views.asset_del, name='asset_del'),
    url(r'^asset_update_html/$', views.asset_update_html, name='asset_update_html'),
    url(r'^asset_update/$', views.asset_update, name='asset_update'),
    url(r'^host_table/$', views.host_table, name='host_table'),
]