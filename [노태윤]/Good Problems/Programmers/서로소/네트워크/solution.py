def find_parent(parent,i) : 
    if parent[i] != i :
        return find_parent(parent,parent[i])
    else :
        return parent[i]

def union_parent(parent,a,b) : 
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a > b : 
        parent[a] = b 
    else :
        parent[b] = a
    
def solution(n, computers):
    parent = [i for i in range(n+1)]
    edge_list = []
    for i in range(len(computers)) : 
        for j in range(len(computers[0])) : 
            if i != j :
                if computers[i][j] == 1 :
                    edge_list.append((i+1,j+1))
    
    for a,b in edge_list : 
        union_parent(parent,a,b)
    
    for i in range(1,n+1) : 
        parent[i] = find_parent(parent,i)

    return len(set(parent)) - 1
