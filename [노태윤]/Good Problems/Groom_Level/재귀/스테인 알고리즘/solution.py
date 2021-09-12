def change(M,N,a=0) : 
    if M==0 or N ==0 : 
        return max(M,N),a
    if M%2==0 and N%2==0 : 
        a+=1
        return change(M//2,N//2,a)
    elif M%2==0 : 
        return change(M//2,N,a)
    elif N%2==0 : 
        return change(M,N//2,a)
    elif M%2==1 and N%2==1 : 
        if M>=N : 
            M-=N
        else : 
            N-=M
        return change(M,N,a)

M,N = list(map(int,input().split()))
b,a = change(M,N,a=0)
print((2**a)*b)
