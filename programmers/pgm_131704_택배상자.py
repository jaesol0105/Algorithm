#
#  Date  : 2023-02-11
#  URL   : https://programmers.co.kr/learn/courses/30/lessons/131704
#

def solution(order):
    answer = 0
    stack = []
    point = 1 # 컨베이어 위치
    i = 0 # 오더 진행도 
    
    while i < len(order):
        if order[i] == point:
            point += 1
            i += 1
            continue
        if order[i] > point:
            for j in range(point,order[i]): # point ~ order[i]-1 스택 넣기
                stack.append(j)
            point = order[i]+1
            i += 1
            continue
        if order[i] < point:
            if stack[-1] == order[i]:
                stack.pop()
                i += 1
                continue
        break
        
    answer = i
      
    return answer
