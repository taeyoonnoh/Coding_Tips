import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

M,N = list(map(int,input().split()))
graph = [list(map(int,input().split())) for _ in range(M)]

drow = [-1,0,1,0]
dcol = [0,-1,0,1]
dp = [[-1] * N for _ in range(M)]

def dfs(x,y) : 
    # 끝 지점에 도달하면 1 반환
    if x == M-1 and y == N-1 : 
        return 1
    
    # memoization
    # 시간 단축 용
    # -1 이 아닌 이미 저장된 값이 있다면 해당 값 반환
    if dp[x][y] != -1 : 
        return dp[x][y]
    
    # 초기화하기
    dp[x][y] = 0

    # 이전 숫자보다 작다면 재귀적으로 호출하기
    # dp 업데이트하고 반환하기
    for i in range(4) : 
        dx = x + drow[i]
        dy = y + dcol[i]
        if 0<=dx<M and 0<=dy<N and graph[dx][dy] < graph[x][y] : 
            dp[x][y] += dfs(dx,dy)
    return dp[x][y]
print(dfs(0,0))
