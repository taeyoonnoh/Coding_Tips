import sys

sudoku_arr = [list(map(int,sys.stdin.readline().split())) for _ in range(9)]
zero_coords = []

for i in range(9) :
    for j in range(9) : 
        if sudoku_arr[i][j] == 0 : 
            zero_coords.append((i,j))

def check_row(x,target) : 
    for i in range(9) : 
        if sudoku_arr[x][i] == target : 
            return False
    return True

def check_col(y,target) : 
    for i in range(9) : 
        if sudoku_arr[i][y] == target : 
            return False
    return True

def check_33(x,y,target) :
    dx = x//3 * 3
    dy = y//3 * 3
    for i in range(dx,dx+3) : 
        for j in range(dy,dy+3) : 
            if sudoku_arr[i][j] == target : 
                return False
    return True

def backtracking(index) : 
    if index == len(zero_coords) : 
        for i in range(9) : 
            print(*sudoku_arr[i])
        sys.exit()
    
    for target in range(1,10) : 
        x = zero_coords[index][0]
        y = zero_coords[index][1]

        if check_row(x,target) and check_col(y,target) and check_33(x,y,target) : 
            sudoku_arr[x][y] = target
            backtracking(index+1)
            sudoku_arr[x][y] = 0

backtracking(0)

# ===================================================================================
# for 문으로 돌리고 그 promising 하다면 넘겨주고 다시 초기화(0) 한번 시켜주는 것이 백트래킹 기법에서는 중요한 것 같다..
