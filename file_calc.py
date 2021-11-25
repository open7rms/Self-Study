#file read and extract info and calculate the values
filename =input("Enter file name : ")
FH = open(filename)
count=0
sumvalue=0
for lines in FH :
    if not lines.startswith("X-DSPAM-Confidence:"):
        continue
    loc=lines.find(":")
    sumvalue = sumvalue + float(lines[loc+1:])
    count=count+1

print("Average spam confidence : ",sumvalue/count)
