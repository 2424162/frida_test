import frida,sys

jscode = '''
console.log("kaishi");
function showStacks(){

    console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new()))
}
Java.perform(function () {
    var qphoto = Java.use('com.yxcorp.gifshow.retrofit.h');
    qphoto.computeSignature.implementation = function (str1,str2,str3) {
        var re = this.computeSignature(str1,str2,str3) ;
        var pair = Java.use("android.util.Pair");
        showStacks();
        console.log("++++++++");
        send("Hook成功!");
        console.log(str1);
        console.log(str2);
        console.log(str3);
        console.log(typeof(str3))
        console.log(re);
        var repa = Java.cast(re,pair);
        console.log("++++++++");
        console.log(typeof(repa));
        console.log(repa.getMethods());
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

process = frida.get_remote_device()#.attach("com.smile.gifmaker")
process  = process.attach('com.smile.gifmaker')
script = process.create_script(jscode)
script.on("message",on_message)
script.load()
sys.stdin.read()