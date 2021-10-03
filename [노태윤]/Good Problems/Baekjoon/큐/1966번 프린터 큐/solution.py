from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for i in range(T) : 
    N,ind = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    q,check_ind = deque([]),0
    for i in arr : 
        q.append((i,check_ind))
        check_ind+=1
    answer = 1
    while True : 
        max_val = max([i[0] for i in q])
        cur_val,cur_ind = q[0]
        if max_val == cur_val and ind==cur_ind : 
            print(answer) 
            break
        elif max_val == cur_val : 
            q.popleft()
            answer+=1
        else : 
            q.append(q.popleft())
