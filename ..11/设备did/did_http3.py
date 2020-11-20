import frida, sys


jscode = '''
Java.perform(function () {
    console.log("kaishi")
        var c = Java.use('com.kwad.sdk.protocol.c.b') ;

    c.a.overload('[B', '[B', 'java.lang.String').implementation = function (str,str2,str3) {

        var re =this.a(str,str2,str3) 
        console.log(str)
        send(str)
        console.log(str2)
        send(str2)
        send(re)
        console.log(str3)
        console.log(re);
        return re;

        console.log("-------");

    }
});
'''

loistss = []


def on_message(message, data):
    if message['type'] == 'send':
        loistss.append(message['payload'])
        print(message['payload'])

    else:
        print(message)


process = frida.get_remote_device()  # .attach("com.smile.gifmaker")
process = process.attach('com.smile.gifmaker')
script = process.create_script(jscode)
script.on("message", on_message)
script.load()
sys.stdin.read()