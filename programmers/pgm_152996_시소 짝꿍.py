#
#  Date  : 2023-01-30
#  URL   : https://programmers.co.kr/learn/courses/30/lessons/152996
#

def solution(weights):
    answer = 0
    pos = [(2,3),(2,4),(3,2),(3,4),(4,2),(4,3)] # 가능한 조합 생각해보기
    
    weight_count = [0]*1001 #계수정렬
    for w in weights:
        weight_count[w] += 1
    
    for w in range(100,1001):
        if weight_count[w] > 0:
            temp_list = []
            # 2개 이상인 경우
            if weight_count[w] >= 2:
                # 같은 무게와의 조합
                answer += ((weight_count[w] -1) * weight_count[w]) / 2
                
            for i,j in pos:
                temp = w * i / j
                if temp - int(temp) == 0: # 정수 판별
                    if temp <= 1000 and temp >= 100: # 무게 범위 판별
                        temp_list.append(int(temp))
            temp_list = list(set(temp_list)) # 중복 제거
            
            for t in temp_list:
                if weight_count[t] > 0:
                    answer += weight_count[t] * weight_count[w]
            weight_count[w] = 0 # 카운팅이 끝난 몸무게는 제거
    
    return answer

# 딕셔너리를 사용하였으면 더 간결한 코드로 해결 가능
'''
def solution(weights):
    dic={}
    friend_list=[2,3/2,4/3]
    answer = 0
    for weight in weights:
        if weight in dic:
            dic[weight]+=1
        else:
            dic[weight]=1

    for weight in dic:
        if dic[weight]>1:
            answer+=dic[weight]*(dic[weight]-1)/2
        for friend in friend_list:
            if weight*friend in dic:
                answer+=dic[weight]*dic[weight*friend]

    return answer
'''
