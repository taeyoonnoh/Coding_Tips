import sys
sys.setrecursionlimit(10000) # recursion limit 정해주기

T = int(input())
tests = []

for i in range(T) : 
    col,row,num = list(map(int,input().split(" ")))
    baechu = [[0] * col for _ in range(row)]
    for j in range(num) : 
        b_col,b_row = list(map(int,input().split(" ")))
        baechu[b_row][b_col] = 1
    tests.append(baechu)

answer = []

def dfs(x,y,row,col,baechu) : 
    if x<0 or x>=row or y<0 or y>=col : 
        return False
    if baechu[x][y] == 1 : 
        baechu[x][y] = 0

        dfs(x-1,y,row,col,baechu)
        dfs(x+1,y,row,col,baechu)
        dfs(x,y-1,row,col,baechu)
        dfs(x,y+1,row,col,baechu)

        return True
    return False

for baechu in tests : 
    row = len(baechu)
    col = len(baechu[0])
    count = 0
    for i in range(row) : 
        for j in range(col) : 
            if dfs(i,j,row,col,baechu) == True : 
                count+=1
    answer.append(count)

for i in answer :
    print(i)
