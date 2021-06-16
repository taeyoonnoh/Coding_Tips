from collections import deque

N,M = list(map(int,input().split(" ")))
graph = [[] for i in range(N)]
for i in range(N) : 
    graph[i] = list(map(int,input()))

dcol = [1,0,-1,0]
drow = [0,1,0,-1]

queue = deque([])
queue.append([0,0]) # 0,0 부터 시작

visited = [[False]*M for _ in range(N)]
visited[0][0] = True

while queue :
    curr_x,curr_y = queue.popleft()
    for i in range(4) : 
        dx = curr_x + drow[i]
        dy = curr_y + dcol[i]

        if not 0 <= dx <= N-1 or not 0<= dy <= M-1 : # 범위 벗어나면 그냥 continue
            continue
        
        if graph[dx][dy] == 0 : # 주변에 0 이면 그냥 continue
            continue
        
        if visited[dx][dy] == True : # True 여도 continue
            continue

        if graph[dx][dy] == 1 :      
            graph[dx][dy]+=graph[curr_x][curr_y] # 계속 더해주기 
            queue.append([dx,dy])
            visited[dx][dy] = True
print(graph[N-1][M-1])
