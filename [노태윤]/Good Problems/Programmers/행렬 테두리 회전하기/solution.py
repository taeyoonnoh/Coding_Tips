def solution(rows,columns,queries) : 
    a = 1 
    arr = [[] for _ in range(rows)]
    for i in range(rows) : 
        for j in range(columns) : 
            arr[i].append(a)
            a+=1

    min_list = []

    for a,b,c,d in queries : 
        a,b,c,d = a-1,b-1,c-1,d-1
        temp = arr[a][b] # arr[a][b] 값은 없어지므로 미리 저장해야함
        min_val = temp

        for i in range(a,c) : # West
            check = arr[i+1][b]
            arr[i][b] = check
            min_val = min(min_val,check)
        
        for i in range(b,d) : # South
            check = arr[c][i+1]
            arr[c][i] = check
            min_val = min(min_val,check)
        
        for i in range(c,a,-1) : # East 
            check = arr[i-1][d]
            arr[i][d] = check
            min_val = min(min_val,check)
        
        for i in range(d,b,-1) : # North
            check = arr[a][i-1]
            arr[a][i] = check
            min_val = min(min_val,check)
        
        arr[a][b+1] = temp # 저장해놓은 값 넣어주기
        min_list.append(min_val)

    return min_list
