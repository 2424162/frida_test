import frida, sys

# .overload('java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String')
jscode = '''
Java.perform(function () {
    console.log("kaishi")

        var c = Java.use('okhttp3.FormBody$a') ;


    c.a.overload('java.lang.String', 'java.lang.String').implementation = function (str1,str2) {

        var re =this.a(str1,str2) 
        console.log("参数1"+str1)
        console.log("参数2"+str2)

        console.log(re);
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


process = frida.get_remote_device()
process = process.attach('com.smile.gifmaker')
script = process.create_script(jscode)
script.on("message", on_message)
script.load()
sys.stdin.read()