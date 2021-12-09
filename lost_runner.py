def solution(participant, completion):
    par=dict()
    com=dict()
    for key1 in participant:
        par[key1]=par.get(key1,0)+1
        
    for key2 in completion:
        com[key2]=com.get(key2,0)+1

    print(par)
    print(com)
    
    for k1,v1 in par.items():
        if (k1 in com and par[k1]==com[k1]):
             pass
        else :
            answer=k1
        
    return answer

participant =["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

print(solution(participant,completion))
