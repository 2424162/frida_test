import frida, sys

jscode = '''
console.log("kaishi");
Java.perform(function () {
    var qphoto = Java.use('com.yxcorp.utility.singleton.a');
    var qc = Java.use("com.yxcorp.gifshow.entity.QCurrentUser")
    qphoto.a.overload('java.lang.Class').implementation = function (str1) {
        var re = this.a(str1) ;
        var mp = qc.mPrefs;



        //send("Hook成功!");
        console.log("a.class的值:"+str1);

        //console.log(str3);
        //console.log(str4);
        console.log("返回值:"+re);
        console.log("mPerfs的值:"+mp);
        console.log("hahahhah"+qc.mService);
        //send(""+re)
        console.log("+++++++++");
        var cc = this.f7284a;
        console.log("构造参数:",cc)
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