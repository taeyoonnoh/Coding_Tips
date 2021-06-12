# array size 가 N by N 일 때

def snail(array):
    if not array[0] : 
        return []
    
    start_row = 0
    start_col = 0
    end_row = len(array) - 1
    end_col = len(array) - 1

    answer_list = []

    while start_row <= end_row: 
        for i in range(start_col,end_col+1) : 
            answer_list.append(array[start_row][i])
        start_row+=1

        for i in range(start_row,end_row+1) : 
            answer_list.append(array[i][end_col])
        end_col-=1

        for i in range(end_col,start_col-1,-1) : 
            answer_list.append(array[end_row][i])
        end_row-=1

        for i in range(end_row,start_row-1,-1) : 
            answer_list.append(array[i][start_col]) 
        start_col+=1
    return answer_list
  
# ==================================================== 
# 빠른 방법 (np.rot90 활용)
# np.rot90 은 반 시계 방향으로 90도 회전하는 것을 의미

def snail(array) : 
    m = []
    array = np.array(array)
    while len(array) > 0 :
        m+=array[0].tolist()
        array = np.rot90(array[1:])
    return m
