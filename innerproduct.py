def solution(a, b):
    answer =0
    i=0
    while i < len(a) :
        answer +=a[i]*b[i]
        i +=1   
    return answer

a=[1,2,3,4]
b=[-3,-1,0,2]
print(solution(a,b))
#def solution(a, b):

#    return sum([x*y for x, y in zip(a,b)])
