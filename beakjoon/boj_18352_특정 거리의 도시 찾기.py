#
#  Date  : 2021-11-23
#  URL   : https://www.acmicpc.net/problem/18352
#

from collections import deque
import sys

# 입력이 많을 경우 시간초과방지 (m = 1,000,000)
input = sys.stdin.readline

n,m,k,x = map(int,input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)

distance= [-1] * (n+1)
distance[x] = 0

q=deque([x])

# 모든 간선의 비용이 동일할 경우
# BFS 사용하여 최단거리를 찾을 수 있다
while q:
    now = q.popleft()
    for i in graph[now]:
        # 첫 방문에만 처리
        if distance[i] == -1:
            distance[i] = distance[now] + 1
            q.append(i)

flag = 0

for i in range(1,n+1):
    if distance[i] == k:
        print(i)
        flag = 1

if flag == 0:
    print(-1)