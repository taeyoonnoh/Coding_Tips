import sys

K,N = map(int,input().split())
arr = [int(sys.stdin.readline()) for _ in range(K)]
start, end = 1, max(arr)

while start <= end : 
    mid = (start + end) // 2
    lines = 0

    for i in arr : 
        lines += i//mid
    
    if lines >= N : 
        start = mid + 1
    else : 
        end = mid - 1

print(end)

# ==================================================
# 평범한 이분탐색 문제였더라.... (조금 변형되었음)
