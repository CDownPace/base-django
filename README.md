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


## 再补充部分
> 模型中 Meta 配置：

我们想要在数据库映射的时候使用自己指定的表名，而不是使用模型的名称。那么我们可以在 Meta 类中添加一个 db_table 的属性。
```python
示例代码如下：
class Book(models.Model):
name = models.CharField(max_length=20,null=False)
desc = models.CharField(max_length=100,name='description',db_column="description1")
class Meta:
db_table = 'book_model'
```
以下将对 Meta 类中的一些常用配置进行解释。
* db_table：

这个模型映射到数据库中的表名。如果没有指定这个参数，那么在映射的时候将会使用模型名来作
为默认的表名。
* ordering：

设置在提取数据的排序方式。后面章节会讲到如何查找数据。
比如我想在查找数据的时候根据添加的时间排序，那么示例代码如下：
```python
class Book(models.Model):
name = models.CharField(max_length=20,null=False)
desc = models.CharField(max_length=100,name='description',db_column="description1")
pub_date = models.DateTimeField(auto_now_add=True)
class Meta:
db_table = 'book_model'
ordering = ['pub_date']
```



> 4.5 外键：外键就是通过一个表来操作另外一个表
```python
from django.db import models

# Create your models here.
# 分类的模型
class Category(models.Model):
    name=models.CharField(max_length=100)

# app.模型的名字

class Article(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    category=models.ForeignKey("Category",on_delete=models.CASCADE)
    author=models.ForeignKey('frontuser.FrontUser',on_delete=models.CASCADE,
null=True,related_name="article")
    # related_name="articles"相当于article_set

    def _str_(self):
        return "<Article:(id:%s,title:%s)>"%(self.id,self.title)

# 引用自身
class Comment(models.Model):
    content=models.TextField()
    origin_comment=models.ForeignKey("self",on_delete=models.CASCADE)
```

>4.5 外键删除操作：

如果一个模型使用了外键。那么在对方那个模型被删掉后，该进行什么样的操作。可以通
过 on_delete 来指定。可以指定的类型如下：
*  CASCADE ：级联操作。如果外键对应的那条数据被删除了，那么这条数据也会被删除。
*  PROTECT ：受保护。即只要这条数据引用了外键的那条数据，那么就不能删除外键的那条数
据。
*  SET_NULL ：设置为空。如果外键的那条数据被删除了，那么在本条数据上就将这个字段设置
为空。如果设置这个选项，前提是要指定这个字段可以为空。
*  SET_DEFAULT ：设置默认值。如果外键的那条数据被删除了，那么本条数据上就将这个字段
设置为默认值。如果设置这个选项，前提是要指定这个字段一个默认值。
*  SET() ：如果外键的那条数据被删除了。那么将会获取 SET 函数中的值来作为这个外键的
值。 SET 函数可以接收一个可以调用的对象（比如函数或者方法），如果是可以调用的对
象，那么会将这个对象调用后的结果作为值返回回去。
*  DO_NOTHING ：不采取任何行为。一切全看数据库级别的约束。




> 模型的操作：

在 ORM 框架中，所有模型相关的操作，比如添加/删除等。其实都是映射到数据库中一条数据的操
作。因此模型操作也就是数据库表中数据的操作。
添加一个模型到数据库中：
添加模型到数据库中。首先需要创建一个模型。创建模型的方式很简单，就跟创建普通
的 Python 对象是一摸一样的。在创建完模型之后，需要调用模型的 save 方法，这样 Django 会
自动的将这个模型转换成 sql 语句，然后存储到数据库中。示例代码如下：
```python
class Book(models.Model):
name = models.CharField(max_length=20,null=False)
desc = models.CharField(max_length=100,name='description',db_column="description1")
pub_date = models.DateTimeField(auto_now_add=True)
book = Book(name='三国演义',desc='三国英雄！')
book.save()
```
* 查找数据：
查找数据都是通过模型下的 objects 对象来实现的。
* 查找所有数据：
要查找 Book 这个模型对应的表下的所有数据。那么示例代码如下：
```python
books = Book.objects.all()
```
以上将返回 Book 模型下的所有数据。

