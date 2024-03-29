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
 
+ ### MySQL 정리
  + #### DCL, DDL 관련
  ```
  # A와 같은 구조의 테이블 만들기
    create table <table-name> like A;
  # A와 같은 구조, 같은 데이터의 테이블 만들기
    create table <table-name> AS
      select * from A;
    
  show create table <table-name>
  truncate table <table-name>
  drop table <table-name>
  ```
  
  <br>
  
  + #### DML, TCL 관련
  ```
  # insert
    insert (ignore) into table ~
  
  # select
    select * from table ~
    
  # update
    update table set ~
    
  # delete
    delete from table
    truncate table
  
  # commit, rollback
    Session 단위로 Tx 제어
    start transaction - commit or rollback
    DDL에 대해서는 Rollback 적용 X
  
  # savepoint
    start transaction;
    savepotint x
    rollback to savepotin x; 
  ```

  <br>
  
  + #### View, Trigger, Function, Procedure
  ```
  # View ( not Updatable )
    CREATE VIEW <view-name> AS
      SELECT …  ;

     장점 : 보안성, 간결성, 성능 등

  # Trigger
   특정 테이블에 INSERT, DELETE, UPDATE 같은 DML 문이 수행되었을 때, 
   데이터베이스에서 자동으로 동작하도록 작성된 프로그램
   
  # Function
    사용자가 임의로 작성한 함수
    반드시 값을 리턴해야 함
    작성시 권한 필요
    
  # Procedure
    Transact-SQL 문장의 집합
    어떠한 동작을 절차적 일괄처리 작업하는데 사용
    SQL Server에서 사용하는 프로그래밍 기능
    
    장점 : 성능, 유지보수, 모듈화, 절차적 배치 작업 등
  ```

<br>

+ ### {Tip&Tech - linux} getopts, getopt - 셸 스크립트에 프로다운 우아한 옵션 주기
  + #### 셸 스크립트나 함수가 파라미터(argument)를 받는 기본 방식
  ```
  $@ 	: 모든 옵션(파라미터)           $1, $2, ...     첫 번째 파라미터, 두 번째 파라미터, ....
  $#  : 파라미터의 개수               shift n	
  ```
  + #### getopts
  ```
  option_string 	옵션을 정의하는 문자, 뒤에 콜론(:)이 있으면 옵션값을 받는 다는 의미 (d:u:f:h)
  varname         옵션 명(d,u,f,h)을 받을 변수, OPTARG 변수에는 실제 옵션의 값이 세팅됨!!
  ```
  + #### getopt
  ```
  shortopts		    옵션을 정의하는 문자
  longopts		    긴 옵션을 정의하는 문자 (--diffs와 같은 긴 옵션 정의) ,(콤마)로 구분한다.
  progname        오류 발생시 리포팅할 프로그램 명칭(현재 셸 스크립트 파일명)
  parameters      옵션에 해당하는 실제 명령 구문(보통은 모든 파라미터를 뜻하는 $@ 사용)
  ```
  + #### 시스템 명령 등록
  ```
  o.bashrc나 .bash_profile 에 해당 셸 스크립트의 alias를 주어 등록
    ex)    alias datefmt='/root/bin/datefmt.sh'
  ```

<br>

+ ### MySQL - With - CTE 로 복잡한 쿼리도 쉽게 코딩하자
  + #### With - CTE
  ```
  MySQL 8.0+, ANSI-SQL99, 메모리에 임시 결과 셋으로 올려놓고 재사용!  (cf. View, Function)

  장점 : 순서에 의한 절차적으로 작성 → 작성하기 쉽고, 읽기 쉽다!
  
  WITH [RECURSIVE]
      cte_name [(col_name [, col_name] ...)] AS (subquery)
      [, cte_name [(col_name [, col_name] ...)] AS (subquery)] 
  select * from cte_name;


  ! MySQL의 CTE에는 아래와 같이 2가지 CTE를 제공함
   1) Common Table Expressions (기본 CTE)
     - 순차적으로 쿼리 작성 가능
   2) Recursive Common Table Expressions (재귀 CTE)
     - 스스로 추가적인 Row를 생성할 수 있음 
  ```

