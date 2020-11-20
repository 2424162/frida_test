import frida, sys

jscode = '''
console.log("kaishi");
Java.perform(function () {
    var qphoto = Java.use('com.yxcorp.utility.l.a');
    qphoto.a.overload('java.lang.String', 'java.lang.String', '[Ljava.lang.Object;').implementation = function (str1,str2,str3) {
        var re = this.a(str1,str2,str3) ;
        send("Hook成功!");
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