#
#  Date  : 2023-01-31
#  URL   : https://programmers.co.kr/learn/courses/30/lessons/154540
#

from collections import deque

def explore(maps,data,sumOfFood):
    global visited
    dr=[-1,0,1,0]
    dc=[0,-1,0,1]
    q = deque([data]) # deque([리스트])
    
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr >= 0 and nc >= 0 and nr < len(maps) and nc < len(maps[0]) :
                if maps[nr][nc] != 'X' and visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    sumOfFood += int(maps[nr][nc]) # int로 형변환
                    q.append((nr,nc))
    return sumOfFood
    
    
def solution(maps):
    answer = []
    
    global visited # global 키워드 : 매개변수(maps)에는 사용불가?
    visited = [[0]*len(maps[0]) for _ in range(len(maps))]
    
    for r in range(len(maps)):
        for c in range(len(maps[0])):
            if maps[r][c] != 'X' and visited[r][c] == 0:
                visited[r][c] = 1
                sumOfFood = explore(maps,[r,c],int(maps[r][c]))
                answer.append(sumOfFood)
                
    if len(answer) == 0:
        answer.append(-1)
        
    return sorted(answer)
