import frida, sys

jscode = '''
console.log("kaishi");
Java.perform(function () {
    var qphoto = Java.use('com.yxcorp.utility.d.c');
    qphoto.b.overload().implementation = function () {
    console.log("开始");
    console.log("mService的值:");
        var re = this.b();

        //send("Hook成功!");


        //console.log("+++++++++");
        //console.log(str);
        //console.log(str4);
        //console.log("--"+re);
        //console.log(this.f7284a);
        send("完");
        console.log(re);
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