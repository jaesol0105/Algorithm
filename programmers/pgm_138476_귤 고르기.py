#
#  Date  : 2023-02-08
#  URL   : https://programmers.co.kr/learn/courses/30/lessons/138476
#

def solution(k, tangerine):
    answer = 0
    # K개, 최대한 같은종류
    partition = [0]*10000001
    for t in tangerine:
        partition[t]+=1
    partition.sort(reverse=True)
    for i in range(len(partition)):
        k-=partition[i]
        if k <= 0:
            answer = i+1
            break
    return answer
