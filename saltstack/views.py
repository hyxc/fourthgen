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

def index(request):
    return render(request, 'base.html')