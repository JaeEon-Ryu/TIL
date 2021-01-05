# About Django Framework    

+ INDEX
  + Django 앱 작성, 1부
  + Django 앱 작성, 2부

------------------------------- 

## Django 앱 작성, 1부
+ ### 개요
  + Python 기반 웹 프레임 워크
  + 웹 애플리케이션을 효율적이고 신속하게 만들 수 있음
  + 문서화, 확장성이 뛰어남
  + 데이터베이스 쉽게 전환 가능
  + 관리 인터페이스가 내장되어 사용이 편리함
  + 웹 스크래핑, 머신러닝, 이미지 프로세싱 등 방대한 라이브러리를 가진 파이썬 언어를 기반으로 함 
  
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

+ ### 장고 설치 ( 윈도우 기준 )
  + cmd 혹은 MINGW64 열기 
    > 알고 있어야 하는 명령어
    
        1. cd ( change directory ) 
          cd 폴더명 : 해당 폴더로 이동
          cd .. : 해당 폴더 전의 경로로 돌아감
        2. Ctrl + c 
          Ctrl + c : 명령 중지 ( 향후 cmd 상에서 장고 웹 실행 중지 시 필요 )  
        
    
  + pip 설치 
    > #### python -m pip install --user pip
      
      이미 설치가 된 경우 건너뛰기 가능  
      
  + 가상 환경 설치    
    > #### pip install virtualenv   
    
      가상 환경을 이용하는 이유 : 같은 도구를 여러 버전 설치해 둘 수 없다는 단점을 보완   
      
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
  + 장고 설치
    > #### pip install django   
 
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
        
  + 폴더 이동하기 ( cmd 에서 ) 
    > #### cd mysite
  + 실행하기
    > #### Python manage.py runserver
  + 웹 페이지 방문하기
    + http://localhost:8000/ 클릭    
      ( 우주선 모양이 나오면 성공 ) 

+ ### polls 앱 만들기
  + 장고 프로젝트는 하나 이상의 애플리케이션으로 구성   
    ( 앱은 웹서비스 중 하나의 기능 의미 ) 
    
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
       
  + 앱 ( polls ) 하위에 있는 views.py 파일 내용 작성
    > polls/view.py
      
        from django.http import HttpResponse

        def index(request):
            return HttpResponse("Hello, world. You're at the polls index.")
  
  + 앱 ( polls ) 하위에 urls.py 파일 생성 후 내용 작성
    > polls/urls.py
    
        from django.urls import path

        from . import views

        urlpatterns = [
            path('', views.index, name='index'),
        ]
        
  + 프로젝트 폴더(mysite)에 있는 urls.py 내용 작성
    > mysite/urls.py
        
        from django.urls import include, path

        urlpatterns = [
            path('polls/', include('polls.urls')),
            path('admin/', admin.site.urls),
        ]
        
  + 웹 페이지 접속
    + python manage.py runserver ( cmd 에서 입력 )
    + http://localhost:8000/polls/ ( 링크 이동 ) 
    + 모든 작업을 완료했으면 다음과 같은 화면이 나옴
  
        <img src="https://user-images.githubusercontent.com/52907116/103541158-51fa5a80-4ede-11eb-9307-9cce567f5ad8.png" width="25%"></img>
 
 
#### 참고 : https://www.geeksforgeeks.org/django-tutorial/, https://www.geeksforgeeks.org/django-basics/, https://docs.djangoproject.com/en/3.1/intro/tutorial01/ , https://velog.io/@jcinsh/Django-%ED%8A%9C%ED%86%A0%EB%A6%AC%EC%96%BC , https://velog.io/@vlvksbdof12/Python-Django-%EA%B8%B0%EC%B4%88-%EC%A0%9C-2%EA%B0%95 
  
  
------------------------

## Django 앱 작성, 2부

+ ### 데이터베이스 설정
  + 기본적으로 SQLite 사용 ( Python에 내장되어 있음 ) 
  > 다른 엔진 사용 가능 
  
      'django.db.backends.sqlite3'
      'django.db.backends.postgresql'
      'django.db.backends.mysql'
      'django.db.backends.oracle'
    
