#
#  Date  : 2022-05-10
#  URL   : https://programmers.co.kr/learn/courses/30/lessons/62048
#

import math

def solution(w,h):
    answer = 1
    
    count_of_all_square = w*h
    disabled_square = w+h-math.gcd(w,h)

    answer = count_of_all_square - disabled_square
    return answer
