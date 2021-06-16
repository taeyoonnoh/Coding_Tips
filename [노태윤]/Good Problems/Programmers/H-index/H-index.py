from collections import defaultdict

def solution(citations):
    count_dict = defaultdict(int)
    length = len(citations)
    for i in range(len(citations)+1) : 
        count_dict[i] = sum(j>=i for j in citations)
    for a,b in list(count_dict.items()) : 
        if b >=a and length - a <=b : 
            answer=a
    return answer
