from collections import deque

V,E,start = list(map(int,input().split(" ")))
graph = [[] for i in range(V+1)]
for i in range(E) : 
    a,b = list(map(int,input().split(" ")))
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,len(graph)) : 
    graph[i] = sorted(graph[i]) # 내부 element 정렬 해줘야 함

dfs_visited = [False] * (V + 1)
bfs_visited = [False] * (V + 1)

dfs_answer_list = []
bfs_answer_list = []

def dfs(graph,v,dfs_visited) : 
    global dfs_answer_list
    dfs_visited[v] = True
    dfs_answer_list.append(str(v))
    for i in graph[v] : 
        if not dfs_visited[i] : 
            dfs(graph,i,dfs_visited)

def bfs(graph,start,bfs_visited) :
    global bfs_answer_list
    queue = deque([start])
    bfs_visited[start] = True
    bfs_answer_list = [str(start)]
    while queue : 
        popped = queue.popleft()
        for i in graph[popped] :
            if not bfs_visited[i] : 
                queue.append(i)
                bfs_answer_list.append(str(i))
                bfs_visited[i] = True

dfs(graph,start,dfs_visited)
bfs(graph,start,bfs_visited)

print(' '.join(dfs_answer_list))
print(' '.join(bfs_answer_list))
