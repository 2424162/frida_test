"""
function_target.py

"""


import frida,sys

jscode = '''
console.log("kaishi");
function showStacks(){

    console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new()))
}

function byteToString(arr) {
if(typeof arr === 'string') {
return arr;
}
var str = '',
_arr = arr;
for(var i = 0; i < _arr.length; i++) {
var one = _arr[i].toString(2),
v = one.match(/^1+?(?=0)/);
if(v && one.length == 8) {
var bytesLength = v[0].length;
var store = _arr[i].toString(2).slice(7 - bytesLength);
for(var st = 1; st < bytesLength; st++) {
store += _arr[st + i].toString(2).slice(2);
}
str += String.fromCharCode(parseInt(store, 2));
i += bytesLength - 1;
} else {
str += String.fromCharCode(_arr[i]);
}
}
return str;
}
Java.perform(function () {

    var qphoto = Java.use('com.yxcorp.gifshow.util.CPU');
    console.log(qphoto)
    console.log(typeof(qphoto))
    
    qphoto.a.implementation = function (str,str2,str3) {
        var re = this.a(str,str2,str3) ;
        console.log("run");
        send("Hook成功!");
        send(str);
        send(str2);
        send(str3);
        send(re);
        showStacks();
        return re;
    }
});
'''

def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)

process = frida.get_remote_device()#.attach("com.smile.gifmaker")
process  = process.attach('com.smile.gifmaker')
script = process.create_script(jscode)
script.on("message",on_message)
script.load()
sys.stdin.read()