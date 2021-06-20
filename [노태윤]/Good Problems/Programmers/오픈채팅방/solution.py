def solution(a):
    answer_list = []
    change_dict = {}
    for i in a : # 처음에는 update 될 dict 만 담기
        split = i.split(" ")
        if split[0] == 'Enter' or split[0] == 'Change' : 
            change_dict[split[1]] = split[2]
    
    for i in a : # dict 에 갱신된 것으로 다시 담기
        split = i.split(" ")
        if split[0] == 'Enter' : 
            answer_list.append(f'{change_dict[split[1]]}님이 들어왔습니다.')
        elif split[0] == 'Leave' : 
            answer_list.append(f'{change_dict[split[1]]}님이 나갔습니다.')

    return answer_list
