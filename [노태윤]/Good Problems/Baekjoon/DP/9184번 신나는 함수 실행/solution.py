from collections import defaultdict
import sys
input = sys.stdin.readline

new_dict = defaultdict(int)

def solution(a,b,c) : 
    if a<=0 or b<=0 or c<= 0 : 
        return 1
    if a>20 or b>20 or c>20 : 
        return solution(20,20,20)
    
    if new_dict[(a,b,c)] : 
        return new_dict[(a,b,c)]
    
    if a<b and b<c :  
        new_dict[(a,b,c)] = solution(a,b,c-1) + solution(a,b-1,c-1) - solution(a,b-1,c)
    else : 
        new_dict[(a,b,c)] = solution(a-1,b,c) + solution(a-1,b-1,c) + solution(a-1,b,c-1) - solution(a-1,b-1,c-1)
    return new_dict[(a,b,c)]

while True : 
    a,b,c = list(map(int,input().split()))
    if a == -1 and b == -1 and c == -1 : 
        break
    
    print(f'w({a}, {b}, {c}) = {solution(a,b,c)}')

# ==================================================================================================================
# memoization 활용해서 풀면 시간초과 안남!
