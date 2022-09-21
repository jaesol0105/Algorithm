#
#  Date  : 2022-09-21
#  URL   : https://programmers.co.kr/skill_checks/420710
#
#  풀이에 걸린 시간 : 9분

def solution(participant, completion):
    answer = ''

    p = sorted(participant)
    c = sorted(completion)

    for i in range(len(p)):
        if i == len(p)-1:
            answer = p[i]
            break;
        if p[i] != c[i]:
            answer = p[i]
            break;
    return answer
