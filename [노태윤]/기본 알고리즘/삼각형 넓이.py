# 좌표가 주어졌을 때
x1,y1 = list(map(int,input().split(" ")))
x2,y2 = list(map(int,input().split(" ")))
x3,y3 = list(map(int,input().split(" ")))

tri_area = 0.5 * abs(x1*(y2-y3) + x2*(y3-y1) + x3* (y1-y2))

# 변의 길이가 주어졌을 때 (헤론의 공식)
A,B,C = list(map(int,input().split(" ")))
s = (A+B+C) / 2 
area = (s * (s-A)*(s-B)*(s-C))**0.5
print('%.2f' % area)