* 数据过滤：
在查找数据的时候，有时候需要对一些数据进行过滤。那么这时候需要调
用 objects 的 filter 方法。实例代码如下：
```python
books = Book.objects.filter(name='三国演义')
> [<Book:三国演义>]
# 多个条件
books = Book.objects.filter(name='三国演义',desc='test')

调用 filter ，会将所有满足条件的模型对象都返回。
```
* 获取单个对象：
使用 filter 返回的是所有满足条件的结果集。

有时候如果只需要返回第一个满足条件的对象。那
么可以使用 get 方法。示例代码如下：
```python
book = Book.objects.get(name='三国演义')
> <Book:三国演义>
```
当然，如果没有找到满足条件的对象，那么就会抛出一个异常。而 filter 在没有找到满足条件的
数据的时候，是返回一个空的列表。

* 数据排序：
在之前的例子中，数据都是无序的。

如果你想在查找数据的时候使用某个字段来进行排序，那么可
以使用 order_by 方法来实现。示例代码如下：
```python
books = Book.objects.order_by("pub_date")
```

以上代码在提取所有书籍的数据的时候，将会使用 pub_date 从小到大进行排序。如果想要进行倒序排序，那么可以在 pub_date 前面加一个负号。实例代码如下：
```python
books = Book.objects.order_by("-pub_date")
```
* 修改数据：在查找到数据后，便可以进行修改了。

修改的方式非常简单，只需要将查找出来的对象的某个属性
进行修改，然后再调用这个对象的 save 方法便可以进行修改。示例代码如下：
```python
from datetime import datetime
book = Book.objects.get(name='三国演义')
book.pub_date = datetime.now()
book.save()
```
* 删除数据：在查找到数据后，便可以进行删除了。

删除数据非常简单，只需要调用这个对象的 delete 方法即
可。实例代码如下：

```python
book = Book.objects.get(name='三国演义')
book.delete()
```

* in：

提取那些给定的 field 的值是否在给定的容器中。容器可以为 list 、 tuple 或者任何一个可以
迭代的对象，包括 QuerySet 对象。示例代码如下：
```python
articles = Article.objects.filter(id__in=[1,2,3])
#以上代码在翻译成 SQL 语句为如下：
select ... where id in (1,3,4)
```
当然也可以传递一个 QuerySet 对象进去。示例代码如下：
```python
inner_qs = Article.objects.filter(title__contains='hello')
categories = Category.objects.filter(article__in=inner_qs)
#以上代码的意思是获取那些文章标题包含 hello 的所有分类。
```
将翻译成以下 SQL 语句，示例代码如下：
```python
select ...from category where article.id in (select id from article where title like '%
hello%');
```
* gt：

