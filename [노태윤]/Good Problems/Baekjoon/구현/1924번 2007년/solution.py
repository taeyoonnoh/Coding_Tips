weekdays = ['SUN','MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

days_list = [0,31,28,31,30,31,30,31,31,30,31,30,31]
agg_days_list = []
a = 0
for i in days_list : 
    a += i
    agg_days_list.append(a)

month,day = list(map(int,input().split()))
days_passed = agg_days_list[month-1]+day

print(weekdays[days_passed%7])

############################################################

# 이렇게도 풀 수 있더라

x, y = map(int, input().split())
for i in range(1, x):
    if i in [1, 3, 5, 7, 8, 10, 12]:
        y += 31
    elif i == 2:
        y += 28
    else:
        y += 30
day_week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
print(day_week[y % 7])
