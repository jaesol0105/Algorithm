#
#  Date  : 2022-05-30
#  URL   : https://programmers.co.kr/learn/courses/30/lessons/92342
#
#  풀이에 걸린 시간 : 1시간

from itertools import combinations_with_replacement
def solution(n, info):
    answer = [0]*11
    
    # 0~11 중복조합
    comb = list(combinations_with_replacement([i for i in range(0,11)],n))
    
    max_score_diff = 0
    rion = []
    info = info[::-1]
    
    for c in comb:
        score_rion = 0
        score_apeach = 0
        # 점수별로 맞춘 횟수 세기
        for i in range(1,11):
            cnt = c.count(i)
            # 맞춘 개수가 어피치보다 많을 경우
            if cnt > info[i]:
                score_rion += i
            # 해당 점수를 어파치가 더 많이 맞췄거나, 동등하게 맞췄을 경우
            if cnt <= info[i] and info[i] != 0 :
                score_apeach += i
        
        # 점수 차이가 최대값일 경우, 기록
        if score_rion - score_apeach > max_score_diff:
            max_score_diff = score_rion - score_apeach
            rion = c
            
    for i in rion:
        answer[10-i] += 1
        
    if max_score_diff == 0:
        answer = [-1]
            
    return answer
  
# BFS 를 사용하여 풀면, 수행시간을 단축 시킬 수 있다.
