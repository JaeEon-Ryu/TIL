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

## axios
+ Promise 기반의 자바스크립트 비동기 처리방식 사용  
  ( 요청후 .then()으로 결과값을 받아서 처리하는 형식 )  
+ get
  + 서버로부터 데이터를 가져오는데 사용  
 ```javascript
  axios.get('/api/data') .then(res => { // 불러온 값을 Console에 뿌려줌
  console.log(res.data) })
 ```  
+ post
  + 값을 입력할 때 사용  
 ```javascript
  axios.post('/api/data', {title: "vue.js"}) 
   .then(res => { console.log(res.data) })
 ```  
+ patch
  + 특정 값을 수정할 때 사용  
 ```javascript
  axios.patch('/api/data/3', {title: "vue.js"}) 
   .then(res => { console.log(res.data) })
 ```  
+ delete
  + 특정 값을 삭제할 때 사용  
 ```javascript
  axios.delete('/api/data/3') 
   .then(res => { console.log(res.data) })
 ```  

<br>

## Vue Routers
+ SPA : 페이지를 이동할 때 서버에 요청해 갱신 ? (X)  
  -> 미리 해당 페이지를 구성해놓고 클라이언트의 라우팅을 이용하여 화면을 갱신 (O)  
+ 라우팅을 이용하면 매끄럽게 화면 전환을 할 수 있음
+ Vue, React, Angular 모두 라우팅을 이용하여 화면을 전환함
+ Vue Router란? : Vue에서 라우팅 기능을 구현할 수 있도록 지원하는 공식 라이브러리

<br>

## Lodash
+ 자바스크립트 라이브러리 중 하나
+ 데이터를 쉽게 다룰 수 있게 도와줌
+ 특히, 배열 안의 객체들의 값을 핸들링할 때 유용함
+ 예제 5가지  
```javascript
1. indexOf : 어느 위치에 있는지 리턴 ( 여러개가 있을 경우 처음 위치 리턴 )
_.indexOf(array, value, [fromIndex=0])

2. fill : array를 원하는 문자 혹은 숫자로 채워넣음
_.fill(array, value, [start=0], [end=array.length])

3. join : array에 seperator를 따로 설정할 수 있게 해줌
_.join(array, [separator=','])

4. find : Collection에 대해서 검색 기능을 담당하고, 첫번째 요소를 가져옴
_.find(collection, [predicate=_.identity], [fromIndex=0])

5. foreach : Collection의 각 요소에 대해 작업을 할 때 사용함
_.forEach(collection, [iteratee=_.identity])
```  

<br>

## Event Bus
+ Vue의 기본적인 컴포넌트 관계 => 상-하위 컴포넌트간 통신
+ 하나의 상위 컴포넌트와 두개의 하위 컴포넌트 구조에서 두 하위 컴포넌트끼리 통신을 해야한다면?  
  -> 상위 컴포넌트를 강제로 거쳐야 하는 상황 발생  
  -> 불필요한 컴포넌트를 만들어야 하는 상황을 해결하기 위해 Event Bus 등장  
+ Event Bus : 컴포넌트 계층 구조와 관계 없이 두 컴포넌트 사이에 데이터 전달 가능  
+ 이벤트와 데이터 송신 : $emit()
+ 이벤트와 데이터 수신 : $on()
  
<br>

## Mixin
+ 컴포넌트에 무언가를 섞어 원하는 것을 구현하는 기능
+ 동작 과정
  1. 믹스인할 개체를 생성
  2. 컴포넌트에 객체를 믹스인
  3. 나머지 부분을 구현하여 완성
+ 같은 코드를 반복하지 않게 되거, 특정 '기능'을 나타내는 파일을 캡슐화 가능
+ 유지보수 및 협업 측면에서 훌륭한 구조 완성 가능

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
[ 어쩌다보니여기까지 - Vue.js에서 axios를 사용하여 서버통신하는 방법 ](https://uxgjs.tistory.com/138)    
[ hyemz - Vue.js 라우팅에 대해 알아보자 ](https://velog.io/@hyemz/Vue.js-%EB%9D%BC%EC%9A%B0%ED%8C%85%EC%97%90-%EB%8C%80%ED%95%B4-%EC%95%8C%EC%95%84%EB%B3%B4%EC%9E%90-1)  
[ jhhan - lodash ](https://jhhan009.tistory.com/48)  
[ 탱구탱구 개발자 일기 - Event Bus를 통한 컴포넌트 통신 ](https://tangoo91.tistory.com/9)  
[ bluestragglr - Vue.js Mixin: 기능 캡슐화하기 ](https://velog.io/@bluestragglr/Vue.js-Mixin-%EA%B8%B0%EB%8A%A5-%EB%B0%98%EB%B3%B5-%EC%A0%9C%EA%B1%B0%ED%95%98%EA%B8%B0)  
