import frida, sys

jscode = '''
console.log("kaishi");
Java.perform(function () {
    var qphoto = Java.use('io.reactivex.subjects.a');


    qphoto.onNext.implementation = function (str1) {
        //var str1 = '10';
        var re = this.onNext(str1) ;

        console.log('can:'+str1);

        //console.log(re);
        //return re;

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