import frida, sys

jscode = '''
Java.perform(function () {
    console.log("kaishi")
        var c = Java.use('com.yxcorp.gifshow.reminder.ReminderTabHostActionBarPresenter$b') ;

    c.onClick.implementation = function (str) {

        var re =this.onClick(str) 
        console.log(str)

        console.log(re)

        return re;

        console.log("-------");

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