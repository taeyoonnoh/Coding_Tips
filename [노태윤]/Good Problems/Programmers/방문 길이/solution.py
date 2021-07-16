def solution(dirs):
    visited = set()
    drow = [-1,0,1,0]
    dcol = [0,-1,0,1]
    dir_dict = {'L':0,'D':1,'R':2,'U':3}
    x,y = 0,0
    answer = 0
    for dir in dirs : 
        dir_index = dir_dict[dir] # index에 맞게 경로 이동
        dx = x + drow[dir_index]
        dy = y + dcol[dir_index]

        if dx<-5 or dx>5 or dy<-5 or dy>5 : # 만약 -5 나 5 사이가 아니라면 continue
            continue

        if (x,y,dx,dy) not in visited : # 길이가 양방향이므로 둘 다 add
            visited.add((x,y,dx,dy))
            visited.add((dx,dy,x,y))
            answer+=1
        x,y=dx,dy # 경로 최신화
    return answer

# ===================================================================================
# 경로 이동 관련 문제일 때 drow, dcol, dir_dict 활용할 수 있는지부터 생각할 것!
