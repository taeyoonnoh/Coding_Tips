N = int(input())
answer =[]
def hanoi(N,a,b,c) : 
    global answer
    if N==1 : 
        answer.append((a,c))
    else : 
        hanoi(N-1,a,c,b)
        answer.append((a,c))
        hanoi(N-1,b,a,c)
hanoi(N,1,2,3)
print(len(answer))
for a,b in answer : 
    print(a,b)
