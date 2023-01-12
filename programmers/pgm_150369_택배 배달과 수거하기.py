#
#  Date  : 2023-01-12
#  URL   : https://school.programmers.co.kr/learn/courses/30/lessons/150369
#
#  풀이에 걸린 시간 : 1시간

def solution(cap, n, deliveries, pickups):
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    
    d = 0
    p = 0
    total = 0
    
    for i in range(n):
        d += deliveries[i]
        p += pickups[i]
        while d>0 or p>0:
            d -= cap
            p -= cap
            total += (n-i)*2
            
    return total
