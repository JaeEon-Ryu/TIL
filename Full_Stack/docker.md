# docker 관련 내용 정리  

+ ### 가상화를 사용하는 이유
  + CPU사용률이 10% 일 정도로 활용도가 낮은 서버   
    -> 리소스 낭비
  + 모든 서비스를 한 서버안에 올린다면 ?   
    -> 안정성에 문제가 생길 수 있음
  + 안정성을 높이며 리소스도 최대한 활용할 수 있는 방법은 무엇인가?   
    -> 서버 가상화

<br>

+ ### 기존 가상화 방식과의 차이점
  + 기존의 가상화 방식은 주로 OS를 가상화 했음 ( VMware, VirtualBox )  
    But, 무겁고 느리다는 단점
  + 위 상황을 개선하기 위해 CPU의 가상화 기술(HVM)을 이용한 KVM과 반가상화 방식의 Xen 등장  
    -> 전체 OS를 가상화하는 방식이 아니였기 때문에 호스트형 가상화 방식에 비해 성능이 향상
  + 추가적인 OS를 설치하여 가상화 하는 방법   
    -> 성능 문제 야기   
    -> 프로세스를 격리하는 방식 등장 ( 리눅스 컨테이너 )  
    
    <br>
    
    <img src="https://user-images.githubusercontent.com/52907116/128663660-2f9abc56-45d6-4833-9ac2-916f4ba5fd0d.png" width="60%">  
  
<br>

<br>

+ ### 컨테이너란?
  + 가상화 기술 중 하나로 대표적으로 LXC(Linux Container)가 있음
  + OS레벨의 가상화로 프로세스를 격리시켜 동작하는 방식

<br>

+ ### Docker란?
  + 애플리케이션을 신속하게 구축, 테스트 및 배포할 수 있는 소프트웨어 플랫폼
  + 소프트웨어를 컨테이너라는 표준화된 유닛으로 패키징  
    ( 이 컨테이너에는 라이브러리, 시스템 도구, 코드, 런타임 등 소프트웨어를 실행하는 데 필요한 모든 것이 포함되어 있음 )
  + 컨테이너 기반의 오픈소스 가상화 플랫폼
  + 환경에 구애받지 않고 애플리케이션을 신속하게 배포 및 확장할 수 있음
  + Google사의 Go 언어로 만들어짐
  + Immutable, Stateless, Scalable
  + 리눅스 기반 체제 ( LXC - Linux Container )
  
<br>

+ ### Docker Image
  + 컨테이너 실행에 필요한 파일과 설정값등을 포함하고 있는 것  
    ( 상태값을 가지지 않고 변하지 않음 - Immutable )
  + 컨테이너는 이미지를 실행한 상태라고 볼 수 있음
  + 2017년 기준, 블로그 저자 [subicura](https://subicura.com/2017/01/19/docker-guide-for-beginners-1.html) 님에 따르면 현재 공개된 도커 이미지는 50만개가 넘고 Docker hub의 이미지 다운로드 수는 80억회에 다다름  
    ( 누구나 쉽게 이미지를 만들고 배포할 수 있음 )

<br>

+ ### 레이어 저장방식
  + 도커 이미지의 용량 : 보통 수백메가(Mb)    
    ( 컨테이너를 실행하기 위한 모든 정보를 가지고 있기 때문 )  
    -> 기존 이미지에 파일 하나 추가했다고 수백메가를 다시 다운로드 ? ( 비효율적 )  
    -> 이런 문제를 해결하기 위해 레이어layer라는 개념을 사용  
    
    ```
    ubuntu 이미지가 A + B + C의 집합이라고 가정,
    ubuntu 이미지를 베이스로 만든 nginx 이미지는? 
      =>  A + B + C + nginx
    webapp 이미지를 nginx 이미지 기반으로 만들었다면 ? 
      = > A + B + C + nginx + source 레이어
    webapp 소스를 수정한다면?
      => A, B, C, nginx 레이어를 제외한 새로운 source(v2) 레이어만 다운
    ```  
  + 컨테이너를 생성할 때도 레이어 방식 사용  
    -> 여러개의 컨테이너를 생성해도 최소한의 용량만 사용함
 
<br>

#### reference  
##### [시니어코딩 - { docker } 도커](https://www.youtube.com/watch?v=MHzxhoBmCwA&list=PLEOnZ6GeucBVj0V5JFQx_6XBbZrrynzMh&ab_channel=%EC%8B%9C%EB%8B%88%EC%96%B4%EC%BD%94%EB%94%A9)
##### [ 아마존 - Docker ](https://aws.amazon.com/ko/docker/)
##### [ subicura  - 초보를 위한 도커 안내서 - 도커란 무엇인가? ](https://subicura.com/2017/01/19/docker-guide-for-beginners-1.html)
##### [ 히진쓰의 서버사이드 기술 블로그 - Docker의 개념 및 핵심 설명](https://khj93.tistory.com/entry/Docker-Docker-%EA%B0%9C%EB%85%90)

