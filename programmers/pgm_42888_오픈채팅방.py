#
#  Date  : 2022-05-08
#  URL   : https://programmers.co.kr/learn/courses/30/lessons/42888
#

def solution(record):
    answer = []
    
    msg = list()
    id_name_table = dict()
    
    for rec in record:
        if len(rec.split(" ")) == 2:
            cmd, uid = rec.split(" ")
            msg.append([uid,cmd])
            
        else:
            cmd, uid, uname = rec.split(" ")
        
            if cmd == "Enter":
                id_name_table[uid] = uname
                msg.append([uid,cmd])
        
            if cmd == "Change":
                id_name_table[uid] = uname
        
            if cmd == "Leave":
                msg.append([uid,cmd])
    
    
    str1 = "님이 들어왔습니다."
    str2 = "님이 나갔습니다."
    str3 = ""
    
    for uid,cmd in msg:
        if cmd == "Enter":
            str3 = id_name_table[uid] + str1
        if cmd == "Leave":
            str3 = id_name_table[uid] + str2
        answer.append(str3)            
    
    return answer
