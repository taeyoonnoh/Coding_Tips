import sys
input = sys.stdin.readline

N,M,B = list(map(int,input().split()))
graph = [list(map(int,input().split())) for _ in range(N)]
time,height = float('inf') , 0

for i in range(257) : 
    plus,minus = 0,0
    for rows in graph : 
        for col in rows : 
            if col > i : 
                plus += col-i
            else : 
                minus += i - col

    if minus > plus + B : # 이 코드가 필수 !
        continue

    cur_time = plus * 2 + minus
    if time >= cur_time : 
        time = cur_time 
        height = i
print(f'{time} {height}')

# =============================================================
# 부르트포스 로 접근하면 쉽게 풀 수 있음
