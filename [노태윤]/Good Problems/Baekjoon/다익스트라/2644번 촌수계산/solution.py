import heapq
import sys
input = sys.stdin.readline

V = int(input())
a,b = list(map(int,input().split()))
E = int(input())
edges = [[] for _ in range(V+1)]
for _ in range(E) : 
    i,j = list(map(int,input().split()))
    edges[i].append(j)
    edges[j].append(i)

INF = int(1e9)
distance = [INF] * (V+1)
distance[a] = 0

q = []
heapq.heappush(q,(0,a))

while q : 
    dist,cur_node = heapq.heappop(q)

    if cur_node == b : 
        break

    if distance[cur_node] < dist : 
        continue
    
    for i in edges[cur_node] : 
        cost = dist + 1
        if cost < distance[i] : 
            distance[i] = cost
            heapq.heappush(q,(cost,i))

if distance[b] == INF : 
    print(-1)
else :
    print(distance[b])

# ===========================================
# 기본적인 다익스트라 문제
# 간선간의 길이가 1이라서 쉽게 풀 수 있었음!
