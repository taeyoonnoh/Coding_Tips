def solution(operations):
    q = []
    for operation in operations :
        splitted = operation.split(" ")
        command = splitted[0]
        num = int(splitted[1])
        if command == "I" : 
            q.append(num)
        elif command =='D' : 
            if not q :
                continue
            if num == 1 : 
                max_num = max(q)
                q.remove(max_num)
            elif num == -1 : 
                min_num = min(q)
                q.remove(min_num)
    if not q : 
        return [0,0]
    else : 
        return [max(q),min(q)]
