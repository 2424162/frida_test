import frida, sys

jscode = '''
console.log("kaishi");
Java.perform(function () {
    var qphoto = Java.use('com.smile.gifshow.annotation.a.a');
    qphoto.getInstance.implementation = function () {
        send("Hook成功!");
        var re=this.getInstance();
        //onsole.log("_____"+str1);
        //send(this.mPrefs);
        //send(this.mService);.
        //console.log(str1);
        //console.log(str2);
        //console.log(str3);
        //console.log(str4);
        
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