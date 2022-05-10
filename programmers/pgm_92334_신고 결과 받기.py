#
#  Date  : 2022-05-07
#  URL   : https://programmers.co.kr/learn/courses/30/lessons/92334
#

def solution(id_list, report, k):    
    report_set = set(report)
    report = list(report_set)
    n = len(id_list)

    answer = [0] * n
    stack = [[] for _ in range(n)]

    dic = dict()
    for i in range(len(id_list)):
        dic[id_list[i]]=i

    for rep in report:
        a,b = rep.split(" ")
        stack[dic[b]].append(a)

    for list_a in stack:
        if len(list_a)>=k:
            for name in list_a:
                answer[dic[name]] = answer[dic[name]]+1
    return answer
