def solution(absolutes, signs):
    co = 0
    answer = 0
    for i in absolutes :
        #print(signs[co])
        if signs[co] == 1 :
            #print(i)
            answer +=i
        else :
            #print(-i)
            answer -=i
        co +=1

    return answer
absolutes = [4,7,12]
signs = [True,False,True]
print(solution(absolutes,signs))



2
3
def #solution(absolutes, signs):
    #return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))
