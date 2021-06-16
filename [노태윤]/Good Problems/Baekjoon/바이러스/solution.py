V = int(input())
E = int(input())
edge_list = []
for i in range(E) : 
    edge_list.append(list(map(int,input().split(" "))))

def find_parent(parent,x) : 
    if parent[x] != x : 
        return find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b) : 
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b : 
        parent[b] = a 
    else : 
        parent[a] = b

parent = [i for i in range(V+1)]

for a,b in edge_list : 
    union_parent(parent,a,b)

for i in range(1, V + 1):
    parent[i] = find_parent(parent,i) # 마지막으로 한번 더 수행해줘야 맞음

print(parent.count(1)-1)
