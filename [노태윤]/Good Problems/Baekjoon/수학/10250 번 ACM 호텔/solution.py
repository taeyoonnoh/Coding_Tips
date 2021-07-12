import sys
N = int(input())
answer = []
for i in range(N) : 
    height,width,number = map(int,sys.stdin.readline().split())
    if number % height != 0 : 
        answer.append(str(number%height) + str(number//height+1).zfill(2)) 
    else : 
        answer.append(str(height) + str(number//height).zfill(2))
for i in answer :
    print(i)
