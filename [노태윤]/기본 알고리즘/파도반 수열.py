N = int(input())
init_arr = [0,1,1,1,2,2]
num_list = [0]
for i in range(1,N+1) : 
    if i <= 5 : 
		    num_list.append(init_arr[i])
    else : 
		    num_list.append(num_list[i-1] + num_list[i-5])
print(num_list[-1])

# =====================================================
# 5번째 index 까지는 1, 1, 1, 2, 2 로 가다가 그 후부터는 arr[i-1] + arr[i-5] 패턴으로 간다
