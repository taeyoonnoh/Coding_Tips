N = int(input())
dist = list(map(int,input().split()))
node = list(map(int,input().split()))
counts, min_price = 0, node[0]
for i in range(len(dist)) : 
    # 주유소 리터당 가격이 낮다면 min price 업데이트 그 외에는 기존 min price 에서 곱해줄 것!
    min_price = min_price if node[i] >= min_price else node[i] if node[i] < min_price else 0
    counts += min_price * dist[i]
print(counts) 
