#
#  Date  : 2023-02-04
#  URL   : https://programmers.co.kr/learn/courses/30/lessons/154539
#

def solution(numbers):
    answer = [-1]*len(numbers)
    stack = []
    
    for i in range(len(numbers)):
        while len(stack) > 0 and numbers[i] > stack[len(stack)-1][0]:
            data = stack.pop()
            answer[data[1]] = numbers[i]
        stack.append([numbers[i],i])
        
    return answer
