#grade the score between 0.0 and 1.0
score=input("Enter your score :")
try :
    s=float(score)
except  :
    print("Enter the numerical input")
    quit()
    
if  1.0<s or s<0.0 :
    print("error")
elif s>=0.9 :
    print("A")
elif s>=0.8 :
    print("B")
elif s>=0.7 :
    print("C")
elif s>=0.6  :
    print("D")
elif s<0.6  :
    print("F")

 
    
