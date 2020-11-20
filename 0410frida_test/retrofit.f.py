import frida, sys

# .overload('java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String')
jscode = '''
Java.perform(function () {
    console.log("kaishi")
    var c = Java.use('com.yxcorp.retrofit.f') ;
    c.a.overload('okhttp3.Request', 'java.util.Map', 'java.util.Map', 'java.lang.String').implementation = function (str1,str2,str3,str4) {
        var re = this.a(str1,str2,str3,str4) ;

        //send("Hook成功!");
        console.log(str1);
        //console.log("+++++++++");
        console.log(str2);
        console.log(str3);
        console.log(str4);
        //console.log(this.f7284a)
        send("完");
        console.log(re);
        send(re);

        return re;
    }

});
'''

loistss = []


def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
        loistss.append(message['payload'])
        print(loistss)

    else:
        print(message)


process = frida.get_remote_device()  # .attach("com.smile.gifmaker")
process = process.attach('com.smile.gifmaker')
script = process.create_script(jscode)
script.on("message", on_message)
script.load()
sys.stdin.read()