import sys
input = sys.stdin.readline

N,L = list(map(int,input().split()))
arr = list(map(int,input().split()))

arr.sort()

count = 0
tmp = 0

for i in arr : 
    if tmp < i : 
        count+=1
        tmp = i+L-1

print(count)

# ===================================
# 오름차순 정렬 후 L 간격에 포함해 있지 않으면 count 에 1 씩 증가
