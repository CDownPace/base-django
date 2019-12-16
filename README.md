## four中需要注意
* 只能通过点的方式获取，如果是字典的形式则会报错。字典的话也通过点语法获取
* 使用字典时，键名不要使用关键字，例如keys,values等
* 而且也不支持[]，如果要取到数据的某一项，如:person.0 获取person的第一项。

## five 过滤器
> 对数据进行一些处理，在python中通过函数实现，而在模板中是通过过滤器。
> 对数据进行一些处理，在python中通过函数实现，而在模板中是通过过滤器。
* add过滤器：尝试值和参数进行相加，如果失败就进行拼接。
```python
{{ value|add:"2" }}
```

* cut过滤器：移除值中所有指定的字符串。类似于 python 中的 replace(args,"")
```python
{{ value|cut:" " }}
```
* date过滤器：将一个日期按照指定的格式，格式化成字符串。
```python
# 数据 

context = { "birthday": datetime.now()
}
```
```python
# 模版 

{{ birthday|date:"Y/m/d" }}
```
* default过滤器:如果值被评估为 False 。比如 [] ， "" ， None ， {} 等这些在 if 判断中为 False 的值，都会 使用 default 过滤器提供的默认值。
```python
{{ value|default:"nothing" }}
# 如果 value 是等于一个空的字符串。比如 "" ，那么以上代码将会输出 nothing
```
* default_if_none过滤器:如果值是 None ，那么将会使用 default_if_none 提供的默认值。这个和 default 有区 别， default 是所有被评估为 False 的都会使用默认值。而 default_if_none 则只有这个值是等 于 None 的时候才会使用默认值
```python
{{ value|default_if_none:"nothing" }}

# 如果 value 是等于 "" 也即空字符串，那么以上会输出空字符串。如果 value 是一个 None 值， 以上代码才会输出 nothing
```

* first过滤器:返回列表/元组/字符串中的第一个元素。
```python
{{ value|first }} 
# 如果 value 是等于 ['a','b','c'] ，那么输出将会是 a 。
```



# 补充部分

> 1.4 一个 URL 由以下几部分组成：
```js
// scheme://host:port/path/?query-string=xxx#anchor
// scheme：代表的是访问的协议，一般为 http 或者 https 以及 ftp 等。
// host：主机名，域名，比如 www.baidu.com 。
// port：端口号。当你访问一个网站的时候，浏览器默认使用80端口。
// path：查找路径。比如： www.jianshu.com/trending/now ，后面的 trending/now 就
// 是 path 。
// query-string：查询字符串，比如： www.baidu.com/s?wd=python ，后面的 wd=python 就是查
// 询字符串。
// anchor：锚点，后台一般不用管，前端用来做页面定位的。
```



> 2.1具体获取某篇文章
```python
from django.contrib import admin
from django.urls import path
from book import views
urlpatterns = [
path('admin/', admin.site.urls),
path('book/',views.book_list),
path('book/<book_id>/',views.book_detail)
]

# 而 views.py 中的代码如下：
def book_detail(request,book_id):
text = "您输入的书籍的id是：%s" % book_id
return HttpResponse(text)
```

* 可以通过查询字符串的方式传递一个参数过去。示例代码如下：
```python
urlpatterns = [
path('admin/', admin.site.urls),
path('book/',views.book_list),
path('book/detail/',views.book_detail)
]

#在 views.py 中的代码如下：
def book_detail(request):
book_id = request.GET.get("id")
text = "您输入的书籍id是：%s" % book_id
return HttpResponse(text)
#以后在访问的时候就是通过 /book/detail/?id=1 即可将参数传递过去。
```

> 2.2urls模块的作用：
可以
在 app 内部包含自己的 url 匹配规则，而在项目的 urls.py 中再统一包含这个 app 的 urls 。
```python
# first_project/urls.py文件：
from django.contrib import admin
from django.urls import path,include
urlpatterns = [
path('admin/', admin.site.urls),
path('book/',include("book.urls"))
]
#在 urls.py 文件中把所有的和 book 这个 app 相关的 url 都移动到 app/urls.py 中了，然后在 first_project/urls.py 中，通过 include 函数包含 book.urls ，以后在请求 book 相关的url的时候都需要加一个 book 的前缀。

# book/urls.py文件：
from django.urls import path
from . import views
urlpatterns = [
path('list/',views.book_list),
path('detail/<book_id>/',views.book_detail)
]
#以后访问书的列表的 url 的时候，就通过 /book/list/ 来访问，访问书籍详情页面的 url 的时候就通过 book/detail/<id> 来访问
```

