arr = [False,False] + [True] * 9999
m = int(10000**0.5)
for i in range(2,m+1) : 
    if arr[i] == True : 
        for j in range(i+i,len(arr),i) : 
            arr[j] = False

M = int(input())
N = int(input())
prime = [i for i in range(M,N+1) if arr[i]]
if prime : 
    print(sum(prime))
    print(min(prime))
else :
    print(-1)

# ==============================================
# arr 로 범위를 먼저 설정 해줌
# 아리스토테네스의 체 알고리즘 활용
