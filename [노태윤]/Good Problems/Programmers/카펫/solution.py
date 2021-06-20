def yaksu(N) :
    yaksu_list = []
    for i in range(1,N+1) :
        if i<3 or N//i<3 : 
            continue
        elif N%i==0:
            if i > N//i :
                continue
            yaksu_list.append((i,N//i))
        
    return yaksu_list

def solution(brown, yellow):
    total = brown+yellow
    yaksu_list = yaksu(total)
    for row,col in yaksu_list :
        if (row-2) * (col-2) == yellow : 
            answer = [col,row]
            break
    return answer
