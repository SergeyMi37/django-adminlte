from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from appmsw.utl import get_env_appmsw
import core.settings

# Create your views here.

def index(request):
    context = {
        "appmsw": get_env_appmsw(request),
    }
    # Page from the theme 
    return render(request, 'pages/index.html',context)

def set_language(request):
    lang = request.POST.get('lang', 'en')
    request.session[core.settings.LANGUAGE_SESSION_KEY] = lang
    response = HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    response.set_cookie(core.settings.LANGUAGE_COOKIE_NAME, lang)
    return response

def utility(request):
    context = {
       "mode": request.GET.get('mode'),
    }
    # Page from the theme 
    return render(request, 'pages/utility.html',context)
