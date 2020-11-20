import frida, sys


jscode = '''
Java.perform(function () {
    console.log("kaishi")
        var c = Java.use('android.view.LayoutInflater') ;

    c.createViewFromTag.overload('android.view.View', 'java.lang.String', 'android.util.AttributeSet', 'boolean').implementation = function (str1,str2,str3,str4) {

        var re =this.createViewFromTag(str1,str2,str3,str4) 
        //console.log(str1)
        console.log(re)
        console.log("--------")

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