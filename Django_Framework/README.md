## Django Framework    

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
  + 폴더 이동하기
    > #### cd mysite
  + 실행하기
    > #### Python manage.py runserver
  + 웹 페이지 방문하기
    + http://localhost:8000/ 클릭 
 
 #### 참고 : https://www.geeksforgeeks.org/django-tutorial/, https://www.geeksforgeeks.org/django-basics/ , https://docs.djangoproject.com/en/3.1/intro/tutorial01/ 
  
