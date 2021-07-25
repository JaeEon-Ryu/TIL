# Full_stack 관련 기술 공부   

<br>

## INDEX   
+ ### 리눅스(Linux) - NCP (Naver Cloud Platform) CentOS 서버 생성 및 설정  
  <img src="https://user-images.githubusercontent.com/52907116/126303190-3556bc06-76a8-48a6-b041-a6337c73dc9d.JPG" width="60%">  
  
  <br>

+ ### 리눅스(Linux) - Linux CentOS7에 Nginx 웹서버 설치  
  <img src="https://user-images.githubusercontent.com/52907116/126303180-20a47a0b-87a4-4401-84da-618e39a3e109.JPG" width="30%"><img src="https://user-images.githubusercontent.com/52907116/126303191-347c92c3-7209-453b-805e-f9332a415db7.JPG" width="30%">  
  
  <br>

+ ### 리눅스(Linux) - Linux 서버에 Volta, node, pm2, python 설치  
  <img src="https://user-images.githubusercontent.com/52907116/126303193-c6cd2c5e-dc79-436e-9819-ae666a6c9499.png" width="50%" >  
  <img src="https://user-images.githubusercontent.com/52907116/126303196-c2d780ea-39dd-4a95-a3e9-167d04ce0c74.png" width="50%" >  
  <img src="https://user-images.githubusercontent.com/52907116/126303201-cd269282-83b6-48a0-8ce8-d05154a8f998.png" width="50%" >  
  <img src="https://user-images.githubusercontent.com/52907116/126303202-0e39653e-2c7b-473f-a527-fd09117f077d.png" width="50%" >  
  
  <br>

+ ### 리눅스(Linux) - Linux CentOS7에 MySQL8 설치  
  <img src="https://user-images.githubusercontent.com/52907116/126426061-ba4fed10-3188-4cdf-a933-9d0743e8ff94.png" width="30%" ><img src="https://user-images.githubusercontent.com/52907116/126426064-ab8f2849-0286-40a9-9ac2-f988f607dd31.png" width="30%" >  
  
  ### 참고) mysql - root 패스워드 초기화하는 방법
  ```python
  1. 먼저 mysql이 떠있으면 중지
  $> systemctl stop mysqld

  2. 암호없이 로그인되도록 my.cnf 파일 - [mysqld] 마지막 줄에 다음을 추가하고 저장하고 다시 구동
  skip-grant-tables

  $> systemctl start mysqld

  3. 패스워드 없이 mysql을 실행
  $> mysql -u root
  mysql>

  4. 인증 문자를 null로 초기화 하고, 패스워드를 변경 (암호는 대문자와 특수문자가 들어가게 해야함)
  mysql> UPDATE mysql.user SET authentication_string=null WHERE User='root';
  mysql> ALTER USER 'root'@'localhost'IDENTIFIED WITH mysql_native_password BY '원하는암호';
  mysql> quit
    만약 ALTER 시 오류가 난다면 mysql을 나갔다가 다시 들어오기

  5. my.cnf 파일에서 이제 다음 라인을 삭제하고 다시 구동
  skip-grant-tables

  $> systemctl restart mysqld
  $> mysql -u root -p
  Enter password: <좀 전에 설정한 패스워드를 입력>
  mysql> 
  ```

  <br>

+ ### 리눅스(Linux) - Nginx 셋팅 및 무료 HTTPS 인증서 설치  
  <img src="https://user-images.githubusercontent.com/52907116/126777294-06271179-5851-4d60-a3b4-7767822b0fff.png" width="30%" >  
    
  ### 참고) 도메인 등록
  ```python
  1. freenom : ga, ka 등으로 끝나는 도메인을 무료로 얻을 수 있음 ( 무료일 경우 최대 1년 )
  2. gabia : 여러가지 도메인 주소 중 'shop'으로 끝나는 도메인 1년에 500원으로 구입 가능 ( freenom을 사용할 수 없을 때 사용 ) 
  ```
 
  <br>

+ ### 리눅스(Linux) - docker image 만들기  
  <img src="https://user-images.githubusercontent.com/52907116/126788759-03bd366c-dd58-4adb-a093-a2e8c954f671.png" width="40%" ><img src="https://user-images.githubusercontent.com/52907116/126859567-0e6f6079-99c6-4547-9326-f0b2b4c110a4.png" width="40%" >       
  <br>
  ( 윈도우 cmd에서 Docker를 활용하여 Linux를 쓰는 모습, 이미지 제작 후, tar 확장자의 압축파일로 배포 준비 완료 )
  
  <br>
  
  ### 참고) Docker 명령어 정리
  ```python
  # 컨테이너 확인(실행중인 image 확인)
  docker ps : 실행중인 컨테이너의 목록을 확인
  docker ps -a : 이전에 종료되었던 컨테이너들을 포함한 컨테이너의 목록을 확인
  
  # start (종료된 컨테이너 시작)
  docker start "container ID" : 컨테이너 실행 ( 컨테이너를 실행한다고 해서 Host OS의 쉘을 벗어나진 않음 )
  
  # attach (컨테이너에 접속하기)
  docker attach "container ID" : 컨테이너 접속 ( Host OS의 쉘을 벗어남 ) 
 
  # .bashrc
  컨테이너에 접속했을 때, 실행되는 프로세스를 지정 가능
  ex) 별칭 지정, 시간 지정, nginx 실행, cd(최초 파일경로 - root) 등
  . .bashrc : 바뀐 bashrc 적용 
  ```
  <br>

+ ### 리눅스(Linux) - 한방에 정리하는 리눅스 명령어와 쉘스크립트
  ```python
  ls / touch / cat 
  head / tail / less
  pwd /  which / clear / echo
  cd / cd - 
  mkdir / rmdir
  cp / mv / rm
  find
  whoami
  passwd
  grep
  ```
  
<br>

#### reference  
##### [시니어코딩 - {SSAC} 스타트업 풀스택 개발자 과정](https://www.youtube.com/watch?v=Y__GznCpioo&list=PLEOnZ6GeucBWaUzqrMvrl-_ernhNwLHOr&ab_channel=%EC%8B%9C%EB%8B%88%EC%96%B4%EC%BD%94%EB%94%A9indiflex)  
##### [시니어코딩 - Linux 실무](https://docs.google.com/presentation/d/1S2WtAXDpFNzWG72AOMnAfPJCrTXmf1TjNxrFLNgosy4/edit#slide=id.gab11b71d47_0_93)  
##### [시니어코딩 - Linux 기본 명령어](https://docs.google.com/presentation/d/1CrOcTTrRRHlredMRwie9WKSo7ChIF4bRylvUxhinRYU/edit#slide=id.p)


