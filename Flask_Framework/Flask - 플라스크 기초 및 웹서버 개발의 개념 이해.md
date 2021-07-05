## 플라스크 기초 및 웹서버 개발의 개념 이해

<br>

### Install Flask & Setup Flask Project
```python
# Install flask module
$> pip install flask

# Setup Flask Project
$> mkdir webapp
	/flaskapp (helloflask)
	    - /static (정적인 파일)
          - /css
          - /images
          - /js
	    - /templates (html들이 존재하는 영역)
	    - __init__.py (모듈의 시작 지점)
	
	start_helloflask.py
  
  
  
* Web Application Server -> 동적인 웹 서버
* Web Server -> 그냥 html

* flask 가벼우면서도 powerfull - 기능은 별로 없지만, 생산성이 강함
* django - 무거움, 서버 자원을 많이 씀
```

<br>

### Hello Flask World
```python
# flaskapp/__init__.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def helloworld():
    return "Hello Flask World!"


# ../start_helloflask.py
from helloflask import app

app.run(host='0.0.0.0')


* route - url을 연결해주는 역할

* MVC - model_view_controller
  Model -> 사용자 객체 등 attribute
  View -> html, json등을 return해줄 때 보여주는 역할
  Controller -> Router

* MVVR - 요즘 MVC보다 이것을 더 선호
  R -> Router

* MVC*R

* lazyloading -> 모든 메모리를 올리지 않고 천천히 올리겠다 ( 필요할때만 )
* environment: production -> 서비스되는것 ( development 없음 )
* WSGI (WebServerGatewayInterface) : request가 오면 안내를 해주도록 함
```

<br>

### Global Object : g
```python
from flask import g

app = Flask(__name__)
app.debug = True     # use only debug!!

@app.before_request
def before_request():
    print("before_request!!!")
    g.str = "한글"

@app.route("/")
def helloworld():
    return "Hello World!" + getattr(g, 'str', '111')
    
    
* Global object : g ( from flask import g ) -> 전역변수 역할

* Application context : 모든 사람들이 공유하는 공간
* Session context : 나만 공유하는 공간

* 한개의 브라우저 -> 한개의 세션
```

<br>

### Response Objects
```python
클래스 -> 요청데이터, http코드, json(response header)
str -> response 객체로 전송 

'return 내용' 대신 'make_response(내용)' 을 쓰는 이유 :  큰 데이터일 경우 더 가볍게 전송 가능
```

<br>

### Request Event Handler
```python
@app.before_first_request 
def ... 
-> 첫 요청을 하기전 함수 실행

@app.before_request 
def ... 
-> 매 요청마다 실행 ( Model에게 전달하기 전에 )
-> ex) 예전에 매번 UTF filter를 사용할 때 사용

@app.after_request 
def ...  (response)
-> 요청을 모두 처리하고 나가기 직전에 수행

@app.teardown_request 
def ... (exception)
-> response가 다 끝나고 나서 실행

@app.teardown_appcontext
def ... (exception)
-> application context가 끝나고 나서 실행
```

<br>

### Routing
```python
@app.route('/test')
def …
-> 베이직 ( get으로 실행 )

@app.route('/test', methods=[ 'POST', 'PUT' ])
def …
-> post로 실행

@app.route('/test/<tid>')
def test3(tid):
	return "tid is %s" % tid
-> ex) 100번 게시글의 댓글들을 뽑을 때 등 
-> tid : 하나의 변수라고 생각
  
@app.route('/test', defaults={'page': 'index'})
@app.route('/test/<page>')
def xxx(page):
-> 사용자 입력이 있으면 해당 페이지를 뽑아줌
-> 그게 아닐시에는 default로 정의한 페이지로 이동
  
@app.route('/test', host='abc.com')
@app.route('/test', redirect_to='/new_test')
-> abc.com 으로 연결했을 경우, abc.com/new_test로 연결
```
  
<br>

### Routing : subdomain
```python
도메인별로 다른 처리를 할 수 있도록 나눠놓음
  
app.config['SERVER_NAME'] = 'local.com:5000'
@app.route("/")
def helloworld_local():
    return "Hello Local.com!"

@app.route("/", subdomain="g")
def helloworld():
    return "Hello G.Local.com!!!"
```
  
<br>

### Request Parameter
```python
# MultiDict Type -> Dict를 상속받은 클래스
...get('<param name>', <default-value>, <type>)
methods: get, getlist, clear, etc
  
# GET
request.args.get('q')
-> ex) http://localhost:5000/rp?q=123 의 형식으로 q에 값을 담아 전달 가능
-> 빠르지만 사이즈 제한이 있음

# POST
request.form.get('p', 123)
-> post로 보낼때는 args가 아닌 form을 써야함
-> 사이즈 제한 없음
  
# GET or POST
request.values.get('v')
-> get이든 post든 헤깔리지 않아도 된다
-> get, post 둘 다 살펴봄
  
# Parameters
request.args.getlist('qs')
-> q에 여러개를 담을 때 사용
```
  
