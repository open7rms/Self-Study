#payment calculation 3
def computepay(hour,rate)    :
    if hour >40 :
        print("Pay", (hour-40)*rate*1.5+40*rate)
    else :
        print("Pay",hour*rate)


Hour= input("Enter your working hour : ")
hour=float(Hour)
Rate = input("Enter your hourly rate : ")
rate = float(Rate)

computepay(hour,rate)

#def computepay(h, r):
#    if h>40:
#        pay = (h-40)*1.5*r+40*r
#    else :
#        pay = h*r
#    return pay

#hrs = input("Enter Hours:")
#rate = input("Enter Hourly rate:")
#
#p = computepay(float(hrs), float(rate))
#print("Pay", p)

