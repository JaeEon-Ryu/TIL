# Models

+ INDEX
  + [모델](#모델)
  + [빠른 예](#빠른-예)
  + [모델 사용하기](#모델-사용하기)
  + [필드](#필드)
    + [필드 타입](#필드-타입)
    + [필드 옵션](#필드-옵션)
    + [자동 기본 키 필드](#자동-기본-키-필드)
    + [자세한 필드 이름](#자세한-필드-이름)
    + [관계](#관계)
  
<br>

------------------------------- 

<br>

## 모델
+ 데이터에 대한 정보 소스
+ 저장중인 데이터의 필수 영역과 동작이 포함됨
+ 각각의 모델은 단일 데이터베이스 테이블에 매핑됨
+ 기본 사항
  + 각 모델 : django.db.models.Model.의 하위클래스
  + 모델의 각 속성은 DB 필드를 나타냄
  + Django에서는 자동으로 생성되는 데이터베이스 액세스 API를 제공함

<br>

## 빠른 예
+ first_name 그리고 last_name 이라는 속성을 지닌 Person 모델 생성
  ```python
  from django.db import models

  class Person(models.Model):
      first_name = models.CharField(max_length=30)
      last_name = models.CharField(max_length=30)
  ```
  + first_name 과 last_name 은 모델의 필드라고 할 수 있음
  + 각각의 필드는 클래스의 속성으로 지정되고 데이터베이스 열에 매핑됨
+ 상단의 Person 모델은 다음과 같은 데이터베이스 테이블을 생성함
  ```python
  CREATE TABLE myapp_person (
      "id" serial NOT NULL PRIMARY KEY,
      "first_name" varchar(30) NOT NULL,
      "last_name" varchar(30) NOT NULL
  );
  ```
  + 테이블 이름인 myapp_person 은 모델 메타 데이터에서 자동으로 생성 ( override 될 수 있음 )
  + id 필드가 자동으로 추가됨 ( override 될 수 있음 )
  + 이 예제의 CREATE TABLE은 PostgreSQL 문법을 사용함  
    -> 하지만 Django는 설정 파일에 지정된 데이터베이스의 백엔드에 맞게 SQL을 사용함

<br>

## 모델 사용하기
+ 모델을 정의한 후 해당 모델을 사용할 것임을 Django에 알려야 함
+ models.py가 포함하고 있는 모듈의 이름을 settings에서 INSTALLED_APPS에 추가할 것
+ ex) 만약 모듈이 myapp.models에 있다면 INSTALLED_APPS에 다음과 같이 추가
  ```python
  INSTALLED_APPS = [
    #...
    'myapp',
    #...
  ]
  ```
 
<br>

## 필드
+ 데이터베이스 필드 리스트 : 모델이 정의하는 가장 중요하고도 필요한 부분
+ 필드는 클래스 속성으로 지정됨
+ 필드 이름을 models API와 다르게 할 것 (clean,save,delete)
+ ex)
  ```python
  from django.db import models

  class Musician(models.Model):
      first_name = models.CharField(max_length=50)
      last_name = models.CharField(max_length=50)
      instrument = models.CharField(max_length=100)

  class Album(models.Model):
      artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
      name = models.CharField(max_length=100)
      release_date = models.DateField()
      num_stars = models.IntegerField()
  ```
  + ### 필드 타입
    + 모델의 각 필드는 적절한 Field 클래스의 인스턴스여야 함
      + 어떤 종류의 데이터를 담고 있는 데이터베이스인지 알려주는 column 타입 ( ex : INTEGER, VARCHAR, TEXT)
      + 폼 필드를 렌더링할 때 사용할 기본 HTML 위젯 ``` (ex :  <input type="text">, <select>) ```
      + Django의 관리자 및 자동 생성 양식에서 사용되는 최소 유효성 검사 요구 사항
    + Django는 수십 개의 기본 제공 필드 유형과 함께 제공됨
    
  <br>

  + ### 필드 옵션
    + 각 필드는 특정 필드 별 인수 집합을 사용함
      + ex) 위에서 볼 수 있듯이 'CharField' 에는 max_length라는 요소를 필요로 함
      + ( max_length : 데이터를 저장하는 데 사용되는 VARCHAR 데이터베이스 필드의 사이즈를 지정해줌 )
    + 모든 필드 유형에 사용할 수있는 공통 인수의 set도 있음 ( 선택사항 )
    + null
      + 참 값이면, Django는 데이터베이스에서 NULL과 같은 비어있는 값을 저장 함 ( 기본값 False )
    + blank
      + 참 값이면, 필드는 비워둘 수 있음 ( 기본값 False )
      + null은 DB와 관련이 있는 반면에 blank는 유효성 검사와 관련이 있음
      + blank = True인 경우, 양식 유효성 검사에서 빈 값 입력 가능
    + choices
      + 필드에 대한 선택으로서 2칸짜리의 튜플 서열을 사용 가능함
      + 기본 양식 위젯은 표준 텍스트 필드 대신 선택 상자가 되며 주어진 선택 항목을 제공함으로써 선택을 제한함
      ```python
      YEAR_IN_SCHOOL_CHOICES = [
      ('FR', 'Freshman'),
      ('SO', 'Sophomore'),
      ('JR', 'Junior'),
      ('SR', 'Senior'),
      ('GR', 'Graduate'),
      ]
      ```
      + choices 교체의 순서마다 새로운 마이그레이션 생성
      + 각 튜플의 첫 번째 요소 : DB에 저장될 값
      + 각 튜플의 두 번째 요소 : 필드의 양식 위젯에 표시될 것
      + 모델 인스턴스가 주어지면 get_FOO_display()를 활용하여 필드의 표시 값에 접근 가능함
      ```python
      from django.db import models

      class Person(models.Model):
          SHIRT_SIZES = (
              ('S', 'Small'),
              ('M', 'Medium'),
              ('L', 'Large'),
          )
          name = models.CharField(max_length=60)
          shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
      ```
      ```python
      >>> p = Person(name="Fred Flintstone", shirt_size="L")
      >>> p.save()
      >>> p.shirt_size
      'L'
      >>> p.get_shirt_size_display()
      'Large'
      ```
      + enumeration 클래스를 사용하여 간단한 방법으로 choices 정의 가능
      ```python
      from django.db import models

      class Runner(models.Model):
          MedalType = models.TextChoices('MedalType', 'GOLD SILVER BRONZE')
          name = models.CharField(max_length=60)
          medal = models.CharField(blank=True, choices=MedalType.choices, max_length=10)
       ```
    + default
      + 필드의 기본값. 값 혹은 호출 가능한 객체일 수 있음
      + 호출 가능하다면 새로운 객체가 생성될 때마다 호출됨
    + help_text
      + 양식 위젯과 함께 표시되는 도움말 텍스트
    + primary_key
      + 값이 참인 경우, 이 필드는 모델의 기본키임
      + primary_key에 참값을 지정하지 않으면 Django가 자동으로 primary_key를 보유하기 위해 IntegerField를 추가함
      + ( 기본키 동작을 재정의하지 않는 이상, 필드에 설정할 필요가 없음 )
      + 기본키 필드는 읽기 전용임 -> 현존하는 객체에 기본키값을 변경한다면 새로운 객체가 이전 객체와 함께 생성됨
      ```python
      from django.db import models

      class Fruit(models.Model):
          name = models.CharField(max_length=100, primary_key=True)
      ```
      ```python
      >>> fruit = Fruit.objects.create(name='Apple')
      >>> fruit.name = 'Pear'
      >>> fruit.save()
      >>> Fruit.objects.values_list('name', flat=True)
      <QuerySet ['Apple', 'Pear']>
      ```
    + unique
      + 값이 참인 경우, 이 필드는 유일해야 함
  
  <br>
    
  + ### 자동 기본 키 필드
    + 기본적으로 Django는 각 모델에 다음 필드를 제공함
    ```python
    id = models.AutoField(primary_key=True)
    ```
    + 위에 나온 예시는 '자동 증가 기본 키' 라고 불림
    + 사용자 지정 기본키를 지정하려면, primary_key=True 를 지정할 것
    + ( 사용자가 명시적으로 필드에 primary_key를 지정하면, Django는 자동으로 id를 추가하지 않음 )
    + 각 모델에는 primary_key=True를 가지기 위해 정확히 하나의 필드가 필요함

  <br> 
  
  + ### 자세한 필드 이름
    + ForeignKey, ManyToManyField 그리고 OneToOneField를 제외한 각각의 필드 타입은 옵션적으로 첫번째에 위치에 인수(verbose name)를 취함
    + verbose name을 만들어주지 않으면 Django는 필드의 속성 이름을 사용하여 자동으로 생성함
    
    <br>
    
    + ex) verbose name -> "person's first name"
    ```python
    first_name = models.CharField("person's first name", max_length=30)
    ```
    
    <br>
    
    + ex) # verbose name -> "first name"
    ```python
    first_name = models.CharField(max_length=30)
    ```
    
    <br>
    
    + ForeignKey, ManyToManyField 그리고 OneToOneField는 첫번째 인수를 모델 클래스로 받음
    + ( 따라서 verbose_name 이라는 키워드를 직접 사용함 )
    + ex) ForeignKey, ManyToManyField, OneToOneField
    ```python
        poll = models.ForeignKey(
        Poll,
        on_delete=models.CASCADE,
        verbose_name="the related poll",
    )
    sites = models.ManyToManyField(Site, verbose_name="list of sites")
    place = models.OneToOneField(
        Place,
        on_delete=models.CASCADE,
        verbose_name="related place",
    )
    ```
    + 관습적으로 verbose_name의 첫 번째 글자는 대문자로 만들지 않음
    
  <br>
  
  + ### 관계  
    
  <br>
  
### 참고 
###### [Django - Models](https://docs.djangoproject.com/en/3.1/topics/db/models/)

