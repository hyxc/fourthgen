from django.shortcuts import render
from .models import Assetmanage
# Create your views here.
def asset_html(request):
    a=[]
    post_list = Assetmanage.objects.all()
    for post in post_list:
        dict = {'asset_num': '%s' % (post.asset_num),'device_type': '%s' % (post.device_type),'local_ip': '%s' % (post.local_ip),'remote_ip': '%s' % (post.remote_ip),'system_type': '%s' % (post.system_type)}
        a.append(dict)
    return render(request, 'assetmanage/asset_table1.html', {'a' : a})

def asset_add(request):
    asset_num = request.GET['asset_num']
    device_type = request.GET['device_type']
    local_ip = request.GET['local_ip']
    remote_ip = request.GET['remote_ip']
    system_type = request.GET['system_type']
    Assetmanage.objects.create(asset_num="%s" % (asset_num),device_type="%s" % (device_type),local_ip="%s" % (local_ip),remote_ip="%s" % (remote_ip),system_type="%s" % (system_type))
    a=[]
    post_list = Assetmanage.objects.all()
    for post in post_list:
        dict = {'asset_num': '%s' % (post.asset_num),'device_type': '%s' % (post.device_type),'local_ip': '%s' % (post.local_ip),'remote_ip': '%s' % (post.remote_ip),'system_type': '%s' % (post.system_type)}
        a.append(dict)
    return render(request, 'assetmanage/asset_table1.html', {'a' : a})

def asset_del(request):
    asset_num = request.GET['asset_num']
    Assetmanage.objects.get(asset_num="%s" % (asset_num)).delete()
    a=[]
    post_list = Assetmanage.objects.all()
    for post in post_list:
        dict = {'asset_num': '%s' % (post.asset_num),'device_type': '%s' % (post.device_type),'local_ip': '%s' % (post.local_ip),'remote_ip': '%s' % (post.remote_ip),'system_type': '%s' % (post.system_type)}
        a.append(dict)
    return render(request, 'assetmanage/asset_table1.html', {'a' : a})

def asset_update(request):
    asset_num = request.GET['asset_num']
    device_type = request.GET['device_type']
    local_ip = request.GET['local_ip']
    remote_ip = request.GET['remote_ip']
    system_type = request.GET['system_type']
    update = Assetmanage.objects.get(asset_num="%s" % (asset_num))
    if device_type != '':
        update.device_type = "%s" % (device_type)
        update.save()
    if local_ip != '':
        update.local_ip = "%s" % (local_ip)
        update.save()
    if remote_ip != '':
        update.remote_ip = "%s" % (remote_ip)
        update.save()
    if system_type != '':
        update.system_type = "%s" % (system_type)
        update.save()
    a=[]
    post_list = Assetmanage.objects.all()
    for post in post_list:
        dict = {'asset_num': '%s' % (post.asset_num),'device_type': '%s' % (post.device_type),'local_ip': '%s' % (post.local_ip),'remote_ip': '%s' % (post.remote_ip),'system_type': '%s' % (post.system_type)}
        a.append(dict)
    return render(request, 'assetmanage/asset_table1.html', {'a' : a})