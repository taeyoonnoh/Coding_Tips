# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
N = int(input())
arr = list(map(int,input().split(" ")))
A = int(input())

def binary_search(arr,target,x,y) : 
	mid = (x+y)//2
	if x >= y : 
		return 'X'
	if arr[mid] == target :
		return mid+1
	elif arr[mid] < target :
		return binary_search(arr,target,mid+1,y)
	else :
		return binary_search(arr,target,x,mid-1)

print(binary_search(arr,A,0,N-1))
