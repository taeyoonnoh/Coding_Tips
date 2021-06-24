def solution(a):
    for i in range(1,len(a)) : 
        for j in range(4) : 
            a[i][j] = max(a[i-1][:j] + a[i-1][j+1:]) + a[i][j]

    return max(a[-1])

# =================================================================
# 풀이

# Top-Down 방식이 아닌 Bottom-Up 로 접근하면 쉽게 풀 수 있음
# a[i-1][:j] + a[i-1][j+1:] 의 의미는 j 를 제외한 나머지 list 들을 묶는다는 의미
# 이 중에서 max 값을 찾고 그 다음 row 의 index j 번째 값과 더해주는 방식
