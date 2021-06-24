import sys
sys.setrecursionlimit(10**6)

M,N,K = list(map(int,sys.stdin.readline().split()))
coords = []
graph = [[0] * N for _ in range(M)]
for i in range(K) : 
    B,A,D,C = list(map(int,sys.stdin.readline().split()))
    for i in range(A,C) : 
        for j in range(B,D) : 
            if graph[i][j] == 1 : 
                continue
            graph[i][j]=1 # graph 만 잘 설정해준다면 나머지는 기본적인 dfs 문제로 해결할 수 있음

def dfs(x,y) : 
    global count
    if x<0 or x>=M or y<0 or y>=N : 
        return False
    if graph[x][y] == 0 :
        graph[x][y] = 1 
        count+=1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return count
    return False

answer_list = []

for i in range(M) : 
    for j in range(N) : 
        count = 0
        ans = dfs(i,j)
        if ans : 
            answer_list.append(ans)

print(len(answer_list))
for i in sorted(answer_list) : 
    print(i,end=' ')
