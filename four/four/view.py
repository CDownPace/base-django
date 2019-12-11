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
# 第一个context是参数名字，第二个context指的是自己定义的context
# 通过后台传递参数，将内容传递给前端
# 只能通过点的方式获取，如果是字典的形式则会报错。字典的话也通过点语法获取
# 使用字典时，键名不要使用关键字，例如keys,values等。
# 而且也不支持[]，如果要取到数据的某一项，如:person.0 获取person的第一项。