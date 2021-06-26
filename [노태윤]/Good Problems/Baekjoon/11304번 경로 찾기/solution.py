import sys
from collections import deque

V = int(input())
graph = [[] for _ in range(V+1)]
path = []
for i in range(1,V+1) : 
    arr = list(map(int,sys.stdin.readline().split()))
    path.append(arr)
    for j in range(len(arr)) : 
        if arr[j] == 1 :
            graph[i].append(j+1)

def find(start,end,graph) : 
    q = deque([start])
    visited = [False] * (V+1)
    while q : 
        cur_node = q.popleft()
        if cur_node == end and visited[cur_node] == True: # 자기 자신으로 돌아오는 경우가 발생함 
            return True
        
        for i in graph[cur_node] : 
            if not visited[i] : 
                q.append(i)
                visited[i] = True
    return False

for i in range(V) : 
    for j in range(V) : 
        if find(i+1,j+1,graph) == True: 
            path[i][j] = '1'
        else :
            path[i][j] = '0'

for i in range(V) : 
    print(' '.join(path[i]))
