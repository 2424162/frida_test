import frida, sys

jscode = '''

console.log("开始");
Java.perform(function () {
    var qphoto = Java.use('com.kuaishou.android.security.adapter.common.KSecurityContext')

    qphoto.setDid.implementation = function (str) {
        var re=this.setDid(str)
        console.log('结果值:'+re);

}
});
'''


def on_message(message, data):
    print(message)
    if message['type'] == 'send':
        print(message['payload'])
    else:
        print(message)


process = frida.get_remote_device()  # .attach("com.smile.gifmaker")
process = process.attach('com.smile.gifmaker')
script = process.create_script(jscode)
script.on("message", on_message)
script.load()
sys.stdin.read()

# frida-trace -U -i "getStringValue" com.smile.gifmaker