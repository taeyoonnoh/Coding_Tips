def solution(price, money, count):
    tot_money = sum([price * i for i in range(1,count+1)])
    return tot_money - money if tot_money > money else 0

# 간단한 방법
def solution(price, money, count):
    tot_money = sum([price * i for i in range(1,count+1)])
    return max(tot_money-money,0)
