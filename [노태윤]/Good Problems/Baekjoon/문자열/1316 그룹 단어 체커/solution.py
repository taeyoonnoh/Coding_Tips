N  = int(input())

ans = 0
for i in range(N) : 
    text = input()
    error = 0
    for j in range(len(text)-1) : # len(text) -1 만큼 진행
        if text[j] != text[j+1] : # 뒷글자와 현재 글자가 다르다면 아래 코드 실행
            check = text[j+1:] # 현재 글자를 제외하고 그 뒤 단어들 보기
            if check.count(text[j]) > 0 : # count 를 해서 그 뒤에도 현재 단어가 포함되어 있으면 error + 1
                error +=1
    
    if error == 0 : 
        ans+=1

print(ans)
