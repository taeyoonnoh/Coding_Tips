from itertools import combinations

def solution(orders, course):
    # 처음에 순서 정렬
    orders = list(map(lambda x : sorted(x),orders))
    new_dict = {}
    
    # course 에 나와있는 숫자만큼 combination 돌려서 dictionary 에 담기
    for order in orders : 
        for i in course : 
            comb_list = list(combinations(order,i))
            for k in comb_list : 
                new_dict[k] = new_dict.get(k,0) + 1
    
    a = list(new_dict.items())
    ans_list = []
    
    # dictionary 에 각 course 의 갯수만큼 dict list 재구성
    # max 값 찾기
    # 만약 없거나 1 이면 continue
    # max 값인 key 값들 join 시켜서 append
    # 마지막으로 다시 재정렬
    for i in course : 
        b = list(filter(lambda x : len(x[0])==i,a))
        b = sorted(b,key=lambda x : x[1],reverse=True)
        if not b : 
            continue
        max_val = b[0][1]
        if max_val == 1 : 
            continue
        max_elements = [x[0] for x in b if x[1]==max_val]
        for j in max_elements : 
            ans_list.append(''.join(j))
    return sorted(ans_list)
  
  # ==========================================================================
  # 재도전
  
from itertools import combinations
from collections import Counter

# counter 사용한 방법
def solution(orders, course):
    ans_list = []
    for i in course :
        combinations_order = [] 
        for j in orders : 
            comb_list = list(combinations(sorted(j),i))
            combinations_order += comb_list
        counter = Counter(combinations_order).most_common()
        # b 가 1 초과고 max 값과 동일하다면 ans_list 에 추가
        ans_list+=[''.join(a) for a,b in counter if b>1 and b==counter[0][1]]

    return sorted(ans_list)

# =========================================================================
# append 와 += 의 차이! 
