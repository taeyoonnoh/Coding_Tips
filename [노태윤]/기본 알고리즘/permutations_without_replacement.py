N = int(input())
answer = 0
for i in range(1,N+1) : 
	answer+= 3**i
print(answer)

# ==========================
# 3 개중 1개씩 --> 6개중 2개씩 --> 9개중 3개씩
# 3 개중 1 자리로 중복없이.. 2자리로 중복없이.. 3자리로 중복없이.. 
# len(set(permutations,i)) 형태로 구할 수도 있지만 시간 초과뜸..
# 결국에는 3**i 와 마찬가지다 
