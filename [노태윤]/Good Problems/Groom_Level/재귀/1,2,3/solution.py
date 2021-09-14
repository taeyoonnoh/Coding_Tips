N = int(input())
count = 0
arr = []
def dfs() : 
    global count
    if sum(arr) == N : 
        count+=1
        return
    elif sum(arr) > N : 
        return 

    for i in range(1,4) : 
        arr.append(i)
        dfs()
        arr.pop()

dfs()
print(count)
# =========================
# 재귀적으로 풀기
