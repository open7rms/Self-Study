def solution(lottos, win_nums):
    zeros =0
    min_v =0
    i=0
    while i < len(lottos) :
        if lottos[i] == 0 :
            zeros=zeros+1
        if lottos[i] in win_nums :
            min_v=min_v+1
        i=i+1
    if min_v ==0:
        min_v=1
    
    answer = [7-min_v-zeros, 7-min_v]
    return answer

loto=[44,1,0,0,31,25]
win_num=[31,10,45,1,6,19]
result = solution(loto,win_num)
print(result)
