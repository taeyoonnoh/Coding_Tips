import sys

# 소수 구하는 알고리즘
sieve = [True] * (10000+1)
sieve[0],sieve[1]=False,False
m = int(10000**0.5)
for i in range(2,m+1) :
    if sieve[i]==True :
        for j in range(i+i,10000+1,i) :
            sieve[j]=False

N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(N)]

ans_list = []

# 반으로 나누고 역순으로 찾기
# 만약 소수이고 뺸 값도 소수이면 break 
# 이 때 두 소수의 차이가 min이 되기 때문!
for i in arr : 
    check = i//2
    for j in range(check,1,-1) : 
        if sieve[i-j] == True and sieve[j]==True : 
            a,b = j,i-j
            break
    ans_list.append((a,b))

for a,b in ans_list : 
    print(a,b)
