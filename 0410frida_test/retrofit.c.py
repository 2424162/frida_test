import frida, sys

# .overload('java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String')
jscode = '''
Java.perform(function () {
    console.log("kaishi")
    var c = Java.use('com.yxcorp.gifshow.retrofit.c') ;

    var exp = null;
 
    var Long = Java.use("java.lang.Long");       
    var str="ks://photo/1390807479/5214323959547783532/3/1_a/2000042300377554865_p0#addcomment";
    var str2="5214323959547783532";
    var str3="1390807479";
    var str4="wqwc11casaszzz";
    var str5=exp;
    var str6=exp;
    var str7=false;
    var str8=Long.parseLong("0");
    var str9=exp;
        
        
        var re = c.a(str,str2,str3,str4,str5,str6,str7,str8,str9) ;

        console.log(re);
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