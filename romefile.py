fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
	sline=line.split()
	

	for sword in sline:
            if not sword in lst:
                lst.append(sword)
            #print(lst)
lst.sort()
print(lst)
