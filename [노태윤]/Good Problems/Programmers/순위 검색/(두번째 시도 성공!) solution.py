# 효율성 테스트 3~4 실패
# import re 써서 그런 듯

from collections import defaultdict
from itertools import combinations
import re 

def solution(info, query):
    answer = []
    new_dict = defaultdict(list)
    for i in info : 
        splitted= i.split(" ")
        keys = splitted[:-1]
        values = int(splitted[-1])
        for j in range(0,5) : 
            comb_keys = list(combinations(keys,j))
            for k in comb_keys : 
                new_keys = '/'.join(k)
                new_dict[new_keys].append(values)

    for i in new_dict.keys() : 
        new_dict[i] = sorted(new_dict[i])
    for i in query : 
        splitted = re.split('\sand\s|\-|\s',i)
        splitted = list(filter(lambda x : x!='',splitted))
        keys = '/'.join(splitted[:-1])
        score = int(splitted[-1])

        if keys in new_dict.keys() : 
            score_list = new_dict[keys]
            start,end = 0,len(score_list)
            while end>start : 
                mid = (start+end)//2
                if score_list[mid] >= score : 
                    end = mid
                else : 
                    start = mid+1
            answer.append(len(score_list[start:]))
        else :
            answer.append(0)

    return answer

# ========================================================================
# 통과!

from collections import defaultdict
from itertools import combinations
import re 

def solution(info, query):
    answer = []
    new_dict = defaultdict(list)
    for i in info : 
        splitted= i.split(" ")
        keys = splitted[:-1]
        values = int(splitted[-1])
        for j in range(0,5) : # 모든 조합에 대해서 dictionary 에 넣어줌 (이 때 '' 도 포함된다)
            comb_keys = list(combinations(keys,j))
            for k in comb_keys : 
                new_keys = '/'.join(k)
                new_dict[new_keys].append(values)

    for i in new_dict.keys() : # binary search 적용해야하므로 sorting 실시
        new_dict[i] = sorted(new_dict[i])
    for i in query : 
        splitted = re.split('\sand\s|\-|\s',i) # and 또는 공백 또는 '-' 기준으로 split
        splitted = list(filter(lambda x : x!='',splitted)) # '' 없애주기
        keys = '/'.join(splitted[:-1]) 
        score = int(splitted[-1])

        if keys in new_dict.keys() : # dict 에 있으면 bst 적용
            score_list = new_dict[keys]
            start,end = 0,len(score_list)
            while end>start : 
                mid = (start+end)//2
                if score_list[mid] >= score : 
                    end = mid
                else : 
                    start = mid+1
            answer.append(len(score_list)-start) # 총 길이 - index 값 빼주기
        else :
            answer.append(0)

    return answer

# ===================================================================
# len(score_list[start:]) 보다는 len(score_list) - start 하는게 효율적이다!
