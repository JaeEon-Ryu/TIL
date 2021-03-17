
### ‘script’ 태그
\<script> 태그를 이용하면 자바스크립트 프로그램을 HTML 문서 대부분의 위치에 삽입할 수 있음

<br>

### 모던 마크업
+ type 속성: \<script type=…>  
  HTML4에선 스크립트에 type을 명시하는 것이 필수였으나 현재는 아니며 모던 HTML 표준에선 이 속성의 의미가 바뀌었음  

+ language 속성: \<script language=…>  
  현재 사용하고 있는 스크립트 언어를 나타냄. 위처럼 현재는 쓰지 않음

<br>

### 외부 스크립트 
  자바스크립트 코드의 양이 많은 경우엔, 파일로 소분하여 저장할 수 있음  
  + 절대경로 사용 : \<script src="/path/to/script.js"></script>  
  + URL 사용 : \<script src="https://cdnjs.cloudflare.com/ajax/libs/lodash.js/4.17.11/lodash.js"></script>  
  + 복수개의 스크립트 사용 :   
    \<script src="/js/script1.js"></script>  
    \<script src="/js/script2.js"></script>  
  
<br>

    
주의! :  src 속성이 있으면 태그 내부의 코드는 무시됨
  
<br>  
<br> 

##### reference
###### [JAVASCRIPT.INFO - 자바스크립트 기본](https://ko.javascript.info/hello-world)
