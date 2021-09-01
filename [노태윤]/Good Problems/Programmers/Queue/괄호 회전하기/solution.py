from collections import deque

def solution(s) : 
    answer = 0
    for i in range(len(s)) : 
        split = list(s)
        q = deque(split)
        stacker = []

        while q : 
            popped = q.popleft()
            if not stacker : 
                stacker.append(popped)
                continue
            
            if popped == ')' and stacker[-1] == '(' : 
                stacker = stacker[:-1]
            elif popped =='}' and stacker[-1] == '{' : 
                stacker = stacker[:-1]
            elif popped == ']' and stacker[-1] =='[' : 
                stacker = stacker[:-1]
            else : 
                stacker.append(popped)
        if not stacker : 
            answer+=1
        s = s[1:] + s[0]
    return answer
  
  # ===================================================
  # 문제 잘 읽자!
  # 닫히면 없애는 방식으로 접근해야 맞음
