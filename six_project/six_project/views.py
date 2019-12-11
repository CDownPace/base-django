from django.shortcuts import render
from datetime import datetime

def greet(word):
    return 'hello word %s' %word
def index (request):
    context={
        'greet':greet
    }
    return render(request,'index.html')

def add_view(request):
    return render(request,'add.html')

def cut_view(request):
    return render(request,'cut.html')

def date_view(request):
    context={
        'today':datetime.now()
    }
    return render(request,'date.html',context=context)