# 첫번째 시도
# 실패

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

# =======================================================================================================================

# 2번째 시도
from collections import deque
import heapq

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]

drow = [0,1,0,-1]
dcol = [1,0,-1,0]

q = []

for i in range(N) :
    for j in range(N) : 
        if graph[i][j] == 9 : 
            heapq.heappush(q,(0,i,j))
            graph[i][j] = 0

def bfs() : 
    ans,size,eat = 0,2,0
    visited = [[False]*N for _ in range(N)]
    while q : 
        dist,x,y = heapq.heappop(q)
        if 0 < graph[x][y] < size : 
            eat+=1
            graph[x][y] = 0 
            if eat == size : 
                size+=1
                eat = 0
            ans+=dist
            dist = 0 
            while q : # 만약 조건에 맞는 x,y 좌표에 도달한다면 q 에 있는 원소들 다 없애주고 visited 도 다시 초기화 해주는 작업이 중요!
                q.pop()
            visited = [[False]*N for _ in range(N)]
        for i in range(4) : 
            ddist,dx,dy = dist+1,x+drow[i],y+dcol[i]
            if dx<0 or dx>=N or dy<0 or dy>= N : 
                continue
            if 0 < graph[dx][dy] and graph[dx][dy] > size or visited[dx][dy] : 
                continue
            visited[dx][dy] = True
            heapq.heappush(q,(ddist,dx,dy))
    print(ans)

bfs()

# ================================================================================================================================
# visited 를 계속해서 초기화 시켜줘야 함
# 좀만 더 생각하면 쉽게 풀 수 있는 문제라고 생각 함..ㅜㅜ
# 그래프는 참 어렵다
