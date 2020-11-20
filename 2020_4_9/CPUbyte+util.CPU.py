import frida, sys

jscode = '''
console.log("kaishi");
Java.perform(function () {
    var qphoto = Java.use('com.yxcorp.gifshow.util.CPU');


    qphoto.a.implementation = function (str1,str2,str3) {
        var re = this.a(str1,str2,str3) ;
               
        console.log('结果值:'+str1);
        send(str2);
        console.log(re);
        console.log("run");
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
#process = frida.get_device_manager().add_remote_device("127.0.0.1:9911").attach('com.smile.gifmaker')
script = process.create_script(jscode)
script.on("message", on_message)
script.load()
sys.stdin.read()

# frida-trace -U -i "getStringValue" com.smile.gifmaker