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
+ js, css, sass, fonts, image 등을 모두 package화   
  -> 네트워크 비용이 적게 발생함  

<br>

## MVVM
+ Model View ViewModel Pattern
+ MVC, MVP : View와 Controller 또는 Presenter가 강하게 연결

<br>

## Vue.js
+ Progressive Javascript Framework   
  ( 매번 Html을 받아서 처리하는 것 뿐만아니라 화면 처리 등을 모두 포함하기 때문 )  
+ SPA - Single Page Application  
  ( 모든 page를 각각 refresh? (X) -> 한 페이지에서 작동 (O) )  
+ 접근성, 유연성, 고성능
+ vue-cli
+ vue-devtools

<br>
  

#### reference
[ 시니어코딩 - { node & vue.js 시작하기 } ](https://www.youtube.com/watch?v=pc1jgmuS02M&list=PLEOnZ6GeucBX5H60GtICsoDs9LaFQVDPz&ab_channel=%EC%8B%9C%EB%8B%88%EC%96%B4%EC%BD%94%EB%94%A9)  
[ 시니어코딩 - 강의 슬라이드 ](https://docs.google.com/presentation/d/1mi1Qp6vsb8H09ChmuCwnGLUfEmb1ZRRhOy0YMJzfSbw/edit#slide=id.g448eca9d39_0_46)  
[ 시니어코딩 - github ](https://github.com/indiflex/nodevue)  
[ 나무위키 - nodejs ](https://namu.wiki/w/Node.js?from=Nodejs)   
[ 발모스토리 - nodejs bluebird promisify 예제 ](https://balmostory.tistory.com/72)  
[ 김승엽 - Node.js와 Socket.io를 이용한 채팅 구현 ](https://berkbach.com/node-js%EC%99%80-socket-io%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-%EC%B1%84%ED%8C%85-%EA%B5%AC%ED%98%84-1-cb215954847b)  
[ Nesoy Blog - Socket.io이란? ](https://nesoy.github.io/articles/2017-04/Socket.io)  
