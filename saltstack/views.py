from django.shortcuts import render

# Create your views here.
from .saltapi import *

def key_list(request):
    minions = api_key()['return'][0]['data']['return']
    return render(request, 'saltstack/key_list.html', {'minions': minions})

def key_accept(request):
    match = request.GET['match']
    api_key(fun='key.accept', match='%s' %(match), arg_num=1)
    minions = api_key()['return'][0]['data']['return']
    return render(request, 'saltstack/key_list.html', {'minions': minions})

def key_delete(request):
    match = request.GET['match']
    api_key(fun='key.delete', match='%s' %(match), arg_num=1)
    minions = api_key()['return'][0]['data']['return']
    return render(request, 'saltstack/key_list.html', {'minions': minions})

def key_reject(request):
    match = request.GET['match']
    api_key(fun='key.reject', match='%s' %(match), arg_num=1)
    minions = api_key()['return'][0]['data']['return']
    return render(request, 'saltstack/key_list.html', {'minions': minions})

def connect_test(request):
    return render(request, 'saltstack/connect_test.html')

def connect_test_exec(request):
    connect_test_ip = request.GET['connect_test_ip']
    connect_test_result = api_exec('%s' %(connect_test_ip), 'test.ping')['return'][0]
    return render(request, 'saltstack/connect_test.html', {'connect_test_result': connect_test_result})

def ip_list(request):
    ip_list_text = []
    ip_list = request.GET['ip_list']
    ip_list_get = ip_list.split('\r\n')
    for i in ip_list_get:
        i = i.strip()
        if i != '':
            ip_list_text.append(i)
        else:
            pass
    return render(request, 'saltstack/connect_test.html', {'ip_list_text': ip_list_text})

def cmd_exec_html(request):
    return render(request, 'saltstack/cmd_exec.html')

def cmd_exec(request):
    ip_list = request.GET['ip_list']
    exec_module = request.GET['exec_module']
    cmd_args = request.GET['cmd_args']
    cmd_exec_result = api_exec('%s' %(ip_list), '%s' %(exec_module) , arg='%s' %(cmd_args), arg_num=1)['return'][0]
    return render(request, 'saltstack/cmd_exec.html', {'cmd_exec_result': cmd_exec_result})

def index(request):
    return render(request, 'base.html')