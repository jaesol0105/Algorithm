#
#  Date  : 2022-06-03
#  URL   : https://programmers.co.kr/learn/courses/30/lessons/76501
#
#  풀이에 걸린 시간 : 3분

def solution(absolutes, signs):
    answer = 0
    for i in range(len(signs)):
        if signs[i]==True:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer
