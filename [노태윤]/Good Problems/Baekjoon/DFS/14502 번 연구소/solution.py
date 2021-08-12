from itertools import combinations
import copy

row,col = list(map(int,input().split(" ")))
graph = []
for i in range(row) : 
    # graph.append(map(int,sys.stdin.readline().split()))
    graph.append(list(map(int,input().split(" "))))

virus_coords = []
zero_coords = []

for i in range(row) : 
    for j in range(col) : 
        if graph[i][j] == 2 :
            virus_coords.append((i,j))
        if graph[i][j] == 0 : 
            zero_coords.append((i,j))

comb_list = list(combinations(zero_coords,3))

def dfs(x,y,copy_graph) : 

    if x<0 or x>=row or y<0 or y>=col : 
        return 

    if copy_graph[x][y]==0 : 
        copy_graph[x][y] = 2 
        dfs(x-1,y,copy_graph) # dfs 진행 
        dfs(x+1,y,copy_graph)
        dfs(x,y-1,copy_graph)
        dfs(x,y+1,copy_graph)     

max_list = []
for a,b,c in comb_list : 
    copy_graph = copy.deepcopy(graph) # deepcopy

    copy_graph[a[0]][a[1]] = 1 
    copy_graph[b[0]][b[1]] = 1
    copy_graph[c[0]][c[1]] = 1

    for x,y in virus_coords : 
        dfs(x-1,y,copy_graph) # (초기 바이러스 주변 확인)
        dfs(x+1,y,copy_graph)
        dfs(x,y-1,copy_graph)
        dfs(x,y+1,copy_graph)

    zero_counts = 0
    for i in copy_graph : 
        zero_counts+=i.count(0)
    max_list.append(zero_counts) # 이 중 max 값만 반환

print(max(max_list))
