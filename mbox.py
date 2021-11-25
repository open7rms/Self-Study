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
        mbox[slt[1]]=mbox.get(slt[1],0)+1
#print(mbox)

bigcount = None
bigmsger = None
for msger,count in mbox.items():
    if bigcount is None or count>bigcount:
        bigmsger = msger
        bigcount = count
        
print(bigmsger,bigcount)
#print("There were", count, "lines in the file with From as the first word")
