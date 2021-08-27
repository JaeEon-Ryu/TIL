## Spring Framework 에 대한 간단한 소개
+ 자바 플랫폼을 위한 오픈소스 애플리케이션 프레임워크
+ 엔터프라이즈급 애플리케이션을 개발하기 위한 모든 기능을 종합적으로 제공하는 경량화된 솔루션  
  ( 엔터프라이즈급 : 대규모 데이터 처리와 트랜잭션이 동시에 여러 사용자로부터 행해지는 매우 큰 규모의 환경 )  
+ Spring Framework : 경량 컨테이너 - 자바 객체를 담고 직접 관리함  
  -> ( IoC 기반의 Framework )  
+ DI ( Dependency Injection ) -> 스프링 프레임워크의 핵심 기능
+ 웹 개발에 필요한 세 가지
``` 
MVC - DI - 느슨한 결합력과 인터페이스
트랜잭션 - AOP
인증과 권한 - Servlet Filter
```

<br>

## 느슨한 결합력과 인터페이스
+ 서비스를 변경하기 위해 Dao를 변경해야 할 경우 
 1) 코드 수정
 2) 코드 추가(덮어쓰기), Dao를 참조하는 Service의 코드를 수정  
    -> 코드를 추가하면 새로 배포를 하지 않아도 되기 때문에 편리  
    -> but 추가된 코드를 참조하기 위해 Service부분이 변경될 수 있음  
      ```
      Class b1 = new Class b1();
      -> Class b2 = new Class b2();
      ```  
    -> 객체 변경 ( 느슨한 결합 )   
      ( 강하게 결합된 두 클래스가 -> 외부 파일을 통해 수정할 수 있는 상태로 바뀐 것 )  
      ( 인터페이스에서는 파일을 읽어와서 자바의 코드를 수정하지 않고 객체의 참조를 변경 가능함 )    

<br>

## DI ( Dependency Injection )
+ 의존성 주입  
  -> 객체가 서로 의존하는 관계가 되도록 의존성을 주입   
      ( 하나의 객체가 어떠한 다른 객체를 사용하고 있음을 의미 )  
일체형 vs 조립형

<br>

## IoC 컨테이너
+ IoC : Inversion of Control  
  -> 제어의 흐름을 사용자가 컨트롤 하지 않고, 위임한 특별한 객체에 모든 것을 맡기는 것  

<br>





#### reference  
[ 뉴렉처 - 스프링 프레임워크 강좌/강의 ALL ](https://www.youtube.com/watch?v=XtXHIDnzS9c&list=PLq8wAnVUcTFUHYMzoV2RoFoY2HDTKru3T&ab_channel=%EB%89%B4%EB%A0%89%EC%B2%98)  
[ 히진쓰의 서버사이드 기술 블로그 - Spring Framework란? 기본 개념 핵심 정리 ](https://khj93.tistory.com/entry/Spring-Spring-Framework%EB%9E%80-%EA%B8%B0%EB%B3%B8-%EA%B0%9C%EB%85%90-%ED%95%B5%EC%8B%AC-%EC%A0%95%EB%A6%AC)  
[ GrapeMilk - 느슨한 결합력(DI)과 인터페이스 ](https://norwayy.tistory.com/258)  
