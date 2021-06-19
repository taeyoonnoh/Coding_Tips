import sys
answer_list = []
for i in sys.stdin : 
    A,B = map(int,i.split())
    answer_list.append(A+B)
for i in answer_list :
    print(i)

# 출력값이 정해지지 않을 때 사용 함 (it is called EOF (end-of-file))
