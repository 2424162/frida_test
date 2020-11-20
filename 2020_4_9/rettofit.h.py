import frida,sys

jscode = '''
console.log("kaishi");
Java.perform(function () {
    var qphoto = Java.use('com.yxcorp.gifshow.retrofit.h');
    var h = qphoto.$new();
    var hh = qphoto.computeSignature();
    console.log(hh);

});
'''

def on_message(message, data):
    print(message)
    if message['type'] == 'send':
        print(message['payload'])
    else:
        print(message)

process = frida.get_remote_device()#.attach("com.smile.gifmaker")
process  = process.attach('com.smile.gifmaker')
script = process.create_script(jscode)
script.on("message",on_message)
script.load()
sys.stdin.read()