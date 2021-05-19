import re 

text = """
Shares of U.S. electric car maker Tesla are sliding after seeing substantial gains last year. 

The share price of Tesla began to plunge after Tesla CEO Elon Musk had made reckless comments on cryptocurrency. 

At the New York Stock Exchange on Monday (local time), share of Tesla plunged 2.19% to close at $576.83. 

Shares of Tesla are losing their allure this year, down about 20%, after surging 740% last year. 

Tesla shares are extending declines primarily because they are being adjusted out of concern for inflation in the U.S. economy. 

However, the downward spiral of Tesla stock was more pronounced than other big tech companies, including Facebook (-0.15%), Apple (-0.93%), and Amazon (+1.47%). 

Experts on Wall Street suspect that a recent plunge in the shares of Tesla reflects the risks of its CEO. 

Musk, who touted Bitcoin early this year, said last week the company no longer plans to accept Bitcoin as payment, sending shock waves through the cryptocurrency market. 

In a tweet on Sunday, Musk implied that Tesla may sell the rest of its Bitcoin holdings. 

Such unpredictable comments and actions by the Tesla CEO gave an impression that Musk is untrustworthy and are also affecting corporate value. Jae-Dong Yu jarrett@donga.com
"""

# 숫자가 포함되어 있는 것 가져오기
pattern = re.compile(r'\$*-*[0-9]+\.*[0-9]*\%*')

matches = pattern.finditer(text)

for match in matches :
    print(match.group(0))
    
'''
2.19%
$576.83
20%
740%
-0.15%
-0.93%
1.47%
'''

# 대문자로 시작하는 것만 가져오기
pattern = re.compile(r'[A-Z][a-z]+')

matches = pattern.finditer(text)

for match in matches :
    print(match.group(0))

    
'''
Shares
Tesla
The
Tesla
Tesla
Elon
Musk
At
New
York
Stock
Exchange
Monday
Tesla
Shares
Tesla
Tesla
However
Tesla
Facebook
Apple
Amazon
Experts
Wall
Street
Tesla
Musk
Bitcoin
Bitcoin
In
Sunday
Musk
Tesla
Bitcoin
Such
Tesla
Musk
Jae
Dong
Yu
'''
