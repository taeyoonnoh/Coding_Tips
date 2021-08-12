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

def solution(n, costs):
    result = 0
    costs = sorted(costs,key=lambda x : x[2])
    parent = [i for i in range(n+1)]
    for edge in costs : 
        a,b,cost = edge 
        if find_parent(parent,a) != find_parent(parent,b) : 
            union_parent(parent,a,b)
            result += cost
    return result
