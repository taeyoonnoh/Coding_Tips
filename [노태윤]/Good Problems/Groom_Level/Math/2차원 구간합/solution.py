N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
x1,y1,x2,y2 = list(map(int,input().split()))
psa = [[0 for _ in range(N)] for _ in range(N)]
psa[0][0] = arr[0][0]

for i in range(1,N) : 
    psa[0][i] = psa[0][i-1] + arr[0][i]

for i in range(1,N) : 
    psa[i][0] = psa[i-1][0] + arr[i][0]

for i in range(1,N) : 
    for j in range(1,N) : 
        psa[i][j] = psa[i-1][j] + psa[i][j-1] - psa[i-1][j-1] + arr[i][j]

print(psa[x2][y2]-(psa[x1-1][y2]+psa[x2][y1-1]-psa[x1-1][y1-1]))
