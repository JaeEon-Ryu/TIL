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

+ polls 앱 만들기
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

+ 데이터베이스 설정
  + 기본적으로 SQLite 사용 ( Python에 내장되어 있음 ) 


#### 참고 : https://docs.djangoproject.com/en/3.1/intro/tutorial02/, https://velog.io/@jcinsh/Django-%ED%8A%9C%ED%86%A0%EB%A6%AC%EC%96%BC-part2 
