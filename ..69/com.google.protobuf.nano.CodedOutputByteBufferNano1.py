import frida, sys

# .overload('java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String')
jscode = '''
Java.perform(function () {
    console.log("kaishi")
    function showStacks(){

    console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new()))
}
        var c = Java.use('com.google.protobuf.nano.CodedOutputByteBufferNano') ;

    c.encode.overload('java.lang.CharSequence', '[B', 'int', 'int').implementation = function (str1,str2,str3,str4) {

      //  showStacks();

        var re =this.encode(str1,str2,str3,str4) 
        console.log(str1);
        send(str2);
        console.log(str3);
        console.log(str4);
        console.log(re);


        send("Hook成功!");
        return re;
    }
});
'''

loistss = []


def on_message(message, data):
    if message['type'] == 'send':
        #print("[*] {0}".format(message['payload']))
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