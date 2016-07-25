from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^key_list/$', views.key_list, name='key_list'),
    url(r'^key_accept/$', views.key_accept, name='key_accept'),
    url(r'^key_delete/$', views.key_delete, name='key_delete'),
    url(r'^key_reject/$', views.key_reject, name='key_reject'),
    url(r'^connect_test/$', views.connect_test, name='connect_test'),
    url(r'^connect_test_exec/$', views.connect_test_exec, name='connect_test_exec'),
    url(r'^ip_list/$', views.ip_list, name='ip_list'),
    url(r'^cmd_exec_html/$', views.cmd_exec_html, name='cmd_exec_html'),
    url(r'^cmd_exec/$', views.cmd_exec, name='cmd_exec'),
    url(r'^$', views.index, name='ba'),
]
