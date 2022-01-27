#
#  Date  : 2022-01-27
#  URL   : https://www.acmicpc.net/problem/18428
#

# 중복변수명 사용하지 않기 !
from itertools import combinations
from collections import deque

n = int(input())

board = []
x_spot = []
teacher = []

for i in range(n):
    data = list(input().split())
    for j in range(n):
        if data[j] == 'X':
            x_spot.append((i,j))
        if data[j] == 'T':
            teacher.append((i,j))
    board.append(data)

def search(x,y,direction):
    q=deque()
    q.append((x,y))

    while q:
        x,y = q.popleft()
        if x<0 or y<0 or x>=n or y>=n:
            return True
        if temp[x][y] == 'O':
            return True
        if temp[x][y] == 'S':
            return False
        q.append((x+dx[direction],y+dy[direction]))


dx = [-1,0,1,0]
dy = [0,-1,0,1]

for c in list(combinations(x_spot,3)):
    temp = [item[:] for item in board]
    result = False
    for i,j in c:
        temp[i][j] = 'O'

    for i,j in teacher:
        for k in range(4):
            result = search(i+dx[k], j+dy[k], k)
            if result == False: break
        if result == False: break

    if result == True:
        print("YES")
        break

if result == False:
    print("NO")
