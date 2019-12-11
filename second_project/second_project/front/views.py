
from django.shortcuts import redirect,reverse

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    username=request.GET.get('username')
    if username:
        return HttpResponse('前台首页')
    else:
        login_url=reverse('front:login')
        return redirect(login_url)

def login(request):
    return HttpResponse('前台登录页面')