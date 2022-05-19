#
#  Date  : 2022-05-19
#  URL   : https://programmers.co.kr/learn/courses/30/lessons/72411
#
#  풀이에 걸린 시간 : 54분

from itertools import combinations

def solution(orders, course):
    answer = []
    dict_set = dict() 
    max_val = [0]*11
    
    # 주문목록을 순회
    for order in orders:
        for i in range(2,len(order)+1):
            # 2개이상의 가능한 모든 조합
            for c in list(combinations(order,i)):
                # 튜플을 정렬하고 문자열로 join
                s = ''.join(sorted(c))
                # 딕셔너리에 추가, 해당 조합에대한 주문 수 카운트
                if s in dict_set:
                    dict_set[s] +=1
                else:
                    dict_set[s] =1
                # 2회 이상 주문된 경우, max(가장 많이 주문된조합)을 계산해둔다.
                if dict_set[s] >=2:
                    max_val[len(s)] = max(max_val[len(s)], dict_set[s])
    
    # 코스요리를 구성하는 메뉴의 개수
    for num in course:
        # 딕셔너리의 키와 값 순회, items() 메소드
        for k,v in dict_set.items():
            # 메뉴가 num개이고, 가장 많이 주문되고, 2회이상 주문된 코스요리를 찾는다.
            if len(k)==num and v==max_val[num] and v>=2:
                answer.append(k)
                
    return sorted(answer)
