from django.http import HttpResponseRedirect
import functools

def login_required(func):
    @functools.wraps(func)
    def wrapper(request,*args, **kw):
        user = request.session.get('username')
        if user is not None:
            return func(request,*args, **kw)
        else:
            return HttpResponseRedirect('/accounts/login/')
    return wrapper