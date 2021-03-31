# Django Overview

+ INDEX
  + [모델 디자인](#모델-디자인)
  
  
<br>

------------------------------- 

<br>

### 모델 디자인
+ 데이터베이스 없이도 Django를 사용 가능함
  + 그래도 객체-관계 매퍼(object-relational mapper)가 함께 제공됨
  + ( Python 코드로 데이터베이스 레이아웃을 묘사할 수 있도록 )
+ 데이터-모델 구문(data-model syntax) : 모델을 표현할 수 있는 다양한 방법 제공
+ 활용예시
```python
from django.db import models # django.db라는 패키지에서 models라는 클래스 가져오기

class Reporter(models.Model): # 엔티티 선언
    full_name = models.CharField(max_length=70) # 속성 선언

    def __str__(self):
        return self.full_name

class Article(models.Model): # 엔티티 선언 
    pub_date = models.DateField() # 속성 선언
    headline = models.CharField(max_length=200) # 속성 선언
    content = models.TextField() # 속성 선언
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE) # 속성 선언

    def __str__(self):
        return self.headline
```

<br>

### 설치
+ DB 자동 생성
``` windows
...\> py manage.py makemigrations
...\> py manage.py migrate
```
+ makemigrations : 테이블이 없는 경우 migrations 생성
+ migrate : migrations 실행 및 테이블 생성 ( 더 풍부한 스키마 제어기능 제공 )


  
   
### 참고 
###### [Django - Documentation](https://docs.djangoproject.com/en/3.1/intro/overview/)

