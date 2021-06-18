import numpy as np
from string import ascii_lowercase
import re

def encrypt(text,key):
    text = re.sub('[^a-zA-Z]+','',text) # 문자 이외는 제외
    text = text.lower()
    if not text : 
        return ''
    if len(text)%2 == 1 : # 홀수면 z 추가하기
        text+='z'
    text = [ascii_lowercase.index(i) for i in text] # 숫자로 바꿔주기
    key = [ascii_lowercase.index(i) for i in key]

    text = np.array(text).reshape(2,len(text)//2,order='F') # 이건 좌우 방식이 아닌 상하 방식으로 만들어주기 위한 용도
    key = np.array(key).reshape(2,2)

    answer = np.dot(key,text)
    answer = np.array(list(map(lambda x : x%26,answer))) # mod 26 으로 바꿔주기
    text_answer = ''
    for i in range(len(answer[0])) : 
        for j in range(len(answer)) : 
            text_answer+=ascii_lowercase[answer[j][i]].upper()
    return text_answer
