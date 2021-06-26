a = ['c=','c-','dz=','d-','lj','nj','s=','z=']
alphas = input()
for i in a :
    alphas = alphas.replace(i,'A') # 지정한 문자를 가지고 replace 를 씌워주면 간단하게 풀 수 있음
print(len(alphas))
