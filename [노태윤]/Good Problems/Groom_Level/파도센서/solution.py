# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
X,Y,R = list(map(int,input().split(" ")))
coords_list = []
for i in range(5) : 
	coords_list.append(list(map(int,input().split(" "))))
left,right = X-R,X+R
top,bott = Y+R,Y-R
count = 1
count_list = []
min_dist_list = []

def dist(a,b,x,y) : # 거리 공식
	dx = abs(x-a)
	dy = abs(y-b)
	return (dx**2 + dy**2)**0.5

for x,y in coords_list : 
	if left<=x<=right and bott<=y<=top : # 이 안에 포함되어 있다면 감지 적용! 
		count_list.append((x,y,count))
	count+=1
if len(count_list) == 1 : # 하나만 있으면 그냥 그거 출력
	print(count_list[0][2])
elif not count_list : # 아무것도 없다면 -1 반환
	print(-1)
else :
	for x,y,index in count_list  : # 그 외 경우에는 거리 비교 후 sort 하고 나서 첫번째 element의 저장된 index 값 반환
		min_dist_list.append((dist(x,y,X,Y),index))
	print(sorted(min_dist_list)[0][1])
