from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {
        'logotitle': "iris_footer",
    }
    # Page from the theme 
    return render(request, 'pages/index.html',context)
