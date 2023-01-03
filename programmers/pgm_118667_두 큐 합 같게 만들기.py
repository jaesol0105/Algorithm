#
#  Date  : 2023-01-03
#  URL   : https://programmers.co.kr/learn/courses/30/lessons/118667
#
#  풀이에 걸린 시간 : 48분

from collections import deque

def solution(queue1, queue2):
    q1, q2 = deque(queue1),deque(queue2)
    count = 0
    sum_1, sum_2 = sum(q1), sum(q2) # 내장함수 sum은 O(N)의 시간복잡도를 가진다.
    
    while True:
        if count > (len(q1)+len(q2))*2: # 한바퀴돌아서 원상복구 되는 경우
            return -1
            
        if sum_1 > sum_2:
            temp = q1.popleft()
            sum_1 -= temp
            sum_2 += temp
            q2.append(temp)
            
        elif sum_1 < sum_2:
            temp = q2.popleft()
            sum_1 += temp
            sum_2 -= temp
            q1.append(temp)
            
        else: #sum_1 == sum_2
            break
            
        count += 1
        
    return count
