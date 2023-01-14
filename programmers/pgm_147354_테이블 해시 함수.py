#
#  Date  : 2023-01-14
#  URL   : https://school.programmers.co.kr/learn/courses/30/lessons/147354
#
#  풀이에 걸린 시간 : 22분

def solution(data, col, row_begin, row_end):
    answer = 0
    sorted_data = sorted(data, key = lambda x:(x[col-1],-x[0]))
    
    s_i_arr = []
    for i in range(row_begin-1,row_end):
        s_i =0
        for j in sorted_data[i]:
            s_i += j % (i+1)
        s_i_arr.append(s_i)
    
    answer = s_i_arr[0]
    for i in range(1, len(s_i_arr)):
        answer = answer ^ s_i_arr[i]
            
    return answer
