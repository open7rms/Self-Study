#sorting number

maxnum = None
minnum = None

num=list()
while True:
    number = input("Enter your number :")
    if number == "done" :
        break
    try :
       n=float(number)
       num.append(n)
    except  :
        print("enter the numerical value")
        continue
        
num.sort(reverse= True)
print("Minimum is ",num[-1])
print("Maximum is ",num[0])
print(num)
