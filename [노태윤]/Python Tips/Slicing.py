# 리스트를 처음부터 끝까지 n 개의 element 만 담도록 하는 slicing 방법

lst = [1,2,3,4]
n = 2

def each_cons(lst, n):
    return [lst[i:i+n] for i in range(len(lst) - n + 1)]
  
# 몇번 iterate 해야되는지는 len(lst) - n + 1 로 구할 수 있다
