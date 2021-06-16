def solution(numbers):
    answer = list(map(str,numbers)) # str 으로 변환
    answer = sorted(answer,key = lambda x : x*3,reverse=True) # 가장 큰 수가 3 자리이므로 곱하기 3을 해준다 
    return str(int(''.join(answer))) # 0 도 있을 수 있으니 int 로 바꿔주고 다시 str 형태로 바꿔준다
  
# '3' 와 '30' 비교
a = '3' * 3
b = '30' * 3 

# a = '333'
# b = '303030'

# 문자열은 자릿수별로 순위를 매긴다
# 그래서 a > b 는 True 가 된다 