某个 field 的值要大于给定的值。示例代码如下：
```python
articles = Article.objects.filter(id__gt=4)
# 以上代码的意思是将所有 id 大于4的文章全部都找出来。
```
将翻译成以下 SQL 语句：
```python
select ... where id > 4;
```
* gte：
类似于 gt ，是大于等于。
* lt：
类似于 gt 是小于。
* lte：
类似于 lt ，是小于等于。
* startswith：
判断某个字段的值是否是以某个值开始的。大小写敏感。示例代码如下：
```python
articles = Article.objects.filter(title__startswith='hello')
# 以上代码的意思是提取所有标题以 hello 字符串开头的文章。
```
将翻译成以下 SQL 语句：
```python
select ... where title like 'hello%'
```
* istartswith：
类似于 startswith ，但是大小写是不敏感的。
* endswith：
判断某个字段的值是否以某个值结束。大小写敏感。示例代码如下：
```python
articles = Article.objects.filter(title__endswith='world')
# 以上代码的意思是提取所有标题以 world 结尾的文章。
```
将翻译成以下 SQL 语句：
```python
select ... where title like '%world';
```
* iendswith：
类似于 endswith ，只不过大小写不敏感。
* range：
判断某个 field 的值是否在给定的区间中。示例代码如下：
```python
from django.utils.timezone import make_aware
from datetime import datetime
start_date = make_aware(datetime(year=2018,month=1,day=1))
end_date = make_aware(datetime(year=2018,month=3,day=29,hour=16))
articles = Article.objects.filter(pub_date__range=(start_date,end_date))
# 以上代码的意思是提取所有发布时间在 2018/1/1 到 2018/12/12 之间的文章。
```
将翻译成以下的 SQL 语句：
```python
select ... from article where pub_time between '2018-01-01' and '2018-12-12'。
# 需要注意的是，以上提取数据，不会包含最后一个值。也就是不会包含 2018/12/12 的文章。

# 而且另外一个重点，因为我们在 settings.py 中指定了 USE_TZ=True ，并且设置了 TIME_ZONE='Asia/Shanghai' ，因此我们在提取数据的时候要使用 django.utils.timezone.make_aware 先将 datetime.datetime 从 navie 时间转换为 aware 时
# 间。 make_aware 会将指定的时间转换为 TIME_ZONE 中指定的时区的时间。
```
* date：
针对某些 date 或者 datetime 类型的字段。可以指定 date 的范围。并且这个时间过滤，还可以使用链式调用。示例代码如下：
```python
articles = Article.objects.filter(pub_date__date=date(2018,3,29))
以上代码的意思是查找时间为 2018/3/29 这一天发表的所有文章。
```
将翻译成以下的 sql 语句：
```python
select ... WHERE DATE(CONVERT_TZ(`front_article`.`pub_date`, 'UTC', 'Asia/Shanghai')) =
2018-03-29
# 注意，因为默认情况下 MySQL 的表中是没有存储时区相关的信息的。因此我们需要下载一些时区
# 表的文件，然后添加到 Mysql 的配置路径中。如果你用的是 windows 操作系统。那么
# 在 http://dev.mysql.com/downloads/timezones.html 下载 timezone_2018d_posix.zip - POSIX
# standard 。然后将下载下来的所有文件拷贝到 C:\ProgramData\MySQL\MySQL Server
# 5.7\Data\mysql 中，如果提示文件名重复，那么选择覆盖即可。
```
如果用的是 linux 或者 mac 系统，那么在命令行中执行以下命令：
```python
 mysql_tzinfo_to_sql
/usr/share/zoneinfo | mysql -D mysql -u root -p ，然后输入密码，从系统中加载时区文件更新
到 mysql 中。
```
*year：
根据年份进行查找。示例代码如下：
```python
articles = Article.objects.filter(pub_date__year=2018)
articles = Article.objects.filter(pub_date__year__gte=2017)
```

以上的代码在翻译成 SQL 语句为如下：
select ... where pub_date between '2018-01-01' and '2018-12-31';
select ... where pub_date >= '2017-01-01';
month：
同 year ，根据月份进行查找。
day：
同 year ，根据日期进行查找。
week_day：
Django 1.11 新增的查找方式。同 year ，根据星期几进行查找。1表示星期天，7表示星期
六， 2-6 代表的是星期一到星期五。

* time：

