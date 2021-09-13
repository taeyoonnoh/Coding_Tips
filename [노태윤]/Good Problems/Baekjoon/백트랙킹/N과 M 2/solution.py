from itertools import combinations
import sys
input = sys.stdin.readline

N,M = list(map(int,input().split()))
arr = [i for i in range(1,N+1)]
ans = list(combinations(arr,M))
for i in ans : 
    print(*i)

# =====================================
# 재귀적으로 풀기

n,m = list(map(int,input().split()))
s = []
def dfs(start):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(start,n+1):
        if i not in s:
            s.append(i)
            dfs(i+1)
            s.pop()
dfs(1)
