import re 

def solution(s):
    num_dict = {
        'zero' : 0,
        'one' : 1,
        'two' : 2,
        'three' : 3,
        'four' : 4,
        'five' : 5,
        'six' : 6,
        'seven' : 7,
        'eight' : 8,
        'nine' : 9
    }

    b = re.split(r'(zero|one|two|three|four|five|six|seven|eight|nine|\d)',s) # 해당 문자 또는 숫자 로 split 
    b = list(filter(lambda x : x!='',b)) # '' 가 포함되는 element 도 있으므로 filter 로 '' 가 아닌 element 만 뽑기
    for i in range(len(b)) : 
        if b[i].isdigit() : # int 형이면 그냥 continue
            continue
        b[i] = str(num_dict[b[i]])
    return int(''.join(b))

# ====================================================================================================================
# replace 만 사용도 되는 문제였다..흠.. 아직 많이 모자르다
