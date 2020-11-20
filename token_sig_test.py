import frida,sys

jscode = '''
Java.perform(function () {
console.log("开始");
function enumMethods(tclass){
    var hook = Java.use(tclass);
    var methods = hook.class.getDeclaredMethods();
    hook.$dispose;
    return methods;
    }
var a = enumMethods("com.yxcorp.gateway.pay.api.-$$Lambda$PayRetrofitInitConfig$CPxG3D6hCvV4QtjWCetTB9GskJ4");
a.forEach(function(s){
console.log(s);
    });

});

'''


def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)


process = frida.get_remote_device().attach("com.smile.gifmaker")
script = process.create_script(jscode)
script.on("message", on_message)
script.load()
sys.stdin.read()