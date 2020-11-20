import frida,sys

jscode = '''
console.log("kaishi");
Java.perform(function () {
    
    var qphoto = Java.use('com.yxcorp.gifshow.retrofit.h');
    var pair = Java.use("android.util.Pair");
    qphoto.computeSignature.implementation = function (str1,str2,str3) {
        var re = this.computeSignature(str1,str2,str3) ;
        send("Hook成功!");
        console.log(str1);
        console.log(str2);
        console.log(typeof(str3));
        console.log(str3.keySet());
        console.log(typeof(str3));
                console.log(str2.keySet());
        console.log(typeof(re));
        console.log("---------------------");

        
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
