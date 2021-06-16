# 내 방식
answer = 0

def check(a,b,target,index=0,num=0) : 
    global answer
    if index>=len(a) : 
        if num == target : 
            answer+=1
            return
        return
        
    num1 = num + a[index] * b[0]
    num2 = num + a[index] * b[1]

    check(a,b,target,index+1,num1)
    check(a,b,target,index+1,num2) 

def solution(numbers, target):
    check(numbers,[1,-1],target,index=0,num=0)
    return answer

# ===================================================  

# product 을 활용한 방식
from itertools import product
numbers = [1,1,1,1,1]
target = 3

def solution(numbers, target):
    l = [(x, -x) for x in numbers] # +1, -1 곱한 것들 담기
    s = list(map(sum, product(*l))) # product 활용해서 모든 경우의 수의 리스트를 구하고 sum 해주기
    return s.count(target) # target 인 것만 count
