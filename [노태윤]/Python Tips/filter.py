list(filter(lambda x : len(x)==3,arr)) # ==> element 중 길이가 3 인것만 반환

from itertools import filterfalse
list(filterfalse(lambda x : len(x)==3,arr)) # ==> element 중 길이가 3아 아닌 것만 반환