+ ### 모델 생성
  + Django에서의 Model : 데이터 서비스를 제공하는 계층
  + models.py 모듈 안에 하나 이상의 모델 클래스를 정의 가능   
    ( 하나의 모델 클래스는 데이터베이스에서 하나의 테이블에 해당 ) 
  + 모델이란?
    + 데이터베이스에 저장될 데이터를 클래스 형태로 구성한 것   
      ( 상속기능을 이용해 필요한 부분만 구현하도록 ) 
    + 데이터와 동작을 함께 정의 ( CRUD : 저장, 읽기, 수정, 삭제 ) 
  + polls 폴더 하위에 있는 models.py 파일에 내용 작성
    > polls/models.py
      
        from django.db import models

        class Question(models.Model): 
            question_text = models.CharField(max_length=200)  # 질문
            pub_date = models.DateTimeField('date published') # publish 시간


        class Choice(models.Model):
            question = models.ForeignKey(Question, on_delete=models.CASCADE)  # 질문 - 외래키, 삭제될 경우 연쇄삭제
            choice_text = models.CharField(max_length=200)  # 답변
            votes = models.IntegerField(default=0)  # 답변 횟수
            
    + Question, Choice 각각 class로 정의하며, django.db.models.Model를 상속받음 
  
  + 모델 생성시
    + 이 앱을 위한 Database schema 생성
    + Question, Choice 객체를 위한 파이썬 데이터베이스 액세스 API 생성
   
+ ### 모델 활성화    
  + polls 앱이 설치 되었음을 알리기
    > mysite / settings.py
    
        INSTALLED_APPS = [
            'polls.apps.PollsConfig',
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
        ]
  
  + > 모델 변경사항 저장하기 ( cmd 입력 )  
    
        python manage.py makemigrations polls
  
    + models.py에 만들어놓은 모델들은 바로 사용할 수 없음, makemigration 과정을 거쳐야 사용 가능
    + 모델 클래스를 생성하고 난 후, 해당 모델에 상응하는 테이블을 DB에서 생성 가능함
      + Migration : 파이썬 모델 클래스의 수정 및 생성을 DB에 적용하는 과정   
        ( 이는 장고가 기본적으로 제공하는 ORM - Object Relational Mapping 을 통해 진행 )
    
  + > SQL문 미리보기 ( cmd 입력 )
        
        python manage.py sqlmigrate polls 0001
  
    + sqlmigrate 명령은 DB에서 migration을 실제로 실행하지 않음
    + Django가 수행 할 작업을 확인하거나 변경을위해 SQL 스크립트를 필요로 할 때 사용
    
  + > 모델 테이블 만들기 ( cmd 입력 ) 
  
        python manage.py migrate
        
    + 실제적인 DB가 생성되는 시점    
      ( makemigrations를 통해 생성된 임시파일을 setting.py에 작성된 데이터베이스에 반영 )
    + Migration을 통해 DB나 테이블을 직접 삭제 or 생성 할 필요없이 모델에 변화를 줄 수 있음

+ ### Django가 제공하는 API 사용하기 ( 예제 ) 
  
  + Shell에서 나올때는 exit() 를 입력

  + > Python Shell 호출 ( cmd 입력 )
    
        python manage.py shell 
        
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
        
  
  + API 사용하기2) - python 코드 추가 
    
    > polls/models.py ( 코드 추가 1 )
    
        from django.db import models

        class Question(models.Model):
            # ...
            def __str__(self):
                return self.question_text

        class Choice(models.Model):
            # ...
            def __str__(self):
                return self.choice_text
  
    \__str__() : 객체의 표현을 사용하기 위해 메서드 추가
  
    > polls/models.py ( 코드 추가 2 ) 
    
        import datetime

        from django.db import models
        from django.utils import timezone


        class Question(models.Model):
            # ...
            def was_published_recently(self):
                return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
            
    변경사항 저장
    
  + > Python Shell 호출 ( cmd 입력 )
    
        python manage.py shell 
        
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
        
        
     
    
#### 참고 : https://docs.djangoproject.com/en/3.1/intro/tutorial02/, https://velog.io/@jcinsh/Django-%ED%8A%9C%ED%86%A0%EB%A6%AC%EC%96%BC-part2 
