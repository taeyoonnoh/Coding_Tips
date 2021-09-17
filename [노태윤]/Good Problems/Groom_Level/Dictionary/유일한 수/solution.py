from collections import Counter

N = int(input())
arr = list(map(int,input().split()))
counter = list(Counter(arr).items())
ans = sorted(counter,key=lambda x : x[1])[0][0]
print(ans)
