"""
function_target.py

"""

import frida, sys

jscode = '''
console.log("kaishi");
Java.perform(function () {

    var b = Java.use('[B');
    var ac = Java.use('android.app.Activity');
    
    var act = Java.cast("arrcc",b);
    //console.log(act);
   // console.log(b);
   // var ba = Java.array('byte',[11,22,33,555]);
    //console.log(ByteArrayString(ba));
    
    

 

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