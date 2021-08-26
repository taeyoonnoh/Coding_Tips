import sys
input = sys.stdin.readline

M,N = list(map(int,input().split()))

graph = [list(input()) for _ in range(M)]

tot_counts = int(1e9)
for i in range(M-8+1) : 
    for j in range(N-8+1) : 
        new_graph,count_A,count_B = [],0,0
        for k in range(i,i+8) : 
            new_graph.append(graph[k][j:j+8])

        start_A,next_A = 'W','B'
        start_B,next_B = 'B','W'
        for l in range(8) : 
            start_count_A = new_graph[l][::2].count(start_A)
            next_count_A = new_graph[l][1::2].count(next_A)
            count_A += (4-start_count_A)
            count_A += (4-next_count_A)
            start_A,next_A = next_A,start_A

            start_count_B = new_graph[l][::2].count(start_B)
            next_count_B = new_graph[l][1::2].count(next_B)
            count_B += (4-start_count_B)
            count_B += (4-next_count_B)
            start_B,next_B = next_B,start_B   
        tot_counts = min(tot_counts,count_A,count_B)
print(tot_counts)

# ================================================================
# 첫번째 값을 W 로 보고 풀었을 때와 B 로 보고 풀었을 때 각각 변하는 값을 담기
# 이때 start 와 next 값 서로 바꿔가면서 연산하기!
# 이 중 min 값으로 계속해서 update 하기!
