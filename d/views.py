from django.shortcuts import render
from django.views.generic import DetailView
from .models import Taom
def home(request):
    return render(request, 'home.html')

def taom(request):
    taom=Taom.objects.all()
    return render(request, 'taom.html', context={'taom':taom})

def detail(request):
    return render(request, 'detail.html')