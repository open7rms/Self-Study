#file open and read
filename = input("Enter file name : ")
FH = open(filename)

for lines in FH :
    print(lines.rstrip().upper())

## Use words.txt as the file name
#fname = input("Enter file name: ")
#fh = open(fname)

#for line in fh:
#	cleanline=line.rstrip()
#	print(cleanline.upper())
    
