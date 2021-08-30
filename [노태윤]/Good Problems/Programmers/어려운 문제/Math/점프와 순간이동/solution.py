def solution(n) : 
    count=0
    while n > 0 : 
        q,r = divmod(n,2)
        if r != 0 : 
            n-=1
            count+=1
        else : 
            n = q
    return count
# =============================
# 항상 Bottom Up 또는 Top Down 방법만 생각하는것 같다
# 여러가지 방법을 시도해보자!

# =====================================================

# 더 쉬운 방법
def solution(n):
    return format(n,'b').count('1')
# ====================================
# 어차피 나누고 1 이 남으면 count 1씩 증가하는거기 때문에 2진수로 변환해서 1의 갯수를 구하는 방식으로 풀어도 됨
