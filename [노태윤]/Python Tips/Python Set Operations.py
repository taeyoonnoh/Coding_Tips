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
