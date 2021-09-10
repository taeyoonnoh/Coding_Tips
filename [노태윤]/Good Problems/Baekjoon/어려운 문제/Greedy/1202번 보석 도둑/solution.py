import heapq
from collections import deque
import sys
input = sys.stdin.readline

N,K = list(map(int,input().split()))
WM_arr = [list(map(int,input().split())) for _ in range(N)]
C_arr = [int(input()) for _ in range(K)]

WM_arr = sorted(WM_arr,key=lambda x : x[0]) # 무게 기준 오름차순 정렬
q = deque(WM_arr)
C_arr = sorted(C_arr) # 가방에 담을 수 있는 보석 무게 오름차순 정렬
count = 0
heap = []

for i in C_arr : 
    while q and i >= q[0][0] : # 보석 무게와 가격이 담긴 큐가 비지 않고 담을 수 있는 가방 무게 >= 보석 무게 라면..
        heapq.heappush(heap,-q.popleft()[1]) # 가격 담기 (- 해줘야 max heap 이 됨)
    if heap : 
        count -= heapq.heappop(heap) # - 붙여져있기 때문에 -= 적용
print(count)

# =============================================================================================================
# heapq 사용하면 쉽게 접근할 수 있음
