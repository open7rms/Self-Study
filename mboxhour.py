fname = input("Enter file name: ")
#if len(fname) < 1:
#    fname = "mbox-short.txt"

fh = open(fname)
count = 0
mbox=dict()
for line in fh:
    if not line.startswith("From "):
        continue
    slt=list()
    slt=line.split()
    #print(slt[1])
    for key in slt:
        hour=slt[5].split(":")
        #print(hour)
        mbox[hour[0]]=mbox.get(hour[0],0)+1


#sorted([(k,v) for k,v in mbox.items()])
tempsort=list()
for k,v in mbox.items():
    sth=(k,v)
    tempsort.append(sth)
tempsort=sorted(tempsort, reverse=False)
for k,v in tempsort :
    print(k,int(v/7))

