import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))
arr.sort()
ans = 0
for i in arr :
    if ans + 1 >= i :
        ans+=i
    else : 
        break
print(ans+1)

# ==================================
# combination 써서 풀어볼까 했지만 colab 폭파...
# 심플하게 풀 수 있었던 문제다..어렵다 그리디
