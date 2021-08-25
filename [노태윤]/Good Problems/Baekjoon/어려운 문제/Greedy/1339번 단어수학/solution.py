N = int(input())
words = [list(input()) for _ in range(N)]

new_dict = {}
for word in words : 
    index = 0
    length = len(word)
    for c in word :
        zeros =  length - index - 1
        if c in new_dict : 
            new_dict[c] += 10**zeros
        else : 
            new_dict[c] = 10**zeros
        index+=1

num_list = sorted(list(new_dict.values()),reverse=True)
ans,X = 0,9

for num in num_list : 
    ans += num * X
    X-=1
print(ans)

# ==============================================================
# AAABB 면 dictionary 에 
# {'A' : 11100,'B' : 11} 형태로 담기
# 그리고 values reverse sorting 해준 뒤 9부터 내림차순으로 곱해서 더해주기!
