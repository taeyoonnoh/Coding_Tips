from collections import deque
import sys
N,M = list(map(int,sys.stdin.readline().split()))
graph = [list(map(int,sys.stdin.readline().strip())) for _ in range(N)]

def bfs() : 
    graph[0][0] = 1

    q = deque([])
    q.append((0,0,0))

    zero_visit,one_visit = 0,0
    visited_counts = [[[zero_visit,one_visit] for _ in range(M)] for _ in range(N)]
    visited_counts[0][0][0] = 1

    dcol = [1,0,-1,0]
    drow = [0,1,0,-1]

    while q : 
        x,y,vis = q.popleft()

        if x == N-1 and y == M-1 : 
            return visited_counts[x][y][vis]

        for i in range(4) : 
            dx = x + drow[i]
            dy = y + dcol[i]

            if 0<=dx<=N-1 and 0<=dy<=M-1 :
                if graph[dx][dy] == 0 and visited_counts[dx][dy][vis] == 0 : # 만약 0 이면서 한번도 가보지 않은 구간이라면 (이 때 벽을 부수고 간 경우와 그렇지 않은 경우로 나뉨) 따라서 vis 따라 바꿔주기
                    visited_counts[dx][dy][vis] = visited_counts[x][y][vis] + 1
                    q.append((dx,dy,vis))
                
                elif graph[dx][dy] == 1 and vis == 0: # 만약 1 이면서 vis 도 0 이면 아래 코드 진행 (벽을 처음 통과하는 경우)
                    visited_counts[dx][dy][1] = visited_counts[x][y][0] + 1
                    q.append((dx,dy,1)) # 1 append 해줘서 따로 보관 
    return -1
print(bfs())
