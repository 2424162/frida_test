import frida, sys

jscode = '''
console.log("kaishi");
Java.perform(function () {
    var qphoto = Java.use('com.yxcorp.g;[.d');
    //var activity = Java.use("android.app.Activity");
    //activity.onResume.implementatiion = function(){
    console.log("开始");
    //var inst = qphoto.$new()
    //qphoto.d.overload()
    //var cc = inst.a();
    //console.log(cc);
    var str1 = "ks://photo/1016876265/5197998419270364594/3/1_a/2000043358900627650_h221#like";
    var str2 = "";
    var str3 = "_/_";
    var str4 = "true";
    console.log(inst);
    //var re =inst.a();

        //send("Hook成功!");


        //console.log("+++++++++");
        //console.log(str3);
        //console.log(str4);
        //console.log("--"+re);
        //console.log(this.f7284a);
      //console.log(re);
     //   return re;
 //}   
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