const fs = require('fs');
const util = require('util');

//console.log('aaaaaaaaaaa')
//util.log('bbbbbbbbb', __dirname)

fs.readFile(__dirname + '/test.json', 'utf-8', (err, data) => {
    if (err) return console.error(err);

    util.log("data>>", data);
});

util.log("------------------------");

const msgfile = __dirname + '/message.txt';
fs.writeFileSync(msgfile, 'Hello Node.js 세종대왕!!', (err) => {
    if (err) throw err;
    console.log('The file has been saved!');
});

let data2 = fs.readFileSync(msgfile, 'utf-8');
util.log("data2>>", data2);

util.log("===================================");
