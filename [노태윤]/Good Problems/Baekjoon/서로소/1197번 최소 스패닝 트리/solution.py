import sys
input = sys.stdin.readline

def find_parent(parent,x) : 
    if parent[x] != x : 
        return find_parent(parent,parent[x])
    else : 
        return parent[x]

def union_parent(parent,a,b) : 
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b : 
        parent[b] = a 
    else : 
        parent[a] = b        

V,E = list(map(int,input().split()))
arr = [list(map(int,input().split())) for _ in range(E)]
arr = sorted(arr,key=lambda x : x[2])
parent = [i for i in range(V+1)]
count = 0

for a,b,cost in arr : 
    if find_parent(parent,a) != find_parent(parent,b) : 
        union_parent(parent,a,b)
        count+=cost

print(count)
