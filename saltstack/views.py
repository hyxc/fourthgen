from django.shortcuts import render

# Create your views here.
from .saltapi import *

def key_list(request):
    salttext = api_key()
    return render(request, 'saltstack/index.html', {'salttext': salttext})

def index(request):
    return render(request, 'base.html')