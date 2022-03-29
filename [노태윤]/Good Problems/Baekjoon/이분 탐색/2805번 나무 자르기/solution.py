N,M = map(int,input().split())
arr = list(map(int,input().split()))
start, end = 1, max(arr)

while start <= end : 
    mid = (start + end) // 2
    heights = 0

    print(start,end, mid)

    for i in arr : 
        if i > mid : 
            heights += (i-mid)
    
    print("heights : ", heights)

    if heights >= M : 
        start = mid + 1
    else : 
        end = mid - 1
    
    print("====================")

print(end)

# ==========================================
# 이분 탐색 변형문제 (매우 쉽네~~)
