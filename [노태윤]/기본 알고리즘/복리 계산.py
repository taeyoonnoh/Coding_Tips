A,B,C = list(map(float,input().split(" ")))
answer = A*(1+(B*0.01))**C
print('%.2f' % answer)

# A : 원금
# B : 이자율
# C : 년도
