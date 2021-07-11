import math
import sys

a,b,v = map(int,sys.stdin.readline().split())
print(math.ceil((v-a)/(a-b))+1)

# 그 전 단계까지 찾은 다음 + 1 해주면 됌
