# Test 7 & 10 실패

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = int(input())
str_list=[]
for i in range(user_input):
	str_list.append(input())

mirror_dict = {
	'b' : 'd',
	'd' : 'b',
	'i' : 'i',
	'l' : 'l',
	'm' : 'm',
	'n' : 'n',
	'o' : 'o',
	'p' : 'q',
	'q' : 'p',
	's' : 'z',
	'z' : 's',
	'u' : 'u',
	'v' : 'v',
	'w' : 'w',
	'x' : 'x'
} 

str_set = list(mirror_dict.values())
str_set.extend(list(mirror_dict.keys()))
str_set_list = list(set(str_set))

answer_list = []
for i in str_list : 
	if len(i) == 1 :
		answer_list.append('Normal')
		continue
	
	a = 0
	b = len(i)-1
	while a < b :
		if i[a] not in str_set_list or i[b] not in str_set_list : 
			break
		if mirror_dict[i[a]] != i[b] : 
			break
		a+=1
		b-=1
	if a < b :
		answer_list.append('Normal')
	elif a == b :
		if mirror_dict[i[a]] == i[b] :
			answer_list.append('Mirror')
		else :
			answer_list.append('Normal')
	else :
		answer_list.append('Mirror')
for i in answer_list : 
	print(i)
