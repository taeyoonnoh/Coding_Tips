def solution(board) : 
    if len(board) == 1 : # 만약 매트릭스 row 가 1 이라면 아래 코드 실행
        for i in board[0] : 
            if i == 1 : 
                return 1
    if len(board) == 2 and len(board[0]) == 1 : # 만약 매트릭스 사이즈가 (2,1) 이라면 아래 코드 실행
        if board[0][0] == 1 or board[0][0] == 1 : 
            return 1 
        else :
            return 0
    max_num = 0
    for i in range(1,len(board)) : 
        for j in range(1,len(board[0])) : 
            if board[i][j] != 0 : 
                board[i][j] = min(board[i][j-1],board[i-1][j],board[i-1][j-1]) + 1
            else : 
                continue
            if max_num < board[i][j] : 
                max_num = board[i][j]
    return max_num**2
  
# ===================================================================================
# 가장 큰 정사각형 알고리즘

# (1,1) 좌표부터 (i-1,j), (i,j-1), (i-1,j-1) 중 min 값 + 1 
# 이때 (i,j) 는 0 이 되어서는 안된다
