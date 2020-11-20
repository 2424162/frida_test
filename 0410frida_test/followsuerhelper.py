import frida, sys

jscode = '''
console.log("kaishi");
Java.perform(function () {
    var qphoto = Java.use('com.yxcorp.gifshow.retrofit.c');
    //var activity = Java.use("android.app.Activity");
    qphoto.a.overload('boolean', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'int').implementatiion = function(str,str2,str3,str4,str5,str6,str7,str8,str9){
    console.log("开始");

    var re = this.a(str,str2,str3,str4,str5,str6,str7,str8,str9);
    console.log(str);
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