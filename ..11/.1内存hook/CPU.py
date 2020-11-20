import frida, sys

jscode = '''
function frida_Module() {
    Java.perform(function () {
    

        var process_Obj_Module_Arr = Process.enumerateModules();
        console.log("cccccc");
        for(var i = 0; i < process_Obj_Module_Arr.length; i++) {
        
            //if(process_Obj_Module_Arr[i].path.indexOf("hello")!=-1)
           // {
                console.log("模块名称:",process_Obj_Module_Arr[i].name);
                console.log("模块地址:",process_Obj_Module_Arr[i].base);
                console.log("大小:",process_Obj_Module_Arr[i].size);
                console.log("文件系统路径",process_Obj_Module_Arr[i].path);
           // }
         }
    });
}
setImmediate(frida_Module,0);

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