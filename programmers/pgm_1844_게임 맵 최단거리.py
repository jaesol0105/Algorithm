#
#  Date  : 2022-06-26
#  URL   : https://programmers.co.kr/learn/courses/30/lessons/1844
#
#  풀이에 걸린 시간 : 24분

from collections import deque

def solution(maps):
    answer = 0
    
    q= deque()
    q.append([0,0,1])
    
    dr=[0,-1,0,1]
    dc=[-1,0,1,0]
    
    row_len = len(maps)
    col_len = len(maps[0])
    
    while q:
        row,col,cnt = q.popleft()

        for i in range(4):
            r= row + dr[i]
            c= col + dc[i]
            if r>=0 and r<row_len and c>=0 and c<col_len:
                if maps[r][c] > 0:
                    if maps[r][c]>cnt+1:
                        maps[r][c] = cnt+1
                        q.append([r,c,cnt+1])
                    elif maps[r][c] == 1:
                        maps[r][c] = cnt+1
                        q.append([r,c,cnt+1])
    
    answer = maps[row_len-1][col_len-1] if maps[row_len-1][col_len-1] != 1 else -1
    
    return answer
