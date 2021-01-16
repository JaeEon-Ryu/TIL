# About Django Framework    

+ INDEX
  + [Django 앱 작성 1부](#django-앱-작성-1부)
    + [1부 개요](#1부-개요)
    + [구성](#구성)
    + [장고 설치 ( 윈도우 기준 )](#장고-설치--윈도우-기준-)
    + [장고 프로젝트 시작하기](#장고-프로젝트-시작하기)
    + [polls 앱 만들기](#polls-앱-만들기)
  + [Django 앱 작성 2부](#django-앱-작성-2부)
    + [데이터베이스 설정](#데이터베이스-설정)
    + [모델 생성](#모델-생성)
    + [모델 활성화](#모델-활성화)
    + [Django가 제공하는 API 사용하기 ( 예제 )](#django가-제공하는-api-사용하기--예제-)
    + [Djnago 관리](#django-관리)
  + [Django 앱 작성 3부](#django-앱-작성-3부)
    + [3부 개요](#3부-개요)
    + [뷰 더 만들기](#뷰-더-만들기)
    + [작동되는 뷰 만들기](#작동되는-뷰-만들기)
    + [404 에러 띄우기](#404-에러-띄우기)
    + [템플릿 시스템 사용하기](#템플릿-시스템-사용하기)
    + [템플릿에서 하드 코딩된 URL 제거하기](#템플릿에서-하드-코딩된-url-제거하기)
    + [URL 이름공간 정해주기](#url-이름공간-정해주기)
  + [Django 앱 작성 4부](#django-앱-작성-4부)
    + [4부 개요](#4부-개요)
    + [최소 양식 작성하기](#최소-양식-작성하기)
    + [제네릭 뷰 사용하기 : 코드가 적을수록 좋음](#제네릭-뷰-사용하기--코드가-적을수록-좋음)
  + [Django 앱 작성 5부](#django-앱-작성-5부)
    + [자동 테스트 도입](#자동-테스트-도입)
    + [기본 테스트 전략](#기본-테스트-전략)
    + [테스트 작성](#테스트-작성)
    + [뷰 테스트](#뷰-테스트)
    + [테스트를 많이 할수록 좋음](#테스트를-많이-할수록-좋음)
    + [추가-테스트](#추가-테스트)
  + [Django 앱 작성 6부](#django-앱-작성-6부)
    + [앱의 모양과 느낌을 커스터마이징](#앱의-모양과-느낌을-커스터마이징)
    + [배경 이미지 추가](#배경-이미지-추가)
  + [Django 앱 작성 7부](#django-앱-작성-7부)
    + [7부 개요](#7부개요)
    + [관리자 폼 커스터마이징](#관리자-폼-커스터마이징)
    + [관련 객체 추가](#관련-객체-추가)
    + [관리자 변경 목록 커스터마이징](#관리자-변경-목록-커스터마이징)
    + [관리자 모양 및 느낌 커스터마이징](#관리자-모양-및-느낌-커스터마이징)
    + [관리자 인덱스 페이지 커스터마이징](#관리자-인덱스-페이지-커스터마이징)
  + [재사용 가능한 앱 제작](#재사용-가능한-앱-제작)
    + [재사용가능성 문제](#재사용가능성-문제)
    + [프로젝트 및 재사용 가능한 앱](#프로젝트-및-재사용-가능한-앱)
    + [일부 필수 구성 요소 설치](#일부-필수-구성-요소-설치)
    + [앱 패키징하기](#앱-패키징하기)
    + [나만의 패키지 사용하기](#나만의-패키지-사용하기)
    + [앱 게시하기](#앱-게시하기)
  
    

<br>

------------------------------- 

<br>

## Django 앱 작성, 1부
+ ### 1부 개요
  + Python 기반 웹 프레임 워크
  + 웹 애플리케이션을 효율적이고 신속하게 만들 수 있음
  + 문서화, 확장성이 뛰어남
  + 데이터베이스 쉽게 전환 가능
  + 관리 인터페이스가 내장되어 사용이 편리함
  + 웹 스크래핑, 머신러닝, 이미지 프로세싱 등 방대한 라이브러리를 가진 파이썬 언어를 기반으로 함 
  
  <br>
  
+ ### 구성
  + MVT 아키텍처를 기반으로 함 
  + MVT ( Model - View - Template )
    + 모델 ( Model ) 
      + 데이터의 인터페이스 역할
      + 데이터 유지보수 담당
      + 전체 애플리케이션의 논리적 데이터 구조
      + 일반적으로 MySql, Postgres와 같은 관계형 데이터베이스 
    + 뷰 ( View )
      + 웹 사이트를 렌더링 할 때 브라우저에서 볼 수 있는 사용자 인터페이스 
      + HTML/CSS/Javascript 
    + 템플릿 ( Template )
      + 원하는 HTML 출력의 정적 부분과 동적 콘텐츠가 삽입되는 방법을 설명하는 몇 가지 특수 구문으로 구성


  <br>
  
+ ### 장고 설치 ( 윈도우 기준 )
  + cmd 혹은 MINGW64 열기 
    > 알고 있어야 하는 명령어
    
        1. cd ( change directory ) 
          cd 폴더명 : 해당 폴더로 이동
          cd .. : 해당 폴더 전의 경로로 돌아감
        2. Ctrl + c 
          Ctrl + c : 명령 중지 ( 향후 cmd 상에서 장고 웹 실행 중지 시 필요 )  
  
  <br>
    
  + pip 설치 
    > #### python -m pip install --user pip
      
      이미 설치가 된 경우 건너뛰기 가능  
  
  <br>
  
  + 가상 환경 설치    
    > #### pip install virtualenv   
    
      가상 환경을 이용하는 이유 : 같은 도구를 여러 버전 설치해 둘 수 없다는 단점을 보완   
  
  <br>
      
  + 가상 환경 설정   
    1. 가상 환경 생성     
      >  #### virtualenv my_env        
      
        env_env는 가상환경 이름 -> 사용자 임의로 만들기 가능

        필자의 경우 'FileNotFoundError: [Errno 2] No such file or directory: ~' 같은 에러가 나왔는데,
        직접 폴더(C:\Users\Ryu)에 들어가보니 이미 env_env 폴더가 생성되어 있었음. 

        위와 다르게 폴더가 생성되지 않는 에러의 경우 https://newbiecs.tistory.com/145 페이지 참고 권장함  
      
      
    2. 폴더 이동하기 1    
      > ####  cd my_env    
    3. 폴더 이동하기 2    
      > ####  cd Scripts  
    4. 가상 환경 활성화      
      > ####  activate    
  
  <br>
  
  + 장고 설치
    > #### pip install django   

  <br>
   
+ ### 장고 프로젝트 시작하기
  + 프로젝트 만들기
    + cmd에서 가상환경 폴더까지 이동
    + 가상 환경 활성화 하기 ( activate )
    + 명령어 입력
      > #### django-admin startproject mysite
          mysite은 프로젝트 이름 -> 사용자 임의로 만들기 가능 
          명령어가 입력된 후 파이참 같은 통합개발환경이나 파일 탐색기로 확인 시 다음과 같은 하위 목록이 만들어져 있음   
        
          mysite/             
            manage.py        ( 장고의 다양한 명령어를 실행하기 위한 파일 )
            mysite/
                __init__.py
                settings.py   ( 프로젝트에 관련된 다양한 설정 ) 
                urls.py       ( 사용자가 URL로 Django에 접근을 하면 Django는 URL로 URL 규칙을 보고 내부에서 일치하는 VIEW를 찾아 연결 ) 
                asgi.py       ( Asynchronous Server Gateway Interface 의 줄임말, django-channels가 사용하고 있는 Daphne와 django-channels가 작동하는 기반 ) 
                wsgi.py       ( Web Server Gateway Interface 의 줄임말, Python 의 표준 Gateway Interface ) 
  
  <br>
        
  + 폴더 이동하기 ( cmd 에서 ) 
    > #### cd mysite
  
  <br>
  
  + 실행하기
    > #### Python manage.py runserver
  
  <br>
  
  + 웹 페이지 방문하기
    + http://localhost:8000/ 클릭    
      ( 우주선 모양이 나오면 성공 ) 

  <br>
  
+ ### polls 앱 만들기
  + 장고 프로젝트는 하나 이상의 애플리케이션으로 구성   
    ( 앱은 웹서비스 중 하나의 기능 의미 ) 
  
  <br>
  
  + 앱 만들기
    > #### python manage.py startapp polls    
      ( cmd상에서 Ctrl + c 로 서버를 중지한 상태에서 명령어 입력 - manage.py 파일이 있는 경로에서 실행해야 함 )
      
        코드가 정상적으로 입력되었다면 다음과 같은 하위목록이 만들어져 있음

        polls/
            __init__.py
            admin.py
            apps.py
            migrations/
                __init__.py
            models.py
            tests.py
            views.py
  
  <br>
       
  + 앱 ( polls ) 하위에 있는 views.py 파일 내용 작성
    > polls/view.py
      
      ```Python
      
      from django.http import HttpResponse

      def index(request):
          return HttpResponse("Hello, world. You're at the polls index.")
      ```
  
  <br>
  
  + 앱 ( polls ) 하위에 urls.py 파일 생성 후 내용 작성
    > polls/urls.py
    
      ```Python
      
      from django.urls import path

      from . import views

      urlpatterns = [
          path('', views.index, name='index'),
      ]
      ```
  
  <br>
        
  + 프로젝트 폴더(mysite)에 있는 urls.py 내용 작성
    > mysite/urls.py
       
      ```Python 
      from django.urls import include, path

      urlpatterns = [
          path('polls/', include('polls.urls')),
          path('admin/', admin.site.urls),
      ]
      ```
  
  <br>
        
  + 웹 페이지 접속
    + python manage.py runserver ( cmd 에서 입력 )
    + http://localhost:8000/polls/ ( 링크 이동 ) 
    + 모든 작업을 완료했으면 다음과 같은 화면이 나옴
  
        <img src="https://user-images.githubusercontent.com/52907116/103541158-51fa5a80-4ede-11eb-9307-9cce567f5ad8.png" width="25%"></img>
 
  <br>
  
  
  <br>
   
### 참고 

###### [GeeksforGeeks - Django Tutorial](https://www.geeksforgeeks.org/django-tutorial/)
###### [GeeksforGeeks - Django Basics](https://www.geeksforgeeks.org/django-basics/)
###### [Django - Writing your first Django app, part 1](https://docs.djangoproject.com/en/3.1/intro/tutorial01/)
###### [jcinsh - Django - 튜토리얼 part1](https://velog.io/@jcinsh/Django-%ED%8A%9C%ED%86%A0%EB%A6%AC%EC%96%BC)
###### [vlvksbdof12 - Python Django 기초 제 2강](https://velog.io/@vlvksbdof12/Python-Django-%EA%B8%B0%EC%B4%88-%EC%A0%9C-2%EA%B0%95)
  

  <br>
    
------------------------

  <br>
  
## Django 앱 작성 2부

+ ### 데이터베이스 설정
  + 기본적으로 SQLite 사용 ( Python에 내장되어 있음 ) 
  > 다른 엔진 사용 가능 
  
    ```Python
    
    'django.db.backends.sqlite3'
    'django.db.backends.postgresql'
    'django.db.backends.mysql'
    'django.db.backends.oracle'
    ```

  <br>
      
+ ### 모델 생성
  + 모델이란?
    + 데이터베이스에 저장될 데이터를 클래스 형태로 구성한 것   
      ( 상속기능을 이용해 필요한 부분만 구현하도록 ) 
    + 데이터와 동작을 함께 정의 ( CRUD : 저장, 읽기, 수정, 삭제 ) 
 
  <br>
  
  + Django에서의 Model : 데이터 서비스를 제공하는 계층
  + models.py 모듈 안에 하나 이상의 모델 클래스를 정의 가능   
    ( 하나의 모델 클래스는 데이터베이스에서 하나의 테이블에 해당 ) 
   
  <br>
  
  + polls 폴더 하위에 있는 models.py 파일에 내용 작성
    > polls/models.py
      
      ```Python
      
      from django.db import models

      class Question(models.Model): 
          question_text = models.CharField(max_length=200)  # 질문
          pub_date = models.DateTimeField('date published') # publish 시간


      class Choice(models.Model):
          question = models.ForeignKey(Question, on_delete=models.CASCADE)  # 질문 - 외래키, 삭제될 경우 연쇄삭제
          choice_text = models.CharField(max_length=200)  # 답변
          votes = models.IntegerField(default=0)  # 답변 횟수
      ```
            
    + Question, Choice 각각 class로 정의하며, django.db.models.Model를 상속받음 
  
  <br>
  
  + 모델 생성시
    + 이 앱을 위한 Database schema 생성
    + Question, Choice 객체를 위한 파이썬 데이터베이스 액세스 API 생성

  <br>
     
+ ### 모델 활성화    
  + polls 앱이 설치 되었음을 알리기
    > mysite / settings.py
    
      ```Python
      
      INSTALLED_APPS = [
          'polls.apps.PollsConfig',
          'django.contrib.admin',
          'django.contrib.auth',
          'django.contrib.contenttypes',
          'django.contrib.sessions',
          'django.contrib.messages',
          'django.contrib.staticfiles',
      ]
      ```
      
  <br>
  
  + > 모델 변경사항 저장하기 ( cmd 입력 )  
    
        python manage.py makemigrations polls
  
    + models.py에 만들어놓은 모델들은 바로 사용할 수 없음, makemigration 과정을 거쳐야 사용 가능
    + 모델 클래스를 생성하고 난 후, 해당 모델에 상응하는 테이블을 DB에서 생성 가능함
      + Migration : 파이썬 모델 클래스의 수정 및 생성을 DB에 적용하는 과정   
        ( 이는 장고가 기본적으로 제공하는 ORM - Object Relational Mapping 을 통해 진행 )
  
  <br>
     
  + > SQL문 미리보기 ( cmd 입력 )
        
        python manage.py sqlmigrate polls 0001
  
    + sqlmigrate 명령은 DB에서 migration을 실제로 실행하지 않음
    + Django가 수행 할 작업을 확인하거나 변경을위해 SQL 스크립트를 필요로 할 때 사용
  
  <br>
    
  + > 모델 테이블 만들기 ( cmd 입력 ) 
  
        python manage.py migrate
        
    + 실제적인 DB가 생성되는 시점    
      ( makemigrations를 통해 생성된 임시파일을 setting.py에 작성된 데이터베이스에 반영 )
    + Migration을 통해 DB나 테이블을 직접 삭제 or 생성 할 필요없이 모델에 변화를 줄 수 있음

  <br>
  
+ ### Django가 제공하는 API 사용하기 ( 예제 ) 
  
  + Shell에서 나올때는 exit() 를 입력
  
  <br>
  
  + > Python Shell 호출 ( cmd 입력 )
    
        python manage.py shell 
  
  <br>
        
  + > API 사용하기1) - Shell 내부에서 코드 입력 
  
        ( shell에 들어간 후 아래 코드중 ' >>> ' 표시가 되어있는 것들만 입력 ) 
        
        >>> from polls.models import Choice, Question  # Import the model classes we just wrote.

        # No questions are in the system yet.
        >>> Question.objects.all()
        <QuerySet []>

        # Create a new Question.
        # Support for time zones is enabled in the default settings file, so
        # Django expects a datetime with tzinfo for pub_date. Use timezone.now()
        # instead of datetime.datetime.now() and it will do the right thing.
        >>> from django.utils import timezone
        >>> q = Question(question_text="What's new?", pub_date=timezone.now())

        # Save the object into the database. You have to call save() explicitly.
        >>> q.save()

        # Now it has an ID.
        >>> q.id
        1

        # Access model field values via Python attributes.
        >>> q.question_text
        "What's new?"
        >>> q.pub_date
        datetime.datetime(2021, 1, 5, 13, 55, 43, 205830, tzinfo=<UTC>)

        # Change values by changing the attributes, then calling save().
        >>> q.question_text = "What's up?"
        >>> q.save()

        # objects.all() displays all the questions in the database.
        >>> Question.objects.all()
        <QuerySet [<Question: Question object (1)>]>
        
        
      <img src="https://user-images.githubusercontent.com/52907116/103659823-33649400-4fb0-11eb-9c04-e79d27575dbc.png" width="90%"></img>
        
  
  <br>
  
  + API 사용하기2) - python 코드 추가 
    
    > polls/models.py ( 코드 추가 1 )
    
      ```Python
      
      from django.db import models

      class Question(models.Model):
          # ...
          def __str__(self):
              return self.question_text

      class Choice(models.Model):
          # ...
          def __str__(self):
              return self.choice_text
      ```
  
    \__str__() : 객체의 표현을 사용하기 위해 메서드 추가
  
    > polls/models.py ( 코드 추가 2 ) 
    
      ```Python
      import datetime

      from django.db import models
      from django.utils import timezone


      class Question(models.Model):
          # ...
          def was_published_recently(self):
              return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
      ```
            
    변경사항 저장
  
  <br>
    
  + > Python Shell 호출 ( cmd 입력 )
    
        python manage.py shell 
  
  <br>
        
  + > API 사용하기3) - Shell 내부에서 코드 입력 
    
        >>> from polls.models import Choice, Question

        # Make sure our __str__() addition worked.
        >>> Question.objects.all()
        <QuerySet [<Question: What's up?>]>

        # Django provides a rich database lookup API that's entirely driven by
        # keyword arguments.
        >>> Question.objects.filter(id=1)
        <QuerySet [<Question: What's up?>]>
        >>> Question.objects.filter(question_text__startswith='What')
        <QuerySet [<Question: What's up?>]>

        # Get the question that was published this year.
        >>> from django.utils import timezone
        >>> current_year = timezone.now().year
        >>> Question.objects.get(pub_date__year=current_year)
        <Question: What's up?>

        # Request an ID that doesn't exist, this will raise an exception.
        >>> Question.objects.get(id=2)
        Traceback (most recent call last):
            ...
        DoesNotExist: Question matching query does not exist.

        # Lookup by a primary key is the most common case, so Django provides a
        # shortcut for primary-key exact lookups.
        # The following is identical to Question.objects.get(id=1).
        >>> Question.objects.get(pk=1)
        <Question: What's up?>

        # Make sure our custom method worked.
        >>> q = Question.objects.get(pk=1)
        >>> q.was_published_recently()
        True

        # Give the Question a couple of Choices. The create call constructs a new
        # Choice object, does the INSERT statement, adds the choice to the set
        # of available choices and returns the new Choice object. Django creates
        # a set to hold the "other side" of a ForeignKey relation
        # (e.g. a question's choice) which can be accessed via the API.
        >>> q = Question.objects.get(pk=1)

        # Display any choices from the related object set -- none so far.
        >>> q.choice_set.all()
        <QuerySet []>

        # Create three choices.
        >>> q.choice_set.create(choice_text='Not much', votes=0)
        <Choice: Not much>
        >>> q.choice_set.create(choice_text='The sky', votes=0)
        <Choice: The sky>
        >>> c = q.choice_set.create(choice_text='Just hacking again', votes=0)

        # Choice objects have API access to their related Question objects.
        >>> c.question
        <Question: What's up?>

        # And vice versa: Question objects get access to Choice objects.
        >>> q.choice_set.all()
        <QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>
        >>> q.choice_set.count()
        3

        # The API automatically follows relationships as far as you need.
        # Use double underscores to separate relationships.
        # This works as many levels deep as you want; there's no limit.
        # Find all Choices for any question whose pub_date is in this year
        # (reusing the 'current_year' variable we created above).
        >>> Choice.objects.filter(question__pub_date__year=current_year)
        <QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>

        # Let's delete one of the choices. Use delete() for that.
        >>> c = q.choice_set.filter(choice_text__startswith='Just hacking')
        >>> c.delete()

  <br>
          
+ ### Django 관리
  + Django Admin : 모델에 대한 관리 인터페이스 생성 자동화
  + 관리자 사이트는 방문자가 사용 불가 ( 관리자를 위한 것 ) 

  + 관리자 생성하기
    > 관리 사이트에 로그인 할 수 있는 사용자 만들기 ( cmd 입력 )
        
        python manage.py createsuperuser
    
    > 사용자 이름 입력
    
        Username : admin
    
    > 이메일 주소 입력
    
        Email address : admin@example.com
    
    > 비밀번호 입력
    
        Password: **********
        Password (again): *********
        Superuser created successfully.

    <br>

  + ### 개발 서버 시작
    + 관리자를 설정 했다면 Django 관리 사이트가 기본적으로 활성화 되어있음

      > 서버 실행

          python manage.py runserver

      > 웹페이지 이동

          http://127.0.0.1:8000/admin/

      <img src="https://user-images.githubusercontent.com/52907116/103661759-6d369a00-4fb2-11eb-8b6d-781a24707f80.png" width="30%"></img>

    <br>

  + ### 관리자 사이트 들어가기
    + 사이트에 로그인을 하게 되면 인증과 권한을 부여할 수 있는 기능이 있음    
      ( django.contrib.auth - 장고에 의해 제공되는 인증 프레임 워크 )

       <img src="https://user-images.githubusercontent.com/52907116/103661762-6e67c700-4fb2-11eb-9e44-5efcb85d7065.png" width="70%"></img>

    <br>

  + ### 관리자의 입장에서 polls앱을 수정 가능하도록 만들기
    +  Question 객체에 관리자 인터페이스가 있음을 알려야 함 ( Python 코드 추가 )

      > polls/admin.py

        ```Python
        
        from django.contrib import admin

        from .models import Question

        admin.site.register(Question)
        ```
    <br>

  + ### 기능 살펴보기
    + 바로 위에서 Question 이라는 것을 관리 사이트에 등록했으므로 아래와 같은 화면이 나옴
      <img src="https://user-images.githubusercontent.com/52907116/103661763-6e67c700-4fb2-11eb-97fd-6070c3ec71db.png" width="70%"></img>

    <br>

    + Questions을 클릭하면 앞서 만든 What's up? 이라는 문항이 나옴 
      <img src="https://user-images.githubusercontent.com/52907116/103661764-6f005d80-4fb2-11eb-8953-ba690058e42b.png" width="65%"></img>

    <br>

    + What's up? 문항 클릭 후 편집 화면
      + 게시된 날짜 값이 질문을 생성한 시간과 맞지 않다면 TIME_ZOME 설정값 변경하기
      + Today, Now 버튼을 누르면 현재 날짜, 시각으로 변경
      <img src="https://user-images.githubusercontent.com/52907116/103665113-6447c780-4fb6-11eb-952f-6f03ce77621c.png" width="70%"></img>

    <br>

    + History 클릭 
      + 시간대별로 누가 변경을 했고 어떤것을 변경했는지 모든 변경사항이 나옴
      <img src="https://user-images.githubusercontent.com/52907116/103665117-64e05e00-4fb6-11eb-9c17-c1f2e31e7c98.png" width="50%"></img>



    <br>
      
### 참고 

###### [Django - Writing your first Django app, part 2](https://docs.djangoproject.com/en/3.1/intro/tutorial02/)
###### [jcinsh - Django - 튜토리얼 part2](https://velog.io/@jcinsh/Django-%ED%8A%9C%ED%86%A0%EB%A6%AC%EC%96%BC-part2)

 <br>
 
-----------------

 <br>

## Django 앱 작성 3부
  + ### 3부 개요
    + 뷰 : Django에 있는 웹 페이지의 종류 ( 특정 기능과 템플릿을 제공 )    
      ( 상호작용 : View <-> URL <-> Django )
    + Django에서 웹 페이지 및 기타 콘텐츠는 뷰를 통해 제공됨
    + Django는 요청된 URL을 검사하여 뷰를 선택함
    + URL에서 뷰로 이동하기 위해 Django는 'URLconfs'를 사용   
      ( URLconf는 URL 패턴을 뷰에 매핑함 )
    
    <br>
  
  + ### 뷰 더 만들기
    + polls 앱에 뷰 추가 
      > polls/view.py
      ```Python
      def detail(request, question_id):
          return HttpResponse("You're looking at question %s." % question_id)

      def results(request, question_id):
          response = "You're looking at the results of question %s."
          return HttpResponse(response % question_id)

      def vote(request, question_id):
          return HttpResponse("You're voting on question %s." % question_id) 
      ```
      + urlpatterns에서 매칭되는 URL pattern을 찾았다면, HttpRequest 객체를 가지고 넘겨준 view function을 call함   
      -> views 함수들의 첫번째 input에 모두 request라는 input을 받게 만들어둠
      
     <br>
     
    + polls 앱에 경로 추가
      > polls/urls.py
      ```Python
      from django.urls import path

      from . import views

      urlpatterns = [
          # ex: /polls/
          path('', views.index, name='index'),
          # ex: /polls/5/
          path('<int:question_id>/', views.detail, name='detail'),
          # ex: /polls/5/results/
          path('<int:question_id>/results/', views.results, name='results'),
          # ex: /polls/5/vote/
          path('<int:question_id>/vote/', views.vote, name='vote'),
      ]
      ```
     
    + 요청 예시 ( "/polls/34/" 를 요청했을 때 )
      + 1) mysite.urls를 불러옴   
          ( mysite/settings.py 에서 ROOT_URLCONF = mysite.urls )
      + 2) mysite.urls에서 urlpatterns라는 리스트를 찾고, 그 중  'polls/'라는 경로를 찾음
      + 3) 일치하는 텍스트("polls/")를 빼고, 남은 텍스트인 "34/"를 'polls.urls' URLconf로 전달하여 남은 처리를 진행한다.   
          ( urlpatterns 중 '<int:question_id>/'와 일치하여, 결과적으로 detail() 뷰 함수가 호출 )
      + > 위와 같은 방식으로 detail 함수가 호출됨
        
            detail(request=<HttpRequest object>, question_id=34)
      
      + 호출된 웹페이지
      
        <img src="https://user-images.githubusercontent.com/52907116/103776770-48eec200-5073-11eb-9ebb-ea2d1930537f.png" width="35%"></img>
        
    <br>
      
  + ### 작동되는 뷰 만들기
    + 뷰의 역할 
      + 1. 요청된 페이지의 내용이 담긴 HttpResponse 객체를 반환
      + 2. Http404같은 예외를 반환
    + 최근 5개 설문 인덱스 화면에 띄우기
      > polls/view.py
        ```Python
        from django.http import HttpResponse

        from .models import Question


        def index(request):
            latest_question_list = Question.objects.order_by('-pub_date')[:5]
            output = ', '.join([q.question_text for q in latest_question_list])
            return HttpResponse(output)
        ```
        
        <img src="https://user-images.githubusercontent.com/52907116/103887198-0508c500-5126-11eb-994f-35298abd7a4e.png" width="25%"></img>    
        
        ( 저장되어 있는 리스트가 1개뿐이라 What's up? 만 나옴 ) 
            
    <br>
        
    + 템플릿 생성
      + 방금 위에서 작업한 코드를 보면 뷰에서 페이지 디자인이 하드 코딩되어 있음      
        -> 페이지 모양을 변경하려면 이 Python 코드를 편집해야 함   
        -> 따라서 템플릿을 생성하여 Python에서 설계를 분리함
          
    <br>
      
      + DjangoTemplates은 각 INSTALLED_APPS 에 있는 "templates" 하위 폴더를 탐색함   
        -> DjangoTemplates이 찾을 수 있도록 polls 폴더 아래에 templates라는 디렉토리를 만들어줌   
        -> 그리고 그 아래에 polls라는 폴더를 하나 더 만들고 그 아래에 index.html 파일을 만들어줌    
          ( Django가 polls/templates 를 찾은 후, polls/index.html 이라는 이름으로 참조 )
        
    <br>
      
      + html 내용 작성 
        > polls/templates/polls/index.html
        ```Html
        {% if latest_question_list %}
            <ul>
            {% for question in latest_question_list %}
                <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
            {% endfor %}
            </ul>
        {% else %}
            <p>No polls are available.</p>
        {% endif %}
        ```
        
    <br>
      
      + 템플릿을 사용하기 위해 인덱스 수정하기
        > polls/views.py
        ```Python
        from django.http import HttpResponse
        from django.template import loader

        from .models import Question


        def index(request):
            latest_question_list = Question.objects.order_by('-pub_date')[:5]
            template = loader.get_template('polls/index.html')                  # 템플릿 로드
            context = {
                'latest_question_list': latest_question_list,
            }
            return HttpResponse(template.render(context, request))              # context 전달
            # context는 템플릿에서 쓰이는 변수명과 Python 객체를 연결하는 사전형 값
        ```
        
        <img src="https://user-images.githubusercontent.com/52907116/103887201-05a15b80-5126-11eb-80c2-903a464adf0b.png" width="25%"></img>   
        <img src="https://user-images.githubusercontent.com/52907116/103887202-0639f200-5126-11eb-9567-fed04c0ccfc4.png" width="25%"></img>    
        ( 클릭시 - 질문의 세부 정보 페이지 ) 
          
    <br>
      
      + 지름길 : render() 
        + request와 template_name을 필수로 받고 넘겨준 것들을 조합해서 HTTPResponse를 리턴해주는 함수
        > polls/views.py
        ```Python
        from django.shortcuts import render

        from .models import Question


        def index(request):
            latest_question_list = Question.objects.order_by('-pub_date')[:5]
            context = {'latest_question_list': latest_question_list}
            return render(request, 'polls/index.html', context)
        ```
     
    <br>
      
  + ### 404 에러 띄우기
    + 요청받은 ID의 question이 없는 경우 Http404 예외 발생
    + 예제를 빠르게 사용하려면
      > polls/templates/polls/detail.html
      ```HTML
      {{ question }}
      ```
     
    <br>
      
    + 지름길 : get_object_or_404()
      + Django 모델을 첫 번째 인수와 임의의 수의 키워드 인수를 사용하여 모델 관리자의 get() 함수에 전달,    
        개체가 없는 경우 Http404를 올림
        > polls/views.py
        ```Python
        from django.shortcuts import get_object_or_404, render

        from .models import Question
        # ...
        def detail(request, question_id):
            question = get_object_or_404(Question, pk=question_id)
            return render(request, 'polls/detail.html', {'question': question})
            
        ```
      + ObjectDoesNotExist 예외를 쓰지 않고 Http404 를 내보내는 모델 API 그리고 get_object_or_404() 를 쓰는 이유?    
        -> 모델 계층과 뷰 계층을 결합하기 때문. Django는 느슨한 결합을 지향함
  
    <br>
      
  + ### 템플릿 시스템 사용하기
    + polls 앱의 세부 정보 보기 편집
      > polls/templates/polls/detail.html
      ```Html
      <h1>{{ question.question_text }}</h1>
      <ul>
      {% for choice in question.choice_set.all %}
          <li>{{ choice.choice_text }}</li>
      {% endfor %}
      </ul>
      ```
      <img src="https://user-images.githubusercontent.com/52907116/103887197-03d79800-5126-11eb-8b15-8fbd7ada5b4f.png" width="20%"></img> 
    + dot-검색 구문을 사용하여 변수 attriubute에 접근 ( {{ question.question_text }} )
    + Django는 question 객체에 사전형 검색 수행
    + attriubute 검색 실패시, list-index 검색 수행
    
    <br>
      
  + ### 템플릿에서 하드 코딩된 URL 제거하기
    + 기존 index.html 코드 중 question 부분
      > polls/index.html
        ``` Html
        <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
        ```
         
    <br>
      
    + 위 코드처럼 긴밀하게 결합된 접근 방식의 문제 : 템플릿이 많은 프로젝트에서 URL을 변경하는 것이 어려워짐   
      -> 따라서 polls.urls 모듈의 함수에서 이미 이름 인수를 정의했음
      -> {% url %} 템플릿 태그를 사용하여 URL 구성에 정의된 특정 URL 경로에 대한 종속성을 제거 가능
            
    <br>
      
    + 수정 후 
      > polls/index.html
        ``` Html
        <li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
        ```
      
    <br>
      
  + ### URL 이름공간 정해주기
    + Django에서는 URL 이름들을 구별해야함     
      ( 현재 polls 앱에서는 detail 뷰 등 ) 
    + URLconf에 namespaces 추가 
      > polls/urls.py
        ```Python
        from django.urls import path

        from . import views

        app_name = 'polls' 
        urlpatterns = [
            path('', views.index, name='index'),
            path('<int:question_id>/', views.detail, name='detail'),
            path('<int:question_id>/results/', views.results, name='results'),
            path('<int:question_id>/vote/', views.vote, name='vote'),
        ]
        ```
    + index.html 부분 수정
      > polls/templates/polls/index.html
        ```Html
        <li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
        ```
  <br>

### 참고 

###### [Django - Writing your first Django app, part 3](https://docs.djangoproject.com/en/3.1/intro/tutorial03/)
###### [wldus9503 - [Django tutorial] 3.첫 번째 장고 앱 작성하기, part 3](https://velog.io/@wldus9503/Django-tutorial-2.%EC%B2%AB-%EB%B2%88%EC%A7%B8-%EC%9E%A5%EA%B3%A0-%EC%95%B1-%EC%9E%91%EC%84%B1%ED%95%98%EA%B8%B0-part-3)
###### [eungding - [Django] 튜토리얼 part 3 (1) - view 만들기, Template 이용하기, r](https://eunjin3786.tistory.com/128)


<br> 

------------------------

<br>

## Django 앱 작성 4부

+ ### 4부 개요
  + polls 앱 양식 처리, 코드 리팩토링에 중점을 둘 것임
  
  <br> 

+ ### 최소 양식 작성하기 
  + poll앱 템플릿의 detail 업데이트하기
    > polls/templates/polls/detail.html
    ```Html
    <h1>{{ question.question_text }}</h1>

    {% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}

    <form action="{% url 'polls:vote' question.id %}" method="post"> 
    <!-- 데이터 서버 측 변경면에서 method="post"는 유용한 메서드임 -->
    {% csrf_token %}
    <!-- 내부 URL을 대상으로 하는 모든 POST 폼들은 csrf_token 템플릿 태그를 사용 ( 사이트간 요청 위조 방지 ) -->
    {% for choice in question.choice_set.all %}
        <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}">
        <!-- 각 질문에 대한 radio 버튼 설정 -->
        <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br>
        <!-- forloop.counter = 말 그대로 반복문 개수 세기 -->
    {% endfor %}
    <input type="submit" value="Vote">
    </form>
    ```
  
  <br> 

  + 제출된 데이터를 처리하는 Django 뷰 만들기 
    + vote 부분 구현하기
      > polls/urls.py
        ```Python
        from django.http import HttpResponse, HttpResponseRedirect
        from django.shortcuts import get_object_or_404, render
        from django.urls import reverse

        from .models import Choice, Question
        # ...
        def vote(request, question_id):
            question = get_object_or_404(Question, pk=question_id)
            try:
                selected_choice = question.choice_set.get(pk=request.POST['choice'])
                # request.Post : 사전 자료형으로 선택된 choice의 ID값 반환 
            except (KeyError, Choice.DoesNotExist):
                # choice가 없으면 KetError
                # Redisplay the question voting form.
                return render(request, 'polls/detail.html', {
                    'question': question,
                    'error_message': "You didn't select a choice.",
                })
            else:
                selected_choice.votes += 1
                selected_choice.save()
                # Always return an HttpResponseRedirect after successfully dealing
                # with POST data. This prevents data from being posted twice if a
                # user hits the Back button.
                return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
                # 선택을 끝낸 사용자에게 보여줄 결과화면의 URL 
                # args = URL로부터 파싱되는 뷰 함수로 이동될 인수 
                # reverse 함수 : 뷰 함수에서 URL을 하드코딩 하지 않도록 하기 위함    
                # ( 제어를 전달하기 원하는 뷰의 이름과 URL패턴의 변수 부분을 조합하여 해당 뷰를 가리킴 ) 
        ```
      
      reverse('polls:results', args=(question.id,)) 을 호출하게 되면  
      urlpatterns에서 name이 results인 것을 찾게 됨    
         
      <img src="https://user-images.githubusercontent.com/52907116/104094375-ec3e1200-52d3-11eb-8a55-b77dc4359236.png" width="60%"></img>
         
      그리고 문자열 '/polls/3/results/' 를 반환함 ( 여기서 3은 question.id 의 값 )    
      그 후 이 리디렉션된 URL이 result 뷰를 호출하여 최종 페이지를 표시함   
            
  <br> 

    + 최종 페이지 수정
      > polls/views.py ( 전에 했던 detail 뷰와 내용 같음 ) 
        ```Python
        from django.shortcuts import get_object_or_404, render

        def results(request, question_id):
            question = get_object_or_404(Question, pk=question_id) # question_id에 해당하는 Question 
            return render(request, 'polls/results.html', {'question': question}) # results.html 렌더링
        ```
        
  <br> 

    + results.html 템플릿 작성
      > polls/templates/polls/results.html
        ```Html
        <h1>{{ question.question_text }}</h1>

        <ul>
        {% for choice in question.choice_set.all %}
            <li>{{ choice.choice_text }} -- {{ choice.votes }} vote{{ choice.votes|pluralize }}</li>
        {% endfor %}
        </ul>

        <a href="{% url 'polls:detail' question.id %}">Vote again?</a>
        ```
    결과화면    
    <img src="https://user-images.githubusercontent.com/52907116/104094378-ed6f3f00-52d3-11eb-81e9-efa382647d12.png" width="25%"></img>

  <br> 

+ ### 제네릭 뷰 사용하기 : 코드가 적을수록 좋음 
  + 뷰 : URL에서 전달된 매개 변수에 따라 DB 데이터 가져오기, 템플릿을 로드하고 렌더링 된 템플릿을 반환하기 등  기본 웹 개발의 일반적인 경우 나타냄    
    -> Django는 이런 매우 일반적인 경우를 위해 Generic View 라는 지름길을 제공함
    
  <br> 

  + 순서
    + URLconf 변환
    + 불필요한 예전 뷰 삭제
    + Django의 제네릭뷰에 기반한 새로운 뷰 도입
 
  <br> 

  + ### URLconf 수정 ( 
    > polls/urls.py
      ```Python
      from django.urls import path

      from . import views

      app_name = 'polls'
      urlpatterns = [
          path('', views.IndexView.as_view(), name='index'),
          path('<int:pk>/', views.DetailView.as_view(), name='detail'),
          path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
          path('<int:question_id>/vote/', views.vote, name='vote'),
      ]
      ```
      
  <br> 

  + ### 뷰 수정
    + index, detail, results 뷰 수정
      > polls/views.py
      ```Python
      from django.http import HttpResponseRedirect
      from django.shortcuts import get_object_or_404, render
      from django.urls import reverse
      from django.views import generic

      from .models import Choice, Question


      class IndexView(generic.ListView):  # ListView로 수정 
          template_name = 'polls/index.html' # 오버라이딩
          context_object_name = 'latest_question_list' # 오버라이딩

          def get_queryset(self): # 템플릿으로 넘겨줄 모델을 반환해주는 함수 
              """Return the last five published questions."""
              return Question.objects.order_by('-pub_date')[:5]


      class DetailView(generic.DetailView):
          model = Question # 오버라이딩
          template_name = 'polls/detail.html' # 오버라이딩


      class ResultsView(generic.DetailView):
          model = Question # 오버라이딩 
          template_name = 'polls/results.html' # 오버라이딩 


      def vote(request, question_id):
          ... # same as above, no changes needed.
      ```
  
    결과화면    
    <img src="https://user-images.githubusercontent.com/52907116/104094379-ee07d580-52d3-11eb-965d-22cd6d9fccb7.png" width="25%"></img>
  
### 참고
###### [Django - Writing your first Django app, part 4](https://docs.djangoproject.com/en/3.1/intro/tutorial04/)
###### [eungding - [Django] 튜토리얼 part 4 (1) - QueryDict](https://eunjin3786.tistory.com/131?category=843118)
###### [eungding - [Django] 튜토리얼 part 4 (2) - QueryDict](https://eunjin3786.tistory.com/132?category=843118)

<br>

---------------------------

<br>

## Django 앱 작성 5부
  + ### 자동 테스트 도입
    + 자동 테스트란?
      + 코드 작동을 확인하는 루틴
      + 셸을 이용하여 메서드 동작을 검사하거나 응용 프로그램을 실행하고 데이터를 입력하여 작동 방식 확인    
        ( 앱 작성 2부에서 다뤄본 것 )
      + 앱 작성 2부에서는 테스트가 사용자에 의하여 수행, 자동 테스트는 시스템에 의하여 수행
      
    <br>
    
    + 테스트를 생성하는 이유
      + 시간 절약이 가능함   
        + 작동하는 것처럼 보이는지 점검 
        + 문제의 원인이 무엇인지 확인하는 것에 빠름
      + 문제를 사전에 방지할 수 있음   
        + app의 목적이나 의도된 동작이 불투명할 수 있기 때문
      + 코드를 더욱 보기좋게 만듦
        + acob Kaplan-Moss 曰 "테스트가 없는 코드는 디자인에 의해 깨진다" 
      + 팀 간의 협업 지원 가능 
        + 동료가 실수로 코드를 깨지 않게끔 하기 위함
      
    <br>
    
  + ### 기본 테스트 전략
    + 테스트 기반 개발   
      -> 코드를 작성하기전에 테스트 작성 
    + 이미 작성된 코드에서 테스팅을 한다면   
      -> 새 기능을 추가하거나 버그를 수정할 때 테스트 작성
    
    <br>
  
  + ### 테스트 작성
    + #### 버그 식별하기
      + 현재 app에서 고쳐야 할 버그 : Question.was_published_recently() 메서드   
        ( pub_date가 미래일 경우에도 True를 반환함 )    
          -> shell을 통하여 확인하도록 함 
      > python manage.py shell 
      ```Python
      import datetime
      from django.utils import timezone
      from polls.models import Question
      # create a Question instance with pub_date 30 days in the future
      future_question = Question(pub_date=timezone.now() + datetime.timedelta(days=30))
      # was it published recently?
      future_question.was_published_recently()
    ```
      
      <img src="https://user-images.githubusercontent.com/52907116/104127548-08aa7f00-53a6-11eb-95c0-594d9d8991aa.png" width="50%"></img>   
      시간이 최근이 아님에도 불구하고, True를 반환하는 것을 확인 가능 
    
    <br>
   
    + #### 버그 검출을 위한 테스트
      + 방금 위에서 식별한 버그를 자동 테스트로 전환
      > polls/tests.py  ( 앱을 테스트 하기 위한 일반적인 장소 ) 
      ```Python
      import datetime

      from django.test import TestCase
      from django.utils import timezone

      from .models import Question


      # django.test.TestCase 의 하위 클래스로 작성
      class QuestionModelTests(TestCase):

          def test_was_published_recently_with_future_question(self):
              """
              was_published_recently() returns False for questions whose pub_date
              is in the future.
              """
              time = timezone.now() + datetime.timedelta(days=30)
              future_question = Question(pub_date=time)
              self.assertIs(future_question.was_published_recently(), False)
      ```
    
    <br>
    
    + #### 테스트 실행
      + 테스트를 위해 cmd 입력
      > python manage.py test polls   
      <img src="https://user-images.githubusercontent.com/52907116/104127549-09431580-53a6-11eb-8356-2e465b722dfd.png" width="80%"></img>             
      asserIs() 메서드를 사용하여, False가 반환되기를 원함에도 불구하고   
      was_published_recently()가 True를 반환다는 메세지 확인   
      ( 어디서 버그를 확인했는지 line까지 알려줌 ) 
    
    <br>
    
    + #### 버그 fix
      + was_published_recently()함수 수정
      > polls/models.py
      ```Python
      def was_published_recently(self):
      now = timezone.now()
      return now - datetime.timedelta(days=1) <= self.pub_date <= now
      ```   
      
      + 다시 테스트 해보기
      > python mange.py test polls
      <img src="https://user-images.githubusercontent.com/52907116/104127550-09dbac00-53a6-11eb-8b0a-58f5a1ed47a3.png" width="40%"></img>   

      버그를 확인한 후 , 버그를 노출시키는 테스트를 작성했고,    
      코드로 들어가 버그를 수정하여 테스트를 통과함   

    <br>
    
    + #### 더욱 포괄적인 테스트 
      + 메서드의 동작을 보다 포괄적으로 테스트하기 위해 같은 클래스에 함수 2개 추가
      > polls/tests.py
      ```Python
      def test_was_published_recently_with_old_question(self):
          """
          was_published_recently() returns False for questions whose pub_date
          is older than 1 day.
          """
          time = timezone.now() - datetime.timedelta(days=1, seconds=1)
          old_question = Question(pub_date=time)
          self.assertIs(old_question.was_published_recently(), False)

      def test_was_published_recently_with_recent_question(self):
          """
          was_published_recently() returns True for questions whose pub_date
          is within the last day.
          """
          time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
          recent_question = Question(pub_date=time)
          self.assertIs(recent_question.was_published_recently(), True)
      ```

      과거, 현재, 미래 총 3가지로 구분하여 테스트를 포괄적으로 할 수 있음  

  <br>
  
  + ### 뷰 테스트
    + 만약 Question의 pub_date가 미래로 설정되어있다고 가정했을 때     
      시간이 지나 그 미래가 된다면 해당 질문이 보여야 하지만  
      미래가 아니라면 그 전 까지 질문이 보이지 않아야 함 
    + 현재 polls 앱은 pub_date 필드가 미래인 질문까지도 포함하여 게시함 
  
    <br>

    + #### Django 테스트 클라이언트
      + 뷰 레벨에서 코드와 상호작용하는 유저를 simulate 하기 위해 테스트 클라이언트 제공
        ( test.py 혹은 shell에서 사용 가능함 ) 
      + shell 부터 확인
      > python manage.py shell 
      ```Python

      from django.test.utils import setup_test_environment
      setup_test_environment()
      '''
       setup_test_environment()를 사용하여 템플릿 렌더러를 설치
       이 메서드는 테스트 데이터베이스를 셋업하지 않음 ( setup_databases 메서드를 따로 불러줘야함 )
      '''

      from django.test import Client
      # create an instance of the client for our use
      client = Client()
      '''
      테스트 클라이언트 import
      ( 나중에 tests.py에서는 django.test.TestCase 클래스에 같이 딸려오는 클라이언트를 사용할 것임 ) 
      환경 설정 끝 
      '''

      # get a response from '/'
      response = client.get('/')
      # Out -> Not Found: /
      # we should expect a 404 from that address; if you instead see an
      # "Invalid HTTP_HOST header" error and a 400 response, you probably
      # omitted the setup_test_environment() call described earlier.
      response.status_code
      # Out -> 404
      # on the other hand we should expect to find something at '/polls/'
      # we'll use 'reverse()' rather than a hardcoded URL
      from django.urls import reverse
      response = client.get(reverse('polls:index'))
      response.status_code
      # Out -> 200
      response.content
      # Out -> b'\n    <ul>\n    \n        <li><a href="/polls/1/">What&#x27;s up?</a></li>\n    \n    </ul>\n\n'
      response.context['latest_question_list']
      # Out -> <QuerySet [<Question: What's up?>]>
      ```
    <br>
    
    + #### 뷰 개선 
      + 현재 polls 목록은 아직 게시되지 않은 polls들(미래에 게시되어야 할)을 보여줌 ( 개선 )
      > polls.views.py
      ```Python
      from django.utils import timezone

      def get_queryset(self):
          """
          Return the last five published questions (not including those set to be
          published in the future).
          """
          return Question.objects.filter(
              pub_date__lte=timezone.now() # 현재 이하인 것으로 필터링
          ).order_by('-pub_date')[:5]
      ```
      
    + #### 새로운 뷰 테스트
      + runserver 실행, site 로드, 과거와 미래에 대한 질문들 등    
        이에 대한 영향을 미치는 변경 작업을 매번 수행할 필요 X   
        -> shell 기반으로 테스트 생성 
      + 질문을 생성하는 함수 및 테스트 케이스들 추가 
      > polls/tests.py
      ```Python
      from django.urls import reverse

      def create_question(question_text, days):
          """
          Create a question with the given `question_text` and published the
          given number of `days` offset to now (negative for questions published
          in the past, positive for questions that have yet to be published).
          """
          time = timezone.now() + datetime.timedelta(days=days)
          return Question.objects.create(question_text=question_text, pub_date=time)


      class QuestionIndexViewTests(TestCase):
          # 최근 질문 리스트가 비어있는지 확인 
          def test_no_questions(self):
              """
              If no questions exist, an appropriate message is displayed.
              """
              response = self.client.get(reverse('polls:index'))
              self.assertEqual(response.status_code, 200)
              self.assertContains(response, "No polls are available.")
              self.assertQuerysetEqual(response.context['latest_question_list'], [])

          # 질문이 생성되어 목록에 나타나는지 확인
          def test_past_question(self):
              """
              Questions with a pub_date in the past are displayed on the
              index page.
              """
              create_question(question_text="Past question.", days=-30)
              response = self.client.get(reverse('polls:index'))
              self.assertQuerysetEqual(
                  response.context['latest_question_list'],
                  ['<Question: Past question.>']
              )

          # 미래 pub_date로 질문 작성
          def test_future_question(self):
              """
              Questions with a pub_date in the future aren't displayed on
              the index page.
              """
              create_question(question_text="Future question.", days=30)
              response = self.client.get(reverse('polls:index'))
              self.assertContains(response, "No polls are available.")
              self.assertQuerysetEqual(response.context['latest_question_list'], [])

          def test_future_question_and_past_question(self):
              """
              Even if both past and future questions exist, only past questions
              are displayed.
              """
              create_question(question_text="Past question.", days=-30)
              create_question(question_text="Future question.", days=30)
              response = self.client.get(reverse('polls:index'))
              self.assertQuerysetEqual(
                  response.context['latest_question_list'],
                  ['<Question: Past question.>']
              )

          def test_two_past_questions(self):
              """
              The questions index page may display multiple questions.
              """
              create_question(question_text="Past question 1.", days=-30)
              create_question(question_text="Past question 2.", days=-5)
              response = self.client.get(reverse('polls:index'))
              self.assertQuerysetEqual(
                  response.context['latest_question_list'],
                  ['<Question: Past question 2.>', '<Question: Past question 1.>']
              )
      ```
      <img src="https://user-images.githubusercontent.com/52907116/104127551-09dbac00-53a6-11eb-8f37-b18f0d19afed.png" width="40%"></img>    
      python manage.py test polls 실행시 8개의 테스트가 성공된 것을 볼 수 있음
    
    <br> 
    
    + #### Detail뷰 테스트
      + 미래의 설문들은 리스트에 나타나지 않음   
        but, 사용자가 URL을 알고 있거나 추측하면 접근할 수 있음  
      + Detail뷰에 제약 조건 추가
      > polls/views.py
      ```python
      class DetailView(generic.DetailView):
          ...
          def get_queryset(self): # get_queryset 오버라이딩 
              """
              Excludes any questions that aren't published yet.
              """
              return Question.objects.filter(pub_date__lte=timezone.now())
      ```
      + 테스트 추가 ( pub_date가 과거인 질문이 표시될 수 있는지, 미래인 질문은 표시될 수 없는지 )  
      > polls/tests.py
      ```Python
      class QuestionDetailViewTests(TestCase):
          def test_future_question(self):
              """
              The detail view of a question with a pub_date in the future
              returns a 404 not found.
              """
              future_question = create_question(question_text='Future question.', days=5) # 기준 : + 5일
              url = reverse('polls:detail', args=(future_question.id,))
              response = self.client.get(url)
              self.assertEqual(response.status_code, 404)

          def test_past_question(self):
              """
              The detail view of a question with a pub_date in the past
              displays the question's text.
              """
              past_question = create_question(question_text='Past Question.', days=-5) # 기준 : - 5일
              url = reverse('polls:detail', args=(past_question.id,))
              response = self.client.get(url)
              self.assertContains(response, past_question.question_text)
      ```
    <img src="https://user-images.githubusercontent.com/52907116/104127547-0811e880-53a6-11eb-8055-e83439cdd8a6.png" width="40%"></img>     
    python manage.py test polls 실행시 10개의 테스트가 성공된 것을 볼 수 있음
    
    + #### 다른 테스트에 대한 아이디어
      + get_queryset 메서드를 Results뷰에 추가, 뷰에 대한 새로운 테스트 만들기   
        ( 지금까지 한 것과 유사 )
      + 테스트를 추가하며 다양한 방법으로 app 개선 가능   
        ( 선택 항목이 없는 사이트에 질문 게시 같은 버그 )
      + 로그인된 관리자는 게시되지 않은 질문을 볼 수 있지만 일반 방문자는 볼 수 없어야 함
   
  <br>
  
  + ### 테스트를 많이 할수록 좋음
    + app보다 테스트 코드가 더 많이 나올지라도 계속하여 작성하기
    + 코드 수정시 -> 기존의 많은 테스트 실패 -> 어떤 테스트를 수정해야 하는지 정확하게 알려줌
    + 테스트가 중복되는 것 : 상관없음 ( 오히려 좋음 ) 
    + 경험에서 나온 바로는 다음을 포괄함
      + 각 모델 혹은 뷰에 대한 독립된 테스트 클래스
      + 테스트 할 각 조건 집합에 대해 독립된 테스트 방법
      + 그 기능을 설명하는 테스트 메서드 이름 
  
  <br>
  
  + ### 추가 테스트
    + 이번 테스트에서는 모델의 내부 논리와 뷰로 정보를 게시하는 방법에 대하여 배움
    + 해당 페이지에서 다루지 않지만 Selenium과 같은 브라우저 내 프레임워크를 사용하여 HTML이 실제로 브라우저에서 렌더링되는 방식도 테스트 가능   
      ( Django 코드의 동작뿐만 아니라, JavaScript의 동작 또한 확인 가능함 ) 
    + 자동으로 테스트를 실행하여 품질 관리가 부분적으로 자동화될수록 할 수 있음
  
  <br> 

### 참고
###### [Django - Writing your first Django app, part 5](https://docs.djangoproject.com/en/3.1/intro/tutorial05/)
###### [eungding - [Django] 튜토리얼 part 5 (1) - 테스트 작성하기](https://eunjin3786.tistory.com/135?category=843118)
###### [eungding - [Django] 튜토리얼 part 5 (2) - 뷰 테스트 작성하기](https://eunjin3786.tistory.com/139?category=843118)

<br>

----------------------

<br>

## Django 앱 작성, 6부
+ 6부 개요 
  + 스타일 시트와 이미지를 추가할 예정
  + 서버에 의해 생성된 HTML 외에도, 웹 애플리케이션은 일반적으로 완전한 웹 페이지를 렌더링 하는데 필요한   
    이미지, javaScript, CSS 들과 같은 추가 파일을 제공해야 함. Django에서는 이러한 파일을 "static files" 라고 함
  + 대규모 프로젝트의 경우 각 app에서 제공하는 정적 파일 세트를 처리하는 작업이 까다로움
  + django.contrib.staticfiles : 위의 문제를 해결하기 위해 만든 것으로, 각 app에서 정적 파일을 단일 위치(프로덕션에서 쉽게 제공할 수 있는)로 수집함
  
<br>  

+ ### 앱의 모양과 느낌을 커스터마이징
  + polls 폴더에 static 폴더 생성
    
<br>  

  + Django의 STATICFILES_FINDERS 설정 
    + 다양한 자원으로부터 정적 파일들을 어떻게 발견하는지에 대한 검색기 목록이 있음
    + 기본값 중 하나는 AppDirectoriesFinder로 INSTALLED_APPS 각각에서 "static" 하위 폴더를 찾음
    + 관리 사이트는 구조적으로 정적 파일에 대해 같은 폴더 구조를 이용함
    
<br>  

  + 방금 만든 static 폴더에 polls라는 폴더를 생성하고 그 안에 style.css 파일을 작성함   
    ( polls/static/polls/style.css )   
    ( AppDirectoriesFinder라는 정적파일 탐색기의 작동방식 때문 - 전에 템플릿 경로를 만든것과 유사함 )
    
<br>  

  + Static file namespacing
    + 템플릿과 마찬가지로 정적 파일을 다른 polls 하위 폴더안에 넣지 않고 직접 polls/static 위치에 놓는 것은 좋지 않음   
     ( 다른 응용 프로그램에 동일한 이름의 정적 파일이 있는 경우 그 파일을 구별할 수 없기 때문 ) 
    
<br>  

  + 스타일 시트 작성하기
    > polls/static/polls/style.css
    ```Html
    li a {
        color: green;
    }
    ```
    
<br>  

  + 인덱스 페이지에 스타일 적용하기
    > polls/templates/polls/index.html
    ```Html
    {% load static %}
    <!-- {% static %} : 이 템플릿 태그는 정적 파일의 URL에 대한 절대 경로를 생성함 --> 

    <link rel="stylesheet" type="text/css" href="{% static 'polls/style.css' %}">
    
    ```
    
<br>  

  + 적용되었는지 확인
    > python manage.py runserver    
    <img src="https://user-images.githubusercontent.com/52907116/104193897-f2fb8f00-5463-11eb-9248-eefc34454eb6.png" width="30%"></img>
 
<br> 

+ ### 배경 이미지 추가
  + 이미지를 위한 하위 폴더만들고 그 안에 background라는 이름을 가진 gif파일 넣기 
   ( polls/static/polls/images/background.gif )
  
<br> 

  + 적용되었는지 확인
    > python manage.py runserver    
    <img src="https://user-images.githubusercontent.com/52907116/104193900-f42cbc00-5463-11eb-96f5-4989339a275e.png" width="30%"></img>
    
<br>  

  + 스타일시트처럼 Django에서 만들지 않은 정적 파일에는 {% static %} 템플릿 태그를 이용할 수 없음   
    ( 정적 파일 간의 연결에는 항상 상대 경로를 사용해야 함 )

### 참고
###### [Django - Writing your first Django app, part 6](https://docs.djangoproject.com/en/3.1/intro/tutorial06/)

  
<br>  

---------------------

<br>

## Django 앱 작성, 7부
+ ### 7부개요
  + Django에서 자동으로 생성되는 관리 사이트(2부에서 살펴봄)를 커스터마이징 하는 것에 초점을 맞춤

<br>

+ ### 관리자 폼 커스터마이징
  + 2부에서 보면 admin.site.register(Question)으로 질문 모델을 등록함으로써 기본 양식을 표현했음    
    여기서, 커스터마이징을 원한다면 객체를 등록할 때 Django에게 원하는 옵션을 말하도록 함
  + 편집 폼의 필드 재정렬
  > polls/admin.py
  ```Python
  from django.contrib import admin

  from .models import Question


  # QuestionAdmin 이라는 클래스를 만든 후 이것을 admin.site.register의 두번째 인자에 집어넣음
  class QuestionAdmin(admin.ModelAdmin): 
      fields = ['pub_date', 'question_text'] # '출판 날짜'가 '질문' 필드보다 우선시 하도록 함

  admin.site.register(Question, QuestionAdmin)
  ```
  <img src="https://user-images.githubusercontent.com/52907116/104461995-6089f580-55f3-11eb-8858-a1e15e79dd36.png" width="70%"></img>    
  '출판 날짜'가 '질문' 필드보다 앞서 있는 모습 
  
  <br>
  
  + 수십 개의 필드가 있는 양식을 다음과 같이 필드 세트로 나눌 수 있음
  > polls/admin.py
  ```Python
  from django.contrib import admin

  from .models import Question


  class QuestionAdmin(admin.ModelAdmin):
      fieldsets = [
          (None,               {'fields': ['question_text']}),
          ('Date information', {'fields': ['pub_date']}),
      ]

  admin.site.register(Question, QuestionAdmin)
  ```
  <img src="https://user-images.githubusercontent.com/52907116/104462003-61bb2280-55f3-11eb-86f8-3e1951819c03.png" width="70%"></img>    
  '질문' 필드가 '출판 날짜' 필드보다 앞서 있고 '출판 날짜' 필드에 제목이 추가된 모습  
  
  <br>
  
+ ### 관련 객체 추가
  + 현재 질문에는 여러가지 선택 항목이 존재하지만, 질문 관리자 페이지에는 선택 항목이 표시되지 않음
  + 첫 번째 solution : 선택 항목을 관리자에 등록
  > polls/admin.py
  ```Python
  from django.contrib import admin

  from .models import Choice, Question
  # ...
  admin.site.register(Choice)
  ```
  <img src="https://user-images.githubusercontent.com/52907116/104462007-6253b900-55f3-11eb-83a5-f581e63eb47b.png" width="70%"></img>      
  왼쪽 POLLS 인덱스에 Choices가 추가되고 해당 부분에 들어가면 선택 항목을 볼 수 있음   
  우측 상단에는 'ADD CHOICE +' 라는 메뉴도 볼 수 있음   
  
  <br>
  
  <img src="https://user-images.githubusercontent.com/52907116/104462011-62ec4f80-55f3-11eb-94f7-e61d6343b0d8.png" width="50%"></img>   
  선택항목 추가 화면   
  
  <br>
  
  + 첫 번째 solution에 대한 고찰 
    + 위에 있는 Add choice 화면에서 "Question" 필드는 DB의 모든 질문이 들어가 있는 선택 상자임   
      ( Django는 이 외래키가 선택 상자로써 관리자에 표시되어야 한다는 것을 알고 있음 )
    
  <br> 
  
    + <img src="https://user-images.githubusercontent.com/52907116/104462014-6384e600-55f3-11eb-93a9-0d9f89f88ddb.jpg" width="50%"></img>   
      "Question" 옆에 있는 "Add another"(플러스 모양)을 누르면 팝업 창이 나옴   
      
      <br>
      
      <img src="https://user-images.githubusercontent.com/52907116/104462020-641d7c80-55f3-11eb-8fed-3f8673342024.png" width="50%"></img>      
      해당 창에서 질문을 추가하고 "Save" 버튼을 누르면 Django가 질문을 DB에 저장하고 현재 보고 있는   
      "Add choice"폼에서 선택한 항목을 동적으로 추가함  
    
  <br> 
  
    + 그러나 실제로 시스템에 Choice 객체를 추가하는것은 효율적이지 않음   
      -> 두 번째 방법에서는 질문 객체를 만들 때 수 많은 선택 항목을 직접 추가해보도록 함 
  
  <br> 
  
  + 두 번째 solution 
    > Choice 모델에 대한 register() 호출 제거 후, 코드 편집
    ```Python
    from django.contrib import admin

    from .models import Choice, Question


    class ChoiceInline(admin.StackedInline):
        model = Choice
        extra = 3 # default 선택 개수를 3개로 정의함


    class QuestionAdmin(admin.ModelAdmin):
        fieldsets = [
            (None,               {'fields': ['question_text']}),
            ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        ]
        inlines = [ChoiceInline] # Choice 객체는 질문 관리 페이지에서 편집되도록 함 

    admin.site.register(Question, QuestionAdmin)
    ```
    <img src="https://user-images.githubusercontent.com/52907116/104462021-64b61300-55f3-11eb-85fd-7490cf4e7cc8.png" width="70%"></img>     
    위 화면에는 선택지와 관련하여 3개의 항목이 존재하며, 이미 생성된 객체의"Change" 버튼으로 들어갈 때마다 세 개의 슬롯이 추가됨   
    "Add another Choice"를 클릭하면 새 슬롯이 추가되며 삭제도 오른쪽 상단의 X 로 가능함
   
   <br>
   
    + 두 번째 solution에 대한 고찰
      + 위 이미지에서도 보다시피 모든 필드를 표시하는데 많은 화면이 필요함   
        따라서 Django는 이에 대해 표 형식의 방법을 제공함
      >polls/admin.py
      ```Python
      class ChoiceInline(admin.TabularInline):
          #...
      ```   
      <img src="https://user-images.githubusercontent.com/52907116/104462022-64b61300-55f3-11eb-9825-459e6bea9c1c.png" width="70%"></img>    
      조금 더 compact하게 정리된 테이블 기반 형식을 볼 수 있음   
      ( "DELETE?" 라는 문구로 삭제 열도 따로 추가되어 있음 )
        
<br>

+ ### 관리자 변경 목록 커스터마이징
  + 시스템의 모든 질문을 표시하는 "Change list"를 수정할 예정   
  <img src="https://user-images.githubusercontent.com/52907116/104462024-654ea980-55f3-11eb-81b4-f3bdcf57f00a.png" width="70%"></img>  
  
  <br>
  
  + 기본적으로 Django는 각 객체의 str()을 보여줌 -> 개별 필드를 보여줄 수 있다면 더 도움이 될 것     
    -> list_display admin 옵션 사용  
    > polls/admin.py
    ```Python
    class QuestionAdmin(admin.ModelAdmin):
        # ...
        list_display = ('question_text', 'pub_date','was_published_recently')
    ```
    <img src="https://user-images.githubusercontent.com/52907116/104462027-65e74000-55f3-11eb-8fb1-2f5891ec7812.png" width="70%"></img>  
    열의 헤더를 클릭함으로써 정렬을 할 수 있음   
    하지만 맨 오른쪽 was_published_recently는 임의의 메서드에 의한 출력으로 정렬이 지원되지 않음   
      -> 이를 해결하기 위한 방법은 아래와 같음 
  
  <br>
  
  + 몇가지 속성을 메서드에 추가하여 기능 개선하기
  <img src="https://user-images.githubusercontent.com/52907116/104462029-667fd680-55f3-11eb-8e6a-e478565c4ac6.png" width="90%"></img>     
    
    <br>
    
    > polls/models.py ( 정렬 및 목록 커스터마이징 (1) )
    ```Python
    class Question(models.Model):
        # ...
        def was_published_recently(self):
            now = timezone.now()
            return now - datetime.timedelta(days=1) <= self.pub_date <= now
        was_published_recently.admin_order_field = 'pub_date' # 정렬 문제
        was_published_recently.boolean = True # True, False 문자열을 띄우지 않고 아이콘을 띄우게 해줌 
        was_published_recently.short_description = 'Published recently?' # 헤더 이름 바꾸기
    ```
    
    <br>
  
    > polls/admin.py ( 필터 추가 (2) )
    ```Python
    class QuestionAdmin(admin.ModelAdmin):
        # ...
        list_filter = ['pub_date']
    ```
    
    <br>
    
    > polls/admin.py ( 검색창 추가 (3) )
    ```Python
    class QuestionAdmin(admin.ModelAdmin):
        # ...
        search_fields = ['question_text']
    ```
    검색의 경우, background에서 쿼리문으로 like를 사용함   
    따라서 검색하는 글자 수를 줄이면 더 빠른 탐색이 가능함   
     
    <br>

+ ### 관리자 모양 및 느낌 커스터마이징
  + 각 관리 페이지 상단에 "Django administration" 문구 지우기   
  
  <br>
  
  + #### 프로젝트 템플릿 커스터마이징
    + manage.py가 포함되어 있는 프로젝트 폴더에 "templates"라는 폴더를 생성
    + DIRS 옵션 추가
     > mysite/settings.py
     ```Python
     TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [BASE_DIR / 'templates'],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]
     ```
     <img src="https://user-images.githubusercontent.com/52907116/104462030-667fd680-55f3-11eb-819c-facfc7d0c0e1.png" width="70%"></img> 
     
    <br>
    
    + 템플릿 구성      
      static 파일들처럼, 모든 템플릿을 하나의 대형 템플릿 폴더에 모을 수 있음  
      하지만 특정 응용 프로그램에 속하는 템플릿은 polls/templates 같은 폴더가 아닌   
      프로젝트의 템플릿 폴더에 배치해야 함 (위처럼)
      이에 대한 이유는 재사용가능한 앱 튜토리얼에서 다루어보도록 함 ( 향후 업로드 예정 ) 
    
    <br>
    
    + DIRS : Django 템플릿을 로드할 때 확인할 파일 시스템 디렉토리의 리스트 ( 검색 경로 )
    + templates 폴더 안에 admin 폴더를 생성  
      django/contrib/admin/templates/admin/base_site.html 파일을 admin 폴더에 복사
      > Django 경로를 모른다면 cmd에 다음과 같이 입력  
        
          $ python -c "import django; print(django.__path__)"
    
    <br>
    
    + 템플릿 수정
      > 복사된 base_site.html 수정
      ``` Html
      <!--#''' -->
      {% block branding %}
      <h1 id="site-name"><a href="{% url 'admin:index' %}">Polls Administration</a></h1>
      {% endblock %}
      <!--#''' -->
      ```
      <img src="https://user-images.githubusercontent.com/52907116/104462034-67186d00-55f3-11eb-9d98-403ee2512639.png" width="30%"></img>  
      
      <br>
    
    + 지금까지 템플릿을 어떻게 오버라이드 하는지 배웠고 나중에 실제 프로젝트를 수행한다면  
      "django.contrib.admin.AdminSite.site_header" 를 커스터마이징 할 때 사용하게 될 것임
    + 템플릿 파일에 있는 {% block branding %} and {{ title }} 중 {% 기호나 {{는 Django 템플릿 언어임
    + Django의 기본 관리 템플릿은 모두 오버라이드 될 수 있음 ( base_site.html을 복사한 것 처럼 하면 됨 )
    
    <br>
  
  + #### 응용 프로그램의 템플릿 커스터마이징
    + DIRS가 기본적으로 비어있다면, Django는 어떻게 기본 관리 템플릿을 찾는가?
      -> APP_DIRS가 True로 설정되어 있기 때문에 Django는 자동으로   
        각 애플리케이션 패키지 내에서 fallback으로 사용 할 templates/하위 폴더를 찾게 됨
    + 애플리케이션이 좀 더 복잡해지고 정교한 수정이 필요한 경우   
      프로젝트의 템플릿보다 애플리케이션의 템플릿을 수정하는 것이 더 현명함
  
  <br>
  
+ ### 관리자 인덱스 페이지 커스터마이징
  + 기본적으로 INSTALLED_APPS에서 모든 app들이 보이게 됨
  + index는 관리자 페이지에서 가장 중요한 페이지임
  + 파일을 편집하면, app_list라는 템플릿 변수를 볼 것이고   
    이 변수에는 설치된 모든 Django 앱이 들어가 있음

  <br>

### 참고
###### [Django - Writing your first Django app, part 7](https://docs.djangoproject.com/en/3.1/intro/tutorial07/)

<br>

------------------------

<br>

## 재사용 가능한 앱 제작  
  + Advanced tutorial 개요   
    여론조사 웹 애플리케이션을 독립형 파이썬 패키지로 전환할 예정  
    ( 새로운 프로젝트에서 재사용하고 다른 사람과 공유할 수 있도록 )  

  <br> 

  + ### 재사용가능성 문제
    + 웹 애플리케이션을 설계, 구축, 테스트 및 유지 관리하는 일에는 많은 작업량이 들어감
    + PyPI(Python Package Index)에는 Python 프로그램에서 사용할 수 있는 다양한 패키지가 포함되어 있음   
      ( Django 그 자체도 Python 패키지임 - 따라서 기존 Python 패키지 또는 Django 앱을 가져와서 자신의 웹 프로젝트로 구성할 수 있음 )
    + 앱을 재사용하는 방법   
      이미 part 1에서 배웠음 ( include를 사용하여 프로젝트 레벨 URLconf로부터 polls 분리시키기 ) 
    + 이번 장에서는 새 프로젝트에서 앱을 쉽게 사용할 수 있도록 하고 
      다른 사용자가 설치 및 사용할 수 있도록 추가 단계를 수행할 것임

  <br>

  + ### 프로젝트 및 재사용 가능한 앱
    + 이번 장에 대하여 공부하기 앞서, 프로젝트 폴더 상황은 다음과 같음
    > 디렉토리 구조
    
        mysite/
            manage.py
            mysite/
                __init__.py
                settings.py
                urls.py
                asgi.py
                wsgi.py
            polls/
                __init__.py
                admin.py
                apps.py
                migrations/
                    __init__.py
                    0001_initial.py
                models.py
                static/
                    polls/
                        images/
                            background.gif
                        style.css
                templates/
                    polls/
                        detail.html
                        index.html
                        results.html
                tests.py
                urls.py
                views.py
            templates/
                admin/
                    base_site.html
    
    + 템플릿을 따로 두 개 만든 이유 ( mysite/templates 그리고 polls/templates )    
      -> polls 폴더 안에 있는 애플리케이션 - 자체적으로 포함되고 새로운 프로젝트에 쉽게 참여 가능함  
      -> polls 폴더를 새 Django 프로젝트로 복사하여 즉시 재사용 가능함  
      ( 하지만 아직 다른 사람이 쉽게 설치할 수 없음 -> 앱을 패키징 해야함 )  
  
  <br>
  
  + ### 일부 필수 구성 요소 설치
    + 패키지를 만들기 위해 setuptools를 이용할 예정
    + 설치와 삭제를 위해 pip을 이용할 예정
  
  <br>
  
  + ### 앱 패
    + 파이썬 패키징 : 쉽게 설치되고 사용될 수 있게끔 특정한 형식으로 app을 준비하는 것 
    
    <br>
    
    + (1) polls의 상위 폴더인 곳에 "django-polls" 폴더 생성
      + 앱(패키지) 이름 고르기 
        + 기존 패키와 이름이 충돌하지 않도록 PyPI와 리소스 확인  
        + 배포할 패키지를 만들 때, 모듈 이름에 django- 를 쓰는것이 좋음  
      + 유의
        + 애플리케이션 레이블(경로의 마지막 부분)은 INSTALLED_APPs에서 고유해야 함   
          ( 'Django 패키지와 동일한 레이블은 피할 것 - auth', 'admin', 'messages' 등 ) 
    
    <br>
    
    + (2) polls 폴더를 "django-polls" 폴더로 옮기기
    
    <br>
    
    + (3) README.rst 파일 만들기
      > django-polls/README.rst
      ```Rst
      =====
      Polls
      =====

      Polls is a Django app to conduct Web-based polls. For each question,
      visitors can choose between a fixed number of answers.

      Detailed documentation is in the "docs" directory.

      Quick start
      -----------

      1. Add "polls" to your INSTALLED_APPS setting like this::

          INSTALLED_APPS = [
              ...
              'polls',
          ]

      2. Include the polls URLconf in your project urls.py like this::

          path('polls/', include('polls.urls')),

      3. Run ``python manage.py migrate`` to create the polls models.

      4. Start the development server and visit http://127.0.0.1:8000/admin/
         to create a poll (you'll need the Admin app enabled).

      5. Visit http://127.0.0.1:8000/polls/ to participate in the poll.
      ```
      
    <br>
    
    + (4) django-polls 폴더에 LICENSE 폴더 만들기 
      + 라이센스 없이 릴리즈된 코드는 유용하지 않음
      + Django 및 많은 Django 호환 앱은 BSD 라이센스에 따라 배포되지만,   
        임의로 라이센스를 자유롭게 선택할 수 있음 
      + 라이센스 선택은 그 해당 코드 사용하는 사용자에게 영향이 있음
    
    <br>
  
    + (5) setup.cfg, setup.py - 앱 빌드 및 설치 방법 제작
      > django-polls/setup.cfg¶
      ```Cfg
      [metadata]
      name = django-polls
      version = 0.1
      description = A Django app to conduct Web-based polls.
      long_description = file: README.rst
      url = https://www.example.com/
      author = Your Name
      author_email = yourname@example.com
      license = BSD-3-Clause  # Example license
      classifiers =
          Environment :: Web Environment
          Framework :: Django
          Framework :: Django :: X.Y  # Replace "X.Y" as appropriate
          Intended Audience :: Developers
          License :: OSI Approved :: BSD License
          Operating System :: OS Independent
          Programming Language :: Python
          Programming Language :: Python :: 3
          Programming Language :: Python :: 3 :: Only
          Programming Language :: Python :: 3.6
          Programming Language :: Python :: 3.7
          Programming Language :: Python :: 3.8
          Topic :: Internet :: WWW/HTTP
          Topic :: Internet :: WWW/HTTP :: Dynamic Content

      [options]
      include_package_data = true
      packages = find:
      ```
      
      <br>
      
      > django-polls/setup.py
      ```
      from setuptools import setup

      setup()
      ```
    
    <br>
    
    + (6) MANIFEST.in 파일 작성 
      ( 기본적으로 패키지에는 파이썬 모듈 및 패키지가 기본적으로 포함됨 )   
      ( 그 이외에 파일들을 추가적으로 포함하기 위해서는 MANIFEST 파일을 작성해야 함 )    
      > django-polls/MANIFEST.in
      ```In
      include LICENSE
      include README.rst
      recursive-include polls/static *
      recursive-include polls/templates *
      ```
    
    <br>
    
    + (7) 선택사항 - 자세한 설명서를 app에 포함시키기   
      7-1 ) django-polls 폴더에 docs 문서 작성 후 내용 쓰기  
      7-2) > django-polls/MANIFEST.in ( 한줄 추가 )  
      ```In
      recursive-include docs *
      ```   
    
    <br>
    
    + (8) 패키지 완성 
      > django-polls 폴더 하에서 명령어 입력
      
          python setup.py sdist
          
      명령어를 입력했다면 dist라는 폴더가 만들어 짐   
      해당 폴더 안에는 패키지인 django-polls-0.1.tar.gz 가 생성되어 있음  
      
    <br>
  
  + ### 나만의 패키지 사용하기
    + 현재 polls 폴더를 프로젝트에서 옮겼기 때문에 더이상 작동되지 않음   
      -> 앞서 만들었던 새로운 Django polls 패키지를 설치할 예정 
    
    <br>
    
    + 패키지 설치
    > 사용자 폴더에서 pip을 사용
      
        python -m pip install --user django-polls/dist/django-polls-0.1.tar.gz  
    
    <img src="https://user-images.githubusercontent.com/52907116/104740392-3e2ae000-578b-11eb-9749-8f9ad12824fc.png" width="80%"></img>
   
    <br>
    
    + 위 이미지처럼 성공했다면 서버 구동시 이전처럼 정상적으로 홈페이지가 동작하게 됨
    
    <br>
    
    + 패키지 삭제의 경우
    > 패키지 삭제를 위해서 마찬가지로 pip 사용
      
        python -m pip uninstall django-polls
    
  <br>
  
  + ### 앱 게시하기
    + PyPI(Python Package Index)와 같은 공용 저장소에 패키지를 업로드하는 등 공유 가능
  
  <br>
  
  
### 참고
###### [Django - Advanced tutorial: How to write reusable apps](https://docs.djangoproject.com/en/3.1/intro/reusable-apps/)



  


  
