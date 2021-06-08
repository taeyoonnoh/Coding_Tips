import numpy as np

def fib(n):
    F1 = np.array([[1,1],[1,0]], dtype='object') 
    b = np.linalg.matrix_power(F1, abs(n)) # minus 일 수도 있기 때문에 abs 씌워줌
    if n < 0 :
        if n % 2 == 0 :
            return -1 * b[0][1]
    return b[0][1]
  
# 5 -3 2 -1 1 0 1 1 2 3 5 .. 순으로 진행됨

# 좀 더 조사 해보자
