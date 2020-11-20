import frida, sys

jscode = '''
console.log("开始");
function showStacks(){

    console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new()))
}
Java.perform(function () {
    var qphoto = Java.use('com.yxcorp.gifshow.KwaiApp');
    qphoto.getApiService.implementation = function () {
        var re = this.getApiService() ;
        showStacks();


        //console.log(str);
        //console.log("+++++++++");
        //console.log(str3);
        //console.log(str4);
        //console.log("--"+re);
        //console.log(this.f7284a)
        console.log(re);

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