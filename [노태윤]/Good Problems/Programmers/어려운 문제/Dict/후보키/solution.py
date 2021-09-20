from collections import defaultdict
from itertools import combinations

def solution(relation) : 
    answer = 0
    new_dict = defaultdict(list)
    id = 1
    for i in range(len(relation)) : 
        for j in range(len(relation[0])) : 
            new_dict[j].append(relation[i][j])

    for i in range(1,len(relation[0])+1) : 
        keys_list = list(new_dict.keys())
        if i > len(new_dict.keys()) : 
            break
        keys_comb_list = []
        if i == 1 : 
            for j in range(len(relation[0])) : 
                keys_comb_list += [j]
            for j in keys_comb_list : 
                if len(new_dict[j]) == len(set(new_dict[j])) : 
                    answer+=1
                    del new_dict[j]

        else : 
            keys_comb_list = list(combinations(keys_list,i))
            check_arr = []
            

        

            print(keys_comb_list)     

    # for i in keys_comb_list : 
           
    return new_dict

solution(relation)

# ==================================================================
# 재도전

from itertools import combinations

def solution(relation) : 
    answer = 0
    row = len(relation)
    col = len(relation[0])
    zipped_list = list(zip(*relation)) # 이렇게 해주면 matrix transpose 한 것처럼 구할 수 있음 
    # ex 
    # [[100,200,300,400,500]
    # [ryan, apeach, tube, con, muzi, apeach]]...

    # index 별로 가능한 combination 담기
    index_list = [i for i in range(col)]
    comb_list = []
    for i in range(1,col+1) : 
        comb_list += list(combinations(index_list,i))

    # 만약 unique 하다면 그 떄의 index 값들 담기
    unique_index_list = []
    for i in comb_list : 
        check_list = []
        for j in i : 
            check_list.append(zipped_list[j])
        if len(set(list(zip(*check_list)))) == row : 
            unique_index_list.append(i)

    # ex
    # (0,) 과 (0,1) 이 있다면 (0,1) 은 필요가 없음 (최소성)
    # & operator 쓰면 쉽게 구할 수 있음
    # set 의 discard 는 list 의 remove 와 비슷한 개념
    ans_list = set(unique_index_list)
    for i in range(len(unique_index_list)) : 
        for j in range(i+1, len(unique_index_list)) : 
            if len(unique_index_list[i]) == len(set(unique_index_list[i]) & set(unique_index_list[j])) : 
                ans_list.discard(unique_index_list[j])
    return len(ans_list)

# ==========================================================================================================
