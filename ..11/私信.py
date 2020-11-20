import frida, sys

# .overload('java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String')
jscode = '''
Java.perform(function () {
    console.log("kaishi")
    function showStacks(){

    console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new()))
}
        var c = Java.use('com.kwai.chat.group.entity.SessionNewsInfo') ;


    c.$init.overload('java.lang.Long', 'java.lang.String', 'long', 'int', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'long', 'boolean', 'int', 'int', 'long').implementation = function (str1,str2,str3,str4,str5,str6,str7,str8,str9,str10,str11,str12) {

        var re =this.$init(str1,str2,str3,str4,str5,str6,str7,str8,str9,str10,str11,str12)
                console.log(str1);
        console.log(str2);
        console.log(str3);
        console.log(str4);
                console.log(str5);
        console.log(str6);
    console.log(str7)
    console.log(str8)
    console.log(str9)
    console.log(str10)
    console.log(str11)
    console.log(str12)
        console.log(re);


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