import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N) : 
    cmd = input().split()
    if len(cmd)>1 : 
        if cmd[0] == 'push_back' : 
            arr.append(int(cmd[1]))
        elif cmd[0] == 'push_front' : 
            arr.insert(0,int(cmd[1]))
    else : 
        if cmd[0] == 'pop_front' : 
            if arr : 
                print(arr.pop(0))
            else : 
                print(-1)
        elif cmd[0] == 'pop_back' : 
            if arr : 
                print(arr.pop(-1))
            else : 
                print(-1)
        elif cmd[0] == 'size' : 
            print(len(arr))
        elif cmd[0] == 'empty' : 
            if arr : 
                print(0)
            else : 
                print(1)
        elif cmd[0] == 'front' : 
            if arr : 
                print(arr[0])
            else : 
                print(-1)
        elif cmd[0] =='back' : 
            if arr : 
                print(arr[-1])
            else : 
                print(-1)
