# import django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')


from django.shortcuts import render
class Person(object):
    def __init__(self,username):
        self.username=username

def index(request):
    p=Person('zhidao')
    context={
        'person':p
    }
    return render(request,'index.html',context=context)

from django.urls import path
from front import views
urlpatterns={
    path('',views.index),
}