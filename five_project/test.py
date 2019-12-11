# from django.urls import path
# from . import views
# urlpatters=[
#     path('',views.index,name='index'),
#     path('book/',views.book,name='book'),
#     path('move/',views.movie,name='movie'),
#     path('city/', views.city,name='city'),
#     path('book/detail/<book_id>/<category>/',views.book_detail,name='detail'),
# ]
#
#
# from django.shortcuts import render
# from django.http import HttpResponse
#
# def index(request):
#     return render(request,'index.html')
#
# def login(request):
#     next=request.GET.get('next')
#     text='登录页面。登录完成后要跳转的url是:%s'%next
#     return HttpResponse(text)
#     return HttpResponse('登录页面')
#
# def book_detail(request,book_id,category):
#     text='您的图书id是：%s,分类是:%s'%(book_id,category)
#     return HttpResponse(text)
# # url 'detail' book_id='1' category=1