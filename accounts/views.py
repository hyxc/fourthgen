from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from .models import User
from .decorators import login_required
# Create your views here.
class UserForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())

def login(request):
    if request.method == 'POST':
        uspa = UserForm(request.POST)
        if uspa.is_valid():
            username = uspa.cleaned_data['username']
            password = uspa.cleaned_data['password']
            user = User.objects.filter(username__exact = username,password__exact = password)
            if user:
                request.session['username'] = username
                return render(request, 'base.html')
            else:
                return HttpResponseRedirect('/accounts/login/')
        else:
            return HttpResponseRedirect('/accounts/login/')
    else:
        uspa = UserForm()
    return render(request, 'accounts/login.html')

def logout(request):
    try:
        del request.session['username']
    except KeyError:
        pass
    return HttpResponseRedirect('/accounts/login/')

