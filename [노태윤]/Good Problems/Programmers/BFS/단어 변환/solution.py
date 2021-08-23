from collections import deque

def solution(begin, target, words):
    if target not in words : 
        return 0

    visited = [False] * (len(words))
    q = deque()
    q.append((begin,0))
    while q :
        word,counts = q.popleft()
        if word == target : 
            return counts
        for i in range(len(words)) : 
            diff_count = 0
            for a,b in zip(list(words[i]),list(word)) : 
                if a!=b : 
                    diff_count+=1
            if diff_count == 1 and visited[i]==False: 
                visited[i]=True
                q.append((words[i],counts+1))
 
# =========================================================
# 하나씩 차이 나면 q 에 쌓기 
# target 에 도달하면 그때의 counts 반환!
