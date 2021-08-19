N,C = list(map(int,input().split()))
new_dict = {}
def combination(N,C) : 
    if (N,C) in new_dict : 
        return new_dict[(N,C)]
    if N==C : 
        return 1
    elif C == 1 :
        return N
    
    new_dict[(N,C)] = combination(N-1,C-1) + combination(N-1,C)
    return new_dict[(N,C)]

print(combination(N,C))
