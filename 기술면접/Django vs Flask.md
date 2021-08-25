# Django vs Flask
+ Python에서 가장 널리 사용되는 오픈소스 기반 웹 프레임워크
+ Django : full stack web framework  
  -> 기능이 훨씬 뛰어나지만 복잡함  
+ Flask : 가볍과 확장 가능한 web framework  
  -> 매우 단순하고 가벼움  

<br>

## Django
+ python기반 web framework 중 가장 많이 사용되고 있는 web framework
+ Flask보다 약 10배 많은 코드 라인으로 개발이 되어있음
+ ORM (Object relational mapping) 기능 내장  
  -> ORM : 데이터베이스 시스템과 데이터 모델 클래스를 연결하는 역할   
  -> SQL 의존적인 코드를 벗어나 생산적인 코딩이 가능하게 되어 유지보수가 편해짐  
+ 자동으로 관리자 화면을 구성  
  -> web application에서 사용하는 데이터들을 쉽게 생성하거나 변경이 가능  

<br>

## Flask
+ Python의 Micro framework를 기반으로 단순하고 매우 가벼운 web framework
+ URL 라우팅, Template, Cookie, Debugger 및 개발서버 등 기본 기능만을 제공
+ django의 1/10밖에 안 되는 코드 (code 28,677 lines)로 구현
+ WSGI용 Library인 Werkzeug와 HTML 렌더링 엔진인 Jinja2 template으로 구성  
  -> 기본 기능 제공에 다양한 확장 모듈을 이용할 수 있는 구조  
+ ORM 기능 제공 X  
  -> 개발자가 직접 SQLAlchemy 등 개발자에게 편하거나 익숙한 패키지를 설치하여 사용  

<br>

## 차이점  
||Django|Flask|
|----|-----|-----|
|레이아웃|한 프로젝트 내에 다양한 </br> 어플리케이션 존재 가능|프로젝트마다 1개의 </br> 어플리케이션을 개발하도록 되어 있음|
|DB접근|ORM 사용 </br> ( DB 접속 최소화 )|SQLAlchemy 등을 사용 </br> (ORM 없음)|
|유연함|Flask보다 기능 추가에 불편함이 있음 </br> (무거움) |기능 추가가 간단함 </br> (가벼움)|

<br>

## 사용시기
+ Django 를 써야 할 때
  + 웹앱이나, API 백엔드를 만들고 싶을 때
  + 빠른 개발, 빠른 배포, 빠른 업데이트를 해야할 때
  + CSRF, XSS, SQL 인젝션, 클릭재킹등 기본적 보안이 필요할 때
  + 스케일링 업, 스케일링 다운을 자유자재로 하고 싶을 때
  + 개발하다 막혔을때 물어보기 위해 ( 정보가 많음 )
  + SQL이 익숙하지 않아서 강력한 ORM이 필요할 때
+ Flask 를 써야 할 때
  + 앱이 너무 크거나 너무 작을 때
  + 밑그림부터 시작할 수 있는 실력에 내가 뭘하고 있는지 알고 있을 때
  + 팀원 중 그 어느 누구라도 Django 와 Python에 익숙치 않을 때
  + DB로 이미 생성된 NoSQL을 사용할 때

<br>

#### reference  
[ 웬디의 기묘한 이야기 - Python django vs Flask. web framework 무엇을 선택해야할까? ](https://wendys.tistory.com/172)  
[ 라이언 - 언제 Django를, 언제 Flask를 사용해야 할까? ](https://dingrr.com/blog/post/%EC%96%B8%EC%A0%9C-django%EB%A5%BC-%EC%96%B8%EC%A0%9C-flask%EB%A5%BC-%EC%82%AC%EC%9A%A9%ED%95%B4%EC%95%BC-%ED%95%A0%EA%B9%8C)  
