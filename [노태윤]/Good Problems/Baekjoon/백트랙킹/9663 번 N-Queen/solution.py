import sys

def check(i):
    global count

    if i == N : 
        count += 1
        return
    for j in range(N) : 
        if not (perpen[j] or up_right[i+j] or down_right[i-j+N-1]) :
            perpen[j] = True
            up_right[i+j] = True
            down_right[i-j+N-1] = True
            check(i+1)
            perpen[j] = False
            up_right[i+j] = False
            down_right[i-j+N-1] = False

N = int(sys.stdin.readline())
count = 0
perpen = [False] * N
up_right = [False] * (2*N-1)
down_right = [False] * (2*N-1)

check(0)
print(count)

# =========================================================================
# pypy3 로 제출해야 풀린다..

# 이전 시도
def promising(i, col) : 
    index = 1
    flag = True
    while (index < i and flag) : 
        if (col[i] == col[index]) or (abs(i-index) == abs(col[i]-col[index])) : 
            flag = False
        index += 1
    return flag

def backtracking(i, col) : 
    global count
    n = len(col) - 1
    if promising(i,col) : 
        if (i==n) : 
            count +=1
        else : 
            for j in range(1,N+1) : 
                col[i+1] = j
                backtracking(i+1,col)

N = int(input())
col = [0] * (N+1)
count = 0
backtracking(0,col)
print(count)

# 이 방법은 느리더라.. (로직은 더 와 닿긴 한다)
# ===================================================================================
