def solution(str1, str2):
    str1,str2 = list(str1),list(str2)
    str1_list = [(str1[i]+str1[i+1]).lower() for i in range(0,len(str1)-1) if (str1[i]+str1[i+1]).isalpha()]
    str2_list = [(str2[i]+str2[i+1]).lower() for i in range(0,len(str2)-1) if (str2[i]+str2[i+1]).isalpha()]
    set_str1 = set(str1_list)
    set_str2 = set(str2_list)

    intersection = set_str1 & set_str2
    union = set_str1 | set_str2

    # intersection
    min_val = 0
    for i in intersection : 
        min_val += min(str1_list.count(i),str2_list.count(i))

    # union
    max_val = 0
    for i in union : 
        max_val += max(str1_list.count(i),str2_list.count(i))

    if min_val == 0 and max_val == 0 :
        return 65536

    return int(min_val / max_val * 65536)
