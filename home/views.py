from django.shortcuts import render
from django.http import HttpResponse
from appmsw.utl import get_env_appmsw

# Create your views here.

def index(request):
    context = {
        "appmsw": get_env_appmsw(request),
    }
    # Page from the theme 
    return render(request, 'pages/index.html',context)
