import frida,sys

jscode = '''
console.log("kaishi");
function showStacks(){

    console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new()))
}
Java.perform(function () {

    var qphoto = Java.use('com.yxcorp.retrofit.f');
    qphoto.a.overload('okhttp3.Request', 'java.util.Map', 'java.util.Map', 'java.lang.String').implementation = function (str,str2,str3,str4) {

        var re = this.a(str,str2,str3,str4) ;
        console.log(str2)
        console.log(str3)
        
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