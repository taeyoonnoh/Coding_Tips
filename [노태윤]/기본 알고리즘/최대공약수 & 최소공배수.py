# 최대공약수
def gcd(a,b) :
    if b == 0 :
        return a 
    else :
        return gcd(b,a%b)

# 최소공배수
def lcm(a,b) :
    return (a*b) / gcd(a,b)

# 스테인 알고리즘으로 최대공약수 구하기
def change(M,N,a=0) : 
    if M==0 or N ==0 : 
        b = max(M,N)
        return 2**a*b
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
