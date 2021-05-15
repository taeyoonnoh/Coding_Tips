n = 10

sieve = [True] * (n+1)

# 0 과 1 은 소수가 아니므로 False
sieve[0] = False
sieve[1] = False

# n 의 최대 약수가 sqrt(n) 이하 임
m = int(n**0.5)

# 아래 코드 해석 참고
for i in range(2,m+1) :
    if sieve[i]==True :
        for j in range(i+i,n+1,i) :
            sieve[j]=False

print(list(enumerate(sieve)))
# [(0, False), (1, False), (2, True), (3, True), (4, False), (5, True), (6, False), (7, True), (8, False), (9, False), (10, False)]

# =========================================================================

# Key Points
  # 예를 들어 n 은 10 이라고 가정
  
  # 처음 sieve 리스트
  #    0      1      2    3     4     5      6     7     8     9    10
  # [False, False, True, True, True, True, True, True, True, True, True]
  
  # m : int(sqrt(10)) ==> 3 
  
  # 2 부터 3 까지 for loop 진행
      # i 가 2 일 때
          # i+i (2+2=4) 부터 10까지 i(2) 씩 증가
              # 4, 6, 8, 10 은 False 가 됨
      
      # i 가 3 일 때
          # i+i (3+3=6) 부터 10까지 i(3) 씩 증가
              # 6, 9 는 False 가 됨
  
  # 결국 sieve 는 
  #    0      1      2     3     4      5     6      7     8      9     10
  # [False, False, True, True, False, True, False, True, False, False, False]
