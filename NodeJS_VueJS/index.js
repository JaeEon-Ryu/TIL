const express = require('express'), 
    app = express(),
    util = require('util');

const Pool = require('./pool'),
    Mydb = require('./mydb');
const testJson = require('./test/test.json');
    
const pool = new Pool();

app.use(express.static('public')); // public 디렉토리를 static으로
app.set('views', __dirname + '/views');
app.set('view engine', 'ejs');
app.engine('html', require('ejs').renderFile);


app.get('/test/:email', (req, res) => {
    testJson.email = req.params.email;  // cf. req.body, req.query
    testJson.aa = req.query.aa;
    res.json(testJson);
});

app.get('/dbtest/:user', (req, res) => {
    let user = req.params.user;
    let mydb = new Mydb(pool);
    mydb.execute(conn => {
        conn.query("select * from User where id=1",[user],(err,ret)=>{
            res.json(ret);
        })
    });
});

const server = app.listen(7000, function(){
    console.log("Express's started on port 7000");
});



// app.get('/', (req, res) => {
//     // res.send("Hello NodeJS!!");
//     res.render('index', {name: '홍길동'});
//   });
  

