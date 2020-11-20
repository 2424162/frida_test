import frida, sys

# .overload('java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String')
jscode = '''
Java.perform(function () {
    console.log("kaishi");
    var c = Java.use('org.chromium.net.impl.CronetUrlRequestContext') ;
    c.openConnection.overload('java.net.URL', 'java.net.Proxy').implementation = function (str1,str2) {
        var openConnection = this.openConnection(str1,str2) ;

        send("Hook成功!");
        console.log(str1);

        //console.log(this.f7284a);
        console.log("++++");
        //console.log(re);


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