# 10~11 시간 초과
def solution(numbers):
    answer = []
    for number in numbers : 
        new = number
        a_bit = format(number,'b').zfill(17)
        while True : 
            new+=1
            b_bit = format(new,'b').zfill(17) 
            c = list(zip(list(a_bit),list(b_bit)))
            diff_bit = sum(list(map(lambda x : x[0]!=x[1],c)))
            if diff_bit <= 2 : 
                break
        answer.append(new)
    return answer

# ================================================================

def solution(numbers):
    answer = []
    for number in numbers : 
        if number % 2 == 0 :
            answer.append(number+1)
        else :
            str_num = ['0'] + list(format(number,'b'))
            index = ''.join(str_num).rfind('0')
            str_num[index] = '1'
            str_num[index+1] = '0' if str_num[index+1] == '1' else '1'
            answer.append(int(''.join(str_num),2))
    return answer

# ================================================================
# 짝수면 그냥 해당 숫자에 1 더해주면 됌
# 홀수면 '111' 또는 '101' 같은 경우가 발생
  # '111' 이면 '0111' 로 변환 후 --> '1011' 로 바꿔줘야함 (왼쪽부터 바꿔줘야 최소값이 나옴)
  # '101' 이면 '110' 로 바꿔줘야함 (이 같은 경우에는 맨 앞의 '1' 을 '0' 으로 바꿔버리면 '101' 보다 작아짐)
    # 그래서 오른쪽을 기준으로 '0' 인 index를 찾고 index , index + 1 에 위치한 숫자만 바꿔주면 됌
    # 이 때는 홀수이므로 가장 오른쪽에 있는 숫자가 '0' 일 수가 없음!
  
  # 처음부터 '0' 을 넣어주면 쉽게 풀 수 있음

# 이런 문제는 전체적으로 for loop 돌리는 거 보다 알고리즘적으로 풀 것!
