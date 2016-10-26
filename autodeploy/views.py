from django.shortcuts import render
from accounts.decorators import login_required

# Create your views here.
from saltstack.saltapi import *

@login_required
def app_deploy_html(request):
    return render(request, 'autodeploy/app_deploy.html')

@login_required
def app_deploy(request):
    ip_list = request.GET['ip_list']
    exec_module = "state.sls"
    state_args = request.GET['app']
    app_deploy_result = api_exec('%s' %(ip_list), '%s' %(exec_module) , arg='%s' %(state_args), arg_num=1)['return'][0]
    return render(request, 'autodeploy/app_deploy.html', {'app_deploy_result': app_deploy_result})
