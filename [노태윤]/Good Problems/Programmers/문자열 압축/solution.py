def solution(text):
    min_val = int(1e9)

    for n in range(1,len(text)//2+2) : # +2 로 해줘야 text 의 length 가 1 일때도 잘 돌아감
        splitted = [text[i:i+n] for i in range(0,len(text),n)] # 순차적으로 묶는 과정
        count = 1 
        answer = ''
        for i in range(0,len(splitted)-1,1) : 

            if splitted[i] == splitted[i+1] : 
                count+=1
            else :
                if count == 1 : 
                    count = ''
                answer+= str(count) + splitted[i] 
                count=1

        if count ==1 : # 마지막에 한번 더 해줄 것
            answer+= splitted[-1]
        else :
            answer+= str(count) + splitted[-1] 
        if min_val > len(answer) : # min 값 갱신
            min_val = len(answer)

    return min_val
