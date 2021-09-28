from collections import defaultdict

N = int(input())
strr = input()
alpha_dict = defaultdict(int)
alpha = 'abcdefghijklmnopqrstuvwxyz'
ind = 1
for i in alpha : 
    alpha_dict[i] = ind
    ind+=1

num=0
for i in range(len(strr)) : 
    num+=alpha_dict[strr[i]] * (31**i)

print(num%1234567891)
