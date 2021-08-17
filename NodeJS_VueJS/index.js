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

const io = require('socket.io')(server, {
    log: false,
    origins: '*:*',
    pingInterval: 3000,
    pingTimeout: 5000
});

io.sockets.on('connection', (socket, opt) => {
    socket.emit('message', {msg: 'Welcome ' + socket.id});

    util.log("connection>>",socket.id, socket.handshake.query)

    socket.on('join',function(roomId, fn) {
        socket.join(roomId, function() {
            util.log("Join",roomId,Object.keys(socket.rooms))
            if (fn)
                fn();
        });
    })

    socket.on('leave',function(roomId, fn) {
        socket.leave(roomId,function(){
            if (fn)
                fn();
        });
    });

    socket.on('rooms',function(fn) {
        if (fn)
            fn(Object.keys(socket.rooms));
    });

    socket.on('message', (data, fn) => {
        util.log("message>>", data.msg, Object.keys(socket.rooms));
        fn(data.msg);
    });

    socket.on('disconnecting',function(data) {
        util.log("disconnecting>>", socket.id, Object.keys(socket.rooms))
    })

    socket.on('disconnect',function(data) {
        util.log("disconnect>>", socket.id, Object.keys(socket.rooms))
    })

});



// app.get('/', (req, res) => {
//     // res.send("Hello NodeJS!!");
//     res.render('index', {name: '홍길동'});
//   });
  

