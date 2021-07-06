## 플라스크 템플릿 엔진 Jinja2 (1)

<br>

### Templates(Jinja)
```python
* Template Engine - Jinja가 포함되어 있음
  -> Spring의 경우 type, leaf, velocity, JSP + JSTL 등

* py파일을 html로 변환하는 엔진을 템플릿 엔진이라고 함
  -> client side 활용

# Jinja2 Librury: Flask Template Engine  (http://jinja.pocoo.org)
# Types
String, XML, HTML, JSON, Image, Video, etc
# example
{% extends "application.html" %}
{% block body %}
	<ul>
		{% for song in songs %}
			<li><a href="{{song.url}}"> {{song.title}} </a></li>
		{% endfor %}
	</ul>
{% endblock %}
render_template("xx.html", username="Jade")
{# comment #}

```

<br>

### trim_blocks
```python
from flask import render_template

@app.route("/")
def tmpl():
    return render_template("index.html")
    
# ./templates/index.html
<pre>
ttt 한글
{% if True  %}
    TTT
{% endif %}qqq
</pre>


공백 제거 작업 - {%- -%}
# trim_blocks app config
app.jinja_env.trim_blocks = True
```

<br>

### escape
```python
# quotation escape ( | escape 가 생략된 것 )
{{ abc {ef} ghi }}  ⇒ {{ "abc {ef} ghi" }}
{{ "}}>> <strong>Strong</strong>"}}    or   {{ '}}>> <strong>Strong</strong>' | escape }}

# cf. safe string & striptags  
{{ "<strong>Strong</strong>" | safe}}
{{ "<strong>Strong</strong>" | striptags}}

# {% raw %} ~ {% endraw %} : display source code
{% raw %}
	{% if True  %}
    		TTT
	{% endif %}
{% endraw %}
```

<br>

### Markup
```python

# from flask import Markup
return render_template("index.html", markup=Markup("<b>B</b>"))

# Example: Markup()
mu = Markup("<h1>iii = <i>%s</i></h1>")
h = mu % "Italic"
print("h=", h)
return render_template("index.html", markup=Markup(h))

# Markup.escape() & unescape()
bold = Markup("<b>Bold</b>")
bold2 = Markup.escape("<b>Bold</b>")
bold3 = bold2.unescape()

print(bold, bold2, bold3)
⇒ <b>Bold</b> &lt;b&gt;Bold&lt;/b&gt; <b>Bold</b>
```

<br>

### FOR loop
```python
# {% for var in iter %}  …  {% endfor %}
{% for item in items %}
	...item 처리..
{% endfor %}

# Example
lst = [ ("만남1", "김건모"), ("만남2", "노사연") ]
return render_template("index.html", lst=lst)

<ul>
    {% for item in lst %}
        <li>{{item[0]}}: {{item[1]}}</li>
    {% endfor %}
</ul>

{% for title, name in lst %}
    <li>{{title}}: {{name}}</li>
{% endfor %}
```

<br>

### loop object
```python
# for loop 속에서 기본으로 제공되는 object : `현재 for loop 의 self`
- loop.index: 1부터 시작하는 index 값  (cf. loop.index0)
- loop.revindex: n~1 내림차순 index값  (cf. loop.revindex0)
- loop.first: boolean(isThisFirstItem), loop의 첫번째인지의 여부
- loop.last: boolean(isThisLastItem), loop의 마지막인지의 여부
- loop.length: size
- loop.depth : loop 깊이 

# loop.cycle (특정 주기로 수행)
<ul>
    {% for item in lst %}
        <li class="{{loop.cycle('aaa', 'bbb')}}">{{item[0]}}: {{item[1]}}</li>
    {% endfor %}
</ul>
```

<br>

### for loop Filtering
```python
# data의 세번째 인자로 숨김 여부 추가
lst = [ (1, "만남", "김건모", False), (2, "만남", "노사연", True), (3, "만남", "익명", False) ]
return render_template("index.html", lst=lst)

# index.html
<ul>
    {% for rank, title, name, hide in lst if not hide %}
        <li class="{{loop.cycle('aaa', 'bbb')}}">{{title}}: {{name}}</li>
    {% endfor %}
</ul>

# for else
{% for title, name, isShow in lst %}
    <li class="{{loop.cycle('aaa', 'bbb', '')}}">{{title}}: {{name}}</li>
{% else %}
    <li>There is no data.</li>
{% endfor %}


```

