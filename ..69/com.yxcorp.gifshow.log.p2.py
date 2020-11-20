import frida, sys

# .overload('java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String')
jscode = '''
Java.perform(function () {
    console.log("kaishi")
    function showStacks(){

    console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new()))
}
function ByteArrayString(byteArray) {
    var str = "";
    var barr = new Uint8Array(byteArray);
    for(var i=0;i<barr.length;i++){
        str+=String.fromCharCode(barr[i]);
    }
    return str;
}

        var c = Java.use('com.yxcorp.gifshow.log.p$b') ;

    c.a.overload('java.util.List').implementation = function (str1) {

      //  showStacks();

        var re =this.a(str1) 
        console.log(typeof(re))
        console.log("haha"+str1.toString());
        console.log(re);
        console.log()



        send("Hook成功!");
        return re;
    }
});
'''

loistss = []


def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
        loistss.append(message['payload'])
        print(loistss)

    else:
        print(message)


process = frida.get_remote_device()  # .attach("com.smile.gifmaker")
process = process.attach('com.smile.gifmaker')
script = process.create_script(jscode)
script.on("message", on_message)
script.load()
sys.stdin.read()



