# Python Study

## 함수

```python
# sum()
one_to_ten = list(range(1, 11))
sum(one_to_ten) # 55

```

```python
family = ['mother', 'father', 'gentleman', 'sexy lady']

# len()
len(family) # 4

# remove()
family.remove('gentleman')
family # ==> ['mother', 'father', 'sexy lady']

# find()
family.find('mother') # ==> 0

# str()

# int()

# float()

# / , * , // , ** , % , 

# == , !=

# for
for x in family : 
  print(x, len(x))
  
# mother 6
# father 6
# gentleman 9
# sexy lady 9

# map, reduce, lambda, filter

# 
```

## 데이터 타입

```python
# 문자열
s = "hello Python!"
s.split() # ==> ['hello', 'Python!']

# 리스트

## append
prime = [3, 7, 11]
prime.append(5)
prime # ==> [3, 7, 11, 5]

## sort
prime.sort()
prime # ==> [3, 5, 7, 11]

## insert
prime.insert(0,2)
prime # ==> [2, 3, 5, 7, 11]

## del 
del prime[4]
prime # ==> [2, 3, 5, 7]

## pop
a = prime.pop()
prime # [2,3,5]
a # 7

## 문자열을 리스트로 바꾸기
characters = []
sentence = 'Be happy!'
for char in sentence : 
  characters.append(char)

print(characters)
# ['B', 'e', ' ', 'h', 'a', 'p', 'p', 'y', '!']

list('Be happy!')
# ['B', 'e', ' ', 'h', 'a', 'p', 'p', 'y', '!']
```

## set 연산자

```python
fruits = {'apple', 'banana', 'orange'}
companies = {'apple', 'microsoft', 'google'}

# 교집합
fruits & companies # ==> {'apple'}

# 합집합
fruits | companies # ==> {'apple', 'mango', 'microsoft', 'orange', 'google', 'banana'}
```

