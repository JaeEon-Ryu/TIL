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
'''블록을 만들어서 실행 가능'''
```python
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

### 
```python

```

<br>

### 
```python

```

<br>

### 
```python

```

<br>

### 
```python

```

<br>

### 
```python

```

<br>

### 
```python

```

<br>

### 
```python

```

<br>

### 
```python

```

<br>

### 
```python

```

<br>

### 
```python

```

<br>

### 
```python

```

<br>

### 
```python

```

<br>

### 
```python

```

<br>

### 
```python

```

<br>

### 
```python

```

<br>

### 
```python

```

<br>

### 
```python

```

<br>

### 
```python

```

<br>

### 
```python

```

<br>

### 
```python

```

<br>

### 
```python

```

<br>

### 
```python

```

<br>

### 
```python

```

<br>

### 
```python

```

<br>

### 
```python

```

<br>

### 
```python

```

<br>

### 
```python

```


### reference 
[시니어코딩indiflex - 파이썬 웹개발 Flask #2-2](https://www.youtube.com/watch?v=mLemCf-mZ90&list=PLEOnZ6GeucBWCR_eYjmKuFykGAQylAl9M&index=12)  
[시니어코딩indiflex - 강의 슬라이드](https://docs.google.com/presentation/d/1S9mMlAYCulzAO8j5x9uCZbMUif8cAJHSHt1avztqeVg/edit#slide=id.p)
