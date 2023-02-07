#
#  Date  : 2023-02-07
#  URL   : https://programmers.co.kr/learn/courses/30/lessons/140107
#

from collections import deque
import math

def solution(k, d):
    answer = 0
    # 완전탐색 -> 100만 x 100만의 탐색을 하게되므로 시간초과
    
    # 층별로 개수 세기
    for y in range(0,d+1,k):
        x = math.sqrt(d*d - y*y) # x = (d^2-y^2)의 제곱근
        x = int(x) # 소수점 자르기
        x = x // k # 간격 k
        answer += (x+1)
        
    return answer
