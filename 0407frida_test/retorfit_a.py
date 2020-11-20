import frida,sys

jscode = '''
console.log("kaishi");
Java.perform(function () {
    var qphoto = Java.use('com.yxcorp.gifshow.entity.QCurrentUser');
    qphoto.getStringValue.implementation = function (str1,str2) {
        var re = this.getStringValue(str1,str2) ;
        send(this.mPrefs);
        //console.log(this.mPrefs);
        console.log("_____");
        //send(this.mService);
        //console.log(this.mService);
        
        //send("Hook成功!");
        //console.log(str1);
        //console.log(str2);
        //console.log(str3);
        //console.log(str4);
        //console.log(re);
        
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

process = frida.get_remote_device()#.attach("com.smile.gifmaker")
process  = process.attach('com.smile.gifmaker')
script = process.create_script(jscode)
script.on("message",on_message)
script.load()
sys.stdin.read()