> 2.2 path 函数的定义为： path(route,view,name=None,kwargs=None) 。
path('detail/<book_id>/',views.book_detail)

> re_path 的参数和 path 参数一模一样，只不过第一个参数也就
是 route 参数可以为一个正则表达式。
```python
re_path(r'articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/', views.month_archive),
```

> include函数中的namespace 参数来指定一个实例命名空间，但是在使用实例命名空间之前，
必须先指定一个应用命名空间。
```python
# 主urls.py文件：
from django.urls import path,include
urlpatterns = [
path('movie/',include('movie.urls',namespace='movie'))
]

#然后在 movie/urls.py 中指定应用命名空间。实例代码如下：
from django.urls import path
from . import views
# 应用命名空间
app_name = 'movie'
urlpatterns = [
path('',views.movie,name='index'),
path('list/',views.movie_list,name='list'),
]
```


> 3.1 模板中是常量：渲染模板有多种方式。这里讲下两种常用的方式。
```python
#1. render_to_string ：找到模板，然后将模板编译后渲染成Python的字符串格式。最后再通过 HttpResponse 类包装成一个 HttpResponse 对象返回回去。示例代码如下：
from django.template.loader import render_to_string
from django.http import HttpResponse
def book_detail(request,book_id):
html = render_to_string("detail.html")
return HttpResponse(html)

#2. 以上方式虽然已经很方便了。但是django还提供了一个更加简便的方式，直接将模板渲染成字符串和包装成 HttpResponse 对象一步到位完成。示例代码如下：
from django.shortcuts import render
def book_list(request):
return render(request,'list.html')
```

> 3.2 模板是变量：
```python
# profile.html模板代码
<p>{{ username }}</p>
# views.py代码
def profile(request):
return render(request,'profile.html',context={'username':'huangyong'})
```

> 3.3 常用标签

* url 标签：

####  在模版中，我们经常要写一些 url ，比如某个 a 标签中需要定义 href 属性。当然如果通过硬编码的方式直接将这个 url 写死在里面也是可以的。但是这样对于以后项目维
护可能不是一件好事。因此建议使用这种反转的方式来实现，类似于 django 中的 reverse 一
样。示例代码如下：
```python
<a href="{% url 'book:list' %}">图书列表页面</a>
```
#### 如果 url 反转的时候需要传递参数，那么可以在后面传递。但是参数分位置参数和关键字参数。位置参数和关键字参数不能同时使用。示例代码如下：
```python
# path部分
path('detail/<book_id>/',views.book_detail,name='detail')
# url反转，使用位置参数
<a href="{% url 'book:detail' 1 %}">图书详情页面</a>
# url反转，使用关键字参数
<a href="{% url 'book:detail' book_id=1 %}">图书详情页面</a>

#如果想要在使用 url 标签反转的时候要传递查询字符串的参数，那么必须要手动在在后面添加。示例代码如下：
<a href="{% url 'book:detail' book_id=1 %}?page=1">图书详情页面</a>

#如果需要传递多个参数，那么通过空格的方式进行分隔。示例代码如下：
<a href="{% url 'book:detail' book_id=1 page=2 %}">图书详情页面</a>
```

* autoescape 标签：开启和关闭这个标签内元素的自动转义功能。

