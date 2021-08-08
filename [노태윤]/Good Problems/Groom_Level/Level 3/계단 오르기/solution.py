from collections import deque

N = int(input())
q = deque([0])
count = 0
while q : 
	x = q.popleft()
	if x == N :
		count+=1
		continue
	dx = x+1
	dxx = x+2
	if dx<=N :
		q.append(dx)
	if dxx<=N :
		q.append(dxx)
print(count)
