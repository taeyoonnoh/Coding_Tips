# 실패
from collections import defaultdict

def solution(enter,leave) : 
    answer,arr = [],[]
    new_dict = defaultdict(list)
    index = 0
    for i in range(len(enter)) : 
        arr.append(enter[i])
        for j in arr : 
            set_list = list(set(arr) - set([j]))
            new_dict[j]+=set_list
        while True : 
            if not leave : 
                break
            if leave[0] in arr : 
                arr.remove(leave[0])
                leave = leave[1:]
                continue
            break

    for i in range(1,len(enter)+1) : 
        answer.append(len(set(new_dict[i])))

    return answer
  
# ============================================
# 성공

def solution(enter,leave) : 
    answer = [0] * len(enter)
    room = []
    index = 0
    for l in leave : 
        while l not in room : 
            room.append(enter[index])
            index+=1
        room.remove(l)
        for r in room : 
            answer[r-1] += 1 
        answer[l-1] += len(room)
    return answer
# =======================================
# 왜 시간 초과가 나는진 모르겠음.. 
# dictionary 써서 그런가..? 확인해보자 다음에..
