import frida, sys

jscode = '''

function showStacks(){


    console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new()))
}
Java.perform(function () {
console.log("开");
    var qphoto = Java.use('com.kuaishou.android.security.a.a.a');
    qphoto['a'].overload('com.kuaishou.android.security.kfree.c.i', 'java.lang.String').implementation = function (str1,str2) {
        console.log("kaishi");
        var b = Java.use("[B");
        var buff = Java.cast(iVar.i(),b);
        var barr = java.array('byte',buff);
        console.log("barr:"+barr);
        var re = this.a(str1,str2) ;
        console.log("参数1:"+str1);
        console.log("参数2:"+str2);
        //console.log(str3);
        //console.log(str4);
        console.log('结果值:'+re);


        return re;
    }
});
'''


def on_message(message, data):
    print(message)
    if message['type'] == 'send':
        print(message['payload'])
    else:
        print(message)


process = frida.get_remote_device()  # .attach("com.smile.gifmaker")
process = process.attach('com.smile.gifmaker')
script = process.create_script(jscode)
script.on("message", on_message)
script.load()
sys.stdin.read()

# frida-trace -U -i "getStringValue" com.smile.gifmaker