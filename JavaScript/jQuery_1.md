## jQuery 정리 1

<br>

### 
``` python
# jQuery Tutorial
https://learn.jquery.com/


# jQuery
Download: https://code.jquery.com/
API Doc: https://jquery.com/
```

<br>

### 
```javascript
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.js"></script>

<script>

# 메모리에 다 올라갔는지 검사할 때
$( window ).on( "load", alert('onload!!') );

# 메모리에 모두 올라가진 않았지만 html에 그릴 수 있는 상태
$( document ).ready(function() {
	console.log( "ready!" );
	$('#err').hide();
});

</script>
```

<br>

### AJAX (Asynchronous JavaScript and XML)
```javascript
var URL= "http://berryservice.net:8080/Berry/g/tests/";

$.get(URL).then( function(json) {
    var content = JSON.stringify(json, null, "  ");
    $("<h1>").text(json.test.length).appendTo("body");
    $("<pre class=\"content\">").html(content).appendTo("body");

}, function(err) {
	console.error("Sorry, there was a problem!", err.status, err);
});

// $.get(URL)에서 서버 접속, Asyncronized이기 때문에 다음 코드 실행됨
// get(URL)이 성공하면, then 이하절이 실행된다. // 실패시 function(err)쪽 실행
// $ == jQeury instance == 메모리에 올라가있는 살아있는 객체, static한 함수
// def then(self,f1,f2):   ...
// 

// 비동기I/O == Non-Blocking I/O == Asyncronized   (cf. 동기 == Synchronized)

```

<br>

### AJAX (Asynchronous JavaScript and XML) 기본방식
```javascript
var URL = "http://berryservice.net:8080/Berry/g/tests/";

$.get(URL).done( function( json ) {
    var content = JSON.stringify(json, null, "  ");
    $("<h1>").text(json.areagroup.length).appendTo("body");
    $("<pre class=\"content\">").html(content).appendTo("body");

}).fail( function( xhr, status, errorThrown ) {
    console.error("Sorry, there was a problem!", xhr, status, errorThrown);
	console.error(">>", xhr.responseJSON);

}).always(function( xhr, status ) {
    console.log( "The request is complete!" );
});

// 성공했을 때 : done, 실패했을 때 : fail, 성공이든 실패든 무조건 실행 : always
```

<br>

### AJAX (Asynchronous JavaScript and XML)
```javascript
var URL = "http://berryservice.net:8080/Berry/g/tests/";
$.ajax({
    url: URL,
    type: "GET",
    dataType : "json"

}).done(function( json ) {
    var content = JSON.stringify(json, null, "  ");
    $("<pre class=\"content\">").html(content).appendTo("body");

}).fail(function( xhr, status, errorThrown ) {
   console.error("Error>>", xhr.responseJSON);
   var $err = $('#err');
   $err.text(xhr.responseJSON.message);
   $err.show();
}).always(function( xhr, status ) {
    console.log( "The request is complete!" );
});
```

<br>

### reference 
[시니어코딩indiflex - jQuery 한방에 정리하기 1-1](https://www.youtube.com/watch?v=kSBvMUo4GTs&list=PLEOnZ6GeucBWCR_eYjmKuFykGAQylAl9M&index=6)  
[시니어코딩indiflex - 강의 슬라이드](https://docs.google.com/presentation/d/12tfiKPdr64z6Eo_7soZAXG3vo54qeEv0B2I0_vmWE00/edit)
