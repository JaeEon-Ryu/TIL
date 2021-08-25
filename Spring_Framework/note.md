# { node & vue.js 시작하기 }

## NodeJS 란?
+ Chrome V8 JavaScript 엔진으로 빌드된 JavaScript 런타임 플랫폼
+ 이벤트 기반, Non Blocking I/O 모델을 사용해 가볍고 효율적

<br>
 
## 특징
+ javascript로 서버 개발을 하는 것
+ single thread model
+ Node.js의 패키지 생태계인 npm - 세계에서 가장 큰 오픈 소스 라이브러리
+ I/O 처리에 있어서의 우수한 성능, 서버 확장의 용이성
+ JavaScript라는 프론트엔드 필수 언어로 백엔드까지 작성 가능

<br>

## 처리
+ 입력 받은 것은 Single Thread로 delegate
+ Async Threads를 통해 리턴값 오는 순서대로 처리  
  ( Single처럼 보이지만 병렬적으로 처리 )  

<br>

## bluebird
+ 비동기 처리의 실패, 이행 등의 상태를 담은 객체
+ 콜백 함수보다 효율적으로 비동기 처리를 도와줌
+ .then() 및 .catch() 를 사용해 구현

<br>

## Socket.io
+ 실시간으로 상호작용하는 웹 서비스를 만드는 기술인 웹 소켓을 사용할 수 있게 해주는 모듈
+ JavaScript를 이용하여 브라우저 종류에 상관없이 실시간 웹을 구현할 수 있도록 한 기술
+ 전송 할 때 : socket.emit('Event',data)
+ 수신 할 때 : socket.on('Event',function(data))

<br>

## WebPack
+ JavaScript는 언어 자체가 지원하는 모듈 시스템이 없음   
  -> webpack 등장  
+ js, css, sass, fonts, image 등을 모두 package화   
  -> 네트워크 비용이 적게 발생함  
+ 모던 JavaScript 애플리케이션을 위한 정적 모듈 번들러  
+ 로더 사용, 빠른 컴파일 속도 등의 장정이 있음
+ Node.js가 설치된 환경에서 실행 가능

<br>

## MVVM
+ Model View ViewModel Pattern
+ 목표 : 비즈니스 로직과 프레젠테이션 로직을 UI로부터 분리
  -> 테스트, 유지 보수, 재사용이 쉬워지도록  
+ MVC, MVP : View와 Controller 또는 Presenter가 강하게 연결  
```
 View : UI 와 UI 로직을 다룸
 View Model : 프레젠테이션 로직과 뷰를 위한 상태를 다룸
 Model : 비즈니스 로직과 데이터를 다룸
```  

<br>

## Vue.js
+ MVVM 패턴에서 ViewModel 레이어에 해당하는 화면단 라이브러리
+ 데이터 바인딩과 화면 단위를 컴포넌트 형태로 제공하며, 관련 API를 지원하는 목적
+ Angular에서 지원하는 양방향 데이터 바인딩을 동일하게 제공  
  ( 하지만 컴포넌트 간 통신의 기본 골격은 React의 단방향 데이터 흐름을 사용 )  
+ 다른 프론트엔드 프레임워크 (Angular, React)와 비교했을 때, 상대적으로 가볍고 빠름
+ 문법이 단순하고 간결하여 초기 학습 비용이 낮고, 누구나 쉽게 접근 가능
+ Progressive Javascript Framework   
  ( 매번 Html을 받아서 처리하는 것 뿐만아니라 화면 처리 등을 모두 포함하기 때문 )  
+ SPA - Single Page Application  
  ( 모든 page를 각각 refresh? (X) -> 한 페이지에서 작동 (O) )  
+ 접근성, 유연성, 고성능

<br>
  

#### reference
[ 시니어코딩 - { node & vue.js 시작하기 } ](https://www.youtube.com/watch?v=pc1jgmuS02M&list=PLEOnZ6GeucBX5H60GtICsoDs9LaFQVDPz&ab_channel=%EC%8B%9C%EB%8B%88%EC%96%B4%EC%BD%94%EB%94%A9)  
[ 시니어코딩 - 강의 슬라이드 ](https://docs.google.com/presentation/d/1mi1Qp6vsb8H09ChmuCwnGLUfEmb1ZRRhOy0YMJzfSbw/edit#slide=id.g448eca9d39_0_46)  
[ 시니어코딩 - github ](https://github.com/indiflex/nodevue)  
[ 나무위키 - nodejs ](https://namu.wiki/w/Node.js?from=Nodejs)   
[ 발모스토리 - nodejs bluebird promisify 예제 ](https://balmostory.tistory.com/72)  
[ 김승엽 - Node.js와 Socket.io를 이용한 채팅 구현 ](https://berkbach.com/node-js%EC%99%80-socket-io%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-%EC%B1%84%ED%8C%85-%EA%B5%AC%ED%98%84-1-cb215954847b)  
[ Nesoy Blog - Socket.io이란? ](https://nesoy.github.io/articles/2017-04/Socket.io)  
[ webpack - concepts ](https://webpack.kr/concepts/)  
[ 김양귀 - JavaScript 모듈화 도구, webpack ](https://d2.naver.com/helloworld/0239818)  
[ k7120792 - MVVM 패턴 ](https://velog.io/@k7120792/Model-View-ViewModel-Pattern)  
[ Captain Pangyo - Vue.js 입문서 - 프론트엔드 개발자를 위한 ](https://joshua1988.github.io/web-development/vuejs/vuejs-tutorial-for-beginner/)  
