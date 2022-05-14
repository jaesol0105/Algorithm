#
#  Date  : 2022-05-14
#  URL   : https://programmers.co.kr/learn/courses/30/lessons/42840
#
#  풀이에 걸린 시간 : 11분

def solution(answers):
    answer = []
    
    score = [0,0,0]
    
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]
    
    for i in range(len(answers)):
        if answers[i] == p1[i%len(p1)]:
            score[0] = score[0]+1
        if answers[i] == p2[i%len(p2)]:
            score[1] = score[1]+1
        if answers[i] == p3[i%len(p3)]:
            score[2] = score[2]+1           
    
    for i in range(3):
        if score[i] == max(score):
            answer.append(i+1)
    return answer
