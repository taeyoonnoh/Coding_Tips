from collections import defaultdict

def solution(clothes) : 
    new_dict = defaultdict(int)
    for i in clothes : 
        new_dict[i[1]]+=1
    
    count = 1 
    for i in list(new_dict.values()) : 
        count *= (i+1) # 경우의 수 알고리즘
    return count-1 # 무조건 한번을 입어야하므로 빼기 1 
