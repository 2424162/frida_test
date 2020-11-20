import frida, sys

# .overload('java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String')
jscode = '''
Java.perform(function () {
    console.log("kaishi")
    var c = Java.use('com.yxcorp.gifshow.retrofit.c') ;

    var Long = Java.use("java.lang.Long");

    c.a.overload('java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'boolean','long',"java.lang.String").implementation = function (str,str2,str3,str4,str5,str6,str7,str8,str9) {

        console.log(str,"类型:",typeof(str));
        


        console.log(str2,"类型:",typeof(str2));

        console.log(str3,"类型:",typeof(str3));

        console.log(str4,"类型:",typeof(str4));

        console.log(str5,"类型:",typeof(str5));

        console.log(str6,"类型:",typeof(str6));

        console.log(str7,"类型:",typeof(str7));

        console.log(str8,"类型:",typeof(str8));
        console.log(str9,"类型:",typeof(str9));
        getc = c.$new();
        var exp = null;

    var str="ks://photo/1073852685/5255137840575800570/3/1_i/2000042069601097425_h347#addcomment";
    var str2="5255137840575800570";
    var str3="1073852685";
    var str4="wqwc11c";
    var str5=exp;
    var str6=exp;
    var str7=false;
    var str8=Long.parseLong("0");
    var str9=exp;


        var re = this.a(str,str2,str3,str4,str5,str6,str7,str8,str9) ;

        console.log(re);
        return re;
    }
});
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