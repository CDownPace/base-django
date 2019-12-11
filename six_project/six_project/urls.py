"""six_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('add/', views.add_view),
    path('cut/', views.cut_view),
    path('date/', views.date_view),
]

# 为什么需要过滤器？
# 在dtl中，不支持函数的调用形式 “()”，因此不能给函数传递参数，这将有很大的局限性。而过滤器其实就是一个函数，而且可以接收一个参数
# 可以对需要的参数进行处理，并且还可以额外接收一个参数，（也就是说，最多只能有两个参数）