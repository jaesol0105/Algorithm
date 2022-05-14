#
#  Date  : 2022-05-11
#  URL   : https://programmers.co.kr/learn/courses/30/lessons/42586
#
#  풀이에 걸린 시간 : 20분

from collections import deque

def solution(progresses, speeds):
    answer = []
    
    q = deque()
    
    for progress in progresses:
        q.append(progress)
    
    day = 0
    idx = 0 # 작업속도 인덱스, 큐에서 진도가 나가면 증가.
    
    while q:
        day = day+1 # 하루 경과
        
        cnt = 0 # 하루의 배포 수
        
        # 큐안의 작업들 작업속도 만큼 진행.
        for i in range(len(q)):
            q[i] = q[i]+ speeds[idx+i]
        # 완료된 작업 앞쪽부터 순차적 검사
        for i in q:
            if i >= 100:
                cnt = cnt +1
            else: break
        # 맨 앞쪽 작업부터 연속으로 완료된 작업 처리 
        if cnt > 0:
            for _ in range(cnt):
                q.popleft()
            answer.append(cnt) # 기록
            idx = idx + cnt
    
    return answer
