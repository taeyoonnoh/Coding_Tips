import sys
sys.setrecursionlimit(10**6)

def star(length) : 
    if length == 1 :
        return ['*']
    
    stars = star(length//3)
    L = []

    for s in stars : 
        L.append(s*3)
    for s in stars : 
        L.append(s+' '*(length//3)+s)
    for s in stars : 
        L.append(s*3)
    return L

N = int(input())
print('\n'.join(star(N)))

# =====================================
# 재귀 핵심은 위 아래로 풀려고 하지 말고
# 아래에서 위로 올라가는 방식으로 풀어보자!
