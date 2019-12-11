from django.urls import path
from . import views
# 从当前导入views模块

#应用命名空间
#应用命名空间的变量叫做app_name
app_name='front'

urlpatterns=[
    path('',views.index,name='index'),
    path('login/',views.login,name='login')
]