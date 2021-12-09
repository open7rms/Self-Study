def solution(numbers, hand):
    answer = ''
    Lposition ="*" # 새로운 위치 설정, *
    Rposition ="#" # 새로운 위치 설정, # "0"은 자동으로 11
    numpo={
        1:(0,0),2:(0,1),3:(0,2),
        4:(1,0),5:(1,1),6:(1,2),
        7:(2,0),8:(2,1),9:(2,2),
        '*':(3,0),0:(3,1),'#':(3,2)
        }
    
    for i in numbers :
        if i==0:
            i=11
        if i%3 ==0 : # 3배수로 열위치가 변경 나머지로 계산, 3열은 오른손
            print(Lposition, Rposition, i, "R")
            answer +="R"
            Rposition=i
        elif i%3==1 :# 1열은 왼손
            print(Lposition, Rposition, i, "L")
            answer +="L"
            Lposition=i
        else :         # 2열은 판단 필요 
            if i==11:
                i=0
            Ldistance = abs(numpo[Lposition][0]-numpo[i][0])+abs(numpo[Lposition][1]-numpo[i][1])
            Rdistance = abs(numpo[Rposition][0]-numpo[i][0])+abs(numpo[Rposition][1]-numpo[i][1])

            if Ldistance > Rdistance :
                print(Lposition, Rposition, i, "R1")
                answer +="R"
                Rposition=i
            elif Ldistance < Rdistance :
                print(Lposition, Rposition, i, "L1")
                answer +="L"
                Lposition=i
            else :
                if hand=="left" :
                    print(Lposition, Rposition, i, "L2")
                    answer +="L"
                    Lposition=i
                else :
                    print(Lposition, Rposition, i, "R2")
                    answer +="R"
                    Rposition=i                   
             
    return answer
num=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
han="right"

print(solution(num,han))
