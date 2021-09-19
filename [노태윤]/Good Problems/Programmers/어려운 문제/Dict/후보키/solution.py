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
