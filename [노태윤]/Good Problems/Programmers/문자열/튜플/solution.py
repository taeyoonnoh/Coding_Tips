def solution(s):
    new_dict = {'{':'[','}':']'}
    for key,value in new_dict.items() : 
        s =s.replace(key,value)
    s_list = eval(s)
    s_list = sorted(s_list,key=lambda x : len(x))
    ans_list = []
    for i in s_list : 
        for j in i : 
            if j not in ans_list : 
                ans_list.append(j)
    return ans_list
  
# 숏코딩
def solution(s):
    s_list = eval(s.replace('{','[').replace('}',']'))
    ans_list = []
    for i in sorted(s_list,key=lambda x : len(x)) : 
        for j in i : 
            if j not in ans_list : 
                ans_list.append(j)
    return ans_list

# =======================================================
# string 을 dictionary 형태로 바꿔줄 때 list 로 먼저 바꿔주면 eval() 함수 써서 변환시킬 수 있음
# replace 
