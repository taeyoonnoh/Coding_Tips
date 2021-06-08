# 구구단 표현방법

N = int(input())
mult_table = []
for i in range(2,10) :
    for j in range(1,10) : 
         mult_table.append(f'{i} * {j} = {i*j}')
modified_table = [mult_table[x:x+N] for x in range(0,len(mult_table),N)] # 특정 지점부터 다음 특정 지점까지의 element를 list 로 반환하는 방법
for i in modified_table : 
    print(' '.join(i) + ' ')
