N = int(input())
index = 1
while True : 
	if N - index <= 0 : 
		break
	N-=index
	index+=1
if index % 2 == 1 : 
	answer = str(index-N+1) + '/' + str(N)
else :
	answer = str(N) + '/' + str(index-N+1)
print(answer)
