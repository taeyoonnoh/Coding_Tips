from collections import deque

N,K = list(map(int,input().split()))

arr = [i for i in range(1,N+1)]
q = deque(arr)
ans = []
while q : 
    for i in range(K-1) : 
        q.append(q.popleft())
    ans.append(str(q.popleft()))
print('<' + ', '.join(ans) + '>')
# ========================================
# 큐로 풀면 쉽게 풀 수 있음!
