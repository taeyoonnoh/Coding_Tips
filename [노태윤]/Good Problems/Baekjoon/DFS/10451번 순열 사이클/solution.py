from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(cur_node) : 
    visited[cur_node] = 1
    for i in new_dict[cur_node] : 
        if not visited[i] : 
            dfs(i)

T = int(input())
ans = []
for _ in range(T) : 
    N = int(input())
    arr = list(map(int,input().split()))
    arr = list(enumerate(arr,1))
    new_dict = defaultdict(list)
    for a,b in arr : 
        new_dict[a].append(b)
    visited = [0] * (N+1)
    count = 0
    for i in range(1,N+1) : 
        if not visited[i] : 
            dfs(i)
            count+=1
    ans.append(count)
for i in ans : 
    print(i)

# ==================================
# BFS 로 접근하면 쉽게 풀 수 있는 문제
# 처음 조회하는 노드는 visited 에 1 로 업데이트
# 만약 for i in range(1,N+1) 루프 과정에서 이미 1로 업데이트 되어 있다면 그냥 무시 (이미 사이클로 카운티이 끝남)
