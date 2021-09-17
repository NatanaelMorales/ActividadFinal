from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    allmascota = mascota.objects.all()
    return render(request, 'index.html', {'allmascota':allmascota})


def Contact(request):
    return render(request, 'contact.html')


def Petmart(request):
    return render(request, 'petmart.html')