from itertools import combinations
import time


N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

tf_list = [False] * N
min_val = 1e9

start_time = time.time()

def backtracking(index) : 
    global min_val
    
    if index == N//2 :
        total_team = set(range(N))
        sum_a, sum_b = 0,0
        a_team = [i for i,j in enumerate(tf_list) if j]
        b_team = list(total_team - set(a_team))
        
        comb_a_list = list(combinations(a_team,2))
        comb_b_list = list(combinations(b_team,2))

        for k in range(len(comb_a_list)) : 
            x_a = comb_a_list[k][0]
            y_a = comb_a_list[k][1]
            x_b = comb_b_list[k][0]
            y_b = comb_b_list[k][1]

            sum_a += (arr[x_a][y_a] + arr[y_a][x_a])
            sum_b += (arr[x_b][y_b] + arr[y_b][x_b])
        
        min_val = min(min_val, abs(sum_a - sum_b))
        # print('a_team : ', a_team)
        # print('b_team : ', b_team)
        # print('sum_a : ', sum_a)
        # print('sum_b : ', sum_b)
        # print('min_val : ', min_val)
        # print("===================================")

        return
    
    for i in range(N) : 
        if tf_list[i] == False : 
            tf_list[i] = True 
            backtracking(index+1)
            tf_list[i] = False

backtracking(0)
print(min_val)
print("time spent : ", time.time() - start_time)

# ==========================================================================
# 첫 시도 : 재귀로 풀어볼려고 했는데 오래 걸림...

from itertools import combinations
import time

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

total_team = set(range(N))
min_val = 1e9

start_time = time.time()

for a_team in combinations(list(total_team), N//2) : 
    b_team = list(total_team - set(a_team))
    sum_a,sum_b = 0, 0
    for i in range(len(a_team)) : 
        for j in range(len(a_team)) : 
            if i!=j : 
                sum_a += arr[a_team[i]][a_team[j]]
    
    for i in range(len(b_team)) : 
        for j in range(len(b_team)) : 
            if i!=j : 
                sum_b += arr[b_team[i]][b_team[j]]
    
    min_val = min(min_val, abs(sum_a - sum_b))

    print('a_team : ', a_team)
    print('b_team : ', b_team)
    print('sum_a : ', sum_a)
    print('sum_b : ', sum_b)
    print('min_val : ', min_val)
    print("===================================")

    
print(min_val)
print("time spent : ", time.time() - start_time)

# ===================================================================
# 다중 for loop + combinations 써서 pypy3 로 해결함.. 
# 역시 파이썬은 느리다.. 
