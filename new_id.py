def solution(new_id):
    step=new_id.lower()
    answer=""
    for i in step:
        if i =="-" or i=="_" or i=="." or i.isalnum() :
            answer = answer + i
        
    while '..' in answer :
        answer=answer.replace("..",".")
    answer=answer.rstrip(".").lstrip(".")
    if answer =="" :
        answer="a"
    if len(answer)>=16 :
        answer=answer[:15].rstrip(".")
    if len(answer)<=2 :
        while len(answer) <3 :
            answer=answer + answer[-1]
        
    return answer

new="...!@BaT#*..y.abcdefghijklm."
result=solution(new)
print(result)

#정규식으로 풀이
#import re

#def solution(new_id):
#    st = new_id
#    st = st.lower()
#    st = re.sub('[^a-z0-9\-_.]', '', st)
#    st = re.sub('\.+', '.', st)
#    st = re.sub('^[.]|[.]$', '', st)
#    st = 'a' if len(st) == 0 else st[:15]
#    st = re.sub('^[.]|[.]$', '', st)
#    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
#    return st
