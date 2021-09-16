import sys
input = sys.stdin.readline

T = int(input())
ans = []
for i in range(T) : 
    N = int(input())
    zero = [1,0,1]
    one = [0,1,1]
    for i in range(3,N+1) : 
        zero.append(zero[i-1] + zero[i-2])
        one.append(one[i-1] + one[i-2])
    ans.append((zero[N],one[N]))
for i in ans : 
    print(*i)

# ==========================================
# 재귀적으로 말고 DP로 풀어야 시간 초과가 안 뜸!
