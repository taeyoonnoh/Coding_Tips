from collections import defaultdict
from functools import reduce

def solution(n,words) : 
    index,counts = 2,1 # 2번째 index부터 시작할 것이기 때문에 index = 2 로 설정
    new_dict = defaultdict(list)
    new_dict[1].append(words[0]) # 초기에 1번째 사람 단어 넣어줌
    for i in range(1,len(words)) : 
        values = list(new_dict.values()) 
        values = list(reduce(lambda x,y:x+y,values)) # 2차원 list를 1차원으로 바꿔주는 작업
        if (words[i][0] != words[i-1][-1]) or words[i] in values : # 만약 전 끝문자랑 후 앞문자랑 다르다면 or 이미 사용된 적이 있다면 
            answer = [index,counts]
            break
        new_dict[index].append(words[i]) # 각 사람별로 list 에 담기
        index+=1 # index 1씩 증가
        if index>n : # 만약 한바퀴 돌면 초기화해줄 것
            index=1
            counts+=1 # counts 1씩 증가
    else : 
        answer = [0,0]
    return answer
  
  # ====================================================================================================================================
  # default dict & reduce 쓰지 않고 풀기
  
  def solution(n,words) : 
    for i in range(1,len(words)) : 
        if words[i-1][-1] != words[i][0] or words[i] in words[:i] : 
            return [i%n+1,i//n+1]
    else : 
        return [0,0]
  
  # ==================================================================
  # 자릿수 반복적으로 진행되거나 할 떄에는 나누기와 몫을 가지고 풀어보자
  # 현재 word 가 이전에 있는 것 확인 하는 방법 ==> words[i] in words[:i]
