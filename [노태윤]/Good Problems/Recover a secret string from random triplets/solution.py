from collections import defaultdict,deque

def recoverSecret(triplets):
    forward_dict = defaultdict(set) # defaultdict 은 없으면 0 으로 변환  
    backward_dict = defaultdict(set) # value 가 set 형식으로 됌
    for a,b,c in triplets : # 정방향 역방향에 add (set 라서)
        forward_dict[a].add(b) 
        forward_dict[b].add(c)
        backward_dict[c].add(b)
        backward_dict[b].add(a)

    start_point = list(set([i for j in backward_dict.values() for i in j]) - set(backward_dict.keys()))[0] # 시작점 찾기
    ending_point = list(set([i for j in forward_dict.values() for i in j]) - set(forward_dict.keys()))[0] # 끝점 찾기
    count_dict = defaultdict(int) # count 가 담긴 default dict
    queue = deque([start_point])

    while queue :
        cur_node = queue.popleft() # 최대 거리 구하기 
        for i in forward_dict[cur_node] : 
            count_dict[i] = count_dict[cur_node] + 1 
            queue.append(i)
    sorted_list = sorted(list(count_dict.items()),key = lambda x : x[1])
    charac_list = list(map(lambda x : x[0], sorted_list))
    return ''.join(charac_list)
