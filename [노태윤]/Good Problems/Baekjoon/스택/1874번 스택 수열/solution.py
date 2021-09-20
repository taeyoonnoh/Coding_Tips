import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
ans1,ans2,num,isTrue = [],[],1,False
for i in arr : 
    while num<=i:
        ans1.append(num)
        ans2.append('+')
        num+=1
    if ans1[-1]==i : 
        ans1.pop(-1)
        ans2.append('-')
    else : 
        isTrue = True
        break
if isTrue : 
    print('NO')
else : 
    for i in ans2 : 
        print(i)
