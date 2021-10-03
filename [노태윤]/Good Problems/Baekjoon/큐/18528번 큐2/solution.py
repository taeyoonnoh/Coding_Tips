from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
q = deque([])
for i in range(N) : 
    cmd = input().split()
    if len(cmd) >= 2 : 
        q.append(int(cmd[1]))
    else : 
        if cmd[0] == 'pop' : 
            ans = -1 if not q else q.popleft()
            print(ans)
        elif cmd[0] =='size' : 
            print(len(q))
        elif cmd[0] =='empty' : 
            ans = 1 if not q else 0
            print(ans)
        elif cmd[0] == 'front' : 
            ans = -1 if not q else q[0]
            print(ans)
        elif cmd[0] == 'back' : 
            ans = -1 if not q else q[-1]
            print(ans)

  # ================================================
  # import sys 해야 시간초과 안남!
