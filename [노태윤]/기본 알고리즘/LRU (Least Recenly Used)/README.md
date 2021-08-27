https://gingerkang.tistory.com/26

```python
def solution(cacheSize,cities) : 
    mem,answer = [],0
    for i in cities : 
        lower = i.lower()
        if cacheSize == 0 : 
            return 5 * len(cities)

        if lower not in mem : 
            if len(mem) < cacheSize : 
                mem.append(lower)
            else : 
                mem.pop(0)
                mem.append(lower)
            answer+=5
        else : 
            mem.pop(mem.index(lower))
            mem.append(lower)
            answer+=1
    return answer
```
