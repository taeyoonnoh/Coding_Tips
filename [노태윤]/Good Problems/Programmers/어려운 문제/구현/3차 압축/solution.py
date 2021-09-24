def solution(msg) : 
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alpha_dict,ind = {}, 1
    for i in alpha  : 
        alpha_dict[i] = ind
        ind+=1
    answer = []
    start,end = 0, len(msg)
    new_ind = 27

    while True : 
        a = msg[start:end]
        if a in alpha_dict.keys() : 
            answer.append(alpha_dict[a])
        
            if end >= len(msg) : 
                return answer

            alpha_dict[a+msg[end]] = new_ind
            new_ind+=1
            start += len(a)
            end = len(msg)
        else : 
            end-=1

# ============================================
# 끝에서부터 확인
# ex)
# KAKAO
# KAKA
# KAK
# KA
# K ==> 딕셔너리에 있는 것 확인 ==> answer 에 append
  # 그 다음 KA 딕셔너리에 추가!
  
# start 업데이트
# 다시 진행
# AKAO
# AKA
# AK
# A ==> 딕셔너리에 있는 것 확인 ==> answer 에 append
  # 그 다음 AK 딕셔너리에 추가!
  
# start 업데이트
# 다시 진행
# KAO
# KA ==> 딕셔너리에 있는 것 확인 ==> answer 에 append
  # 그 다음 KAO 딕셔너리에 추가!
  
# start 업데이트
# 다시 진행
# O ==> 딕셔너리에 있는 것 확인 ==> answer 에 append ==> 종료
