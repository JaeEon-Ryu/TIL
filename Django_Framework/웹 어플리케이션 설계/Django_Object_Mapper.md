# Models

+ INDEX
  + [모델](#모델)
  + [빠른 예](#빠른-예)
  + [모델 사용하기](#모델-사용하기)
  + [필드](#필드)
    + [필드 타입](#필드-타입)
  
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
      + 폼 필드를 렌더릴할 때 사용할 기본 HTML 위젯 (ex :  <input type="text">, <select>)
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
      + 
    
### 참고 
###### [Django - Models](https://docs.djangoproject.com/en/3.1/topics/db/models/)

