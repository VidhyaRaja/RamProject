from django.shortcuts import render
from .models import Site,Fields

# Create your views here.

def index(request):
    sites = Site.objects.all()
    return render(request,"index.html",{'site':sites})

def info(request):
    info = Fields.objects.all()
    whichSite = request.POST.get('siteName',None)
    return render(request,"info.html",{'info':info, 'site':whichSite})

