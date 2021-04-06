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
      + [N1 관계](#n1-관계)
      + [N:M 관계](#nm-관계)
      + [N:M 관계에 대한 추가 필드](#nm-관계에-대한-추가-필드)
      + [1:1 관계](#11-관계)
    + [파일간의 모델](#파일간의-모델)
    + [필드 이름 제한](#필드-이름-제한)
    + [사용자 정의 필드 유형](#사용자-정의-필드-유형)
    + [Meta 옵션](#meta-옵션)
    + [모델 속성](#모델-속성)
    + [모델 메서드](#모델-메서드)
      + [미리 정의된 모델 메서드 재정의](#미리-정의된-모델-메서드-재정의)
      + [사용자 정의 SQL 실행](#사용자-정의-sql-실행)
  
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
  
  <br>
  
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
  
  <br>
  
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
    
    <br>
  
    + null
      + 참 값이면, Django는 데이터베이스에서 NULL과 같은 비어있는 값을 저장 함 ( 기본값 False )
     
    
    <br>
  
    + blank
      + 참 값이면, 필드는 비워둘 수 있음 ( 기본값 False )
      + null은 DB와 관련이 있는 반면에 blank는 유효성 검사와 관련이 있음
      + blank = True인 경우, 양식 유효성 검사에서 빈 값 입력 가능
    
    <br>
  
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
      
    <br>
  
    + default
      + 필드의 기본값. 값 혹은 호출 가능한 객체일 수 있음
      + 호출 가능하다면 새로운 객체가 생성될 때마다 호출됨
    
    <br>
  
    + help_text
      + 양식 위젯과 함께 표시되는 도움말 텍스트
    
    <br>
  
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
    + DB 관계를 정의하는 방법 ( 일반적 유형 소개 ) -> N:1, N:M, 1:1 관계
    
    <br>
  
    + #### N:1 관계
      + models.ForeignKey 사용
      + ex) Car 모델이 Manufacturer를 갖고 있을 때 
      + Manufacturer가 여러 개의 car를 만들지만, 각 Car에는 하나의 Manufacturer만 있는 경우
      ```python
      from django.db import models

      class Manufacturer(models.Model):
          # ...
          pass

      class Car(models.Model):
          manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
          # ...
      ```
      
    <br>
  
    + #### N:M 관계
      + models.ManyToManyField 사용 
      + ex) 한 pizza에 여러 topping 객체들이 있으며, 한 topping이 여러 pizza가 될 수 있는 경우 
      ```python
      from django.db import models

      class Topping(models.Model):
          # ...
          pass

      class Pizza(models.Model):
          # ...
          toppings = models.ManyToManyField(Topping)
      ```
      + 어떤 모델이 ManyToManyField를 갖고 있느냐는 중요하지 않지만, 두 모델 중 하나에만 있어야 함
    
    <br>
  
    + #### N:M 관계에 대한 추가 필드
      + 두 모델 사이의 관계를 데이터와 연관시킬 때 사용
      + ex) person과 group 사이의 관게를 회원과 연관시킨 예
      ```python
      from django.db import models

      class Person(models.Model):
          name = models.CharField(max_length=128)

          def __str__(self):
              return self.name

      class Group(models.Model):
          name = models.CharField(max_length=128)
          members = models.ManyToManyField(Person, through='Membership')

          def __str__(self):
              return self.name

      class Membership(models.Model):
          person = models.ForeignKey(Person, on_delete=models.CASCADE)
          group = models.ForeignKey(Group, on_delete=models.CASCADE)
          date_joined = models.DateField()
          invite_reason = models.CharField(max_length=64)
      ```
      + 중간 모델은 소스 모델에 대한 외래 키를 하나만 포함해야 함
      
      <br>
  
      + 중간 모델의 인스턴스 생성하기
      ```python
      >>> ringo = Person.objects.create(name="Ringo Starr")
      >>> paul = Person.objects.create(name="Paul McCartney")
      >>> beatles = Group.objects.create(name="The Beatles")
      >>> m1 = Membership(person=ringo, group=beatles,
      ...     date_joined=date(1962, 8, 16),
      ...     invite_reason="Needed a new drummer.")
      >>> m1.save()
      >>> beatles.members.all()
      <QuerySet [<Person: Ringo Starr>]>
      >>> ringo.group_set.all()
      <QuerySet [<Group: The Beatles>]>
      >>> m2 = Membership.objects.create(person=paul, group=beatles,
      ...     date_joined=date(1960, 8, 1),
      ...     invite_reason="Wanted to form a band.")
      >>> beatles.members.all()
      <QuerySet [<Person: Ringo Starr>, <Person: Paul McCartney>]>
      ```
      
      <br>
  
      + add(), create(), set() 등의 문법을 통해 관계를 생성 가능함
      ```python
      >>> beatles.members.add(john, through_defaults={'date_joined': date(1960, 8, 1)})
      >>> beatles.members.create(name="George Harrison", through_defaults={'date_joined': date(1960, 8, 1)})
      >>> beatles.members.set([john, paul, ringo, george], through_defaults={'date_joined': date(1960, 8, 1)})
      ```
      
      <br>
  
      + 중간 모델에 의해 정의된 사용자 테이블이 고유성의 성격을 띄지 않는 경우,   
        (여러 값을 허용하는 경우) remove() 메서드는 모든 중간 모델 인스턴스를 제거함
      ```python
      >>> Membership.objects.create(person=ringo, group=beatles,
      ...     date_joined=date(1968, 9, 4),
      ...     invite_reason="You've been gone for a month and we miss you.")
      >>> beatles.members.all()
      <QuerySet [<Person: Ringo Starr>, <Person: Paul McCartney>, <Person: Ringo Starr>]>
      >>> # This deletes both of the intermediate model instances for Ringo Starr
      >>> beatles.members.remove(ringo)
      >>> beatles.members.all()
      <QuerySet [<Person: Paul McCartney>]>
      ```
      
      <br>
  
      + clear() 메서드는 인스턴스에 대한 모든 N:N 관계를 제거하는 데에 사용
      ```
      >>> # Beatles have broken up
      >>> beatles.members.clear()
      >>> # Note that this deletes the intermediate model instances
      >>> Membership.objects.all()
      <QuerySet []>
      ```
      
      <br>
  
      + N:N 관계를 설정하면 쿼리를 실행할 수 있음
      ```python
      # Find all the groups with a member whose name starts with 'Paul'
      >>> Group.objects.filter(members__name__startswith='Paul')
      <QuerySet [<Group: The Beatles>]>
      ```
      
      <br>
  
      + 중간 모델을 사용하고 있으므로 해당 속성에 대한 쿼리도 실행 가능함
      ```python
      # Find all the members of the Beatles that joined after 1 Jan 1961
      >>> Person.objects.filter(
      ...     group__name='The Beatles',
      ...     membership__date_joined__gt=date(1961,1,1))
      <QuerySet [<Person: Ringo Starr]>
      ```
      
      <br>
  
      + 회원 정보에 접근해야 하는 경우 Membership 모델을 직접 쿼리하여 접근 가능함
      ```python
      >>> ringos_membership = Membership.objects.get(group=beatles, person=ringo)
      >>> ringos_membership.date_joined
      datetime.date(1962, 8, 16)
      >>> ringos_membership.invite_reason
      'Needed a new drummer.'
      ```
      
      <br>
  
      + 동일한 정보에 접근하는 또 다른 방법으로 N:N관계를 역이용 하는 방법이 있음 ( Person 객체로부터 )
      ```python
      >>> ringos_membership = ringo.membership_set.get(group=beatles)
      >>> ringos_membership.date_joined
      datetime.date(1962, 8, 16)
      >>> ringos_membership.invite_reason
      'Needed a new drummer.'
      ```
      
    <br>
  
    + #### 1:1 관계
      + OneToOneField 사용
      + 다른 객체를 확장할 때 유용함
      + ForeignKey와 같이 재귀적인 관계는 정의될 수 있으며 아직 정의되지 않은 모델을 참조하는 것이 만들어질 수 있음
      + option으로 parent_link 인수가 있음
  
  <br>
  
  + ### 파일간의 모델
    + 다른 앱으로부터 모델을 연관시키기 ( ZipCode 사용 )
    ```python
    from django.db import models
    from geography.models import ZipCode

    class Restaurant(models.Model):
        # ...
        zip_code = models.ForeignKey(
            ZipCode,
            on_delete=models.SET_NULL,
            blank=True,
            null=True,
        )
    ```
  
  <br>
  
  + ### 필드 이름 제한
    + 1. 필드 이름은 Python 예약어가 될 수 없음 ( 구문 오류 발생 )
    ```python
    class Example(models.Model):
    pass = models.IntegerField() # 'pass' is a reserved word!
    ```
    + 2. 필드 이름은 한 행에 하나 이상의 밑줄을 포함 할 수 없음
    ```python
    class Example(models.Model):
    foo__bar = models.IntegerField() # 'foo__bar' has two underscores!
    ```
    + 3. 필드 이름은 밑줄로 끝날 수 없음
  
  <br>
  
  + ### 사용자 정의 필드 유형
    + 기존 모델 필드 중 하나를 용도에 맞게 사용할 수 없거나  
      덜 일반적인 데이터베이스 열 유형을 활용하려는 경우  
      고유한 필드 클래스를 만들 수 있음  
  
  <br>
  
  + ### Meta 옵션
    + 아래와 같이 안쪽에 Meta 클래스를 사용함으로써 메타데이터 모델을 만들 수 있음 
    ```python
    from django.db import models

    class Ox(models.Model):
        horn_length = models.IntegerField()

        class Meta:
            ordering = ["horn_length"]
            verbose_name_plural = "oxen"
    ```
  
  <br>
  
  + ### 모델 속성
    + 모델의 가장 중요한 속성 : Manager   
      + Django 모델에 DB 쿼리 작업이 제공됨  
      + 데이터베이스에서 인스턴스를 검색하는데에 사용되는 인터페이스  
      + 사용자 정의 Manager가 정의 되지 않은 경우 기본 이름은 objects로 정의됨  
      + 관리자는 모델 인스턴스가 아닌 모델 클래스를 통해서만 접근 가능함
  
  <br>
  
  + ### 모델 메서드
    + 모델에 사용자 지정 메서드를 정의하여 객체에 'row-level' 기능을 추가
    + Manager 메서드가 '테이블 전체' 작업을 수행하도록 설계된 반면에,   
      모델 메서드는 특정 모델 인스턴스에서 작업을 수행함
    
    <br>
    
    ```python
    from django.db import models

    class Person(models.Model):
        first_name = models.CharField(max_length=50)
        last_name = models.CharField(max_length=50)
        birth_date = models.DateField()

        def baby_boomer_status(self):
            "Returns the person's baby-boomer status."
            import datetime
            if self.birth_date < datetime.date(1945, 8, 1):
                return "Pre-boomer"
            elif self.birth_date < datetime.date(1965, 1, 1):
                return "Baby boomer"
            else:
                return "Post-boomer"

        @property
        def full_name(self):
            "Returns the person's full name."
            return '%s %s' % (self.first_name, self.last_name)
    ```
    
    <br>
    
    + 모델 인스턴스 참조에는 각 모델에 자동으로 제공되는 전체 메서드 목록이 있음
    + 대부분의 항목을 재정의할 수 있지만 거의 항상 정의하고자 하는 두 가지는 다음과 같음
    + __str__()
      + 모든 객체의 문자열 표현을 반환하는 메서드
      + 파이썬이나 장고에서 모델 인스턴스를 강제하고 일반 문자열로 표시해야 할 때마다 사용
      + 대화형 콘솔이나 관리자에 개체를 표시할 때 이러한 현상이 발생
    + get_absolute_url()
      + Django에게 개체의 URL을 계산하는 방법을 알려줌
      + Django는 이를 관리 인터페이스에서 사용하며, 개체의 URL을 확인해야 할 때마다 사용
    
    <br>
    
    + #### 미리 정의된 모델 메서드 재정의
      + 여러 데이터베이스의 동작을 캡슐화하는 또 다른 모델 방법이 존재함
      + 특히 save() 및 delete() 작업 방식을 변경하는 경우가 많음  
        -> 메서드를 재정의하여 동작을 변경할 수 있음
      
      <br>
      
      + 개체를 저장할 때마다 작업이 수행되기를 원하는 경우 ( 일반적인 방법 )
      ```python
      from django.db import models

      class Blog(models.Model):
          name = models.CharField(max_length=100)
          tagline = models.TextField()

          def save(self, *args, **kwargs):
              do_something()
              super().save(*args, **kwargs)  # Call the "real" save() method.
              do_something_else()
      ```
      
      <br>
      
      + 저장을 방지 할 수도 있음 ( 조건문을 통하여 )
      ```python
      from django.db import models

      class Blog(models.Model):
          name = models.CharField(max_length=100)
          tagline = models.TextField()

          def save(self, *args, **kwargs):
              if self.name == "Yoko Ono's blog":
                  return # Yoko shall never have her own blog!
              else:
                  super().save(*args, **kwargs)  # Call the "real" save() method.
      ```
      
      <br>
      
      + super().save(*args, *\*kwargs) 에 관련하여
        + 수퍼클래스 메소드를 호출하여 개체가 데이터베이스에 저장되어 있는지 확인해야 함
        + 수퍼클래스 메서드를 호출하는 것을 잊으면 기본 동작이 발생하지 않고 데이터베이스가 터치되지 않음
        + *args, *\*kgs 비트가 하는 것처럼 모델 메서드에 전달할 수 있는 인수를 전달하는 것이 중요함
        + *args, *\*kwags를 메서드 정의에 사용하는 경우, 코드가 추가될 때 해당 인수를 자동으로 지원함
      + 재정의 된 모델 메서드는 대량 작업에서 호출되지 않음
    
    <br>
    
    + #### 사용자 정의 SQL 실행
      + 또 다른 일반적인 패턴으로 model 메서드와 module_level 메서드에 사용자 정의 SQL문을 작성하는 방법이 있음
    
    <br>
    
  
### 참고 
###### [Django - Models](https://docs.djangoproject.com/en/3.1/topics/db/models/)

