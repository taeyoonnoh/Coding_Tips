import sys

row,col = list(map(int,sys.stdin.readline().split()))
graph = []
for i in range(row) : 
    graph.append(sys.stdin.readline())

q = set([(0,0,graph[0][0])]) # set 로 묶은 이유는 중복이 발생할 수도 있음 --> 중복 연산이 되므로 set 사용

drow = [-1,0,1,0]
dcol = [0,-1,0,1]

count = 1

while q : 
    x,y,string = q.pop()

    for i in range(4) : 
        dx = x + drow[i]
        dy = y + dcol[i]

        if dx<0 or dx>=row or dy<0 or dy>=col : 
            continue

        if graph[dx][dy] not in string : 
            q.add((dx,dy,string+graph[dx][dy])) # set 를 사용했기 때문에 add
            count = max(count,len(string)+1)

print(count)
