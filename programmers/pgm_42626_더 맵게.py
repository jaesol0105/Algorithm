#
#  Date  : 2022-05-22
#  URL   : https://programmers.co.kr/learn/courses/30/lessons/42626
#
#  풀이에 걸린 시간 : 39분

import heapq

def solution(scoville, K):
    answer = 0
    
    hq = []
    for food in scoville:
        heapq.heappush(hq, food)
    
    cnt = 0
    
    # hq에 음식이 1개 남게되면 종료
    while len(hq) > 1:
        # 가장 덜 매운 두개 추출
        combined = [heapq.heappop(hq) for i in range(1,3)]
        # 모두 K 이상인지 체크
        flag = [1 if c>=K else 0 for c in combined]
        # 조합
        combined = sum([i*combined[i-1] for i in range(1,3)])
        
        if sum(flag) == 2:
            break
        heapq.heappush(hq, combined)
        cnt += 1
        flag = 0
        
        # 1개 남았는데 K 미만일 경우
        if len(hq) < 2 and sum(hq) < K:
            return -1
            
    answer = cnt
    
    return answer
