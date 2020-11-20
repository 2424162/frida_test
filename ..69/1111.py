import frida, sys

# .overload('java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String')
jscode = '''
Java.perform(function () {
    console.log("kaishi")
    function byteToString(arr) {
if(typeof arr === 'string') {
return arr;
}
var str = '',
_arr = arr;
for(var i = 0; i < _arr.length; i++) {
var one = _arr[i].toString(2),
v = one.match(/^1+?(?=0)/);
if(v && one.length == 8) {
var bytesLength = v[0].length;
var store = _arr[i].toString(2).slice(7 - bytesLength);
for(var st = 1; st < bytesLength; st++) {
store += _arr[st + i].toString(2).slice(2);
}
str += String.fromCharCode(parseInt(store, 2));
i += bytesLength - 1;
} else {
str += String.fromCharCode(_arr[i]);
}
}
return str;
}
    function showStacks(){

    console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new()))
}
        var c = Java.use('com.google.protobuf.nano.MessageNano') ;

    c.toByteArray.overload('com.google.protobuf.nano.MessageNano', '[B', 'int', 'int').implementation = function (str1,str2,str3,str4) {

        var re =this.toByteArray(str1,str2,str3,str4) 
        console.log(str1);
        console.log("参数2");

        return re;
    }
});
'''

loistss = []


def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
        loistss.append(message['payload'])
        #print(loistss)

    else:
        print(message)


process = frida.get_remote_device()  # .attach("com.smile.gifmaker")
process = process.attach('com.smile.gifmaker')
script = process.create_script(jscode)
script.on("message", on_message)
script.load()
sys.stdin.read()