N = int(input())
dist = [0 for _ in range(N+1)]

for i in range(2,N+1) : 
    dist[i] = dist[i-1] + 1

    if i%2==0 and dist[i] > dist[i//2] + 1 : 
        dist[i] = dist[i//2] + 1
    
    if i%3 == 0 and dist[i] > dist[i//3] + 1 : 
        dist[i] = dist[i//3] + 1 
print(dist[N])

# ==============================================
# dp 로 풀기
# 위에서 아래로 가는것보다 아래에서 위로 가는게 좀 더 수월하게 풀 수 
