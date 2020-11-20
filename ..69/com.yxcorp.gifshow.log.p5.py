import frida, sys

# .overload('java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String')
jscode = '''
Java.perform(function () {
    console.log("kaishi")
    function showStacks(){

    console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new()))
}
        var c = Java.use('com.yxcorp.gifshow.log.p$b') ;
        var clazz = Java.use("java.lang.Class")

    c.a.overload('java.util.List').implementation = function (str1) {

      //  showStacks();
        var cc = Java.cast(c.getClass(),clazz).getDeclaredField('f46101b');
        console.log(cc)
        var re =this.a(str1)
        var haha=this.f46101b
        console.log(str1)
        send(re);
        console.log(haha.value);
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



