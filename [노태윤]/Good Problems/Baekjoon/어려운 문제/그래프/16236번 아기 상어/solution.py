from collections import deque
import heapq

drow = [0,1,0,-1]
dcol = [1,0,-1,0]
visited = [[False]*N for _ in range(N)]
fish = []

for i in range(N) :
    for j in range(N) : 
        if 1<=graph[i][j]<=6 : 
            heapq.heappush(fish,(graph[i][j],i,j))
        elif graph[i][j] == 9 : 
            shark_x,shark_y = i,j
            graph[i][j] = 0

# print(fish)
def bfs(x,y) : 
    q = deque([(x,y,0)])
    ans,size,eat = 0,2,0
    isTrue = False
    while q : 
        x,y,count = q.popleft()
        for i in range(4) : 
            dx = x + drow[i]
            dy = y + dcol[i]

            if 0<=dx<N and 0<=dy<N : 
                if graph[dx][dy] == 0 and visited[dx][dy] == False : 
                    # visited[dx][dy] = True
                    q.append((dx,dy,count+1))
                elif (1<=graph[dx][dy]<=6) and (visited[dx][dy] == False) and (dx==fish[0][1]) and (dy==fish[0][2]):
                    if size>graph[dx][dy] :
                        eat+=1
                        ans+=count
                        if eat == size : 
                            size+=1
                            eat = 0
                        visited[dx][dy] = True
                        q.append((dx,dy,count+1))
                        heapq.heappop(fish)
                        if not fish : 
                            isTrue = True
                            break
                    else : 
                        continue

        # print(q)
        # print(ans)
        if isTrue : 
            break
    print(ans)

bfs(shark_x,shark_y)
