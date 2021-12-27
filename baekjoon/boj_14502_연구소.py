#
#  Date  : 2021-11-28
#  URL   : https://www.acmicpc.net/problem/14502
#

from collections import deque
from itertools import combinations

n,m = map(int,input().split())

lab = []
zero = []
two = []

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(m):
        if data[j] == 0:
            zero.append((i,j))
        if data[j] == 2:
            two.append((i,j))

    lab.append(data)

dx=[-1,0,1,0]
dy=[0,-1,0,1]

def bfs(lab_copy,x,y):
    q=deque()
    q.append((x,y))

    while q:
        x, y = q.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx>=0 and ny>=0 and nx<n and ny<m:
                if lab_copy[nx][ny] == 0:
                    lab_copy[nx][ny] = 2
                    q.append((nx,ny))

max_value = 0

for c in list(combinations(zero,3)):
    #lab_copy = copy.deepcopy(lab)
    lab_copy = [item[:] for item in lab]

    for i,j in c:
        lab_copy[i][j] = 1

    for i,j in two:
        bfs(lab_copy,i,j)

    count = 0
    for i in range(n):
        for j in range(m):
            if lab_copy[i][j] == 0:
                count +=1

    max_value = max(max_value,count)

print(max_value)