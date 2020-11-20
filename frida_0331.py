#c.a.a(cls)

import frida, sys

# .overload('java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String')
jscode = '''


Java.perform(function () {
    //查找android.view.View类在堆上的实例化对象
    Java.choose("com.yxcorp.gifshow.retrofit.c", {
        //枚举时调用
        onMatch:function(instance){
            //打印实例
            console.log(instance);
        },
        //枚举完成后调用
        onComplete:function() {
            console.log("end")
        }});
});
'''


def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)


process = frida.get_remote_device()  # .attach("com.smile.gifmaker")
process = process.attach('com.smile.gifmaker')
script = process.create_script(jscode)
script.on("message", on_message)
script.load()
sys.stdin.read()

#
# def on_message(message, data):
#     if message['type'] == 'send':
#         print("[*] {0}".format(message['payload']))
#     else:
#         print(message)
#
#
# process = frida.get_remote_device()  # .attach("com.smile.gifmaker")
# process = process.attach('com.smile.gifmaker')
# script = process.create_script(jscode)
# script.on("message", on_message)
# script.load()
# sys.stdin.read()