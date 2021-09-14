import heapq
import sys
input = sys.stdin.readline

T = int(input())
q = []
ans = []
for _ in range(T) : 
    cmd = int(input())
    if cmd == 0 : 
        if not q : # q 에 아무것도 없으면 0 append
            ans.append(0)
        else : 
            ans.append((-heapq.heappop(q))) # 최대 힙이기 때문에 - 붙여줘야함
    else : 
        heapq.heappush(q,-cmd) # 최대 힙이기 때문에 0 붙여줘야함
for i in ans : 
    print(i)
