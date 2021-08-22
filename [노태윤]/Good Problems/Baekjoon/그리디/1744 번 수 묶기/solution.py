N = int(input())
pos_arr,neg_arr = [],[]
for i in range(N) : 
    num = int(input())
    if num>0:
        pos_arr.append(num)
    elif num <= 0 : # 0 도 음수 array 에 담기
        neg_arr.append(num)
    else :
        continue
sort_pos_arr = sorted(pos_arr,reverse=True) # 양수는 내림차순
sort_neg_arr = sorted(neg_arr) # 음수는 오름차순 

pos,neg = 0,0

while sort_pos_arr : 
    if len(sort_pos_arr)==1 : # 만약 하나만 남으면 바로 더하기
        pos += sort_pos_arr.pop(0)
    else : 
        A = sort_pos_arr.pop(0)
        B = sort_pos_arr.pop(0)
        if A==1 or B==1 : # 둘중 하나라도 1 이면 더해주는 것이 맞음
            pos += A+B
        else :
            pos += A*B

while sort_neg_arr : 
    if len(sort_neg_arr) == 1 : # 만약 하나만 남으면 바로 더하기
        neg += sort_neg_arr.pop(0)
    else : 
        A = sort_neg_arr.pop(0) # 음수 곱하기 음수는 양!
        B = sort_neg_arr.pop(0)
        neg += A*B
print(pos+neg)

# =============================================
# 반례 참고!
