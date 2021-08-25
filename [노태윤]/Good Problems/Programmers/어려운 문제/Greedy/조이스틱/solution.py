def solution(name) :
    dist_list = [min(ord(i)-ord('A'),ord('Z')-ord(i)+1) for i in name] # 한번에 바로 풀어버리기!
    idx,answer = 0,0
    
    while True : 
        answer +=dist_list[idx]
        dist_list[idx] = 0
        if sum(dist_list) == 0 :
            return answer
        
        left,right = 1,1
        while dist_list[idx-left] == 0 : # 좌로 
            left+=1
        while dist_list[idx+right] ==0: # 우로
            right+=1

        answer += left if left<right else right # 왼쪽으로 움직인게 더 적다면
        idx += -left if left<right else right # idx 갱신!
    return dist_list
