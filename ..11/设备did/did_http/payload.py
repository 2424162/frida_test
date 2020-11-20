import frida, sys

jscode = '''
Java.perform(function () {
    console.log("kaishi")
    var c = Java.use('com.kuaishou.android.vader.persistent.LogRecord') ;
    c.payload.implementation = function () {

        var re =this.payload()
        
        
        re[4]=200
        re[5]=1
        console.log(re[2])
        console.log(re[4])
        console.log(re[5])
        send(re)
        
        console.log("-------");
        
        return re;
       

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