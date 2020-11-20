import frida, sys


jscode = '''
Java.perform(function () {
    console.log("kaishi")
        var c = Java.use('com.kwad.sdk.protocol.c.b') ;

    c.a.overload('[B').implementation = function (str) {
  
        var re =this.a(str)
        send(str) 
        console.log(re)

        //return re;

        console.log("-------");

    }
});
'''

loistss = []


def on_message(message, data):
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