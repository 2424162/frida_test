import frida, sys


jscode = """
var exports = Module.enumerateExportsSync("libart.so");
for(var i=0;i<exports.length;i++){
if(exports[i].name == "_ZN3art7DexFile10OpenMemoryEPKhjRKNSt3__112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEjPNS_6MemMapEPKNS_7OatFileEPS9_"){
var openMemory = new NativePointer(exports[i].address);
console.log(openMemory)
}
}



Interceptor.attach(openMemory, {
onEnter: function (args) {

var begin = args[1]

console.log("magic : " + Memory.readUtf8String(begin))

var address = parseInt(begin,16) + 0x20

var dex_size = Memory.readInt(ptr(address))

console.log("dex_size :" + dex_size)

var file = new File("/data/data/快手  /" + dex_size + ".dex", "wb")
file.write(Memory.readByteArray(begin, dex_size))
file.flush()
file.close()

var send_data = {}
send_data.base = parseInt(begin,16)
send_data.size = dex_size
send(send_data)
},
onLeave: function (retval) {
if (retval.toInt32() > 0) {
}
}
});
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
