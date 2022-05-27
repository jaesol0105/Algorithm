#
#  Date  : 2022-05-23
#  URL   : https://programmers.co.kr/learn/courses/30/lessons/12899
#

def solution(n):
    answer = ''
    while True:
        remain = 4 if n % 3 ==0 else n % 3
        answer = str(remain) + answer
        if n <= 3 :
            break
        else:
            n = n // 3 - (n % 3 == 0)
    return answer
