from collections import Counter

def loop_size(node):
    empty_list = []
    while node : # empty_list 에 node 가 loop 이루어질 때까지 append
        if node in empty_list :
            empty_list.append(node)
            break
        empty_list.append(node)
        node = node.next
    counter = Counter(empty_list)
    check = sorted(list(counter.items()),key=lambda x : x[1],reverse=True)[0][0]
    index = empty_list.index(check) # 첫번째로 loop을 형성하는 index 찾기
    count=0
    for i in range(index+1,len(empty_list)) : # 다음 같은 index 나올때까지 count +=1
        count+=1
        if empty_list[i] == empty_list[index] : 
            break
    return count
