orgf=open("2021_SemiSales_HPG.csv", encoding="utf8")
#import numpy as np

def avr(num) :
    adv=float()
    for v in num :
        adv=adv+float(v)
    return adv/len(num)

def std(num,av) :
    sumv=float()
    for v in num :
       sumv=sumv+(float(v)-float(av))**2
    svalue =(sumv/float(av))**0.5
    return svalue

codet=list()

for lines in orgf :
    sw= lines.split(",")
    #count=count +1
    fname = "./HPG/"+ sw[5] + ".csv"
    if sw[5] not in codet:
        codet.append(sw[5])
    
    #print(fname) 
    stof=open(fname,"a",encoding="utf8")
    stof.write(lines)
    stof.close()

for fname in codet :
    orderqty=list()
    ref=open("./HPG/"+fname+".csv",encoding="utf8")
    for lines in ref :
        sw=lines.split(",")
        orderqty.append(sw[8].strip('"'))
        #print(orderqty)
    #print(fname, orderqty[])
    ref=open("./HPG/"+fname+".csv","a", encoding="utf8")
    averagev=avr(orderqty)
    svalue = std(orderqty,averagev)
    staticlines="Average,"+ str(averagev) + ", Sigma ," + str(svalue)
    ref.write(staticlines)
    ref.close()
print(len(codet))
    
            
        
