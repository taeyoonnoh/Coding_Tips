N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
ans = []
for weight, height in arr : 
    rank = 1
    for loop_weight,loop_height in arr : 
        if (loop_weight>weight) and (loop_height>height) : 
            rank+=1
    ans.append(rank)
for i in ans:
    print(i)

# =============================================================
# 때론 다 돌아보는 것이 가장 쉬울 수도 있더라..
