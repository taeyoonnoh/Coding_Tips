import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))

sorted_arr = sorted(set(arr))
new_dict = {}
for i in range(len(sorted_arr)) : 
    new_dict[sorted_arr[i]] = i
for i in arr : 
    print(new_dict[i],end = ' ')

# ======================================
# set 로 풀고 0 부터 증가하기
# 이게 곧 자기 밑으로 몇개가 있는지 보여줌
