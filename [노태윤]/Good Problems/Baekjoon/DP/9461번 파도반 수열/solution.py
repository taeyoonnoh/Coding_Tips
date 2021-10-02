init_arr = [0,1,1,1,2,2]
num_list = [0]
for i in range(1,100+1) : 
    if i <= 5 : 
        num_list.append(init_arr[i])
    else : 
        num_list.append(num_list[i-1] + num_list[i-5])

T = int(input())
for i in range(T) : 
    N = int(input())
    print(num_list[N])
