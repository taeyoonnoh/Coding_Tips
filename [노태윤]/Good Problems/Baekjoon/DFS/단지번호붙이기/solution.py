danji = int(input())
danji_graph = [[] for i in range(danji)]
for i in range(danji) : 
    danji_graph[i] = list(map(int,input()))

counts = 0
total_list = []

def dfs(x,y) : 
    global counts
    if x<0 or x >= danji or y<0 or y>=danji : 
        return False 
            
    if danji_graph[x][y] == 1 :
        danji_graph[x][y] = 0

        counts+=1
        dfs(x-1,y) # stack 활용
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)

        return counts
    return False

for i in range(danji) : 
    for j in range(danji) : 
        val = dfs(i,j)
        if val : 
            total_list.append(val)
            counts = 0 # 있다 싶으면 counts append 하고 counts 초기화하기
print(len(total_list))
for i in sorted(total_list) : 
    print(i)
