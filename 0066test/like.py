import frida, sys

# .overload('java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String')
jscode = '''
Java.perform(function () {
    console.log("kaishi")
    function showStacks(){

    console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new()))
}

        console.log(str4);        var c = Java.use('com.yxcorp.gifshow.retrofit.c') ;

    c.a.overload('com.yxcorp.gifshow.entity.QPhoto', 'boolean', 'java.lang.String', 'java.lang.String', 'java.lang.String').implementation = function (str,str2,str3,str4,str5) {

        //showStacks();

        console.log(str);
        console.log(str2);
        console.log(str3);
        console.log(str5);
        var re = this.a(str,str2,str3,str4,str5) ;
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