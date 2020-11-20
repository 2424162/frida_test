import frida, sys

# .overload('java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String')
jscode = '''

    function showStacks(){

    console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new()))
}

Java.perform(function () {
    console.log("kaishi")


        var c = Java.use('com.yxcorp.plugin.message.b.b.p') ;



    c.$init.overload('int', 'java.lang.String', 'java.lang.String').implementation = function (str1,str2,str3) {

           // send(str1)
        showStacks()
        var re =this.$init(str1,str2,str3) 
        console.log(str1)
        console.log(str2)
        console.log(str3)

        console.log(re); 

        return re;


        console.log("-------");




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