class Point:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

def find_area(points):
    X,Y = [],[]
    new_X,new_Y = [],[]

    for i in points : 
        X.append(i.X)
        Y.append(i.Y)
    
    if Y[0] > 0 : 
        X.insert(0,X[0])
        Y.insert(0,0)
    if Y[-1] > 0 :
        X.append(X[-1])
        Y.append(0)

    for i in range(len(X)) : 
        if i == len(X)- 1 :
            new_X.append((X[i],X[0]))
            new_Y.append((Y[i],Y[0]))
        else :
            new_X.append((X[i],X[i+1]))
            new_Y.append((Y[i],Y[i+1]))
    
    summed = 0
    for i in range(len(new_X)) : 
        summed += (new_X[i][0] * new_Y[i][1] - new_X[i][1] * new_Y[i][0]) # ad-bc 한다고 생각하면 됨 
    return abs(summed)/2
  
  # ==================================================================================================
  # X = [x1,x2,x3,x4]
  # Y = [y1,y2,y3,y4]
  
  # area = 
    # abs((x1*y2 - x2*y1) + (x2*y3 - x3*y2) + (x3*y4 - x4*y3) + (x4*y1 - x1*y4)) / 2
