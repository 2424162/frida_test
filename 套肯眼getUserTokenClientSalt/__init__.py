import frida, sys

jscode = '''
console.log("kaishi");
Java.perform(function () {
    var context = Java.use('com.yxcorp.gifshow.retrofit.m$1')
    var qphoto = Java.use('com.yxcorp.gifshow.util.CPU');
    context.getUserTokenClientSalt.implementation = function () {


        var re = this.getUserTokenClientSalt() ;

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


process = frida.get_remote_device()  # .attach("com.smile.gifmaker")
process = process.attach('com.smile.gifmaker')
script = process.create_script(jscode)
script.on("message", on_message)

script.load()
sys.stdin.read()