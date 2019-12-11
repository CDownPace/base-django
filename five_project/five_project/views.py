from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def login(request):
    next=request.GET.get('next')
    text='登录页面。登录完成后要跳转的url是:%s'%next
    return HttpResponse(text)
    return HttpResponse('登录页面')

def book(request):
    return HttpResponse('读书页面')

def book_detail(request,book_id,category):
    text='您的图书的id是： %s, 分类是: %s'%(book_id,category)
    return HttpResponse(text)

def movie(request):
    return HttpResponse('电影页面')

def city(request):
    return HttpResponse('同城页面')