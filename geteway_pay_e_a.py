import frida,sys

jscode = '''
console.log("kaishi");
Java.perform(function () {
    var qphoto = Java.use('com.yxcorp.gateway.pay.e.b');
    qphoto.a.overload().implementation = function (str,str2,str3,str4) {
        var re = this.a(str,str2,str3,str4) ;
        send("Hook成功!");
        send(str);
        send(str2);
        send(str3);
        send(re);
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