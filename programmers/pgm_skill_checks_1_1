#
#  Date  : 2022-09-21
#  URL   : https://programmers.co.kr/skill_checks/420710
#
#  풀이에 걸린 시간 : 7분

def solution(nums):
    answer = 0
    arr = [0]*200001
    for i in nums:
        arr[i] += 1

    count =0

    for i in range(1,200001):
        if arr[i] != 0 :
            count +=1
            if count == len(nums)/2:
                break;
    answer = count
    return answer
