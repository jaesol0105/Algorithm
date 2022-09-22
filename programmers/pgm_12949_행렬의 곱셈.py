#
#  Date  : 2022-09-23
#  URL   : https://school.programmers.co.kr/learn/courses/30/lessons/12949
#
#  풀이에 걸린 시간 : 19분

def solution(arr1, arr2):
    answer = [[0]*len(arr2[0]) for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            mul = []
            for k in range(len(arr1[0])):
                mul.append(arr1[i][k]*arr2[k][j])
            answer[i][j] =sum(mul)              
    return answer
