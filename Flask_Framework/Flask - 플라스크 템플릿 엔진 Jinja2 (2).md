## 플라스크 템플릿 엔진 Jinja2 (2)

<br>

### Macro
```python
# {% macro macro_name(args…) %} ~ {% endmacro %}
{% macro test_macro(type) -%}
	<h3>
		TEST MACRO: {{type}} - {{test_macro.caller}}        # False
	</h3>
{%- endmacro %}

# main.html
{% block … %}
    <p>{{ test_macro('password') }}</p>
{% endblock %}
```

<br>

### Callable Macro
```python
'''블록을 만들어서 실행 가능'''

# {% call macro_name(args…) %} ~ {% endcall %}
{% macro test_macro2(name, class='red') -%}
	<h3 class="{{class}}">
		TEST MACRO2: {{name}} - {{test_macro2.caller}}   # True cf. hasBlock
		<div> {{caller()}} </div>
	</h3>
{%- endmacro %}

# main.html
{% block … %}
    {% call test_macro2('Hong') %}
	  <p>This is main.macro.call</p>
    {% endcall %}
{% endblock %}

# call with args
{% call(x) test_macro('password') $}  {{x}} {% endcall %}
  ⇐  in macro: caller(x=200)

```

<br>

### Import Macro Module
```python
# {% import "macro_file_path" as <macro-alias> [with context] %}
{% import "macro/commons.html" as cm %}
	<h3>
		TEST MACRO2: {{cm.test_macro2()}}
	</h3>
	
# {% import "macro_file_path" as <macro-alias> with context %}
  (macro.html에서 main.html의 변수를 사용할 수 있음
  
# 특정 매크로만 import 하기!! 
# {% from "file_path" import <macro1>, <macro2> %}
{% block … %}
    <p>{{ test_macro('password') }}</p>
{% endblock %}

# macro_name이 _ (underscore)로 시작하면 private(import 불가)!!

```

<br>

### Include
```python
# {% include "include_file_path" %}
<div>
	{% include "inc/navbars.html" %}
</div>

'''ignore missing 쓰는 것이 원칙'''
# {% include "include_file_path" ignore missing %}

'''a.html이 없다면 b.html을 넣어라'''
# {% include ["a.html", "b.html"] %}
<div>
	{% include ["inc/navbars.html", "inc/menus.html"] ignore missing %}
</div>

# {% include "include_file_path" without context %}  # default: with context!!
<div>
	{% include "inc/navbars.html" without context %}
</div>
```

<br>

### Template Filters
```python
@app.template_filter('ymd')               # cf. Handlebars' helper
def datetime_ymd(dt, fmt='%m-%d'):
    if isinstance(dt, date):
        return dt.strftime(fmt)
    else:
        return dt
	
# in template
{{ today | ymd }}  or {{ today | ymd('%m/%d') }}  or {{today | ymd('%m-%d') | safe}}

# basic filters
safe, striptags, abs, escape, filesizeformat, replace, int, round, trim, truncate, wordwrap, indent, center

'''
wordwrap : 글자 쓰다가 개수 기준 개행
center : 개수 기준 가운데 정렬
indent : tab
'''

# batch filter : batch(div size, str to fill)
{% for row in range(-2, 32) | batch(7, 'TT') %}
    <p>{{row}}</p>
{% endfor %}
'''
반복문으로 row를 써주는데 7개마다 개행함
그 후, 마지막에 빈칸이 생기면 남는자리 'TT' 삽입
'''
```

<br>

### reference 
[시니어코딩indiflex - 파이썬 웹개발 Flask #2-2](https://www.youtube.com/watch?v=mLemCf-mZ90&list=PLEOnZ6GeucBWCR_eYjmKuFykGAQylAl9M&index=12)  
[시니어코딩indiflex - 강의 슬라이드](https://docs.google.com/presentation/d/1S9mMlAYCulzAO8j5x9uCZbMUif8cAJHSHt1avztqeVg/edit#slide=id.p)
