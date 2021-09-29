import re
from collections import deque

while True : 
    input_text = input()
    if input_text =='.' : 
        break
    text_arr = re.findall('[\[\]\(\)]',input_text)
    q = deque(text_arr)
    stack = []
    while q : 
        if not stack : 
            stack.append(q.popleft())
            continue
        popped = q.popleft()
        if popped == ']' and stack[-1] == '[' : 
            stack = stack[:-1]
        elif popped == ')' and stack[-1] == '(' : 
            stack = stack[:-1]
        else : 
            stack.append(popped)
    if stack : 
        print('no')
    else : 
        print('yes')
