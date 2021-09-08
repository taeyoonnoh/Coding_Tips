def solution(weights, head2head):
    answer = []
    new_arr = [[] for _ in range(len(weights))]
    for i in range(len(weights)) : 
        counts = 0 
        for j in range(len(weights)) : 
            if weights[i] < weights[j] and head2head[i][j]=='W' : 
                counts+=1
        length = len(weights)
        count_N = head2head[i].count('N')
        if length == count_N : 
            rate = 0
        else : 
            rate = head2head[i].count('W')/(length-count_N)
        new_arr[i] = (weights[i],rate,counts,i+1)
    new_arr = sorted(new_arr,key=lambda x : (-x[1],-x[2],-x[0],x[3]))

    return [i[3] for i in new_arr]

# ======================================================================
# sorted key 잘 설정하면 쉽게 풀 수 있는 문제!
