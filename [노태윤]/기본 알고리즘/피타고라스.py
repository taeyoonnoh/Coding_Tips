# 피타고라스

c = m**2 + n ** 2
b = m**2 - n**2
a = 2*m*n

# find a+b+c = 1000
# 2mn + 2m^2 = 1000
# mn + m^2 = 500

# quadratic formula
def check(n) : 
    return (-1 * n + (n**2+2000)**0.5) / 2

n = 1
while True : 
	m = check(n)
	if len(str(m)) == 4 : 
		break
	n+=1

a = 2 * m * n
b = m**2 - n**2
c = m**2 + n**2
print(int(a*b*c))
