def solution(cacheSize,cities) : 
    mem,answer = [],0
    for i in cities : 
        lower = i.lower()
        if cacheSize == 0 : 
            return 5 * len(cities) # cache 사이즈가 0 이면 그냥 5 * len(cities)

        if lower not in mem : # cache 에 없으면
            if len(mem) < cacheSize : # cache 에 빈 메모리가 있다면..
                mem.append(lower)
            else : 
                mem.pop(0) # 빈 메모리가 없다면 최신화 시켜줘야함 
                mem.append(lower)
            answer+=5
        else : 
            mem.pop(mem.index(lower)) # cache에 있으면 없애주고 최신화
            mem.append(lower)
            answer+=1
    return answer

# ==============================================================================
# 중요한 점은 계속해서 최신화를 시켜줘야 한다는 것!