<br>

### for recursion
```python
# loop(data)
a = (1, "만남1", "김건모", False, [])
b = (2, "만남2", "노사연", True, [a])
c = (3, "만남3", "익명", False, [a,b])
d = (4, "만남4", "익명", False, [a,b,c])

return render_template("index.html", lst=[a,b,c,d])
# index.html
<ul>
   {% for rank, title, name, hide, ref in lst recursive %}
        <li>
            {{title}}: {{name}}
            <ul class="sub">{{ loop(ref) }}</ul>
        </li>
    {% endfor %}
</ul>
```

<br>

### {% if condition %}  …  {% endif %}
```python
# grammar
{% if <Condition> %}
	....
{ % endif %}

# Example
{% if lst %}
	{% for .... %}
{ % endif %}

# if else (elif)
{% if <Condition> %}
	....
{% elif <Other Condition> %}
	...
{% else %}
	...
{ % endif %}
```

<br>

### Try This: Recursive For
```python
다음과 같은 형태를 갖는 메뉴(NavigationBar)를 for recursive를 이용하여 HTML로 출력하시오.(title, url, children)
	프로그래밍 언어
		파이썬
		자바
	웹 프레임워크
		플라스크
			Jinja
			Genshi Cheetah
		스프링
		노드JS
	기타
		나의 일상
		이슈 게시판
```

<br>

### set & parent's loop object
```python
# set value
{% set title = 'ABC' %}

# access parent(outer) loop
<ul>
    {% for rank, title, name, hide, ref in lst2 recursive %}
    <li>
        {{loop.index}} - <small>{{title}}</small>: {{name}}
        {%- if ref -%}
            {% set outer_loop = loop %}
            {% for ref_song in ref %}
                <p>{{outer_loop.index}} - {{loop.index}} : {{ ref_song[1] }}</p>
            {% endfor %}
        {%- endif %}
    </li>
    {% endfor %}
</ul>
```

<br>

### URL & Link
```python
# url_for('folder', filename='filename.ext')
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}" >

# url_for('router-link')
Copyright <a href="/tmpl">IndiFlex Senior Coding</a>
Copyright <a href="{{ url_for('tmpl') }}">IndiFlex Senior Coding</a>
```

<br>

### Template Extends (block ~ endblock)
상속받아 사용하게끔 함 

```python
# Base Template: 구조 및 자리 잡기용 (layout.html)
<body>
	<h1>{% block <block-name> %}{% endblock %} - Layout Title </h1>
</body>

# extends the base layout html (main.html) 
{% extends "layout.html" %}

# mapping block : block 사용, 순서 무관! (in main.html)
{% block <block-name> %}AAAAA{% endblock %}

# super() : import html from same block-name
{% block <block-name> %}
	{{ super() }}
	<p>TTT</p>
{% endblock %}

```

<br>

### Duplicate Blocks
```python
html이 많아지다 보면 복잡해지므로, block이름을 명시해줌

# layout.html
{% block outer_block %}
	<h3>
		{% block inner_block %}{% endblock inner_block %} 
	</h3>
{% endblock outer_block %}

# main.html
{% block outer_block %}
    <p>1111111111</p>
    {% block inner_block %}BBBBBB{% endblock inner_block %}
{% endblock outer_block %}
```

<br>

### Use blocks in For loop
scoped 써주어야 item 쓴 것 적용됨

```python
# layout.html
<h2>{% block title2 %}{% endblock %} - Layout Title2</h2>

# main.html
{% for item in [1,2,3] %}
    {% block title2 scoped %} <p>XXXXXXXXXX {{item}}</p> {% endblock %}
{% endfor %}
```

<br>

### reference 
[시니어코딩indiflex - 파이썬 웹개발 Flask #2](https://www.youtube.com/watch?v=pb-DDSdqD-I&list=PLEOnZ6GeucBWvOGSbIKNMp6RMQL9LYRc3&index=3)  
[시니어코딩indiflex - 강의 슬라이드](https://docs.google.com/presentation/d/1S9mMlAYCulzAO8j5x9uCZbMUif8cAJHSHt1avztqeVg/edit#slide=id.p)

