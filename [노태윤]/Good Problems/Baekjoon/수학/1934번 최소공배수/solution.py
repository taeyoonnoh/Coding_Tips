def gcd(A,B) : 
    if B == 0 :   
        return A
    else : 
        return gcd(B,A%B)

T = int(input())
for i in range(T) : 
    A,B = list(map(int,input().split()))
    print(A*B//(gcd(A,B)))
