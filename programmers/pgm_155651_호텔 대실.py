#
#  Date  : 2023-02-05
#  URL   : https://programmers.co.kr/learn/courses/30/lessons/155651
#
#  풀이에 걸린 시간 : 20분

import heapq

def solution(book_time):
    answer = 0
    book_times = []
    for stime, etime in book_time:
        s = int(stime[0:2])*60 + int(stime[3:5])
        e = int(etime[0:2])*60 + int(etime[3:5])
        book_times.append([s,e])
    book_times = sorted(book_times)
    
    #최소객실의 수 #청소시간 10분
    #입장시 끝난거 있나 검사하기
    heap = []
    using_room_cnt = 0
    
    for stime, etime in book_times:
        heapq.heappush(heap, etime)
        using_room_cnt += 1
        while stime >= heap[0]+10:
            heapq.heappop(heap)
            using_room_cnt -= 1
        answer = max(answer,using_room_cnt)
             
    return answer
