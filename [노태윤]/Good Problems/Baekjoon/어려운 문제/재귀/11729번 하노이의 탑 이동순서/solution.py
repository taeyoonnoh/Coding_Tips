N = int(input())
answer =[]
def hanoi(N,a,b,c) : 
    global answer
    if N==1 : 
        answer.append((a,c))
    else : 
        hanoi(N-1,a,c,b)
        answer.append((a,c))
        hanoi(N-1,b,a,c)
hanoi(N,1,2,3)
print(len(answer))
for a,b in answer : 
    print(a,b)

# =============================
# 재귀를 풀 때는 첫번재, 두번째, 세번째, 네번째 ? 정도까지 모든 경우의 수를 확인
# 일정 패턴 찾기
# 만약 경우의 수가 주어지거나 구하게 된다면 그만큼의 답이 return 또는 print 되도록 코드를 짤 것!
