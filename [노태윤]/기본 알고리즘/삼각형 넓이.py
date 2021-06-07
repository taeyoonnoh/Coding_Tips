x1,y1 = list(map(int,input().split(" ")))
x2,y2 = list(map(int,input().split(" ")))
x3,y3 = list(map(int,input().split(" ")))

tri_area = 0.5 * abs(x1*(y2-y3) + x2*(y3-y1) + x3* (y1-y2))
