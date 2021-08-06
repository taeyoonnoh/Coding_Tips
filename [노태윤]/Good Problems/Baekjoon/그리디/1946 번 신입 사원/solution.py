import sys
T = int(sys.stdin.readline())
ans_list = []
for i in range(T) : 
    N = int(sys.stdin.readline())
    counts,index = 1,0
    grades_list = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
    sorted_grades = sorted(grades_list,key=lambda x : x[0])
    
    # 만약 현재 index 값의 면접 점수가 다음 index의 면접 점수보다 낮다면 update 해줄 것
    for j in range(len(sorted_grades)) : 
        if j == 0 :
            continue
        if sorted_grades[index][1] > sorted_grades[j][1] : 
            index = j
            counts+=1
    ans_list.append(counts)
for i in ans_list : 
    print(i)
