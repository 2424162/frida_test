import frida, sys

# .overload('java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String')
jscode = '''
Java.perform(function () {
    console.log("kaishi")


        //var c = Java.use('com.kwad.sdk.widget.KsAdWebView$b') ;
        //var c = Java.use('com.yxcorp.gifshow.webview.a.a') ;
        var c = Java.use('com.kuaishou.android.security.adapter.common.KSecurityContext') ;



    c.getDid.implementation = function () {

           // send(str1)
    
        var re =this.getAppkey() 
        var cc = this.getContext()
        var id = this.getDid()
        console.log(re); 
        console.log(cc);
        console.log(id);
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