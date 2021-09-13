def solution(m,n,board) : 
    answer = 0
    board = list(map(lambda x : list(x),board))
    count = 0 
    while True :
        remove_arr = [[0]*n for _ in range(m)] # 없애줄 문자열 표시해주기 용도, 계속 최신화 해줘야 함
        for i in range(m-1) : 
            for j in range(n-1) : 
                if board[i][j]!=0 and board[i][j+1]!=0 and board[i+1][j]!=0 and board[i+1][j+1] != 0 : # 0 이 아니여야 함
                    if board[i][j]==board[i][j+1]==board[i+1][j]==board[i+1][j+1]: # 0이 아니면서 같은 문자열이라면 remove_arr 에 1 담기
                        remove_arr[i][j],remove_arr[i][j+1],remove_arr[i+1][j],remove_arr[i+1][j+1] = 1,1,1,1
        summ = 0
        for i in range(m) : 
            summ += remove_arr[i].count(1) # 1의 갯수 담기
        if summ == 0 : # 만약 0 이라면 (없애줄 문자열이 없다는 의미)
            break

        answer+=summ

        for i in range(1,m) : # board 최신화 ==> 채워넣는 방식
            for j in range(n) : 
                if remove_arr[i][j] == 1 : 
                    for k in range(i,0,-1) : 
                        board[k][j] = board[k-1][j]
                        board[k-1][j] = 0

    return answer

# ==============================================================================================================
# 빡구현 문제
