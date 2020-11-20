import frida, sys

# .overload('java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String')
jscode = '''
Java.perform(function () {
    console.log("kaishi")
    var c = Java.use('com.yxcorp.gifshow.KwaiApp') ;
    
    var inst = c.$new();
    inst.getApiService()

    c.a.overload('com.yxcorp.gifshow.entity.QPhoto', 'boolean', 'java.lang.String', 'java.lang.String', 'java.lang.String').implementation = function (str,str2,str3,str4,str5) {




        send(str);
        send(str2);
        send(str3);
        send(str4);
        send(str5);
        var re = this.a(str,str2,str3,str4,str5) ;
        send("Hook成功!");
        send(re)
        return re;
    }
});
'''


def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)


process = frida.get_remote_device()  # .attach("com.smile.gifmaker")
process = process.attach('com.smile.gifmaker')
script = process.create_script(jscode)
script.on("message", on_message)
script.load()
sys.stdin.read()