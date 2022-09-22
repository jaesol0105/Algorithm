#
#  Date  : 2022-09-23
#  URL   : https://school.programmers.co.kr/learn/courses/30/lessons/87946
#
#  풀이에 걸린 시간 : 34분

from collections import deque
import copy

def solution(k, dungeons):
    answer = -1
    q=deque()

    for i in range(len(dungeons)):
        visited = [0]*len(dungeons)
        visited[i] = 1
        q.append((k-dungeons[i][1],visited))

        while q:
            uhp,v = q.popleft()
            if sum(v) == len(dungeons):
                answer = max(answer,sum(v))
            for j in range(len(dungeons)):
                if v[j] == 0: #방문 안한 던전이면
                    if uhp >= dungeons[j][0]: #최소 피로도 이상일경우
                        v_= copy.deepcopy(v)
                        v_[j] = 1  #방문된 v
                        q.append((uhp-dungeons[j][1],v_)) #유저 피로도 소모   
                    else:
                        answer = max(answer,sum(v))

    return answer
  
  #permutations 사용시 간단한 풀이 가능.
