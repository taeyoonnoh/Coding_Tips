# Queue 활용한 방식
# bottom to top
from collections import deque
import sys
input = sys.stdin.readline

A,B = list(map(int,input().split()))
q = deque([])
q.append((A,1))
while q : 
    popped,count = q.popleft()
    if popped >B :
        continue
    elif popped == B  :
        print(count)
        break
    q.append((popped*2,count+1))
    q.append((int(str(popped)+'1'),count+1))
else : 
    print(-1)

# =============================================
# 이렇게 되면 하나씩 조회하면서 2개씩 쌓아야 함 (곱하기 2 & 뒤에 1 추가)
# 그렇다보니 불필요한 정보도 같이 조회해야 함 ==> 비효율적

# Top-Down 방식
# 위에서 아래로 필요한 부분만 조회하고 카운팅 적용
import sys
input = sys.stdin.readline

A,B = list(map(int,input().split()))
count = 1
while A!=B : 
    if A>B : 
        print(-1)
        break
    elif str(B)[-1] =='1' : 
        B=B//10
        count+=1
    elif B%2==0 : 
        B=B//2
        count+=1
    else : 
        print(-1)
        break
else : 
    print(count)
