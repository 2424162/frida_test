import frida, sys

jscode = '''
console.log("kaishi");
Java.perform(function () {
    var qphoto = Java.use('com.smile.gifshow.annotation.a.a');
    qphoto.getInstance.implementation = function () {
        var re = this.getInstance() ;

        //send("Hook成功!");
        //console.log(str1);
        //console.log("+++++++++");
        //console.log(str3);
        //console.log(str4);
        //console.log("--"+re);
        //console.log(this.f7284a)
        send("完");
        console.log(re);
        send(re);

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