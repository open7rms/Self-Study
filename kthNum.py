def solution(array, commands):
    answer = []    
    

    return [sorted(array[i-1:j])[k-1] for i,j,k in commands]

array = [1, 5, 2, 6, 3, 7, 4]
commands=[[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array,commands))
