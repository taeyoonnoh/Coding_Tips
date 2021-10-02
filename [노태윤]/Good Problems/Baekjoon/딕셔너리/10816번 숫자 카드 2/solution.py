from collections import defaultdict

new_dict = defaultdict(int)
N = int(input())
card = list(map(int,input().split()))
for i in card : 
    new_dict[i]+=1
find = int(input())
ans = []
num = list(map(int,input().split()))
for i in num :
    ans.append(str(new_dict[i]))
print(' '.join(ans))

# ======================================
# Counter 써서 풀 수도 있음!
