# 6~10 test 실패

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import math

user_input = int(input())
num_list = list(map(int,input().split(" ")))
count=0
answer_list = []
for i in range(len(num_list)) : 
	if math.log(num_list[i],2).is_integer() == False : 
		count+=1
		answer_list.append(str(i+1))

if not answer_list : 
	print(count)
else :
	print(count)
	print(' '.join(answer_list))
