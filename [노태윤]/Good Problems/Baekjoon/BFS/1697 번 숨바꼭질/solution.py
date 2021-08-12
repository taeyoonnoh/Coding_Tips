from collections import deque

A,B = list(map(int,input().split(" ")))

def bfs(A,B) :
    if A == B : 
        return 0 
    queue = deque([])
    queue.append((A,0))
    visited = [False] * 100001 # input 값이 100000 까지니까 index 는 100001 

    while queue : 
        num,count = queue.popleft()
        for i in [num+1,num-1,num*2] : 
            if i<0 or i>100000 : 
                continue
            if visited[i] == True :
                continue
            
            if i == B :
                count+=1
                return count
            
            else :
                visited[i] = True
                queue.append((i,count+1))

    return count

print(bfs(A,B))
