import sys

N = int(input())
times = []
for i in range(N) : 
    times.append(list(map(int,sys.stdin.readline().split())))

a = sorted(times,key=lambda x : x[0]) # 시작 시간 기준으로 오름차순 정렬
a = sorted(a,key=lambda x : x[1]) # 끝나는 시간 기준으로 오름차순 정렬

ans_list = []
for x,y in a : 
    if not ans_list : 
        ans_list.append([x,y]) # 처음 꺼는 무조건 append
        continue
    if x>= ans_list[-1][1] : 
        ans_list.append([x,y]) # 그 다음부터는 현재 시작 시간이 이전 끝나는 시간 보다 크거나 같으면 append
print(len(ans_list))
