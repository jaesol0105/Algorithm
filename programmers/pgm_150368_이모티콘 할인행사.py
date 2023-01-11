#
#  Date  : 2023-01-11
#  URL   : https://programmers.co.kr/learn/courses/30/lessons/150368
#
#  풀이에 걸린 시간 : 59분

from collections import deque

def total_price_calculate(users,emoticons,now_discount):
    num_of_plus = 0
    amount_of_price = 0
    
    for urate, uprice in users:
        total_price = 0
        for i in range(len(now_discount)):
            if now_discount[i] >= urate: # 할인 비율이 유저의 기준보다 높으면
                total_price += emoticons[i] * (1 - now_discount[i]/100) # 구매
        if total_price >= uprice: # 총 금액이 기준 가격 이상인경우
            num_of_plus +=1 # 가입
        else:
            amount_of_price += total_price
    return [num_of_plus,amount_of_price]
    
def solution(users, emoticons):
    answer = [0,0]
    m = len(emoticons)
    
    q = deque([])
    for i in [10,20,30,40]:
        q.append([i])
    
    # 10% 20% 30% 40% 에서 중복순열 m개 뽑기 -> 완전 탐색으로 구현
    while q:
        now_discount = q.popleft()
        if len(now_discount) == m: # m개일 경우
            result = total_price_calculate(users,emoticons,now_discount) # 계산
            if result[0] > answer[0]: # 더 많은 가입자를 만드는 경우
                answer = result[:]
            elif result[0] == answer[0]: # 가입자 수는 같지만 수익이 더 많은 경우
                if result[1] > answer[1]:
                    answer = result[:]
                
        else: # 아직 m개가 아닌 경우
            for i in [10,20,30,40]: # 완전 탐색
                temp = now_discount[:]
                temp.append(i)
                q.append(temp)
    
    return answer
