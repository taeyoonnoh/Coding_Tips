# Python Set Operations
  
# sets are define
A = {0, 2, 4, 6, 8};
B = {1, 2, 3, 4, 5};
  
# union
print("Union :", A | B)
# Union : {0, 1, 2, 3, 4, 5, 6, 8}
  
# intersection
print("Intersection :", A & B)
# Intersection : {2, 4}
  
# difference
print("A - B Difference :", A - B)
print("B - A Difference :", B - A)
# A - B Difference : {0, 8, 6}
# B - A Difference : {1, 3, 5}
  
# symmetric difference (A & B 합집합에서 교집합 뺀 것!)
print("A ^ B Symmetric difference :", A ^ B)
print("B ^ A Symmetric difference :", B ^ A)
# Symmetric difference : {0, 1, 3, 5, 6, 8}
# Symmetric difference : {0, 1, 3, 5, 6, 8}

# {} set 또는 dictionary 에서만 가능한 operation!

# ========================================================

# Counter

from collections import Counter
# element의 갯수를 dictionary 형태로 반환

a = [1,1,2,3,2,1,2,3,4,5,2,3,3]
b = [4,5,3,1,2,3,2,4,5,3,1,6,1]

a = Counter(a) 
b = Counter(b)

print(a) # Counter({2: 4, 3: 4, 1: 3, 4: 1, 5: 1})
print(b) # Counter({3: 3, 1: 3, 4: 2, 5: 2, 2: 2, 6: 1})

# dictionary 형태이므로 python set operation 가능

print(a+b) # 갯수 더하기 : Counter({3: 7, 1: 6, 2: 6, 4: 3, 5: 3, 6: 1})
print(a-b) # a-b : Counter({2: 2, 3: 1})
print(b-a) # b-a : Counter({4: 1, 5: 1, 6: 1})
print(a|b) # a b 합집합 (갯수 더 많은 게 반환되는 듯) : Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 2, 6: 1})
print(a&b) # a b 교집합 : Counter({1: 3, 3: 3, 2: 2, 4: 1, 5: 1})
print(a^b) # TypeError 남.. 왜 그런진 아직 모르겠음

# set within list 형태로 바꿔보기

print(list((a-b).items())) # [(2, 2), (3, 1)]
