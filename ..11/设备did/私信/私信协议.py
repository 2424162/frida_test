import frida, sys

jscode = '''
Java.perform(function () {
    console.log("kaishi")
        var c = Java.use('com.kwai.chat.g') ;

    c.k.overload().implementation = function () {
        var re =this.k() 
        console.log(this.p.value)
         this.p.value = "3213213"
       // console.log(cc);
        console.log(re);
        return re;

       

    }
    var re =this.sendMsg() 
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