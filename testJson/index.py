import json

f = open("xiangmu.txt", "r", encoding="utf-8")
fs = open("111.txt", "r", encoding="utf-8")

newf = open("sss.json","w",encoding="utf-8")
flist = []
fslist = {}
fdict = {}

for i in fs:
    fslist[i.strip().split("	")[0]] = i.strip().split("	")[-1]

print(fslist)
for i in f:
    datslsit = (i.strip().split("|"))
    xid = datslsit[1]
    platformname = datslsit[2]
    fdict["xid"] = xid
    fdict["platformname"] = platformname
    if xid in fslist:
        fdict["price"] = fslist[xid]
    else:
        fdict["price"] = None

    flist.append(json.dumps(fdict))


newf.write(json.dumps({"data":flist}))
print(flist)
#
