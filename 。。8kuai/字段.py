import frida, sys

# .overload('java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String')
jscode = '''
Java.perform(function () {
    console.log("kaishi")
    function showStacks(){

    console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new()))
}
        var c = Java.use('com.kwai.framework.model.user.QCurrentUser') ;


    c.getStringValue.implementation = function (str1,str2) {

        var re =this.getStringValue(str1,str2) 
        console.log("参数1"+str1)
        console.log(re)

        console.log("-------");



        //send("Hook成功!");
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


process = frida.get_remote_device().attach("com.smile.gifmaker")
script = process.create_script(jscode)
script.on("message", on_message)
script.load()
sys.stdin.read()