# lambda 를 활용한 sorting

import re

files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
new_files = [re.split('([0-9]+)',file) for file in files]

# lambda 에 2가지 요소가 들어가도 됌
# 이 때 files 의 순서를 기준으로 정렬 실시
# x[0] 은 lowercase 내림차순이면서 x[1] 내림차순
sorted_list = sorted(new_files, key =lamda x : (x[0].lower(),int(x[1])))

sorted_list = sorted(new_files, key =lamda x : (x[0].lower(),-int(x[1]))) # 이렇게 - 부호를 넣어주면 오름차순으로도 가능함

# ============================================================================================================================

# 그나마 효율적인 sorting 방법
import sys
input = sys.stdin.readline

N = int(input())
arr = [0 for i in range(10001)] # 미리 배열 사이즈 정해놓기
for _ in range(N) :
    num = int(input())
    arr[num]+=1 # 1씩 증가!
for i in range(10001):
    for j in range(arr[i]):
        print(i)
