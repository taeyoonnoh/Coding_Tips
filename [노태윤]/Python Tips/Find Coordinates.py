imprt numpy as np

numbers = [
           [1,2,3],
           [4,5,6],
           [7,8,9],
           ['*',0,'#']
]
numbers = np.array(numbers)
coordinates = list(np.argwhere(numbers=='8').flatten())
print(coordinates) # ==> [2,1]

np.argwhere(numbers=='8') # ==> array([[2, 1]])

np.argwhere(numbers=='8').flatten() # ==> array([2, 1])

list(np.argwhere(numbers=='8').flatten()) # ==> [2,1]
