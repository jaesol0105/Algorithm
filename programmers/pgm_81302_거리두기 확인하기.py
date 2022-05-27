#
#  Date  : 2022-05-24
#  URL   : https://programmers.co.kr/learn/courses/30/lessons/81302
#
#  풀이에 걸린 시간 : 1시간

from itertools import combinations

def solution(places):
    answer = []
    p = [[] for _ in range(5)] # 대기실 별 P의 위치
    for pl in range(5): # 대기실
        for r in range(5): # 행
            for c in range(5): # 열
                if places[pl][r][c] == 'P':
                    p[pl].append([r,c])

    for i in range(5): # 대기실 별로
        comb = list(combinations(p[i],2)) # 두 자리간의 가능한 모든 조합
        state = 1
        for a, b in comb: # a=(r1,c1) b=(r2,c2)
            m = abs(a[0]-b[0]) + abs(a[1]-b[1])
            if m <= 2: # 맨하튼거리가 2 이하일경우
                if a[0] == b[0]: # 같은 행
                    if places[i][a[0]][max(a[1],b[1])-1] != 'X':
                        state = 0
                        break
                elif a[1] == b[1]: # 같은 열
                    if places[i][max(a[0],b[0])-1][a[1]] != 'X':
                        state = 0
                        break
                else: # 대각선
                    if max(a[0],b[0]) == a[0]:
                        if (places[i][a[0]-1][a[1]] != 'X' or places[i][b[0]+1][b[1]] != 'X'):
                            state = 0
                            break
                    else:
                        if (places[i][a[0]+1][a[1]] != 'X' or places[i][b[0]-1][b[1]] != 'X'):
                            state = 0
                            break
        answer.append(state)
                        
    return answer
  
  # BFS 로 풀었으면 간단하게 풀수있는 문제였다...
