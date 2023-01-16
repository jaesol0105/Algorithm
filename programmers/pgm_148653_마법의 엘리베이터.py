#
#  Date  : 2023-01-16
#  URL   : https://programmers.co.kr/learn/courses/30/lessons/148653
#

def solution(storey):
    answer = 0
    
    while storey > 0:
        n = storey % 10
        nn = (storey //10) % 10

        if n == 5:
            if nn >= 5:
                answer += 10-n
                storey += 10-n
            else:
                answer += n
        else:
            if n > 5:
                answer += 10-n
                storey += 10-n
            else:
                answer += n
        storey //= 10
    
    return answer
