N,M = list(map(int,input().split()))
A = [list(map(int,input())) for _ in range(N)]
B = [list(map(int,input())) for _ in range(N)]

def convert(x,y,arr) : 
    for i in range(x,x+3) : 
        for j in range(y,y+3) : 
            A[i][j] = 1 - A[i][j]

count = 0

for i in range(N-2) : 
    for j in range(M-2) : 
        if A[i][j] != B[i][j] : 
            convert(i,j,A)
            count+=1

if A!=B : 
    print(-1)
else : 
    print(count)

# ==============================================
# 결국에는 한번에 업데이트 계속 해주고 count 1씩 증가
# 최종적으로 두개가 같지 않다면 -1, 그 외에는 count 출력!
