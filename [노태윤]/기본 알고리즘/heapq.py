import heapq

a = [5,3,10,8,9,20]

heapq.heapify(a)
a #==> [3, 5, 10, 8, 9, 20] heapsort 된 것으로 나옴

# 하지만 heappop 을 해주면 계속해서 이 때의 min 값이 반환되서 나옴
heapq.heappop(a) # ==> 3
heapq.heappop(a) # ==> 5
heapq.heappop(a) # ==> 8

# heappush 방법
heapq.heappush(a,4)
