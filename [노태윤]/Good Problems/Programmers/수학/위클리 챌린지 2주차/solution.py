def solution(scores) : 
    ans = ''
    for i in range(len(scores[0])) :
        check_list = []
        
        for j in range(len(scores)) : 
             check_list.append(scores[j][i])
        max_score = max(check_list)
        min_score = min(check_list)
        if max_score == check_list[i] and check_list.count(check_list[i]) == 1 :
            check_list[i] = -1
        if min_score == check_list[i] and check_list.count(check_list[i]) == 1 : 
            check_list[i] = -1
        
        filter_list = list(filter(lambda x : x!=-1,check_list))
        avg = sum(filter_list) / len(filter_list)
        grade = 'A' if avg >= 90 else 'B' if 80<=avg<90 else 'C' if 70<=avg<80 else 'D' if 50<=avg<70 else 'F' if avg<50 else None
        ans += grade

    return ans

# -=========================================================================================================================================
# 문제 잘 읽자 ㅜㅜ

# 간소화
def solution(scores) : 
    ans = ''
    for i in range(len(scores[0])) :
        check_list = []
        
        for j in range(len(scores)) : 
             check_list.append(scores[j][i])
        max_score = max(check_list)
        min_score = min(check_list)
        if (max_score == check_list[i] or min_score == check_list[i]) and check_list.count(check_list[i]) == 1 :
            check_list[i] = -1
        
        filter_list = list(filter(lambda x : x!=-1,check_list))
        avg = sum(filter_list) / len(filter_list)
        grade = 'A' if avg >= 90 else 'B' if 80<=avg<90 else 'C' if 70<=avg<80 else 'D' if 50<=avg<70 else 'F' if avg<50 else None
        ans += grade

    return ans
