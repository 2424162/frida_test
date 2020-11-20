"""
function_target.py

"""

import frida, sys

jscode = '''
console.log("kaishi");
function showStacks(){
    console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new()))
}


Java.perform(function () {

    var vader = Java.use("com.kuaishou.android.vader.d.d$a")
    vader.run.implementation = function () {
        var re = this.run();

        //send(str);
        //send(str2);
        showStacks();
        

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