#
#  Date  : 2022-05-09
#  URL   : https://programmers.co.kr/learn/courses/30/lessons/60062
#

from itertools import permutations

def solution(n, weak, dist):
    answer = len(dist)+1
    length = len(weak)
    
    for i in range(len(weak)):
        weak.append(n+weak[i])
    
    for i in range(length):
        weak_copy = weak[i:i+length]
        for p in list(permutations(dist,len(dist))):
            distance = weak_copy[0]+p[0]
            count = 1
            dist_index = 0
            
            for index in range(length):
                if distance < weak_copy[index]:
                    count +=1
                    if count > len(dist):
                        break
                    dist_index += 1
                    distance = weak_copy[index]+p[dist_index]
            answer = min(answer, count)
    if answer > len(dist):
        answer = -1
        
    return answer
