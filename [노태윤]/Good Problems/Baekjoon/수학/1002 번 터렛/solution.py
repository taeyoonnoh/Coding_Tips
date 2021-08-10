import sys
input = sys.stdin.readline
T = int(input())
ans_list = []
for i in range(T) : 
    x1,y1,r1,x2,y2,r2 = list(map(int,input().split()))
    R = ((x1-x2)**2 + (y1-y2)**2)**0.5
    radius = [r1,r2,R]
    max_R = max(radius)
    radius.remove(max_R)
    ans_list.append(-1 if R == 0 and r1==r2 else 1 if R == r1+r2 or max(r1,r2) == min(r1,r2) + R else 0 if max_R > sum(radius) else 2)
for i in ans_list : 
    print(i)

#==========================================================================================================================================
