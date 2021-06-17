import sys

V,E = list(map(int,input().split(" ")))
edges = []
for i in range(E) : 
    edges.append(map(int,sys.stdin.readline().split())) # 이렇게 해야 통과하더라.. ㅜㅜ 백준에선 그럼

def find_parent(parent,x) : 
    if parent[x]!=x : 
        return find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b) : 
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b : 
        parent[b] = a 
    else :
        parent[a] = b

parent= [i for i in range(V+1)]

for a,b in edges : 
    union_parent(parent,a,b)

for i in range(1,V+1) : 
    parent[i] = find_parent(parent,i)

print(len(set(parent[1:])))
