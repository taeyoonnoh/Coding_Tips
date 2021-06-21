def solution(number, k):
    stack = []

    for i in number : 
        while stack and stack[-1]<i : # stack 마지막 index 값 보다 작으면 갱신
            if k>0 : # k 하나씩 줄이기
                k-=1
                stack.pop()
            else :
                break
        stack.append(i)
    if k > 0 : # 4444 같은 경우에는 위 for 문에 append 만 일어남
        for i in range(k) : # 따라서 k 만큼 pop 시키기
            stack.pop()
    return ''.join(stack)
