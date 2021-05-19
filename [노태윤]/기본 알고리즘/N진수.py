# 십진수 2진수 변환
bin(50) # ==> '0b110010' (str 형태)

format(50,'b') # ==> '110010'

# 십진수 8진수 변환
oct(50) # ==> '0o62'

format(50,'o') # ==> '62'

# 십진수 16진수 변환
hex(50) # ==> '0x32'

format(50,'h') # ==> '32'

# N 진수 ==> 10진수 변환
print(int('111',2)) 
print(int('222',3))
print(int('333',4))
print(int('444',5))
print(int('555',6))
print(int('FFF',16))

'''
7
26
63
124
215
4095
'''

# 그외 진수
import string

tmp = string.digits+string.ascii_lowercase # ==> 0123456789abcdefghijklmnopqrstuvwxyz
def convert(num, base) :
    q, r = divmod(num, base) # q : quotient / r : remainder
    if q == 0 :
        return tmp[r] 
    else :
        return convert(q, base) + tmp[r]

print(convert(10,2))
print(convert(10,3))
print(convert(10,4))
print(convert(10,5))

'''
1010
101
22
20
'''
