import frida, sys

# .overload('java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String')
jscode = '''
Java.perform(function () {
    console.log("kaishi1")
    var c = Java.use('com.yxcorp.utility.ay') ;
    var send = Java.use('com.yxcorp.plugin.message.chat.presenter.MsgChatKeyboardPresenter');
    send.sendMsg.implementation = function (){
    c.a.overload('java.lang.CharSequence').implementation = function (str1) {
        console.log("----")
        var re =c.a(str1) 
        console.log("1")
        //return re  

    }
            var re =this.sendMsg() 
            return re
    
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