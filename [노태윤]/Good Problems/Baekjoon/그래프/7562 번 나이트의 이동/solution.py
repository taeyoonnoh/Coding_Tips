from collections import deque
import sys

input = sys.stdin.readline

drow = [-2,-2,2,2,1,1,-1,-1] 
dcol = [-1,1,-1,1,-2,2,-2,2]

def bfs(start,end,graph,N) :
    q = deque()
    q.append(start) 
    while q : 
        x,y = q.popleft()
        
        # 만약 끝지점에 도달한다면 return
        if x == end[0] and y == end[1] : 
            return graph[end[0]][end[1]]

        for i in range(8) : 
            dx = x + drow[i]
            dy = y + dcol[i]

            # 하나씩 업데이트
            if 0<=dx<N and 0<=dy<N and graph[dx][dy] == 0: 
                graph[dx][dy] = graph[x][y] + 1
                q.append([dx,dy])

ans_list = []

T = int(input())
for i in range(T) : 
    N = int(input())
    graph = [([0] * N) for _ in range(N)]
    start = list(map(int,input().split()))
    end = list(map(int,input().split()))
    ans_list.append(bfs(start,end,graph,N))

for i in ans_list : 
    print(i)
