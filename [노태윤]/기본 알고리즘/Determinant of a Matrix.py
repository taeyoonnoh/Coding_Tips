def getcofactor(m, i, j):
    return [row[: j] + row[j+1:] for row in (m[: i] + m[i+1:])] # cofactor 구하는 알고리즘 

def determinant(matrix) : 
    if len(matrix) == 1 : 
        return matrix[0][0]
    elif len(matrix) == 2 : 
        return matrix[0][0] * matrix[1][1] - matrix[0][1]*matrix[1][0] # length 가 2 면 ad-bc 진행
    summed = 0

    for i in range(len(matrix)) : 
        sign = (-1) ** i # sign 달라지는 것 적용
        sub_det = determinant(getcofactor(matrix,0,i)) # stack 자료구조로 진행

        summed += sign * sub_det * matrix[0][i]
    return summed

# Simple way
import numpy as np

round(np.linalg.det(matrix))
