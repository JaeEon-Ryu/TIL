## 구현 화면

<img src="https://user-images.githubusercontent.com/52907116/124490611-47694100-dded-11eb-8a51-8d91710719a0.png" width="70%" height="70%"><img src="https://user-images.githubusercontent.com/52907116/124490626-4b955e80-dded-11eb-973e-13422947654d.png" width="30%" height="30%">


## 구현 목록

<br>

1. photo 앱 만들기  
2. 모델 설계하기  
3. views 설계하기  
  3-1. list페이지  
  3-2. 상세페이지  
  3-3. 삭제하기  
  3-4. 수정하기  
  3-5. 생성페이지  
4. url 연결시켜주기  
5. template 만들기  
  5-1. create/list/update/delete/detail  
6. 사진 업로드 할 수 있도록 만들기  
7. success url을 get_absolute_url로 연동시켜보기  
8. account 앱 만들기  
  8-1. 로그인/로그아웃 기능 구현하기  
  8-2. 로그아웃 되었을 때는 create 및 sign out가 안 보이도록 구현하기(분기)  
9. 권한 문제 해결하기  
  9-1. html 기준에서 해결하기  
  9-2. 링크로 들어와도 안 되도록 해결해보기   
    &nbsp; &nbsp; 9-2-1. view를 조정하기   
10. 댓글 기능 구현하기  
  10-1. 댓글은 상세페이지에서 가능하도록 하기  
  10-2. 소셜 댓글기능으로 구현하기  
11. 좋아요 버튼 만들기  
  11-1. 스프라이트 이미지 기법 활용하기  
  11-2. 클릭하면 색깔 바뀌도록 구현하기  
  11-3. 로그인을 해야지 버튼 클릭이 되도록 하고 클릭을 하면 like count 올라가기  
  11-4. like에 대한 정보를 저장하기  
  11-5. 좋아요 counting 표시해주기  
  11-6. 디테일 페이지에서 좋아요를 누르면 디테일 페이지에서 그대로 유지하도록 하기   
    &nbsp; &nbsp; 11-6-1. view와 like에서의 분기  
    &nbsp; &nbsp; 11-6-2. 레퍼러를 활용하여 해당 주소가 어디서부터 시작됐는지 확인
12. 좋아요한 포스팅만 보기 기능 구현하기  
13. 포스팅 저장하기 기능 구현하기  
14. 저장한 포스팅 리스트 페이지 구현하기  
15. 모델 폼을 통해 회원가입 기능 구현하기  
  15-1. views를 통해 로직 구현하기  
    &nbsp; &nbsp; 15-1-1. POST형태로 받을 때와 처음 실행할 때 화면 구현   
    &nbsp; &nbsp; 15-1-2. render의 특징  
    &nbsp; &nbsp; 15-1-3. POST형태의 데이터 저장하기  
  15-2. 템플릿 만들기  
  15-3. url 연결하기  
  15-4. 비밀번호 암호화하기  
  15-5. forms.py를 구현하여 views.py를 간락햐게 만들기  
    &nbsp; &nbsp; 15-5-1. forms.py 오버라이딩하기  
    &nbsp; &nbsp; 15-5-2. views.py 간략히 수정하기  
    &nbsp; &nbsp; 15-5-3. 중복 입력 받기(commit=False)  
    &nbsp; &nbsp; 15-5-4. signup_complete에 회원가입한 사람 이름 띄어주기  
    &nbsp; &nbsp; 15-5-5. form을 통해 받은 자료 암호화하기  
  15-6. 비밀번호 재입력창 만들기  
    &nbsp; &nbsp; 15-6-1. 비밀번호 중복 확인하기  

<br>

## 참고
###### [Django 인스타그램 클론코딩](https://daeguowl.tistory.com/41?category=823041)
