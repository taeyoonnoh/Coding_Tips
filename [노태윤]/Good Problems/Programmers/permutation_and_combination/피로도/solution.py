from itertools import permutations

def solution(k, dungeons):
    answer = -1
    length = len(dungeons)
    dung_list = list(permutations(dungeons,length))
    for dung in dung_list : 
        count = 0
        new_k = k
        for a,b in dung : 
            if new_k>= a and new_k>=b : 
                new_k-=b
                count+=1
            else : 
                break
        answer = max(count,answer)
    return answer
  
  # =====================================
  # 이 문제는 경우 수가 적기 때문에 그냥 permutation 써도 됨!
