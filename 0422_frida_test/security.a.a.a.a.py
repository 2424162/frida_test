"""
function_target.py

"""

import frida, sys

jscode = '''
console.log("kaishi");
function ByteArrayString(byteArray){

var str = "";
var barr = new Uint8Array(byteArray);
for(var i=0;i<barr.length;i++){
    str+=String.fromCharCode(barr[i]);
    }
    return str;

}
var shu=[1,21,1,11,5];
console.log(shu);
console.log(typeof(shu));
console.log(shu.toString());

function showStacks(){

    console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new()));
}
Java.perform(function () {

    var qphoto = Java.use('com.kuaishou.android.security.a.a.a');
    qphoto.a.overload('com.kuaishou.android.security.kfree.c.i', 'java.lang.String').implementation = function (ivar,str) {
        var re = this.a(ivar,str) ;
        var b = Java.use('[B')
        var buf = Java.cast(ivar.i(),b);
        console.log(typeof(buf))
        var sig3 = Java.array("byte",buf);
        var jstr = Java.use("java.lang.String");

     
        //console.log(haha);
        var sign = ByteArrayString(sig3);
        console.log(sign);

        //console.log(sig3);
        //showStacks();
        console.log("开始");

        
        return re;

    }
});
'''


def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)


process = frida.get_remote_device()  # .attach("com.smile.gifmaker")
process = process.attach('com.smile.gifmaker')
script = process.create_script(jscode)
script.on("message", on_message)
script.load()
sys.stdin.read()