根据时间进行查找。示例代码如下：
```python
articles = Article.objects.filter(pub_date__time=datetime.time(12,12,12));
以上的代码是获取每一天中12点12分12秒发表的所有文章。
更多的关于时间的过滤，请参考 Django 官方文
档： https://docs.djangoproject.com/en/2.0/ref/models/querysets/#range 。
isnull：
根据值是否为空进行查找。示例代码如下：
articles = Article.objects.filter(pub_date__isnull=False)
以上的代码的意思是获取所有发布日期不为空的文章。
将来翻译成 SQL 语句如下：
select ... where pub_date is not null;
regex和iregex：
大小写敏感和大小写不敏感的正则表达式。示例代码如下：
articles = Article.objects.filter(title__regex=r'^hello')
以上代码的意思是提取所有标题以 hello 字符串开头的文章。
将翻译成以下的 SQL 语句：
select ... where title regexp binary '^hello';
iregex 是大小写不敏感的。
根据关联的表进行查询：
假如现在有两个 ORM 模型，一个是 Article ，一个是 Category 。代码如下：
class Category(models.Model):
"""文章分类表"""
name = models.CharField(max_length=100)
class Article(models.Model):
"""文章表"""
title = models.CharField(max_length=100,null=True)
category = models.ForeignKey("Category",on_delete=models.CASCADE)
比如想要获取文章标题中包含"hello"的所有的分类。那么可以通过以下代码来实现：
categories = Category.object.filter(article__title__contains("hello"))








1. filter ：将满足条件的数据提取出来，返回一个新的 QuerySet 。具体的 filter 可以提供
什么条件查询。请见查询操作章节。
2. exclude ：排除满足条件的数据，返回一个新的 QuerySet 。示例代码如下：
Article.objects.exclude(title__contains='hello')
以上代码的意思是提取那些标题不包含 hello 的图书。
3. annotate ：给 QuerySet 中的每个对象都添加一个使用查询表达式（聚合函数、F表达式、Q
表达式、Func表达式等）的新字段。示例代码如下：
articles = Article.objects.annotate(author_name=F("author__name"))
以上代码将在每个对象中都添加一个 author__name 的字段，用来显示这个文章的作者的年
龄。
4. order_by ：指定将查询的结果根据某个字段进行排序。如果要倒叙排序，那么可以在这个字
段的前面加一个负号。示例代码如下：
# 根据创建的时间正序排序
articles = Article.objects.order_by("create_time")
# 根据创建的时间倒序排序
articles = Article.objects.order_by("-create_time")
# 根据作者的名字进行排序
articles = Article.objects.order_by("author__name")
# 首先根据创建的时间进行排序，如果时间相同，则根据作者的名字进行排序
articles = Article.objects.order_by("create_time",'author__name')
# 一定要注意的一点是，多个 order_by ，会把前面排序的规则给打乱，而使用后面的排序方
# 式。比如以下代码：
articles = Article.objects.order_by("create_time").order_by("author__name")
# 他会根据作者的名字进行排序，而不是使用文章的创建时间。
# 5. values ：用来指定在提取数据出来，需要提取哪些字段。默认情况下会把表中所有的字段全
# 部都提取出来，可以使用 values 来进行指定，并且使用了 values 方法后，提取出
# 的 QuerySet 中的数据类型不是模型，而是在 values 方法中指定的字段和值形成的字典：
articles = Article.objects.values("title",'content')
for article in articles:
print(article)
以上打印出来的 article 是类似于 {"title":"abc","content":"xxx"} 的形式。
如果在 values 中没有传递任何参数，那么将会返回这个恶模型中所有的属性。
```
 * values_list ：类似于 values 。只不过返回的 QuerySet 中，存储的不是字典，而是元组。

```python
# 示例代码如下：
articles = Article.objects.values_list("id","title")
print(articles)
# 那么在打印 articles 后，结果为 <QuerySet [(1,'abc'),(2,'xxx'),...]> 等。
# 如果在 values_list 中只有一个字段。那么你可以传递 flat=True 来将结果扁平化。示例代
# 码如下：
articles1 = Article.objects.values_list("title")
>> <QuerySet [("abc",),("xxx",),...]>
articles2 = Article.objects.values_list("title",flat=True)
>> <QuerySet ["abc",'xxx',...]>
```

