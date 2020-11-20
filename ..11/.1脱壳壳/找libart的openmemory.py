import frida, sys

jscode = """
var exports = Module.enumerateExportsSync("libart.so");
for(var i=0;i<exports.length;i++){
send("name:————"+exports[i].name+" ————地址address:—————"+exports[i].address);

}
"""


def on_message(message, data):
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