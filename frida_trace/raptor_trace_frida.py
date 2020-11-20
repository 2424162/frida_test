import frida,sys

f = open('raptor_trace_2.js','r',encoding='utf-8')

jscode = f.read()



def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)


process = frida.get_remote_device().attach("com.smile.gifmaker")
script = process.create_script(jscode)
#script.on("message", on_message)
script.load()
sys.stdin.read()