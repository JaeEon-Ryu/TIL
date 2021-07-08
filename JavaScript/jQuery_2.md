## jQuery 정리 2

<br>

### JAX (Asynchronous JavaScript and XML) : Parameter
``` javascipt
var URL = "http://berryservice.net:8080/Berry/g/tests/",
    p = { cmd: "test-by-icode", icode: 3 };
$.ajax({
    url: URL,
    type: "GET",
    data: p,
    dataType : "json"

}).done(function( json ) {
    var content = JSON.stringify(json, null, "  ");
    $("<pre class=\"content\">").html(content).appendTo("body");

}).fail(function( xhr, status, errorThrown ) {
    console.error("Sorry, there was a problem!", status);
}).always(function( xhr, status ) {
    console.log( "The request is complete!", URL + '?' + $.param(p));
});
```

<br>

### AJAX (Asynchronous JavaScript and XML) : POST
``` javascipt
var URL = "http://berryservice.net:8080/Berry/g/tests/";
$.ajax({
    url: URL,
    data: { name: "test333-1", icode: 3 },
    type: "POST",
    dataType : "json"

}).done(function( json ) {
    var content = JSON.stringify(json, null, "  ");
    $("<pre class=\"content\">").html(content).appendTo("body");

}).fail(function( xhr, status, errorThrown ) {
    console.error("Sorry, there was a problem!", status);
}).always(function( xhr, status ) {
    console.log( "The request is complete!" );
});
```

<br>

### AJAX (Asynchronous JavaScript and XML) : DELETE
``` javascipt
var test28_url = "http://berryservice.net:8080/Berry/g/tests/28";
$.ajax({
    url: test28_url,
    type: "DELETE"

}).done(function( json ) {
    var content = JSON.stringify(json, null, "  ");
    $("<pre class=\"content\">").html(content).appendTo("body");

}).fail(function( xhr, status, errorThrown ) {
    console.error("Sorry, there was a problem!", status);
}).always(function( xhr, status ) {
    console.log( "The request is complete!" );
});
```

<br>

### reference 
[시니어코딩indiflex - jQuery 한방에 정리하기 2](https://www.youtube.com/watch?v=w2ULuAO7NUY&list=PLEOnZ6GeucBWCR_eYjmKuFykGAQylAl9M&index=7)  
[시니어코딩indiflex - 강의 슬라이드](https://docs.google.com/presentation/d/12tfiKPdr64z6Eo_7soZAXG3vo54qeEv0B2I0_vmWE00/edit)
