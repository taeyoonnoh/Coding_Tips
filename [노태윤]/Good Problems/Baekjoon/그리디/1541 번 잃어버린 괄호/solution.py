from functools import reduce
equation = list(map(str,input().split('-')))
new_equation = list(map(lambda x : x.split('+'),equation))
for i in range(len(new_equation)) : 
    if len(new_equation[i]) >=2 : 
        new_equation[i] = sum(list(map(lambda x : int(x),new_equation[i])))
    else : 
        new_equation[i] = int(new_equation[i][0])
print(reduce(lambda x,y : x-y,new_equation))

# ===============================================================================
# - 로 split 해주고, + 담긴 애들끼리 따로 split
# 앞자리에 0 이 포함될 수 있으므로 int형으로 변환
# reduce 활용해서 빼주기

# 더 빠른 방법
equation = list(input().split('-'))
new_equation = [sum(list(map(int,x.split('+')))) for x in equation]
print(new_equation[0] - new_equation[1:])
