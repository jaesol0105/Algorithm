#
#  Date  : 2023-02-06
#  URL   : https://programmers.co.kr/learn/courses/30/lessons/142085
#

import heapq

def solution(n, k, enemy):
    answer = len(enemy)
    # 병사 N명, 무적권 K(50만)번, 최대 몇라운드(100만)
    heap = []
    for i in range(len(enemy)):
        n -= enemy[i]
        heapq.heappush(heap,-enemy[i]) # 최대 힙이므로 음수로 삽입
        if n < 0 and k > 0: # 남은 무적권 있을경우
            n -= heapq.heappop(heap) # 최대힙에서 뽑기, 부호 변경
            k -= 1
        elif n < 0 and k == 0:
            answer = i # 현재단계 이전 단계까지
            break
    return answer