+ ### MySQL - JSON 데이터 타입 사용하기
  + #### Json 데이터 다루기
  ```
  JSON : JavaScript Object Notation
  데이터 = 정형 데이터 + 비정형 데이터
   - 비정형 데이터의 필요성 급증
   - 비정형 데이터를 마치 정형 테이블 처럼!
    (정형 테이블과 비정형 데이터의 조인?)
  MySQL JSON Data Type is
   - Same as LONGBLOB, LONGTEXT
   - Access directly
     (by key or array index)
   - Very Fast, More Efficiently
     (use JSON Function)
   - Returning JSON format directly
             c.f. MySQL X DevAPI
  ```
  + #### Functions  
  <img src="https://user-images.githubusercontent.com/52907116/127808379-9da4033f-7c0a-411d-a186-82f9c793804e.png" width="70%" >    
 
  <br>
  
+ ### MySQL - Tip&Tech:Rollup & Pivot
  + #### Rollup
  ```
  ROLLUP을 활용하면 GROUP BY에서 선택한 기준에 따라 합계가 구해짐
  MySQL에서는 WITH ROLLUP을 사용
  ```
  + #### Pivot
  ```
  row와 column의 위치 교체 가능
  집계함수인 Avg를 Group by절과 함께 사용 시, 이미 평균 값을 한 컬럼 내에 정의할 수 있음
  UNION을 써가며 행 추가
  ```
  
  <br>
  
+ ### MySQL - 데이터 모델 설계
  + #### DB Modeling
  ```
  개념적(Conceptual, Contextual) 모델링
    → Entity 도출

  논리적(Logical) 모델링
    → Data 구조 및 속성 정의
    → 무결성 정의 및 정규화(Normal Form, NF)

  물리적(Physical) 모델링
    → Schema, Table, Index 생성
  ```  
  
  + #### 정규화
  ```
  중복 데이터를 없애고 관계를 단순하게 가져 가기 위함
  ```  

  + #### 모델링 요령
  ```
  1.  PK (기본키)가 가장 중요함
      유일값을 갖는 기본키 필수
      변경이 없는 안정적인 값 ( null X )
      가능한 1개 컬럼, 실수형 보다는 정수형 (자동증가 컬럼)

  2.  적절한 정규화를 할 것
      1NF(원자성)을 준수하고 최대한 중복 데이터가 없도록 함
      계산 결과 컬럼을 최대한 자제함
      Nullable 할 필요가 없다면 Not Null로 할 것

  3.  참조(데이터) 무결성을 위해 FK를 정의

  4.  서로 다른 성격의 컬럼들은 테이블 분리
  ```  
  
  + #### MySQL WorkBench에서 EERD 그리기 ( 데이터 모델 )
  <img src="https://user-images.githubusercontent.com/52907116/128361382-f79b97be-9ef7-496f-9969-6946f301ec41.png" width="50%" >    

  <br>
  
+ ### MySQL - X DevAPI를 이용한 NoSQL 구현 및 채팅 데이터 모델 구성
  + #### MySQL X-DevAPI 를 쓰는 이유
  ```
  배경 : 클라우드와 빅데이터의 시대가 도래함에 따라 비정형 데이터가 많아짐
  만약 RDBMS와 NoSQL DBMS를 같이 사용한다면?
    -> 개발하기 어려움
    -> 백업과 복구를 각각 해야함
    -> 운영, 장애, 점검 등 모든것이 두 배가 됨
    -> 데이터가 나누어져 있어 서버 애플리케이션 코드가 복잡해지고,
      서로 조인이 바로 되지 않아 data mapping이 번거로우며, Transaction 처리가 힘들어짐
  ```   
  
  + #### info
  ```
  실제로 서버가 없는 구조는 아님
    -> 서버에서 처리하는 작업을 클라우드 기반의 서비스로 처리
    -> 서부 구축 및 관리 비용을 줄이는 구조
  따라서 
    1. 개발 기간과 비용 단축 가능
    2. 서버 운영과 유지 보수의 어려움을 줄일 수 있음
    3. 플랫폼 종속에서 벗어날 수 있음
  ```
  
  + #### PaaS의 장점
  ```
  인프라를 서비스로 제공함으로써 PaaS는 IaaS와 같은 장점을 제공함
  But, 미들웨어, 개발 도구, 기타 업무 도구 등의 추가기능은 다음과 같은 장점을 추가로 제공함
  1. 코딩 시간 단축 ( 미리 코딩된 앱 구성 요소 기본 제공 )
  2. 직원 추가 없이 개발 능력 추가
  3. 모바일을 비롯한 여러 플랫폼용으로 더 쉽게 개발
  4. 저렴하게 정교한 도구 사용
  5. 지리적으로 분산된 개발 팀 지원
  6. 애플리케이션 수명 주기를 효율적으로 관리
  ```   

  + #### Transaction
  ```
  session.startTransaction()
  session.rollback()
  session.commit() 
  session.setSavepoint('tx-id')
  session.rollbackTo('tx-id')
  ```   
  
  + #### tip
  ```
  MongoDB 데이터를 그대로 MySQL에 불러올 수 있는 기능을 제공함 ( 파이썬 언어 지원 )
  ```  
  
  + #### 채팅 구현
  <img src="https://user-images.githubusercontent.com/52907116/128585287-e06a3ece-fabe-4f78-8f43-9331e7c79def.png" width="30%" ><img src="https://user-images.githubusercontent.com/52907116/128585288-0223134e-8502-4b14-ab94-0ed2140931ad.png" width="60%" >    
  
  <br>
  