* all ：获取这个 ORM 模型的 QuerySet 对象。
* select_related ：在提取某个模型的数据的同时，也提前将相关联的数据提取出来。比如提取文章数据，可以使用 select_related 将 author 信息提取出来，以后再次使用 article.author 的时候就不需要再次去访问数据库了。可以减少数据库查询的次数。示例
代码如下：
```python
article = Article.objects.get(pk=1)
>> article.author # 重新执行一次查询语句
article = Article.objects.select_related("author").get(pk=2)
>> article.author # 不需要重新执行查询语句了
select_related 只能用在 一对多 或者 一对一 中，不能用在 多对多 或者 多对一 中。比如可
以提前获取文章的作者，但是不能通过作者获取这个作者的文章，或者是通过某篇文章获取这
个文章所有的标签。
```
* prefetch_related ：这个方法和 select_related 非常的类似，就是在访问多个表中的数据的时候，减少查询的次数。这个方法是为了解决 多对一 和 多对多 的关系的查询问题。比如要获取标题中带有 hello 字符串的文章以及他的所有标签，示例代码如下：
```python
from django.db import connection
articles = Article.objects.prefetch_related("tag_set").filter(title__contains='hel
lo')
print(articles.query) # 通过这条命令查看在底层的SQL语句
for article in articles:
print("title:",article.title)
print(article.tag_set.all())
# 通过以下代码可以看出以上代码执行的sql语句
for sql in connection.queries:
print(sql)
```
但是如果在使用 article.tag_set 的时候，如果又创建了一个新的 QuerySet 那么会把之前的 SQL 优化给破坏掉。比如以下代码：
```python
tags = Tag.obejcts.prefetch_related("articles")
for tag in tags:
articles = tag.articles.filter(title__contains='hello') #因为filter方法会重新生成一个QuerySet，因此会破坏掉之前的sql优化
# 通过以下代码，我们可以看到在使用了filter的，他的sql查询会更多，而没有使用filter的，只有两次sql查询
for sql in connection.queries:
print(sql)
```
那如果确实是想要在查询的时候指定过滤条件该如何做呢，这时候我们可以使用 django.db.models.Prefetch 来实现， Prefetch 这个可以提前定义好 queryset 。示例代码如下：
```python
tags = Tag.objects.prefetch_related(Prefetch("articles",queryset=Article.objects.f
ilter(title__contains='hello'))).all()
for tag in tags:
articles = tag.articles.all()
for article in articles:
print(article)
for sql in connection.queries:
print('='*30)
print(sql)
# 因为使用了 Prefetch ，即使在查询文章的时候使用了 filter ，也只会发生两次查询操作。
```
* defer ：在一些表中，可能存在很多的字段，但是一些字段的数据量可能是比较庞大的，而此时你又不需要，比如我们在获取文章列表的时候，文章的内容我们是不需要的，因此这时候我们就可以使用 defer 来过滤掉一些字段。这个字段跟 values 有点类似，只不过 defer 返回的不是字典，而是模型。示例代码如下：
```python
articles = list(Article.objects.defer("title"))
for sql in connection.queries:
print('='*30)
print(sql)
```
在看以上代码的 sql 语句，你就可以看到，查找文章的字段，除了 title ，其他字段都查找出来了。当然，你也可以使用article.title 来获取这个文章的标题，但是会重新执行一个查询的语句。示例代码如下：
```python
articles = list(Article.objects.defer("title"))
for article in articles:
# 因为在上面提取的时候过滤了title
# 这个地方重新获取title，将重新向数据库中进行一次查找操作
print(article.title)
for sql in connection.queries:
print('='*30)
print(sql)
```
defer 虽然能过滤字段，但是有些字段是不能过滤的，比如 id ，即使你过滤了，也会提取出来。
* only ：跟 defer 类似，只不过 defer 是过滤掉指定的字段，而 only 是只提取指定的字
段。
* get ：获取满足条件的数据。这个函数只能返回一条数据，并且如果给的条件有多条数据，
那么这个方法会抛出 MultipleObjectsReturned 错误，如果给的条件没有任何数据，那么就会
抛出 DoesNotExit 错误。所以这个方法在获取数据的只能，只能有且只有一条。
* create ：创建一条数据，并且保存到数据库中。这个方法相当于先用指定的模型创建一个对
象，然后再调用这个对象的 save 方法。示例代码如下：
```python
article = Article(title='abc')
article.save()
# 下面这行代码相当于以上两行代码
article = Article.objects.create(title='abc')
```
* get_or_create ：根据某个条件进行查找，如果找到了那么就返回这条数据，如果没有查找到，那么就创建一个。示例代码如下：
```python
obj,created= Category.objects.get_or_create(title='默认分类')
# 如果有标题等于 默认分类 的分类，那么就会查找出来，如果没有，则会创建并且存储到数据库中。
# 这个方法的返回值是一个元组，元组的第一个参数 obj 是这个对象，第二个参数 created 代表是否创建的。
```
* bulk_create ：一次性创建多个数据。示例代码如下：
```python
Tag.objects.bulk_create([
Tag(name='111'),
Tag(name='222'),
])
```
* count ：获取提取的数据的个数。如果想要知道总共有多少条数据，那么建议使用 count ，而不是使用 len(articles) 这种。因为 count 在底层是使用 select count(*) 来实现的，这种方式比使用 len 函数更加的高效。
* first 和 last ：返回 QuerySet 中的第一条和最后一条数据。
* aggregate ：使用聚合函数。
* exists ：判断某个条件的数据是否存在。如果要判断某个条件的元素是否存在，那么建议使用 exists ，这比使用 count 或者直接判断 QuerySet 更有效得多。示例代码如下：
```python
if Article.objects.filter(title__contains='hello').exists():
print(True)
比使用count更高效：
if Article.objects.filter(title__contains='hello').count()  > 0:
print(True)
# 也比直接判断QuerySet更高效：
if Article.objects.filter(title__contains='hello'):
print(True)
```
* distinct ：去除掉那些重复的数据。这个方法如果底层数据库用的是 MySQL ，那么不能传递任何的参数。比如想要提取所有销售的价格超过80元的图书，并且删掉那些重复的，那么可
以使用 distinct 来帮我们实现，示例代码如下：
```python
books = Book.objects.filter(bookorder__price__gte=80).distinct()
```
需要注意的是，如果在 distinct 之前使用了 order_by ，那么因为 order_by 会提取 order_by 中指定的字段，因此再使用 distinct 就会根据多个字段来进行唯一化，所以就不会把那些重复的数据删掉。示例代码如下：
```python
orders = BookOrder.objects.order_by("create_time").values("book_id").distinct()
# 那么以上代码因为使用了 order_by ，即使使用了 distinct ，也会把重复的 book_id 提取出来。
```
* update ：执行更新操作，在 SQL 底层走的也是 update 命令。比如要将所有 category 为空的 article 的 article 字段都更新为默认的分类。示例代码如下：
```python
Article.objects.filter(category__isnull=True).update(category_id=3)
# 注意这个方法走的是更新的逻辑。所以更新完成后保存到数据库中不会执行 save 方法，因此不会更新 auto_now 设置的字段。
```
* delete ：删除所有满足条件的数据。删除数据的时候，要注意 on_delete 指定的处理方式。
* 切片操作：有时候我们查找数据，有可能只需要其中的一部分。那么这时候可以使用切片操作来帮我们完成。 QuerySet 使用切片操作就跟列表使用切片操作是一样的。示例代码如下：
```python
books = Book.objects.all()[1:3]
for book in books:
print(book)
# 切片操作并不是把所有数据从数据库中提取出来再做切片操作。而是在数据库层面使用 LIMIE 和 OFFSET 来帮我们完成。所以如果只需要取其中一部分的数据的时候，建议大家使
# 用切片操作。
```
