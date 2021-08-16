const Promise = require('bluebird');

module.exports = class {
    constructor(pool) {
        this.pool = pool;
    }

    execute(fn) {
        Promise.using( this.pool.connect(), conn => {
            fn(conn);
        });
    }

    executeTx(fn) {
        Promise.using( this.pool.connect(), conn => {
            conn.beginTransaction( txerr => {
                fn(conn);
            });
        });
    }
};