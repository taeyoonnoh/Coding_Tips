ans_list = []
while True :
    L,P,V = list(map(int,input().split()))
    if L==0 and P==0 and V==0 : 
        break
    ans_list.append(V//P*L + min(V%P,L)) # 핵심은 나머지 & L 중 작은 것 더하기
for i in range(1,len(ans_list)+1) : 
    print(f'Case {i}: {ans_list[i-1]}')