> 3.4 过滤器
* first
```python
#返回列表/元组/字符串中的第一个元素。示例代码如下：
{{ value|first }}
#如果 value 是等于 ['a','b','c'] ，那么输出将会是 a 。
```
* last
```python
#返回列表/元组/字符串中的最后一个元素。示例代码如下：
{{ value|last }}
#如果 value 是等于 ['a','b','c'] ，那么输出将会是 c 。
```
* join
```python
#类似与 Python 中的 join ，将列表/元组/字符串用指定的字符进行拼接。示例代码如下：
{{ value|join:"/" }}
#如果 value 是等于 ['a','b','c'] ，那么以上代码将输出 a/b/c 。
```
* length
```python
#获取一个列表/元组/字符串/字典的长度。示例代码如下：
{{ value|length }}
#如果 value 是等于 ['a','b','c'] ，那么以上代码将输出 3 。如果 value 为 None ，那么以上将返回 0 。
```
* lower
```python
#将值中所有的字符全部转换成小写。示例代码如下：
{{ value|lower }}
#如果 value 是等于 Hello World 。那么以上代码将输出 hello world
```
* upper
```python
#类似于 lower ，只不过是将指定的字符串全部转换成大写。
```
* random
```python
# 在被给的列表/字符串/元组中随机的选择一个值。示例代码如下： 
{{ value|random }}
# 如果 value 是等于 ['a','b','c'] ，那么以上代码会在列表中随机选择一个
```
* safe
```python
# 标记一个字符串是安全的。也即会关掉这个字符串的自动转义。示例代码如下：
{{value|safe}}
# 如果 value 是一个不包含任何特殊字符的字符串，比如 <a> 这种，那么以上代码就会把字符串正常的输入。如果 value 是一串 html 代码，那么以上代码将会把这个 html 代码渲染到浏览器中。
```
* slice
```python
#类似于 Python 中的切片操作。示例代码如下：
{{ some_list|slice:"2:" }}
#以上代码将会给 some_list 从 2 开始做切片操作
```
* truncatechars
```python
#如果给定的字符串长度超过了过滤器指定的长度。那么就会进行切割，并且会拼接三个点来作为省略号。示例代码如下：
{{ value|truncatechars:5 }}
#如果 value 是等于 北京欢迎您~ ，那么输出的结果是 北京... 。可能你会想，为什么不会 北京欢迎您... 呢。因为三个点也占了三个字符，所以 北京 +三个点的字符长度就是5。
```
* truncatechars_html
```python
#类似于 truncatechars ，只不过是不会切割 html 标签。示例代码如下：
{{ value|truncatechars:5 }}
#如果 value 是等于 <p>北京欢迎您~</p> ，那么输出将是 <p>北京...</p> 。
```


> 3.7 模板结构优化:
```python
#include:
#想要使用相同的模板，就通过 include 包含进来。这个标签就是 include 。示例代码如下：
# header.html
<p>我是header</p>
# footer.html
<p>我是footer</p>
# main.html
{% include 'header.html' %}
<p>我是main内容</p>
{% include 'footer.html' %}
#include 标签寻找路径的方式。也是跟 render 渲染模板的函数是一样的。默认 include 标签包含模版，会自动的使用主模版中的上下文，也即可以自动的使用主模版中的变量。如果想传入一些其他的参数，那么可以使用 with 语句。示例代码如下：
# header.html
<p>用户名：{{ username }}</p>
# main.html
{% include "header.html" with username='huangyong' %}
```

> 3.7 模板继承:
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
<link rel="stylesheet" href="{% static 'style.css' %}" />
<title>{% block title %}我的站点{% endblock %}</title>
</head>
<body>
<div id="sidebar">
{% block sidebar %}
<ul>
<li><a href="/">首页</a></li>
<li><a href="/blog/">博客</a></li>
</ul>
{% endblock %}
</div>
<div id="content">
{% block content %}{% endblock %}
</div>
</body>
</html>
口，让子模版来根据具体需求来实现。子模板然后通过 extends 标签来实现，示例代码如下：
<!-- 这个模版，我们取名叫做 base.html ，定义好一个简单的 html 骨架，然后定义好两个 block 接 -->
```
```python
{% extends "base.html" %}
{% block title %}博客列表{% endblock %}
{% block content %}
{% for entry in blog_entries %}
<h2>{{ entry.title }}</h2>
<p>{{ entry.body }}</p>
{% endfor %}
{% endblock %}
```



> 3.8 加载静态文件:
```python
STATICFILES_DIRS = [
os.path.join(BASE_DIR,"static")
]
#在模版中使用 load 标签加载 static 标签。比如要加载在项目的 static 文件夹下的 style.css 的文件。那么示例代码如下：
{% load static %}
<link rel="stylesheet" href="{% static 'style.css' %}">
```
