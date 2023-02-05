#
#  Date  : 2023-02-05
#  URL   : https://programmers.co.kr/learn/courses/30/lessons/154538
#
#  풀이에 걸린 시간 : 25분

# 중복제거가 핵심. set을 사용하여도 됨.
from collections import deque
def solution(x, y, n):
    answer = -1
    q=deque([[y,0]]) # Y부터 거꾸로 X만들기
    while q:
        temp,cnt = q.popleft()
        if temp == x:
            answer = cnt
            break
        for i in range(1,4):
            if i == 1:
                if temp - n >= x:
                    q.append([temp - n,cnt+1])
            else:
                if (temp / i) - int(temp / i) == 0 and temp / i >= x:
                    q.append([temp / i,cnt+1])
    return answer
