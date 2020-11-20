"""
function_target.py

"""

import frida, sys

jscode = '''
console.log("kaishi");
function showStacks(){

    console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new()));
}
Java.perform(function () {

    var qphoto = Java.use('com.kwai.chat.messagesdk.client');
    showStacks();
    qphoto.a.implementation = function () {
        var re = this.a() ;
        console.log("run");

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