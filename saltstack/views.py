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

def match_arg(request):
    return render(request, 'saltstack/match_arg.html')

def connect_test_exec(request):
    err_ip = {}
    minions = api_key()['return'][0]['data']['return']
    connect_test_ip = request.GET['connect_test_ip']
    ip_list_real = connect_test_ip.split(',')
    connect_test_result = api_exec('%s' %(connect_test_ip), 'test.ping')['return'][0]
    for i in ip_list_real:
        if connect_test_result.has_key('%s' %(i)):
            pass
        elif str(i) == "":
            pass
        elif str(i) == "*":
            pass
        else:
            err_ip[i] = False
    return render(request, 'saltstack/key_list.html', {'connect_test_result': connect_test_result,'err_ip': err_ip,'minions': minions})

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
    return render(request, 'saltstack/match_arg.html', {'ip_list_text': ip_list_text})

def cmd_exec_html(request):
    return render(request, 'saltstack/cmd_exec.html')

def cmd_exec(request):
    ip_list = request.GET['ip_list']
    exec_module = "cmd.run"
    cmd_args = request.GET['cmd_args']
    cmd_exec_result = api_exec('%s' %(ip_list), '%s' %(exec_module) , arg='%s' %(cmd_args), arg_num=1)['return'][0]
    return render(request, 'saltstack/cmd_exec.html', {'cmd_exec_result': cmd_exec_result})

def state_exec_html(request):
    return render(request, 'saltstack/state_exec.html')

def state_exec(request):
    ip_list = request.GET['ip_list']
    exec_module = "state.sls"
    state_args = request.GET['state_args']
    state_exec_result = api_exec('%s' %(ip_list), '%s' %(exec_module) , arg='%s' %(state_args), arg_num=1)['return'][0]
    return render(request, 'saltstack/state_exec.html', {'state_exec_result': state_exec_result})

def minion_service_start_html(request):
    return render(request, 'saltstack/minion_service_start.html')

def minion_service_start(request):
    master_ip = "10.211.55.100"
    exec_module = "cmd.run"
    cmd_args_null = ">/salt-ssh/gg"
    api_exec('%s' %(master_ip), '%s' %(exec_module) , arg='%s' %(cmd_args_null), arg_num=1)
    ip_list = request.GET['ip_list']
    ip_list_real = ip_list.split(',')
    for i in ip_list_real:
        cmd_args = "echo '%s' >> /salt-ssh/gg" %(i)
        api_exec('%s' %(master_ip), '%s' %(exec_module) , arg='%s' %(cmd_args), arg_num=1)
    cmd_args = "sh /salt-ssh/ip.sh"
    api_exec('%s' %(master_ip), '%s' %(exec_module) , arg='%s' %(cmd_args), arg_num=1)
    cmd_kill_args = "salt-ssh -ir '*' 'sudo killall salt-minion'"
    api_exec('%s' %(master_ip), '%s' %(exec_module) , arg='%s' %(cmd_kill_args), arg_num=1)
    cmd_start_args = "salt-ssh -ir '*' 'sudo salt-minion -d'"
    api_exec('%s' %(master_ip), '%s' %(exec_module) , arg='%s' %(cmd_start_args), arg_num=1)
    return render(request, 'saltstack/minion_service_start_ok.html')

def minion_install_html(request):
    return render(request, 'saltstack/minion_install.html')

def minion_install(request):
    master_ip = "10.211.55.100"
    exec_module = "cmd.run"
    cmd_args_null = ">/salt-ssh/gg"
    api_exec('%s' %(master_ip), '%s' %(exec_module) , arg='%s' %(cmd_args_null), arg_num=1)
    ip_list = request.GET['ip_list']
    ip_list_real = ip_list.split(',')
    for i in ip_list_real:
        cmd_args = "echo '%s' >> /salt-ssh/gg" %(i)
        api_exec('%s' %(master_ip), '%s' %(exec_module) , arg='%s' %(cmd_args), arg_num=1)
    cmd_args = "sh /salt-ssh/ip.sh"
    api_exec('%s' %(master_ip), '%s' %(exec_module) , arg='%s' %(cmd_args), arg_num=1)
    cmd_install_args = "salt-ssh -i '*' state.sls minions.install"
    minion_install_result = api_exec('%s' %(master_ip), '%s' %(exec_module) , arg='%s' %(cmd_install_args), arg_num=1)['return'][0]['10.211.55.100']
    return render(request, 'saltstack/minion_install.html', {'minion_install_result': minion_install_result})

def index(request):
    return render(request, 'base.html')