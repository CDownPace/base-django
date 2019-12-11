from django.urls import path
from . import views
app_name='cms'
urlpatterns=[
    path('',views.index),
    path('login/',views.login)
]


from django.http import HttpResponse
from django.shortcuts import redirect,reverse
def index(request):
    return HttpResponse('cms首页')
def login(request):
    return HttpResponse('cms登录页面')


app_name='front'

urlpatterns=[
    path('',views.index,name='index'),
    path('login/',views.login,name="login")
]

def index(request):
    username=request.GET.get('username')
    if username:
        return HttpResponse('前台首页')
    else:
        return redirect(reverse('front:login'))
def login(request):
    return HttpResponse('前台登录页面')