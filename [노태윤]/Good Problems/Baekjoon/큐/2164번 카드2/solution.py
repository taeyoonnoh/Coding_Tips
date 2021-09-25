from collections import deque

N = int(input())
arr = [i for i in range(1,N+1)]
q = deque(arr)

while len(q) != 1 : 
    q.popleft()
    q.append(q.popleft())
print(q[0])

# ==============================
# 큐 popleft() 가 기본 list 의 pop() 보다 빠르다는 것을 항상 명심하자!
