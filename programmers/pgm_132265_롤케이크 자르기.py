#
#  Date  : 2023-02-10
#  URL   : https://programmers.co.kr/learn/courses/30/lessons/132265
#

def solution(topping):
    answer = 0
    # 100만
    s_left = set()
    s_right = set()
    count = [[0]*2 for _ in range(len(topping)+1)]

    for i in range(len(topping)):
        # 1 양쪽에서 토핑가지수 세기
        s_left.add(topping[i])
        s_right.add(topping[len(topping)-1-i])
        count[i+1][0] = len(s_left)
        count[len(topping)-1-i][1] = len(s_right)

    for l,r in count:
        if l == r:
            answer += 1

    return answer
