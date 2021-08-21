N = int(input())
ans = []
for i in range(N) : 
    A,B = list(map(int,input().split()))
    distance = B-A
    num = int(distance**0.5)
    squared = num**2

    if distance == squared : 
        ans.append(2*num-1)
    elif distance < 4 : 
        ans.append(distance)
    elif distance <= num+squared : 
        ans.append(2*num)
    elif distance > num+squared : 
        ans.append(2*num+1) 
for i in ans : 
    print(i)
