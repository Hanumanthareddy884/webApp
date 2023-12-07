from django.shortcuts import render

from django.http import HttpResponse
from datetime import datetime

def home(request):
    today = datetime.now
    return render(request,'home.html',{"today":today})

def add(request):
    a=int(request.POST['input1'])
    b=int(request.POST['input2'])
    output = a+b
    return render(request,'home.html', {"output":output})