import sys
input = sys.stdin.readline

N,M = list(map(int,input().split()))
arr = []

def change(index) :
    if len(arr) == M : 
        print(' '.join(arr))
        return
    for i in range(index,N+1) : 
        arr.append(str(i))
        change(i)
        arr.pop(-1)

change(1)
