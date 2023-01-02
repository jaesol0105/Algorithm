#
#  Date  : 2023-01-02
#  URL   : https://school.programmers.co.kr/learn/courses/30/lessons/92341
#
#  풀이에 걸린 시간 : 52분

import math

def solution(fees, records):
    answer = []
    being_parked = dict()
    parking_time = dict()
    
    for record in records:
        time, car_num, content = record.split()
        if content == "IN": # IN
            being_parked[car_num] = int(time[0:2]) * 60 + int(time[3:5])
        else: # OUT
            use_time = (int(time[0:2]) * 60 + int(time[3:5])) - being_parked[car_num]
            if car_num in parking_time:
                parking_time[car_num] += use_time
            else:
                parking_time[car_num] = use_time
            being_parked[car_num] = -1
    
    for car_num, time in being_parked.items():
        if time !=-1:
            use_time = (23*60 + 59) - time
            if car_num in parking_time:
                parking_time[car_num] += use_time
            else:
                parking_time[car_num] = use_time
                
    parking_time = sorted(parking_time.items())
    for car_num, time in parking_time:
        fee = fees[1] + math.ceil((time-fees[0])/fees[2])*fees[3] if time>fees[0] else fees[1]
        answer.append(fee)
    
    return answer
