#
#  Date  : 2023-01-18
#  URL   : https://programmers.co.kr/learn/courses/30/lessons/150370
#
#  풀이에 걸린 시간 : 15분

def solution(today, terms, privacies):
    answer = []
    
    y,m,d = today.split(".")
    now_date = int(d) + (int(m)*28) + (int(y)*28*12)
    
    terms_dict = dict()
    for t in terms:
        privacy, term = t.split()
        terms_dict[privacy] = term
        
    for i in range(len(privacies)):
        day, privacy = privacies[i].split()
        
        ny,nm,nd = day.split(".")
        date = int(nd) + (int(nm)*28) + (int(ny)*28*12)

        if now_date >= date + int(terms_dict[privacy])*28:
            answer.append(i+1)
            
    return answer
