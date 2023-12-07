from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):
    des= Destination.objects.all()
    return render(request,'index.html',{'price':752, 'des':des})

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')
