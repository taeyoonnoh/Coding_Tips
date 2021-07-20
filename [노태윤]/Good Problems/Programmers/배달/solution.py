import heapq

# heapq 를 활용한 dijkstra
def dijkstra(start,distance,graph) : 
    q = []
    heapq.heappush(q,(0,1))
    distance[1] = 0

    while q : 
        dist,curr = heapq.heappop(q)

        if distance[curr] < dist : 
            continue
        
        for i in graph[curr] : 
            cost = dist + i[1]

            if cost < distance[i[0]] : 
                distance[i[0]] = cost 
                heapq.heappush(q,(cost,i[0]))

def solution(N, road, K):
    INF = int(1e9)
    graph = [[] for _ in range(N+1)]
    distance = [INF] * (N+1)

    # 양방향이므로 둘 다 append
    for a,b,dist in road : 
        graph[a].append((b,dist))
        graph[b].append((a,dist))
    
    # dijkstra 진행
    dijkstra(1,distance,graph)

    # K 이하 인 것만 담기
    return len([i for i in distance[1:] if i<=K])
