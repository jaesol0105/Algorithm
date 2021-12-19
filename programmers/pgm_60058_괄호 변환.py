#
#  Date  : 2021-12-19
#  URL   : https://programmers.co.kr/learn/courses/30/lessons/60058
#

def check(s):
    if s == "":
        return ""

    left = 0
    right = 0

    for i in range(len(s)):
        if s[i] == '(':
            left += 1
        if s[i] == ')':
            right += 1
        if left == right and left != 0:
            u = s[0:i + 1]
            v = s[i + 1:]
            break

    stack = []
    for i in range(len(u)):
        if u[i] == '(':
            stack.append('(')
        if u[i] == ')':
            if not stack:
                temp = ""
                for i in range(1, len(u) - 1):
                    if u[i] == '(':
                        temp = temp + ')'
                    if u[i] == ')':
                        temp = temp + '('

                return '(' + check(v) + ')' + temp
            stack.pop()
    return u + check(v)


def solution(p):
    answer = ''
    answer = check(p)
    return answer