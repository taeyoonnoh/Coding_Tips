from collections import defaultdict

def solution(tickets):
    answer = []
    new_dict = defaultdict(list)
    stack = ['ICN']
    for a,b in tickets : 
        new_dict[a].append(b)
    for i in new_dict :
        new_dict[i] = sorted(new_dict[i],reverse=True) # 내림차순 정렬 --> 나중에 reverse 시킬거임 (알파벳 내림차순으로 순회해야되기 때문)
    while stack : 
        top = stack[-1]
        if not new_dict[top] or top not in new_dict : # 만약 top 이 new dict의 key 에 없거나 new_dict[top] 이 없으면 answer 에 stack의 마지막 element append
            answer.append(stack.pop())
        else :
            stack.append(new_dict[top][-1]) # stack 에 append
            new_dict[top] = new_dict[top][:-1] # append 한 값 없애주기
    return answer[::-1]

# ============================================================================
# 결국에는 DFS 로 푸는 문제!
