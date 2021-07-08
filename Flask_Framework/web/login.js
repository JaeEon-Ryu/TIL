function checkLogin() {
    var uid = get('userid'),
        upw = get('userpw');
    console.log(">>>>>>", uid, upw)

    var frm = document.getElementById('frm'),
        msg = document.getElementById('msg'),
        err = document.getElementById('err');
    if (uid === 'a' && upw === '1') {
        frm.style.display = 'none';
        msg.style.display = 'block';
        err.style.display = 'none';

    } else {
        err.style.display = 'block';
        frm.style.display = 'block';
    }

    return false;
}

function get(id) {
    return document.getElementById(id).value;
}