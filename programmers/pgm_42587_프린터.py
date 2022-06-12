#
#  Date  : 2022-06-12
#  URL   : https://programmers.co.kr/learn/courses/30/lessons/42587
#
#  풀이에 걸린 시간 : 20분

from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque()
    for i in range(len(priorities)):
        q.append((i,priorities[i])) 
    while q:
        m= max([p1 for n1,p1 in q])
        n, p = q.popleft()
        if p == m:
            answer += 1
            if location == n:
                break
        else:
            q.append((n,p))
            
    return answer
