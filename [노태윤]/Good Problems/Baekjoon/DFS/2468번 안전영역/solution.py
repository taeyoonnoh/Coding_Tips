import copy
import sys
sys.setrecursionlimit(1000000)

N = int(input())
graph = []
min_val = int(1e9)
max_val = 0
for i in range(N) :
    rows = list(map(int,sys.stdin.readline().split()))
    check_min = min(rows)
    check_max = max(rows)
    if min_val > check_min : # min 값 업데이트
        min_val = check_min
    if max_val < check_max : # max 값 업데이트
        max_val = check_max 
    graph.append(rows)

def dfs(x,y) : 
    if x<0 or x>=N or y<0 or y>=N : 
        return False
    if copy_graph[x][y] == 1 : 
        copy_graph[x][y] = 0 

        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

answer_list = []

for i in range(min_val-1,max_val+1) : # min_val - 1 해준 이유는 다 같은 숫자로 구성된 graph가 있을 수도 있기 때문
    copy_graph = copy.deepcopy(graph)
    for k in range(N) : 
        for j in range(N) : # copy graph binary 형태로 바꿔주기
            if copy_graph[k][j] <= i :
                copy_graph[k][j] = 0
            else : 
                copy_graph[k][j] = 1
    counts = 0
    for k in range(N) : 
        for j in range(N) : 
            if dfs(k,j) == True : 
                counts+=1
    answer_list.append(counts)
print(max(answer_list))
