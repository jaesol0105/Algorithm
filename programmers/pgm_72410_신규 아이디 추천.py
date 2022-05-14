#
#  Date  : 2022-05-13
#  URL   : https://programmers.co.kr/learn/courses/30/lessons/72410
#
#  풀이에 걸린 시간 : 32분

def solution(new_id):
    answer = ''

    # 조건 1,2
    newid2 = ''
    for char in new_id.lower():
        if char.isalpha() or char.isdigit() or char == '.' or char == '_' or char == '-':
            newid2 += char
        # if char.isalnum() or char in '-_.' 을 사용하면 더 간단하게 구현 할 수 있다.
    
    # 조건 3
    newid3 = ''
    newid3 += newid2[0]
    for i in range(1,len(newid2)):
        if newid2[i-1] == newid2[i] and newid2[i] == '.':
            continue
        else:
            newid3 += newid2[i]
    # while '..' in answer: answer = answer.replace('..', '.')
    
    # 조건 4
    newid4 = ''
    for i in range(len(newid3)):
        if (i == 0 and newid3[i] =='.') or (i == len(newid3)-1 and newid3[i] =='.'):
            continue
        else:
            newid4 += newid3[i]
    
    # 조건 5
    if newid4 == '':
        newid4 = 'a'
        
    # 조건 6
    if len(newid4) >= 16:
        newid4 = newid4[0:15]
        if newid4[len(newid4)-1] == '.':
            newid4 = newid4[0:14]
    
    # 조건 7
    if len(newid4) <= 2:
        add = newid4[len(newid4)-1]
        for _ in range(3-len(newid4)):
            newid4 += add
    
    answer = newid4
    return answer
