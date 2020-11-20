import json
path = 'C:\\Users\\二筒\Desktop\\'
f1 = open(path+"duijie.txt","r",encoding="utf-8")
f2 = open(path+"renwu.txt","r",encoding="utf-8")
dict_c = {}
f = open("banban.json", "a", encoding="utf-8")
dict_d = {}
for i in f1.readlines():
    list1 = i.split(":")
   # print(list1[1][:4])
    f2 = open(path + "renwu.txt", "r", encoding="utf-8")
    for j in f2.readlines():
        list2 = j.split(":")

        if list1[2][:6]==list2[2][:6] and list1[1][:4]!=list2[1][:4] :
            print(list1[2]+"____"+list1[1][:4]+"____"+list2[1][:4])
            dict_c["id"] = list1[2]
            dict_c["value"] = list1[1][:4]+"-"+list2[1][:4]
            print(str(dict_c))

            f.write(str(dict_c))
            f.write(",")



print(dict_c)



