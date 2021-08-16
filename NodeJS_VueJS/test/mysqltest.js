const mysql = require('mysql');

const connection = mysql.createConnection({
    host     : '',
    user     : '',
    password : '',
    database : ''
});
 
connection.connect();
 

// 이런식으로 query문을 중첩시키면 비동기 처리를 원하는 순서대로 나오게끔 할 수 있다
connection.query('select * from User where id=2',['user2'], function (error, results, fields) {
    if (error) throw error;
    console.log('The First User is: ', results[0]);

    connection.query('select * from User where id=1',['user2'], function (error, results, fields) {
        if (error) throw error;
        console.log('The First User is: ', results[0]);
    });

    connection.end();
});
 
// bluebird 모듈을 쓰면 위 방식처럼 중첩을 하지 않아도 된다

