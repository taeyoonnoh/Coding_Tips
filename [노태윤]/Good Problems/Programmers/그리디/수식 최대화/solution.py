import re
from itertools import permutations

def solution(expression):
    answer = 0
    operator = ['*','+','-']
    for i in permutations(operator,3) : 
        a = re.findall('\d+|\*|\-|\+',expression)
        for j in i : 
            new_arr = []
            for k in range(len(a)) : 
                if j == a[k-1] : 
                    aft = a[k]
                    oper = new_arr.pop(-1)
                    bef = new_arr.pop(-1)
                    new_arr.append(str(eval(bef+oper+aft)))
                else : 
                    new_arr.append(a[k])
            a = new_arr
        answer = max(answer,abs(int(a[0])))

    return answer
  
# ==========================================================

# 더 괜찮은 방법

def solution(expression):
    operations = [('+', '-', '*'),('+', '*', '-'),('-', '+', '*'),('-', '*', '+'),('*', '+', '-'),('*', '-', '+')]
    answer = []
    for op in operations:
        a = op[0]
        b = op[1]
        temp_list = []
        for e in expression.split(a):
            temp = [f"({i})" for i in e.split(b)]
            temp_list.append(f'({b.join(temp)})')
        answer.append(abs(eval(a.join(temp_list))))
    return max(answer)
  
# ======================================================================================================================

# 괄호를 넣어주면서 eval로 한꺼번에 푸는 방법
