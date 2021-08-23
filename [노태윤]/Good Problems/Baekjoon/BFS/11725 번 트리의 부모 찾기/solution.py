from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
parent = [i for i in range(N+1)]
graph = [[] for _ in range(N+1)]
for _ in range(N-1) : 
    a,b = list(map(int,input().split()))
    graph[a].append(b)
    graph[b].append(a)

visited = [False]*(N+1)
q = deque([1])

while q : 
    cur_node = q.popleft()
    for i in graph[cur_node] : # 방문한적 없으면 업데이트!
        if visited[i]==False :
            parent[i]=cur_node
            visited[i]=True
            q.append(i)

for i in range(2,N+1) : 
    print(parent[i])
