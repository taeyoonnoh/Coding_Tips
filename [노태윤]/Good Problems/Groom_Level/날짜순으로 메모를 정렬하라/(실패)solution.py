# 2번 테스트케이스 실패

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import re
from datetime import datetime

str_list = []
while True :
	user_input = input()
	if user_input == 'END' : 
		break
	str_list.append(user_input)

text_list = []

pattern = re.compile(r'\d+.\d+.\d+')
for i in str_list : 
    matches =  pattern.finditer(i) 
    for match in matches : 
        text = match.group()
        text = re.sub('[^\d+]','-',text)
        if '-' in text[:4] : 
            text = '20' + text
        text_list.append(text)

for i in range(len(text_list)) : 
    datetimeobject = datetime.strptime(text_list[i],'%Y-%m-%d')
    text_list[i] = datetimeobject.strftime('%Y-%m-%d')

sorted_list = sorted(list(zip(str_list,text_list)),key=lambda x : x[1])

for i in sorted_list : 
	print(i[0])
