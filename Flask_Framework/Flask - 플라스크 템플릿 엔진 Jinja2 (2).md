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

<br>

### 
```python

```


### reference 
[시니어코딩indiflex - 파이썬 웹개발 Flask #2-2](https://www.youtube.com/watch?v=mLemCf-mZ90&list=PLEOnZ6GeucBWCR_eYjmKuFykGAQylAl9M&index=12)  
[시니어코딩indiflex - 강의 슬라이드](https://docs.google.com/presentation/d/1S9mMlAYCulzAO8j5x9uCZbMUif8cAJHSHt1avztqeVg/edit#slide=id.p)
