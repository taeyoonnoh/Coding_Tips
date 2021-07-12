import re
def solution(files):
    # 숫자를 기준으로 split (이 때 숫자도 함께 나옴
    new_files = [re.split('([0-9]+)',file) for file in files]
    
    # x[0] 내림차순 및 x[1] 내림 차순으로 정렬 (key 함수를 쓰게 되면 이미 주어진 리스트를 기준으로 정렬이 진행 됌)
    sorted_files = sorted(new_files,key=lambda x : (x[0].lower(), int(x[1])))
    
    # 마지막으로 join 시키기
    answer = list(map(lambda x : ''.join(x),sorted_files))
    return answer
