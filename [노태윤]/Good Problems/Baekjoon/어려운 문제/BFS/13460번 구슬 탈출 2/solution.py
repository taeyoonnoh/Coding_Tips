from collections import deque
import sys
input = sys.stdin.readline

N,M = list(map(int,input().split()))
graph = [list(input()) for _ in range(N)]

for i in range(len(graph)) : 
    for j in range(len(graph[0])) : 
        if graph[i][j] == 'B' : 
            bx,by = [i,j]
        elif graph[i][j] =='R' : 
            rx,ry = [i,j]

drow = [-1,0,1,0]
dcol = [0,-1,0,1]

# 4차원 배열에 visited 담기
visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
visited[rx][ry][bx][by] = True

q = deque([(rx,ry,bx,by,1)])

# 간 거리와 벽 또는 탈출구를 만나지 않는 선에서 계속 움직이기
def move(x,y,dx,dy) : 
    distance = 0
    while graph[x+dx][y+dy] != '#' and graph[x][y] != 'O' : 
        x += dx
        y += dy
        distance +=1
    return x,y,distance

def bfs(q) : 
    while q : 
        rx,ry,bx,by,depth = q.popleft()
        if depth > 10 : 
            break
        for i in range(4) : 
            drx,dry,dist_r = move(rx,ry,drow[i],dcol[i])
            dbx,dby,dist_b = move(bx,by,drow[i],dcol[i])
            
            # 파란구슬이 탈출구에 도달하지 않는다면
            if graph[dbx][dby] != 'O' : 
              
                # 빨간구슬이 탈출구에 도달한다면
                if graph[drx][dry] == 'O' : 
                    return depth
                  
                # 파란구슬과 빨간구슬이 같은 지점에 있다면
                if drx==dbx and dry==dby : 
                    # 더 많이 간 것을 자신이 온 방향만큼 마이너스
                    if dist_r > dist_b : 
                        drx -= drow[i]
                        dry -= dcol[i]
                    elif dist_r < dist_b : 
                        dbx -= drow[i]
                        dby -= dcol[i]
                
                # 아직 방문하지 않았다면
                if not visited[drx][dry][dbx][dby] : 
                    visited[drx][dry][dbx][dby] = True
                    q.append((drx,dry,dbx,dby,depth+1))
    return -1
print(bfs(q))
