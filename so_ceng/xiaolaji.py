import frida, sys

jscode = '''
Java.perform(function(){

    var nativePointer = Module.findExportByName("libcore.so", "Java_com_yxcorp_gifshow_util_CPU_getClock");
    console.log("native: " + nativePointer);
    Interceptor.attach(nativePointer, {
        onEnter: function(args){                                                                                            

            console.log(args[0]);


        },
        onLeave: function(retval){
            send(retval.toInt32());
        }
    });


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