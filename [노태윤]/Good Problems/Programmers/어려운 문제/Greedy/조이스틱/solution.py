def solution(name) :
    dist_list = [min(ord(i)-ord('A'),ord('Z')-ord(i)+1) for i in name]
    idx,answer = 0,0
    
    while True : 
        answer +=dist_list[idx]
        dist_list[idx] = 0
        if sum(dist_list) == 0 :
            return answer
        
        left,right = 1,1
        while dist_list[idx-left] == 0 :
            left+=1
        while dist_list[idx+right] ==0:
            right+=1

        answer += left if left<right else right
        idx += -left if left<right else right
    return dist_list
