from itertools import product 

def solution(word) : 
    alpha = ['A','E','I','O','U']
    words,check = [],[]
    for i in range(1,6) : 
        check.append(alpha)
        words += list(product(*check))
    words = list(map(lambda x : ''.join(x),words))
    words = sorted(words)
    return words.index(word)+1
