from collections import defaultdict

def solution(n,results) : 
    win_dict,lose_dict = defaultdict(set),defaultdict(set)
    for win,lose in results : 
        win_dict[win].add(lose)
        lose_dict[lose].add(win)
    
    for i in range(1,n+1) : 
        for loser in win_dict[i] : 
            lose_dict[loser].update(lose_dict[i]) # lose_dict 업데이트
        for winner in lose_dict[i] : 
            win_dict[winner].update(win_dict[i]) # win dict 업데이트
    
    answer = 0 
    for i in range(1,n+1) : 
        if len(win_dict[i]) + len(lose_dict[i]) == n-1 : # 자신 기준으로 위에 승자와 밑에 패자의 갯수가 n-1 이면 순위를 알 수 있음!
            answer+=1
    return answer
