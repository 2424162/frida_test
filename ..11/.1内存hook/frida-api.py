import frida, sys

jscode = '''
function frida_Module() {
    Java.perform(function () {


        var process_Obj_Module_Arr = Process.enumerateModules();
        var libart = Process.findModuleByName("libart.so")
        var libcore = Process.findModuleByName("libcore.so")
       send(libart)
            var addr_DefineClass = null;
    var symbols = libart.enumerateSymbols();
    console.log(symbols.length)
    for (var index = 0; index < symbols.length; index++) {
        var symbol = symbols[index];
        var symbol_name = symbol.name;
        send(symbol_name)
        //这个DefineClass的函数签名是Android9的
        //_ZN3art11ClassLinker11DefineClassEPNS_6ThreadEPKcmNS_6HandleINS_6mirror11ClassLoaderEEERKNS_7DexFileERKNS9_8ClassDefE
        if (symbol_name.indexOf("ClassLinker") >= 0 && 
            symbol_name.indexOf("DefineClass") >= 0 && 
            symbol_name.indexOf("Thread") >= 0 && 
            symbol_name.indexOf("DexFile") >= 0 ) {
            console.log(symbol_name, symbol.address);
            addr_DefineClass = symbol.address;
        }
    }
    var dex_maps = {};

    console.log("[DefineClass:]", addr_DefineClass);
    });
}
setImmediate(frida_Module,0);

'''

loistss = []


def on_message(message, data):
    if message['type'] == 'send':
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