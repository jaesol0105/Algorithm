#
#  Date  : 2022-05-12
#  URL   : https://programmers.co.kr/learn/courses/30/lessons/67256
#
#  풀이에 걸린 시간 : 26분

def solution(numbers, hand):
    answer = ''
    # 초기 손가락 위치
    l_finger = [3,0]
    r_finger = [3,2]
    
    for num in numbers:
        # 왼쪽 키패드
        if num == 1 or num == 4 or num == 7:
            answer = answer + 'L'
            l_finger=[num//3,0]
        # 오른쪽 키패드
        elif num == 3 or num == 6 or num == 9:
            answer = answer + 'R'
            r_finger=[(num//3)-1,2]
        # 가운데 키패드
        else:
            if num == 2 or num == 5 or num == 8:
                target= [num//3,1]
            else:
                target= [3,1]
            
            # 거리 계산
            l_len = abs(target[0]-l_finger[0])+abs(target[1]-l_finger[1])
            r_len = abs(target[0]-r_finger[0])+abs(target[1]-r_finger[1])
            
            if l_len > r_len:
                answer = answer + 'R'
                r_finger = target
            elif l_len == r_len:
                if hand == "left":
                    answer = answer + 'L'
                    l_finger = target
                else:
                    answer = answer + 'R'
                    r_finger = target
            else:
                answer = answer + 'L'
                l_finger = target
                    
    return answer
