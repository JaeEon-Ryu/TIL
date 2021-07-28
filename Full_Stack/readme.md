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
  
+ ### 리눅스(Linux) - 실무에서 꼭 필요한 기술
  + #### sudo 권한 부여
  ```
  # 설정 확인
  #root> visudo
    %wheel  ALL=(ALL)       ALL
    %wheel  ALL=(ALL)       NOPASSWD: ALL
  #root> usermod -aG wheel <user>
  
  $user> sudo bash
  $user> sudo vi /etc/hosts
  ```
  + #### 파일 압축
  ```
  $> gzip x.log         # x.log → x.log.gz
  $> gzip x.log.gz -d   # x.log.gz → x.log
  $> gzip x.log.gz -l   # compress status & list
  ```
  + #### ftp vs sftp vs samba vs ownCloud
  ```
  ftp:   21 port
  sftp:  22 port (ssh)
  samba: windows remote directory
  ownCloud: 클라우드 파일 서버(mariadb, httpd, php, etc)
  ```
  + #### 지난 log 파일 정리
  ```
  $> find . -name "*.gz"
  $> find . -name \*.gz | sort
  $> find . -name \*.gz -mtime +30
  $> find . -name \*.gz -mtime +30 -delete
  ```
  + #### vmstat (Virtual Memory STATistics) 시스템 모니터링  
  프로세스, 메모리, 페이징, I/O 블럭, CPU 활동 사항들의 정보를 출력하는 기능  
  ```
  $> vmstat
  $> vmstat 1         # 1초에 한번씩 출력
  $> vmstat 1 3       # 1초에 한번씩 3번
  $> vmstat -a        # active 한것과 그렇지 않은 것을 보여줌
  $> vmstat -d        # 디스크 사용량
  $> vmstat -s        # 메모리 스탯
  ```
  + #### sar (System Activity Reporter) 지난 시스템 모니터링
  ```
  # CPU average
  $> sar
  $> sar -f /var/log/sa/sa20
  
  # memory average
  $> sar -r
  $> sar -f /var/log/sa/sa20 -r
  
  # load average
  $> sar -q
  ```
  + #### netstat (NETwork STATistics)  &  ss  네트워크 상태 보기
  ```
  $> netstat
  $> netstat -an
  $> netstat -anl
  $> netstat -an | grep 3306
  
  # cf. ss (more fast)
  $> ss -an | grep 3306
  ```
  + #### Load Balancing
  ```
  하나의 인터넷 서비스가 발생하는 트래픽이 많을 때, 여러 대의 서버가 분산처리하여 해결해주는 서비스
  ( 서버의 로드율 증가, 부하량, 속도저하 등 고려 )
  
  Load Balancer : 여러 대의 Server에게 균등하게 Traffic을 분산시켜주는 역할을 하는 것
  
  NAT(Network Address Translation)
  사설 IP 주소를 공인 IP 주소로 바꾸는 데 사용하는 통신망의 주소 변조기
  
  Tunneling
  인터넷상에서 눈에 보이지 않는 통로를 만들어 통신할 수 있게 하는 개념
  데이터를 캡슐화해서 연결된 상호 간에만 캡슐화된 패킷을 구별해 캡슐화를 해제할 수 있음
  
  DSR(Dynamic Source Routing protocol)
  서버에서 클라이언트로 되돌아가는 경우, 목적지 주소를 클라이언트의 IP 주소로 전달해서 찾아가는 개념
  ( 네트워크 스위치를 거치지 않음 )
  ```
  
  <br>
  
+ ### MySQL 시작 - 샘플 데이터 생성
  + #### 기본설정
    ```
    1. ncloud 서버 접속 후, vi /etc/my.cnf   ->  mysqld 하단에 두줄 추가

    sql_mode=NO_ENGINE_SUBSTITUTION,STRICT_TRANS_TABLES
    log_bin_trust_function_creators=1
    
    2. mysql 접속해서 권한 부여
      ( 2-1 방법이 되지 않을 경우, 2-2 방법을 쓸 것 )
    
    2-1)  grant all privileges on testdb.* to 이름@'%';
          flush privileges;
    
    
    2-2)  update mysql.user set Super_priv='Y' where user = '이름';
          flush privileges;
    ```
    
    <br>
    
  + #### 함수예제
    ```
    CREATE DEFINER=`test0114`@`%` FUNCTION `f_rand1`(_str varchar(255)) RETURNS varchar(31) CHARSET utf8mb4 COLLATE utf8mb4_unicode_ci
    BEGIN
      declare v_ret varchar(31);
      declare v_len tinyint;

      set v_len = char_length(_str);
      set v_ret = substring(_str,CEIL(rand() * v_len),1);

    RETURN v_ret;
    END
    ```
    
    <br>
    
  + #### 프로시저 예제
    ```
    CREATE DEFINER=`test0114`@`%` PROCEDURE `sp_test_emp`(_cnt int)
    BEGIN
      declare v_idx int default 0;

      while v_idx < _cnt
      do
        insert into Emp(ename, dept, salary) values (f_randname(), f_rand1('34567'), f_rand1('123456789') * 100);
        set v_idx = v_idx + 1;
      end while;
    END
    
    
    CREATE DEFINER=`test0114`@`%` FUNCTION `f_randname`() RETURNS varchar(31) CHARSET utf8mb4 COLLATE utf8mb4_unicode_ci
    BEGIN
      declare v_ret varchar(31);
      declare v_lasts varchar(255) default '김이박조회전천방지마우배원';
      declare v_firsts varchar(255) default '순신세종성호지혜가은세호윤국가나다라마바사아자차카결찬희';

      set v_ret = concat( f_rand1(v_lasts), f_rand1(v_firsts), f_rand1(v_firsts));

    RETURN v_ret;
    END
    ```
    
    <br>
 
  
<br>

#### reference  
##### [시니어코딩 - {SSAC} 스타트업 풀스택 개발자 과정](https://www.youtube.com/watch?v=Y__GznCpioo&list=PLEOnZ6GeucBWaUzqrMvrl-_ernhNwLHOr&ab_channel=%EC%8B%9C%EB%8B%88%EC%96%B4%EC%BD%94%EB%94%A9indiflex)  
##### [시니어코딩 - Linux 실무](https://docs.google.com/presentation/d/1S2WtAXDpFNzWG72AOMnAfPJCrTXmf1TjNxrFLNgosy4/edit#slide=id.gab11b71d47_0_93)  
##### [시니어코딩 - Linux 기본 명령어](https://docs.google.com/presentation/d/1CrOcTTrRRHlredMRwie9WKSo7ChIF4bRylvUxhinRYU/edit#slide=id.p)  
##### [시니어코딩 - MySQL 실무](https://docs.google.com/presentation/d/1fhtpdjbIPi0fvZbY9TlUKJRqIeqoIsJIzeWCaRktwBI/edit#slide=id.p)

