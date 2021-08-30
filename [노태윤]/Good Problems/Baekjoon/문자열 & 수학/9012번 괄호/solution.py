from collections import deque

N = int(input())
answer = []
for i in range(N) : 
    paren = list(input())
    q = deque(paren)
    stack =[]
    while q : 
        popped = q.popleft()
        if not stack : 
            stack.append(popped)
            continue
        if popped == ')' and stack[-1]=='(' : 
            stack = stack[:-1]
            continue
        stack.append(popped)
    if stack : 
        answer.append('NO')
    else : 
        answer.append('YES')
for i in answer:
    print(i)

# ===============================================
# deque 활용한 방식

#####################################################
# 수학적으로 푼 방식
N = int(input())
answer = []
for i in range(N) : 
    a = input()
    counts = 0
    for j in a : 
        if j =='(' : 
            counts+=1
        else : 
            counts-=1
            if counts < 0 : 
                break
    if counts ==0 : 
        answer.append('YES')
    else : 
        answer.append('NO')
for i in answer : 
    print(i)