+ ### MySQL 성능 향상 기법 - 인덱스(Index), Fulltext Search, 파티션(Partition)
  + #### 인덱스
  ```
  컬럼의 값과 해당 레코드가 저장된 주소를 키와 값의 쌍으로 인덱스를 만들어 두는 것
  ```  
  ```
  클러스터(Clustered) 인덱스는 데이터 파일과 직접 연관
  데이터 크기가 너무 클 경우 : 페이지 분할이 빈번하여 쓰기 성능 절하됨
  카디널리티(Cardinality)가 높을수록 유리함
  cluster index : 읽기 성능은 보조 인덱스보다 빠르지만 쓰기는 느림
  페이지 분할은 시스템 부담
  다중 컬럼 인덱스는 순서를 고려해서 할 것
  인덱스는 꼭 필요한 것만 할 것 
  전체 테이블의 10~15% 이상을 읽을 경우 보조 인덱스 사용 X
  ```  
  + #### Sargable(Search ARGument ABLE) Query
  ```
  where, order by, group by 등에는 가능한 index가 걸린 컬럼을 사용 할 것
  범위 보다는 in 절을 사용하는 게 좋고, in 보다는 exists가 더 좋음
  꼭 필요한 경우가 아니라면 서브 쿼리보다는 조인(Join)을 사용 할 것
  
  Sargable 하지 않은 경우
  1. where 절에 함수, 연산, Like(시작 부분 %)문
  2. between, like, 대소비교(>, < 등)의 범위가 클 경우
  3. or 연산자 ( 필터링의 반대 개념, 즉 로우수를 늘려가는 개념이므로 )
  4. offset이 길어질 경우
  ```  
  + #### Fulltext Search
  ```
  OPTIMIZE TABLE
  저장된 단어들을 INFORMATION_SCHEMA.INNODB_FT_INDEX_TABLE에서 확인해 볼 수 있음
  ```  
  ```
  Search Expression
    *   Partial Search
    +   Required Search
    -   Excluded Search
  ```  
  + #### 파티션
  ```
  MySQL 서버 입장 : 데이터를 별도의 테이블로 분리해서 저장
  사용자 입장 : 하나의 테이블로 읽기와 쓰기를 할 수 있음
  
  장점
  1. INSERT와 범위 SELECT의 빠른 처리
  2. 주기적으로 삭제 등의 작업이 이루어지는 이력성 데이터의 효율적인 관리
  3. 데이터의 물리적인 저장소를 분리
  ```
  ```
  8,192개까지 가능
  FK 지정 불가
  PK를 지정할 경우 PK가 Partition Key
  ```  

<br>

#### reference  
##### [시니어코딩 - {SSAC} 스타트업 풀스택 개발자 과정](https://www.youtube.com/watch?v=Y__GznCpioo&list=PLEOnZ6GeucBWaUzqrMvrl-_ernhNwLHOr&ab_channel=%EC%8B%9C%EB%8B%88%EC%96%B4%EC%BD%94%EB%94%A9indiflex)  
##### [시니어코딩 - Linux 실무](https://docs.google.com/presentation/d/1S2WtAXDpFNzWG72AOMnAfPJCrTXmf1TjNxrFLNgosy4/edit#slide=id.gab11b71d47_0_93)  
##### [시니어코딩 - Linux 기본 명령어](https://docs.google.com/presentation/d/1CrOcTTrRRHlredMRwie9WKSo7ChIF4bRylvUxhinRYU/edit#slide=id.p)  
##### [시니어코딩 - MySQL 실무](https://docs.google.com/presentation/d/1fhtpdjbIPi0fvZbY9TlUKJRqIeqoIsJIzeWCaRktwBI/edit#slide=id.p)
##### [카카오 다니는 개발자 아저씨 '김용환' - getopt() 함수](https://knight76.tistory.com/entry/30026565533)

