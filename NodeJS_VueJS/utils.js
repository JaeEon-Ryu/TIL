const ogs = require('open-graph-scraper'),
    HashMap = require('hashmap'),
    Crypto = require('crypto-js'),
    SHA256 = ("crypto-js/sha256");

const EKey = "nodevue";
module.exports = {

    makeMap(key,value){
        const map = new HashMap();
        map.set(key,value);
        console.log("TTT>>",map.get(key))
        return map;
    },

    encrytSha2(data,key){
        if (!data) return null;
        key = key || EKey;

        try {
            return Crypto.SHA256(data + key).toString();
        }catch(Err){
            console.error("Error on encrytSha2::",err);
        }
    },

    encrypt(data,key){
        return Crypto.AES.encrypt(data,key || EKey).toString();
    },

    decrypt(data,key){
        return Crypto.AES.decrypt(data,key || EKey).toString(Crypto.enc.Utf8);
    },

    ogsinfo(url, fn){
        return ogs({url: url}, (err, ret) => {
            fn(err, ret);
        });
    }

};



