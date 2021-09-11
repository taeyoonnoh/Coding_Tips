from bisect import bisect_left,bisect_right
import sys
input = sys.stdin.readline

N = int(input())
arr1 = list(map(int,input().split()))
arr1.sort()
M = int(input())
arr2 = list(map(int,input().split()))
ans = []
for i in arr2 : 
    left_index = bisect_left(arr1,i)
    right_index = bisect_right(arr1,i)
    if right_index - left_index == 0 : 
        ans.append(0)
    else  : 
        ans.append(1)
for i in ans : 
    print(i)
