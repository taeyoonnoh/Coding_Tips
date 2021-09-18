# 첫번째 시도

N,M = list(map(int,input().split()))
arr = []
def change() : 
    if len(arr) ==M : 
        print(*arr)
        return

    for i in range(1,N+1) : 
        arr.append(i)
        change()
        arr.pop(-1)
change()

# ===================================
# 통과는 하지만 시간 오래 걸림

# 다른 방법
from itertools import product

N,M = list(map(int,input().split()))
arr = list(map(str,range(1,N+1)))
for i in list(product(arr,repeat=M)) : 
    print(' '.join(i))

# =======================================
# arr 에 문자열로 담은 뒤 print(' '.join(i)) 로 하니까 속도가 대폭 개선됨 
