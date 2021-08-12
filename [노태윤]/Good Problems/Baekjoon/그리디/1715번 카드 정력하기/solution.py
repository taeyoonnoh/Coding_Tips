import sys
import heapq
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N) : 
    heapq.heappush(arr,int(input()))

if len(arr) == 1 : 
    print(0)
else : 
    sums = 0
    while len(arr) > 1 : 
        A = heapq.heappop(arr)
        B = heapq.heappop(arr)
        sums += A + B
        heapq.heappush(arr,A+B)
    print(sums)

# heapq 이용하면 쉽게 풀 수 있었던 문제!
