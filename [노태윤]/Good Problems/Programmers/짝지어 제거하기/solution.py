# 시간 초과 및 실패

def solution(q):
    q = list(q)
    check = list(q)
    while q :  # while loop을 돌리기 때문에 시간이 오래 걸렸던 것 같다
        for i in range(len(q)-1) : 
            if q[i] == q[i+1] : 
                q = q[:i] + q[i+2:]
                break
        if q == check :
            ans = 0
            break

    if not q : 
        ans = 1
    return ans
  
# ====================================================================
# 수정본

def solution(s):
    stack_list = []
    for i in s :  
        if not stack_list : # stack 안에 없으면 append
            stack_list.append(i)
        elif i == stack_list[-1] : # 만약 현재 값이 stack 마지막 값과 같다면 pop
            stack_list.pop()
        else :
            stack_list.append(i) # 그 외에는 그냥 append
    if not stack_list : # stack 에 없으면 1 반환
        return 1
    else : # stack 에 있으면 0 반환
        return 0
      
# 문자열 반복 수행하며 짝을 찾고 제거하는 문제에는 stack 을 활용해서 풀도록 하자!
