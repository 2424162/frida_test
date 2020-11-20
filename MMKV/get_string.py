import frida, sys

jscode = '''
console.log("kaishi");

function showStacks(){

    console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new()))
}
Java.perform(function () {
    var qphoto = Java.use('com.tencent.mmkv.MMKV');
    qphoto.getString.overload('java.lang.String','java.lang.String').implementation = function (str1,str2) {
    //showStacks();
        var re = this.getString(str1,str2) ;



        console.log("参数1:"+str1);
        console.log("参数2:"+str2);

        console.log('结果值:'+re);

      //var str1='vvvvvvvvvvvvv';
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

