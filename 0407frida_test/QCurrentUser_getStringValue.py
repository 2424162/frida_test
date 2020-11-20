import frida, sys

jscode = '''
console.log("kaishi");
function showStacks(){

    console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new()))
}
Java.perform(function () {
    var qphoto = Java.use('com.yxcorp.gifshow.entity.QCurrentUser');
    qphoto.getStringValue.implementation = function (str1,str2) {

        var re = this.getStringValue(str1,str2) ;
        //showStacks();
        //console.log("__________");

        // console.log(JSON.stringify(this.mService));
        
        
        console.log("参数1:"+str1);
        console.log("参数2:"+str2);
        //console.log(str3);
        //console.log(str4);
        console.log('结果值:'+re);


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


# process = frida.get_remote_device()  # .attach("com.smile.gifmaker")
# process = process.attach('com.smile.gifmaker')
process = frida.get_device_manager().add_remote_device("127.0.0.1:9988").attach('com.smile.gifmaker')
script = process.create_script(jscode)
script.on("message", on_message)
script.load()
sys.stdin.read()


#frida-trace -U -i "getStringValue" com.smile.gifmaker