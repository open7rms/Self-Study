largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try :
        fvalue=float(num)
    except:
        print("Invalid input")
        continue
    #largest number detection
    if largest is None   :
        largest=fvalue
    elif fvalue > largest :
        largest=fvalue

    #smallest number detection
    if  smallest is None  :
        smallest=fvalue
    elif fvalue<smallest  :
        smallest=fvalue

print("Maximum is", largest)
print("Minimum is", smallest)

        
