import sys
sys.setrecursionlimit(10**6)

N = int(input())
graph = [list(sys.stdin.readline()) for _ in range(N)]
    
drow = [-1,0,1,0]
dcol = [0,-1,0,1]

def dfs(x,y) : 
    visited[x][y] = True

    for i in range(4) : 
        dx = x + drow[i]
        dy = y + dcol[i]

        if dx<0 or dx>=N or dy<0 or dy>=N : 
            continue

        if graph[x][y] == graph[dx][dy] and visited[dx][dy] == False : # visited[dx][dy] == False 안 써줘서 시간 초과가 났던 것 같음
            dfs(dx,dy)

visited = [[False] * N for _ in range(N)]
counts_one = 0
counts_two = 0

for i in range(N) : 
    for j in range(N) : 
        if visited[i][j] == False : 
            dfs(i,j)
            counts_one+=1

for i in range(N) : 
    for j in range(N) : 
        if graph[i][j] == 'R' : 
            graph[i][j] = 'G'

visited = [[False] * N for _ in range(N)]

for i in range(N) : 
    for j in range(N) : 
        if visited[i][j] == False : 
            dfs(i,j)
            counts_two+=1

print(counts_one, counts_two)

# ===========================================================================
# 1. visited False 이면 ==> 경로 탐색 후 이전 값과 같으면 dfs 함수 진행 ==> visited 해당 위치 True 로 변환
# 2. 'R' 을 'G' 로 변환 후 1번 step 다시 수행
