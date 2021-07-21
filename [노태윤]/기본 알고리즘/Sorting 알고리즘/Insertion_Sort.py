for i in range(1,N) : 
	for j in range(i,0,-1) : 
		if arr[j-1] > arr[j] : 
			arr[j-1],arr[j] = arr[j],arr[j-1]
	if ind == count : 
		break
