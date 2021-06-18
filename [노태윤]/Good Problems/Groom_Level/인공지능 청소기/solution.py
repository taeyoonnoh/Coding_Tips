# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
N = int(input())
coords_list = []
yes_no_list = []
for i in range(N) :
	coords_list.append(list(map(int,input().split(" "))))
for x,y,target in coords_list :
	dist = abs(x) + abs(y)
	if dist == target : 
		yes_no_list.append('YES')
	elif dist > target : 
		yes_no_list.append('NO')
	else :
		if (target - dist) % 2 == 0 :
			yes_no_list.append('YES')
		else :
			yes_no_list.append('NO')
for i in yes_no_list :
	print(i)
