import os



path = "D:\黑宝宝"
f1 = open('lxml_read.txt','a+')
for root,paths,files in os.walk(path):

    for file in files:
        print(file)
        f = open(path+"//"+file,"r",encoding="utf8")
        cc = f.read()
        print(cc)

        f1.write(cc)
