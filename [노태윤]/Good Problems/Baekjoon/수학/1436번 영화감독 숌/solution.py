N = int(input())
count = 0
six_3 = 666
while True:
    if '666' in str(six_3):
        count += 1
    if count == N:
        print(six_3)
        break
    six_3 += 1

#===========================
# 좀 많이 비효율적임..
