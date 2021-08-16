# CentOS

# 정의
+ Red Hat 엔터프라이즈 리눅스와 완전하게 호환되는 무료 기업용 리눅스 운영체제
+ 리눅스의 배포판 중 하나
+ RHEL의 소스를 기반으로 만들어짐

<br>

## 특징
+ 무료이면서 설치또한 간편함
+ 서버용 리눅스 1인자라고 불리는 RHEL을 그대로 미러링 하는것에 목표를 두고 있음
+ 네이버나 카카오에서도 사용중인 운영체제

<br>

## 단점
+ RHEL과 달리 사후 지원이 없음 ( 기업이 아닌 커뮤니티 차원에서 제공되기 때문 )  
  -> 전산실에서 안정성의 문제 야기 가능  
+ RHEL이 마이너 업데이트 될 경우, CentOS의 해당 버전이 릴리즈 될 때까지 공백이 생길 수 있음  
  -> 소프트웨어 기업 : CentOS 선호 ( 자체적으로 프로그래머 인력을 보유했기 때문 )  
  -> 은행 또는 공공기관의 전산실 : RHEL 선호  

<br>

## 지원 종료 ( 2020년 12월 발표 )
```
원래 CentOS는 RHEL의 다운스트림 빌드로 출시하여 안정적인 패치 및 업데이트를 보장할 수 있었음
하지만 추후 CentOS가 RHEL의 업스트림 빌드로 전환된다고 발표함 ( CentOS Stream )

2020년 까지 릴리즈 방식 : Fedora -> RHEL -> CentOS 
변경되는 릴리즈 방식    : Fedora -> CentOS -> RHEL

CentOS Stream 은 보안이나 안정성 면에서 위험에 노출될 확률이 높아지게 될 것으로 예상
```  
RHEL 종료 시기  
||Full Support|Maintenance Support|
|------|---|---|
|RHEL8|2024년 5월 31일|2029년 5월 31일|
|RHEL7|2019년 8월 6일|2024년 6월 30일|
  
CentOS 종료 시기
||Full Support|Maintenance Support|
|------|---|---|
|CentOS 8|2021년 12월 31일|2021년 12월 31일|
|CentOS 7|2020년 4분기|2024년 6월 30일|

<br>

## CentOS 를 대체할 OS는?
+ CentOS Stream  
  -> 기존 CentOS를 사용했던 사용자는 상용 Redhat이나 CentOS Stream으로 마이그레이션 가능  
+ Oracle Linux  
  -> RHEL과 호환 100% 되는 app binary  
  -> CentOS Linux와 마찬가지로 RHEL의 소스를 기반으로한 재 구축 배포판  
+ Cloud Linux  
  -> 공유 호스팅 제공 업체를 위해 설계된 RHEL 재 구축 배포판  
+ Springdale Linux  
  -> 학술 과학 커뮤니티에서 만든 RHEL 재 구축 배포판  
+ Rocky Linux  
  -> RHEL OS 소스 코드를 사용하는 다운스트림 배포판  

<br>

#### reference
[ Hackerrior - 리눅스 centOS를 업계에서 많이 쓰는 이유와 장점 ](https://hack-cracker.tistory.com/5)  
[ 서버용으로 우분투보다 centOS를 쓰는 이유는 뭔가요? ](https://okky.kr/article/716711)  
[ 썬구루 - CentOS 란 무엇인가? ](https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=sunguru&logNo=221008975880)  
[ 나무위키 - CentOS ](https://namu.wiki/w/CentOS)  
[ 서버 프로그래머 로그 - CentOS 의 죽음 ](https://blog.kesuskim.com/archives/death-of-centos/)  
[ 삵 - RHEL과 CentOS의 차이는? ](https://sarc.io/index.php/os/1753-rhel-centos)  
[ jhkang - Rocky Linux 8.3 RC1 설치로 본 RHEL와 CentOS의 비교 ](https://tech.osci.kr/2021/05/12/119374564/)  
[ 닥터최 오이시이 - CentOS 대체 방안은 어떤 것이 있을까 ](https://couplewith.tistory.com/entry/Trend-CentOS-is-Dead-CentOS-%EB%8C%80%EC%B2%B4-%EB%B0%A9%EC%95%88%EC%9D%80-%EC%96%B4%EB%96%A4-%EA%B2%83%EC%9D%B4-%EC%9E%88%EC%9D%84%EA%B9%8C)
