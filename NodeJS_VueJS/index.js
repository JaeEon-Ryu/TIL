const express = require('express'); // 웹서버
const app = express(),
      testJson = require('./test/test.json');
      
app.use(express.static('public')); // public 디렉토리를 static으로
app.set('views', __dirname + '/views');
app.set('view engine', 'ejs');
app.engine('html', require('ejs').renderFile);

app.get('/', (req, res) => {
    //res.send("Hello NodeJS!!");
    res.render('index', {name: '홍길동'});

});

app.get('/test/:email', (req, res) => {
    testJson.email = req.params.email;  // cf. req.body, req.query
    testJson.aa = req.query.aa;
    res.json(testJson);
});

const server = app.listen(7000, function(){
    console.log("Express's started on port 7000");
});



// app.get('/', (req, res) => {
//     // res.send("Hello NodeJS!!");
//     res.render('index', {name: '홍길동'});
//   });
  

