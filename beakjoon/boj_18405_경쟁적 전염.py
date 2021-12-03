#
#  Date  : 2021-12-03
#  URL   : https://www.acmicpc.net/problem/18405
#

from collections import deque

n,k = map(int,input().split())

lab = []
virus = []

for i in range(n):
    data = list(map(int,input().split()))
    for j in range(n):
        if data[j] != 0:
            virus.append((data[j],i,j,0))
    lab.append(data)

s,x,y = map(int,input().split())
x= x-1
y= y-1

virus.sort()
q = deque(virus)

dx=[-1,0,1,0]
dy=[0,-1,0,1]

def bfs(number,row,col,time):
    for i in range(4):
        nx = row + dx[i]
        ny = col + dy[i]
        if nx>=0 and ny>=0 and nx<n and ny<n:
            if lab[nx][ny] == 0:
                lab[nx][ny] = number
                q.append((number,nx,ny,time+1))
'''
time = 0

while q:
    if time == s:
        break

    for _ in range(len(q)):
        data = q.popleft()
        bfs(data[0],data[1],data[2])

    time += 1
'''

# 위와 결과는 동일, 코드의 간략화
while q:
    data = q.popleft()
    if data[3] == s:
        break
    bfs(data[0],data[1],data[2],data[3])

print(lab[x][y])