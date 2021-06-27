from string import digits,ascii_uppercase

uppercase = digits + ascii_uppercase

def jinsu(N,base) : # N 진수 변환 알고리즘
    ans = ''
    q,r = divmod(N,base)
    if q == 0 :
        return uppercase[r]
    else :
        return jinsu(q,base) + uppercase[r]

def solution(n, t, m, p):
    strings = ''
    answer = ''
    i = 0
    while True : 
        strings += jinsu(i,n)
        i+=1
        if len(strings) >= t*m : # strings 길이 변환해주고 반환
            strings = strings[:t*m]
            break

    for i in range(p-1,len(strings),m) : # 간격에 맞게 반환
        answer+=strings[i]
    return answer
