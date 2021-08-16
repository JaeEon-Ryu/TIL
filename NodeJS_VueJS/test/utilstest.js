const util = require('util');
const utils = require('../utils');

let map = utils.makeMap('name','hong');
util.log('map>>>>>>>>>>>>',map.get('name'));

return;

let str = "NodeJS";

let enc2 = utils.encrytSha2(str);
util.log("enc=",enc2);
let enc = utils.encrypt(str);
util.log("enc=",enc);
let dec = utils.decrypt(enc);
util.log("enc=",dec);

return;

let url = 'https://naver.com';

utils.ogsinfo(url, (err,ret) =>{
    util.log(err,ret);
});