<br>

### Request Parameter Custom Function Type
```python
from datetime import datetime, date
# request 처리 용 함수
def ymd(fmt):
    def trans(date_str):
        return datetime.strptime(date_str, fmt)
    return trans


@app.route('/dt')
def dt():
    datestr = request.values.get('date', date.today(), type=ymd('%Y-%m-%d'))
    return "우리나라 시간 형식: " + str(datestr)

```

<br>

### request.environ
```python
return ('REQUEST_METHOD: %(REQUEST_METHOD) s <br>'
        'SCRIPT_NAME: %(SCRIPT_NAME) s <br>'
        'PATH_INFO: %(PATH_INFO) s <br>'
        'QUERY_STRING: %(QUERY_STRING) s <br>'
        'SERVER_NAME: %(SERVER_NAME) s <br>'
        'SERVER_PORT: %(SERVER_PORT) s <br>'
        'SERVER_PROTOCOL: %(SERVER_PROTOCOL) s <br>'
        'wsgi.version: %(wsgi.version) s <br>'
        'wsgi.url_scheme: %(wsgi.url_scheme) s <br>'
        'wsgi.input: %(wsgi.input) s <br>'
        'wsgi.errors: %(wsgi.errors) s <br>'
        'wsgi.multithread: %(wsgi.multithread) s <br>'
        'wsgi.multiprocess: %(wsgi.multiprocess) s <br>'
        'wsgi.run_once: %(wsgi.run_once) s') % request.environ
```

<br>

### request
```python
request.is_xhr
-> xml,http 헤더 ( boolean )

request.url

request.path

request.endpoint

request.get_json()
-> json 파일 받아오기

app.config.update(MAX_CONTENT_LENGTH=1024*1024)
-> request 파일 업로드 할 때, 제한

request.max_content_length
-> 내 max_content_length를 알고 싶을 때
```

<br>

### Response Object
```python
from flask import Response

# Response Attributes
 - headers
 - status
 - status_code
 - data
 - mimetype
 
ex)
res = Response("Test")
res.headers.add('Program-Name', 'Test Response')
res.set_data("This is Test Program.")
res.set_cookie("UserToken", "A12Bc9")
```

<br>

### Cookie
```python
* Cookie : 네트워크에 정보를 보낼 때, 쿠키를 달아서 보냄 ( from client )  


from flask import Response

# Cookie __init__ Arguments # 클래스
 - key
 - value
 - max_age
 - expires
 - domain
 - path
 
ex)
res = Response("Test")
res.set_cookie("UserToken", "A12Bc9")

# other request
request.cookies.get('UserToken', 'default token')
```

<br>

### Try This: Cookie
```python
다음 형태로 요청했을때 해당 key로 Cookie를 굽는 코드를 작성하시오.
http://localhost:5000/wc?key=token&val=abc


다음과 같이 요청했을때 해당 key의 Cookie Value를 출력하는 코드를 작성하시오.
http://localhost:5000/rc?key=token
```

<br>

### Session 
```python
* Session : 서버 메모리에 떠있는 객체 (서버에 심어넣는 것)
  -> ex) 로그인 정보를 담기위해 


from flask import session

app.secret_key = 'X1243yRH!mMwf' # app의 멤버변수

OR
app.config.update(
	SECRET_KEY='X1243yRH!mMwf',
	SESSION_COOKIE_NAME='pyweb_flask_session',
	PERMANENT_SESSION_LIFETIME=timedelta(31)      # 31 days  cf. minutes=30
)

* Save to Memory, File or DB
```

<br>

### Session (Cont'd)
```python
from flask import session
@app.route('/setsess')
def setsess(): # ex) 로그인 처리
    session['Token'] = '123X'
    return "Session이 설정되었습니다!"

@app.route('/getsess')
def getsess():
    return session.get('Token')

@app.route('/delsess')
def delsess(): # ex) 로그아웃 처리
    if session.get('Token'):
        del session['Token']
    return "Session이 삭제되었습니다!"
```
  
<br>

### reference 
[시니어코딩indiflex - 파이썬 웹개발 Flask #1](https://www.youtube.com/watch?v=u2KnTZa1_WU&list=PLEOnZ6GeucBWvOGSbIKNMp6RMQL9LYRc3&index=2)  
[시니어코딩indiflex - 강의 슬라이드](https://docs.google.com/presentation/d/1S9mMlAYCulzAO8j5x9uCZbMUif8cAJHSHt1avztqeVg/edit#slide=id.p)
