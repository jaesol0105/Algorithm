#
#  Date  : 2023-01-17
#  URL   : https://programmers.co.kr/learn/courses/30/lessons/131705
#
#  풀이에 걸린 시간 : 3분

from itertools import combinations

def solution(number):
    answer = 0
    comb =list(combinations(number,3))

    for x,y,z in comb:
        if x+y+z == 0:
            answer+=1
    return answer
