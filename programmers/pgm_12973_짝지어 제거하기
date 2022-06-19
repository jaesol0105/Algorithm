#
#  Date  : 2022-06-19
#  URL   : https://programmers.co.kr/learn/courses/30/lessons/12973
#
#  풀이에 걸린 시간 : 40분

def solution(s):
    answer = 0
    
    temp=[s[0]]
    for i in range(1,len(s)):
        if len(temp)>0:
            if temp[-1] == s[i]:
                temp.pop()
            else:
                temp.append(s[i])
        else:
            temp.append(s[i])
            
    if len(temp)==0:
        answer=1
        
    return answer
    
#  리스트의 마지막 원소에대한 접근이나 비교가 이루어지는경우, 스택을 사용하면 용이 하다.
