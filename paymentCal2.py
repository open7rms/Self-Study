#payment calculation2
Hour = input("Enter your working hour")
HR = input("Enter your hourly rate")

#if(float(Hour)>40):
#    print((float(Hour)-40)*float(HR)*1.5+40*float(HR))
#else :
#    print(float(Hour)*float(HR))
#
h=float(Hour)
r=float(HR)
if h>40 :
    pay=(h-40)*r*1.5+40*r
else :
    pay=h*r

print(pay)
