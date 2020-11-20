import json
path = 'C:\\Users\\二筒\Desktop\\'
f1 = open(path+"xing.txt","r",encoding="utf-8")
f2 = open("banban.json","a")
dict_f ={}
for data in f1.readlines():
    i = data.split(":")

    dict_f["ID"] = i[1][0:6].strip()
    dict_f["name"] = i[2].split("          ")[0].strip()
    dict_f["money"]=i[3].split("/")[0].strip()
    js = json.dumps(dict_f)
    f2.write(js)
    f2.write(',')
