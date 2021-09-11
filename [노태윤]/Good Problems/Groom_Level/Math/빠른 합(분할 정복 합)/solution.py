N = int(input())
def divsum(N) : 
		if N == 1 : 
				return 1
		elif N%2 == 1 : 
				return divsum(N-1) + N
		else :
				return divsum(N/2)*2 + N**2/4
print(int(divsum(N)))

# =======================================

# 1부터 N 까지 합을 반으로 쪼개면
# = (1+2+3+4+...+N/2) + (N/2+1 + N/2+2 + N/2+3 ... N/2+N/2)

# 뒷부분에 N/2 가 N/2 만큼 있음
# = (1+2+3+4+...+N/2) + (1+2+3+4+...+N/2) + (N/2*N/2)

# 앞에 두개 같으므로 묶을 수 있음
# = (1+2+3+4+...+N/2) * 2 + (N^2/4)

# 점화식
# f(N) = f(N/2)*2 + N^2/4

# 반으로 계속 쪼개면서 합을 구하고 하나씩 정복하는 방식
# O(log(N)) 만큼 소요

# 비교

# 분할 정복
start = time.time()
print(int(divsum(10000000)))
end = time.time() - start
print(end)

'''
50000005000000
0.0010905265808105469
'''

# Loop 
start = time.time()
print(sum([i for i in range(1,10000001)]))
end = time.time() - start
print(end)

'''
50000005000000
0.990983247756958
'''

# 확실히 차이가 큼!
