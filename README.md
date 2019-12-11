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
# 数据 
```python
context = { "birthday": datetime.now()
}
```
# 模版 
```python
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
