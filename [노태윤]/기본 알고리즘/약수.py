def yaksu(N) :
    yaksu_list = [False] * (N+1)
    for i in range(1,N+1) :
      
        # 이미 약수라고 정의 되었다면 그냥 continue
        if yaksu_list[i] == True :
            continue
        
        a = N//i
        b = N%i
        
        # 만약 나누어 떨어진다면 아래 코드 실행
        if b == 0 :
            yaksu_list[i] = True
            yaksu_list[a] = True
    
    # 약수이면 True / 아니면 False 가 담긴 리스트 반환
    return list(enumerate(yaksu_list))

# 예시
yaksu(10)
'''
[(0, False),
 (1, True),
 (2, True),
 (3, False),
 (4, False),
 (5, True),
 (6, False),
 (7, False),
 (8, False),
 (9, False),
 (10, True)]
'''

yaksu(24)
'''
[(0, False),
 (1, True),
 (2, True),
 (3, True),
 (4, True),
 (5, False),
 (6, True),
 (7, False),
 (8, True),
 (9, False),
 (10, False),
 (11, False),
 (12, True),
 (13, False),
 (14, False),
 (15, False),
 (16, False),
 (17, False),
 (18, False),
 (19, False),
 (20, False),
 (21, False),
 (22, False),
 (23, False),
 (24, True)]
'''

# 약수만 뽑기
[i[0] for i in yaksu(24) if i[1]==True]

'''
[1, 2, 3, 4, 6, 8, 12, 24]
'''
